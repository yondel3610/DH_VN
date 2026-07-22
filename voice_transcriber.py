"""
voice_transcriber.py
=====================
Step 1 of the voice-line tagging pipeline for Dragon's Heart: Crimson Rebirth.

WHAT THIS DOES
--------------
1. Recursively scans a folder AND ALL ITS SUBFOLDERS for .ogg voice files
    (path set below in VOICE_FOLDER). Point this at a whole chapter folder
    (e.g. "game/audio/Chapter 3") and every .ogg under every subfolder
    (per-character folders, per-scene folders, however you've organized it)
    will be picked up in a single run.
2. Transcribes each file locally using faster-whisper (a CTranslate2-based
    reimplementation of Whisper — noticeably faster than openai-whisper on
    both CPU and GPU, especially with int8 quantization).
3. Takes the first 5 words of the transcript.
4. Finds the matching `define audio.xxx = "path/to/file.ogg"` line inside your
    central audio.rpy (path set below in AUDIO_RPY_PATH), matched by filename
    (subfolder location doesn't matter — matching is by basename only).
5. Writes (or updates) a `# transcript: <first 5 words>` comment at the end of
    that define line.

Re-running this script is SAFE and idempotent: it replaces its own
"# transcript: ..." comment instead of stacking duplicates. Any other
trailing comment you already had on that line (not starting with our
marker) is preserved and appended after a " | " separator.

REQUIREMENTS
------------
    pip install faster-whisper
    ffmpeg must be installed and on your PATH:
        - Windows: choco install ffmpeg   (or download from ffmpeg.org)
        - Mac:     brew install ffmpeg
        - Linux:   sudo apt install ffmpeg

WHY faster-whisper
-------------------
Same models as openai-whisper, run through a CTranslate2 backend instead.
Meaningfully faster for batch/mass transcription like this script does —
often 2-4x faster on CPU with int8 quantization, and faster on GPU too.

FIRST RUN NOTE
--------------
The model weights download once on first use (a few hundred MB for
"base"). This requires an internet connection ONCE; transcription itself
runs fully offline afterward.

HOW TO USE
----------
1. Edit VOICE_FOLDER and AUDIO_RPY_PATH below to match your project.
    VOICE_FOLDER can be a chapter folder containing subfolders — everything
    underneath is scanned automatically.
2. Run:  python voice_transcriber.py
3. Check the console output for any WARNINGS (unmatched files, missing
    defines, etc.) and resolve them manually if needed.
4. Open audio.rpy and confirm the "# transcript:" comments look correct.
"""

import os
import re
import sys

# =============================================================================
# CONFIG — EDIT THESE TWO PATHS FOR YOUR PROJECT
# =============================================================================

# Folder containing the .ogg voice files to transcribe.
VOICE_FOLDER = r"game/audio/Chapter 5"

# Path to your central audio.rpy file containing all `define audio.xxx = ...` lines.
AUDIO_RPY_PATH = r"game/01_voice_lines.rpy"

# Whisper model size. Options (fastest -> most accurate):
#   "tiny", "base", "small", "medium", "large-v3"
# "tiny" or "base" is recommended here — voice lines are short, and mass
# transcribing a whole chapter folder adds up fast, so smaller = faster.
WHISPER_MODEL = "base"

# faster-whisper compute type. "int8" is the fastest option on CPU by a wide
# margin with only a small accuracy trade-off — good fit for short lines.
# If you have a CUDA GPU, change DEVICE to "cuda" and this can be "float16"
# for both speed and accuracy.
COMPUTE_TYPE = "int8"

# "cpu" or "cuda" (if you have an NVIDIA GPU with CUDA installed).
DEVICE = "cpu"

# Number of words to keep from the transcript.
WORD_COUNT = 5

# If False, the script will SKIP files that already have a "# transcript:" 
# comment in audio.rpy. Set to True if you want to force re-transcription.
OVERWRITE_EXISTING = False

# Our comment marker, so re-runs can find and replace their own prior output
# instead of appending duplicates.
COMMENT_MARKER = "# transcript:"

