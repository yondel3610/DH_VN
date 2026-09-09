"""
voice_tag_inserter.py
=======================
Step 2 of the voice-line tagging pipeline for Dragon's Heart: Crimson Rebirth.

WHAT THIS DOES
--------------
1. Reads your central audio.rpy and pulls out every:
        define audio.xxx = "path/to/file.ogg"  # transcript: "some words here"
    into a map of  { audio_id: transcript_text }.

2. Scans one or more chapter .rpy files for dialogue lines.

3. Filters transcripts to ONLY those belonging to the current chapter
    (by matching the chapter number in the audio ID, e.g. "ch3").

4. Fuzzy-matches each transcript against dialogue lines, enforcing that
    the character in the audio ID matches the speaker of the dialogue line.

5. For each confident match, inserts:
        voice "audio.xxx"  # transcript: "matched transcript text"
    directly above the matched dialogue line, with the same indentation.
    The trailing comment lets you eyeball whether the match is correct
    without needing to jump back to audio.rpy.

DUPLICATE LINE HANDLING
------------------------
Some dialogue is genuinely repeated verbatim in more than one place -
most commonly the same line appearing in both a chapter 9 and chapter 10
route, or a line reused across two menu branches. When several dialogue
candidates share an identical line of text, this is NOT treated as an
ambiguous match (which would previously cause both to be skipped). Instead,
each is resolved in order: audio IDs are processed in ascending "_lineN"
order, and each is assigned to the earliest not-yet-used duplicate
occurrence in the chapter file. Genuinely different-but-similarly-scored
lines are still flagged as ambiguous and skipped, same as before.
"""

import os
import re
import difflib

# =============================================================================
# CONFIG — EDIT THESE FOR YOUR PROJECT
# =============================================================================

AUDIO_RPY_PATH = r"game/01_voice_lines.rpy"

CHAPTER_FILES = [
    r"game/13_chapter_10.rpy",
]
MATCH_THRESHOLD = 0.55
AMBIGUITY_MARGIN = 0.05

OVERWRITE_ORIGINAL = False

COMMENT_MARKER = "# transcript:"

# When True, every inserted `voice audio.xxx` line also gets the matched
# transcript appended as a trailing comment, e.g.:
#     voice audio.dorian_ch5_line12  # transcript: "I choose Niko."
# This makes it much faster to eyeball whether a match is correct directly
# in the chapter file, without cross-referencing audio.rpy.
INCLUDE_TRANSCRIPT_COMMENT = True

# --- Chapter & character filtering ---

# When True, only transcripts whose audio ID contains the current chapter's
# number (e.g. "ch3" in "dorian_ch3_line95") will be considered for that
# chapter file. Prevents a chapter-5 transcript from matching a chapter-3 line.
ENFORCE_CHAPTER_FILTER = True

# When True, the character prefix extracted from the audio ID (e.g. "dorian"
# from "dorian_ch3_line95") must match the speaker of the dialogue line.
# Prevents a Dorian voice clip from being placed above an Elias line.
ENFORCE_CHARACTER_MATCH = True

# If your audio IDs use a character name that differs from the Ren'Py speaker
# variable in dialogue, map them here.
#   e.g. audio IDs use "dorian" but dialogue uses the variable `dh`:
#        CHARACTER_ALIASES = {"dorian": "dh"}
CHARACTER_ALIASES = {
    "man1": "man_1",
    "minjoon": "emperor_minjoon",
    "shen": "long_shen",
    "woman3": "woman_3",
    "toatie_roar": "taotie",
    "femaleguard": "female_guard",
    "gustav": "king_gustav",
    "lars": "mjoll_lars",
    "pavel": "mjoll_pavel",
    "yuki": "yuki_onna",
    "vasily_laugh": "vasily",
    "elera": "elara",
    "sunwoo": "captain_sunwoo",
    "tianxun": "tian_xun",
    "door": "door_voice",
    "roboto1": "roboto",
    "chung": "chung_hee",
    "mjoll_soldier_female_1": "femaleguard",
    "girl_ald" : "girl_ald_soldier",
    "hulijing" : "huli_jing",
    "supplyrobot" : "supply_robot",
}

# Speaker names in audio IDs that should match narrator lines (no speaker).
# e.g. "narrator_ch3_line1" matches `"Some narration."`
NARRATOR_KEYWORDS = {"narrator", "narration", "mono", "internal", "thought"}

# =============================================================================
# END CONFIG
# =============================================================================


def load_audio_transcripts(audio_rpy_path):
    define_pattern = re.compile(
        r'^\s*define\s+audio\.(\w+)\s*=\s*"[^"]+\.ogg"'
    )
    transcript_pattern = re.compile(
        re.escape(COMMENT_MARKER) + r'\s*"([^"]*)"'
    )

    transcripts = {}
    skipped_no_transcript = []

    with open(audio_rpy_path, "r", encoding="utf-8") as f:
        for line in f:
            define_match = define_pattern.match(line)
            if not define_match:
                continue
            audio_id = define_match.group(1)
            transcript_match = transcript_pattern.search(line)
            if transcript_match:
                transcripts[audio_id] = transcript_match.group(1).strip()
            else:
                skipped_no_transcript.append(audio_id)

    if skipped_no_transcript:
        print(f"NOTE: {len(skipped_no_transcript)} audio define(s) have no "
            f"'{COMMENT_MARKER}' comment yet. Skipping these:")
        for a in skipped_no_transcript:
            print(f"    - audio.{a}")

    return transcripts


DIALOGUE_PATTERN = re.compile(
    r'^(?P<indent>\s*)'
    r'(?P<charid>[a-zA-Z_][a-zA-Z0-9_]*\s+)?'
    r'"(?P<text>(?:[^"\\]|\\.)*)"'
    r'(?P<trailing>\s*(?:\([^)]*\))?)\s*$'
)


# =============================================================================
# Chapter extraction & filtering
# =============================================================================

def extract_chapter_num(chapter_path):
    """
    Determine the chapter number from a filename.
        "05_chapter_03.rpy"  -> 3
        "chapter_3.rpy"      -> 3
        "ch3.rpy"            -> 3
        "03_something.rpy"   -> 3
    Returns None if no chapter number can be determined.
    """
    name = os.path.basename(chapter_path)

    # Try "chapter_03", "chapter3", "chapter03", etc.
    m = re.search(r'chapter_?0*(\d+)', name, re.IGNORECASE)
    if m:
        return int(m.group(1))

    # Try "ch3", "ch_3", "ch03" (but NOT "chung" or other words containing "ch")
    m = re.search(r'(?<![a-z])ch_?0*(\d+)', name, re.IGNORECASE)
    if m:
        return int(m.group(1))

    # Fallback: leading number like "05_..." or "05."
    m = re.match(r'0*(\d+)[_.]', name)
    if m:
        return int(m.group(1))

    return None


def build_chapter_regex(chapter_num):
    """
    Build a regex that matches the chapter marker inside an audio ID.
    For chapter 3, matches:  ch3, ch03, chapter3, chapter_3, chapter03, chapter_03
    Does NOT match:          ch13, ch30, chapter30
    """
    return re.compile(
        rf'(?<![a-z])ch(?:apter)?_?0*{chapter_num}(?!\d)',
        re.IGNORECASE
    )


def filter_transcripts_for_chapter(transcripts, chapter_num):
    """
    Return only transcripts whose audio_id contains the chapter marker
    for the given chapter number.
    e.g. with chapter_num=3, keeps "dorian_ch3_line95" but drops "dorian_ch5_line20".
    """
    if chapter_num is None:
        return transcripts, []

    chapter_re = build_chapter_regex(chapter_num)
    kept = {}
    dropped = []
    for audio_id, transcript in transcripts.items():
        if chapter_re.search(audio_id):
            kept[audio_id] = transcript
        else:
            dropped.append(audio_id)

    return kept, dropped