# =============================================================================
# END CONFIG
# =============================================================================


def load_whisper():
    """Import and load the faster-whisper model, with a helpful error if missing."""
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print(
            "ERROR: faster-whisper is not installed.\n"
            "Install it with:  pip install faster-whisper\n"
            "You also need ffmpeg installed and on your PATH."
        )
        sys.exit(1)

    print(f"Loading faster-whisper model '{WHISPER_MODEL}' "
          f"(device={DEVICE}, compute_type={COMPUTE_TYPE})...")
    try:
        model = WhisperModel(WHISPER_MODEL, device=DEVICE, compute_type=COMPUTE_TYPE)
    except Exception as e:
        print(f"ERROR loading faster-whisper model: {e}")
        print("Make sure ffmpeg is installed and on your PATH.")
        sys.exit(1)

    return model


def transcribe_file(model, filepath):
    """Transcribe a single .ogg file and return the first WORD_COUNT words."""
    try:
        # beam_size=1 is the fastest greedy-decoding option; fine for short
        # voice lines where we only need the first few words anyway.
        segments, _info = model.transcribe(filepath, beam_size=1)
        text = " ".join(segment.text for segment in segments).strip()
    except Exception as e:
        print(f"  WARNING: failed to transcribe {os.path.basename(filepath)}: {e}")
        return None

    if not text:
        return None

    words = text.split()
    snippet = " ".join(words[:WORD_COUNT])
    return snippet


def build_define_index(audio_rpy_lines):
    """
    Parse audio.rpy and build a mapping of:
        basename_of_ogg_file -> line_index_in_file

    Matches lines like:
        define audio.some_name = "audio/voice/dorian_001.ogg"
        define audio.some_name = "audio/voice/dorian_001.ogg"  # some existing comment
    """
    define_pattern = re.compile(
        r'^\s*define\s+audio\.\w+\s*=\s*"([^"]+\.ogg)"'
    )

    index = {}
    for i, line in enumerate(audio_rpy_lines):
        match = define_pattern.match(line)
        if match:
            path_in_define = match.group(1)
            basename = os.path.basename(path_in_define)
            if basename in index:
                print(
                    f"  WARNING: duplicate define found for '{basename}' "
                    f"at lines {index[basename] + 1} and {i + 1}. "
                    f"Using the first occurrence."
                )
                continue
            index[basename] = i

    return index


def update_comment_on_line(line, new_snippet):
    """
    Given a single line from audio.rpy and a new transcript snippet,
    return the line with the comment updated/added.

    - If the line already has our COMMENT_MARKER, replace just that part.
    - If it has some other comment, keep it and append ours after " | ".
    - If it has no comment, add one.
    """
    line = line.rstrip("\n")

    # Does this line already contain our marker?
    if COMMENT_MARKER in line:
        # Replace everything from our marker onward.
        base = line.split(COMMENT_MARKER)[0].rstrip()
        return f'{base}  {COMMENT_MARKER} "{new_snippet}"\n'

    # Does it have some other, non-ours comment?
    hash_index = line.find("#")
    if hash_index != -1:
        base = line[:hash_index].rstrip()
        existing_comment = line[hash_index:].rstrip()
        return f'{base}  {existing_comment} | {COMMENT_MARKER} "{new_snippet}"\n'

    # No comment at all yet.
    return f'{line.rstrip()}  {COMMENT_MARKER} "{new_snippet}"\n'