def extract_expected_character(audio_id, chapter_num):
    """
    Extract the character prefix from an audio ID.
        "dorian_ch3_line95"       -> "dorian"
        "chung_hee_ch3_line95"    -> "chung_hee"
        "narrator_ch3_line1"      -> "narrator"
    Returns None if no character prefix can be determined.
    """
    if chapter_num is None:
        return None

    chapter_re = build_chapter_regex(chapter_num)
    m = chapter_re.search(audio_id)
    if m:
        char = audio_id[:m.start()].rstrip('_')
        return char.lower() if char else None
    return None


def extract_line_number(audio_id):
    """
    Extract the trailing line number from an audio ID for ordering purposes.
        "dorian_ch3_line95" -> 95
        "narrator_ch10_line5" -> 5
    Returns a large sentinel value if no line number is found, so IDs
    without one sort to the end rather than crashing the sort.
    """
    m = re.search(r'line(\d+)\s*$', audio_id, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return float("inf")


def extract_existing_voice_tags(lines):
    """
    Scan chapter lines and return a set of audio IDs that already have 
    a `voice audio.xxx` tag anywhere in the file.
    """
    existing_tags = set()
    voice_pattern = re.compile(r'^\s*voice\s+audio\.(\w+)')
    for line in lines:
        match = voice_pattern.match(line)
        if match:
            existing_tags.add(match.group(1))
    return existing_tags

# =============================================================================


def already_has_voice_above(lines, line_index):
    i = line_index - 1
    while i >= 0 and lines[i].strip() == "":
        i -= 1
    if i < 0:
        return False
    return lines[i].strip().startswith("voice ")


def extract_dialogue_candidates(lines):
    """
    Scan chapter lines and return a list of dicts:
        { "index", "text", "indent", "speaker" }
    speaker is lowercased, "" for narrator lines.
    """
    candidates = []

    for i, line in enumerate(lines):
        stripped = line.rstrip("\n")
        lstripped = stripped.strip()
        if not lstripped:
            continue
        if lstripped.startswith("#"):
            continue
        if lstripped.startswith("$"):
            continue
        if lstripped.startswith(("label ", "jump ", "call ", "menu:", "scene ",
                                    "show ", "hide ", "play ", "stop ", "if ",
                                    "elif ", "else:", "return", "pause",
                                    "define ", "default ", "python:", "init ")):
            continue

        match = DIALOGUE_PATTERN.match(stripped)
        if not match:
            continue
        if stripped.rstrip().endswith(":"):
            continue

        # Extract speaker (None for narrator lines like "Some text.")
        speaker = match.group("charid")
        speaker = speaker.strip().lower() if speaker else ""

        candidates.append({
            "index": i,
            "text": match.group("text"),
            "indent": match.group("indent"),
            "speaker": speaker,
        })

    return candidates


def _normalize_text(text):
    """Collapse whitespace and lowercase, for exact-duplicate comparison."""
    return " ".join(text.split()).lower()


def find_best_match(transcript, candidates, used_indices, expected_char=None):
    """
    Return (best_candidate, best_score, is_ambiguous).

    If expected_char is provided, only dialogue lines spoken by that
    character are considered. This prevents a Dorian voice clip from
    matching an Elias line.

    DUPLICATE HANDLING: if the top-scoring candidates are tied within
    AMBIGUITY_MARGIN but their full dialogue text is identical (a genuine
    duplicate line, e.g. the same line repeated across a ch9/ch10 route
    split), this is NOT treated as ambiguous. The earliest (lowest index)
    unused duplicate is returned instead. Ties between candidates with
    genuinely different text are still flagged as ambiguous, unchanged
    from before.
    """
    # Resolve any alias mapping
    expected_speaker = None
    is_narrator_audio = False
    if expected_char is not None:
        if expected_char in NARRATOR_KEYWORDS:
            is_narrator_audio = True
        else:
            expected_speaker = CHARACTER_ALIASES.get(expected_char, expected_char)

    scored = []
    for cand in candidates:
        if cand["index"] in used_indices:
            continue

        if expected_char is not None:
            if is_narrator_audio:
                # Narrator audio should only match lines with no speaker
                if cand["speaker"] != "":
                    continue
            else:
                # Character audio must match the speaker exactly
                if cand["speaker"] != expected_speaker:
                    continue

        text_start = " ".join(cand["text"].split()[:8])
        score = difflib.SequenceMatcher(
            None, transcript.lower(), text_start.lower()
        ).ratio()
        scored.append((score, cand))

    if not scored:
        return None, 0.0, False

    scored.sort(key=lambda pair: pair[0], reverse=True)
    best_score, best_cand = scored[0]

    if best_score < MATCH_THRESHOLD:
        return None, best_score, False

    # Gather every candidate within the ambiguity margin of the best score -
    # this is the "top group" we need to check for genuine duplicates.
    top_group = [pair for pair in scored if (best_score - pair[0]) < AMBIGUITY_MARGIN]

    if len(top_group) > 1:
        normalized_texts = {_normalize_text(cand["text"]) for _, cand in top_group}

        if len(normalized_texts) == 1:
            # All tied candidates have IDENTICAL dialogue text - this is a
            # duplicate line (e.g. repeated across routes), not a genuinely
            # ambiguous match. Deterministically resolve to the earliest
            # unused occurrence so repeated audio IDs (processed in
            # ascending line-number order) fill duplicates top-to-bottom.
            top_group.sort(key=lambda pair: pair[1]["index"])
            best_cand = top_group[0][1]
            best_score = top_group[0][0]
        else:
            # Tied candidates have different text - genuinely ambiguous.
            return None, best_score, True

    return best_cand, best_score, False


def process_chapter_file(chapter_path, all_transcripts):
    print(f"\n{'=' * 70}")
    print(f"Processing: {chapter_path}")
    print(f"{'=' * 70}")

    if not os.path.isfile(chapter_path):
        print(f"  ERROR: file not found, skipping.")
        return

    chapter_num = extract_chapter_num(chapter_path)

    if ENFORCE_CHAPTER_FILTER:
        if chapter_num is None:
            print(f"  WARNING: Could not determine chapter number from filename.")
            print(f"           Using ALL transcripts — cross-chapter matches possible.")
            transcripts = all_transcripts
        else:
            transcripts, dropped = filter_transcripts_for_chapter(
                all_transcripts, chapter_num
            )
            print(f"  Chapter {chapter_num} filter: "
                  f"{len(transcripts)} transcript(s) kept, "
                  f"{len(dropped)} from other chapters excluded.")
    else:
        transcripts = all_transcripts

    with open(chapter_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    existing_voice_tags = extract_existing_voice_tags(lines)
    skipped_already_inserted = 0

    candidates = extract_dialogue_candidates(lines)
    print(f"  Found {len(candidates)} dialogue candidate line(s).")

    used_indices = set()
    insertions = []
    ambiguous_log = []
    no_match_log = []
    no_char_log = []

    # Process audio IDs in ascending "_lineN" order. This matters for
    # duplicate-line resolution: when several audio IDs all match the same
    # repeated dialogue text, processing them in recording order and always
    # claiming the earliest unused occurrence gives a deterministic,
    # sensible top-to-bottom assignment instead of an arbitrary one.
    ordered_transcripts = sorted(
        transcripts.items(),
        key=lambda pair: extract_line_number(pair[0])
    )

    for audio_id, transcript in ordered_transcripts:
        if not transcript:
            continue

        if audio_id in existing_voice_tags:
            skipped_already_inserted += 1
            continue

        expected_char = extract_expected_character(audio_id, chapter_num)

        if ENFORCE_CHARACTER_MATCH and expected_char is None:
            no_char_log.append(audio_id)
            # Still proceed — will match against any speaker

        best_cand, score, is_ambiguous = find_best_match(
            transcript, candidates, used_indices, expected_char
        )

        if is_ambiguous:
            ambiguous_log.append((audio_id, transcript, score, expected_char))
            continue

        if best_cand is None:
            no_match_log.append((audio_id, transcript, score, expected_char))
            continue

        line_idx = best_cand["index"]

        if already_has_voice_above(lines, line_idx):
            existing_voice_line = lines[line_idx - 1].strip() if line_idx > 0 else ""
            print(f"  SKIP: audio.{audio_id} matched line {line_idx + 1}, "
                f"but it already has a voice tag ({existing_voice_line}).")
            continue

        used_indices.add(line_idx)
        insertions.append((line_idx, audio_id, score, best_cand["indent"], transcript))

    # Apply insertions from bottom to top
    insertions.sort(key=lambda x: x[0], reverse=True)

    for line_idx, audio_id, score, indent, transcript in insertions:
        if INCLUDE_TRANSCRIPT_COMMENT:
            voice_line = (
                f'{indent}voice audio.{audio_id}  '
                f'{COMMENT_MARKER} "{transcript}"\n'
            )
        else:
            voice_line = f'{indent}voice audio.{audio_id}\n'

        lines.insert(line_idx, voice_line)
        print(f"  INSERTED: voice \"audio.{audio_id}\" above line {line_idx + 1} "
            f"(confidence {score:.2f})")

    if skipped_already_inserted > 0:
        print(f"\n  NOTE: {skipped_already_inserted} voice line(s) were already "
            f"inserted in this file and were skipped without warning.")

    if no_char_log:
        print(f"\n  NOTE: {len(no_char_log)} audio ID(s) had no extractable "
            f"character prefix — matched against any speaker:")
        for a in no_char_log:
            print(f"    - audio.{a}")

    if ambiguous_log:
        print(f"\n  WARNING: {len(ambiguous_log)} transcript(s) had ambiguous "
            f"matches and were SKIPPED:")
        for audio_id, transcript, score, char in ambiguous_log:
            char_str = f" [char={char}]" if char else ""
            print(f'    - audio.{audio_id}  ("{transcript}"){char_str}  '
                f'best score {score:.2f}')

    if no_match_log:
        print(f"\n  NOTE: {len(no_match_log)} transcript(s) had no confident "
            f"match in this file:")
        for audio_id, transcript, score, char in no_match_log:
            char_str = f" [char={char}]" if char else ""
            print(f'    - audio.{audio_id}  ("{transcript}"){char_str}  '
                f'best score {score:.2f}')

    if not insertions and skipped_already_inserted == 0:
        print("  No insertions made in this file.")
        return

    if OVERWRITE_ORIGINAL:
        out_path = chapter_path
    else:
        base, ext = os.path.splitext(chapter_path)
        out_path = f"{base}_voiced{ext}"

    with open(out_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"\n  Wrote {len(insertions)} voice tag(s) to: {out_path}")


def main():
    if not os.path.isfile(AUDIO_RPY_PATH):
        print(f"ERROR: AUDIO_RPY_PATH does not exist: {AUDIO_RPY_PATH}")
        return

    all_transcripts = load_audio_transcripts(AUDIO_RPY_PATH)
    print(f"Loaded {len(all_transcripts)} transcript(s) from {AUDIO_RPY_PATH}.")

    if not all_transcripts:
        print("Nothing to match. Run voice_transcriber.py first.")
        return

    for chapter_path in CHAPTER_FILES:
        process_chapter_file(chapter_path, all_transcripts)

    print(f"\n{'=' * 70}")
    print("Done. Review the console warnings above, then check the "
        "'_voiced.rpy' output files before replacing your originals.")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()