def main():
    if not os.path.isdir(VOICE_FOLDER):
        print(f"ERROR: VOICE_FOLDER does not exist: {VOICE_FOLDER}")
        print("Edit the VOICE_FOLDER constant at the top of this script.")
        sys.exit(1)

    if not os.path.isfile(AUDIO_RPY_PATH):
        print(f"ERROR: AUDIO_RPY_PATH does not exist: {AUDIO_RPY_PATH}")
        print("Edit the AUDIO_RPY_PATH constant at the top of this script.")
        sys.exit(1)

    # Recursively walk VOICE_FOLDER and every subfolder underneath it.
    ogg_filepaths = {}
    duplicate_basenames = []

    for root, _dirs, files in os.walk(VOICE_FOLDER):
        for filename in files:
            if not filename.lower().endswith(".ogg"):
                continue
            if filename in ogg_filepaths:
                duplicate_basenames.append(filename)
                continue
            ogg_filepaths[filename] = os.path.join(root, filename)

    if duplicate_basenames:
        print(f"WARNING: {len(duplicate_basenames)} filename(s) appeared in "
              f"more than one subfolder under {VOICE_FOLDER}. Only the first "
              f"one found is used for each:")
        for name in duplicate_basenames:
            print(f"    - {name}")

    ogg_files = list(ogg_filepaths.keys())

    if not ogg_files:
        print(f"No .ogg files found in {VOICE_FOLDER} or its subfolders. Nothing to do.")
        return

    print(f"Found {len(ogg_files)} .ogg file(s) under {VOICE_FOLDER} (including subfolders).\n")

    with open(AUDIO_RPY_PATH, "r", encoding="utf-8") as f:
        original_lines = f.readlines()

    audio_lines = list(original_lines)

    define_index = build_define_index(audio_lines)
    print(f"Found {len(define_index)} `define audio.xxx` line(s) in {AUDIO_RPY_PATH}.\n")

    # We only need to load the heavy Whisper model if there are actually 
    # files that need transcribing.
    model = None 
    updated_count = 0
    unmatched_files = []
    skipped_count = 0

    for ogg_filename in sorted(ogg_files):
        filepath = ogg_filepaths[ogg_filename]

        if ogg_filename not in define_index:
            unmatched_files.append(ogg_filename)
            continue

        line_idx = define_index[ogg_filename]
        current_line = audio_lines[line_idx]

        # --- NEW: Skip if already transcribed ---
        if not OVERWRITE_EXISTING and COMMENT_MARKER in current_line:
            print(f"Skipping (already transcribed): {ogg_filename}")
            skipped_count += 1
            continue
        # --- END NEW ---

        # Lazy-load the model only when we hit the first file that needs it
        if model is None:
            model = load_whisper()

        print(f"Transcribing: {ogg_filename}")
        snippet = transcribe_file(model, filepath)

        if snippet is None:
            print(f"  WARNING: no usable transcript for {ogg_filename}, skipping.")
            continue

        audio_lines[line_idx] = update_comment_on_line(audio_lines[line_idx], snippet)
        print(f'  -> "{snippet}"')
        updated_count += 1

    if skipped_count > 0:
        print(f"\nSkipped {skipped_count} file(s) that already had transcripts.")

    if unmatched_files:
        print(f"\nWARNING: {len(unmatched_files)} .ogg file(s) had no matching "
            f"`define audio.xxx` entry in {AUDIO_RPY_PATH}:")
        for f in unmatched_files:
            print(f"    - {f}")
        print("These were skipped. Add a define for them if they should be used.")

    unused_defines = set(define_index.keys()) - set(ogg_files)
    if unused_defines:
        print(f"\nWARNING: {len(unused_defines)} define(s) in {AUDIO_RPY_PATH} "
            f"point to files not found in {VOICE_FOLDER}:")
        for d in sorted(unused_defines):
            print(f"    - {d}")

    # If no lines were updated, don't bother writing a backup and rewriting the file.
    if updated_count == 0:
        print("\nNo new transcriptions were made. File left untouched.")
        return

    # Write a backup of the ORIGINAL (pre-edit) content first.
    backup_path = AUDIO_RPY_PATH + ".bak"
    with open(backup_path, "w", encoding="utf-8") as f:
        f.writelines(original_lines)

    # Now write the updated content over the real file.
    with open(AUDIO_RPY_PATH, "w", encoding="utf-8") as f:
        f.writelines(audio_lines)

    print(f"\nDone. Updated {updated_count} define line(s) in {AUDIO_RPY_PATH}.")
    print(f"A backup of the file before changes was saved to: {backup_path}")


if __name__ == "__main__":
    main()