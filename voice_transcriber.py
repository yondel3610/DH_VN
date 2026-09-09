"""
voice_transcriber.py
=====================
Step 1 of the voice-line tagging pipeline for Dragon's Heart: Crimson Rebirth.

WHAT THIS DOES
--------------
1. Recursively scans a folder AND ALL ITS SUBFOLDERS (including character 
   route subfolders like Dorian's) for .ogg voice files.
2. Transcribes each file locally using faster-whisper.
3. Takes the first 5 words of the transcript.
4. Finds the matching `define audio.xxx = "path/to/file.ogg"` line inside your
   central audio.rpy, matched by filename.
5. Writes (or updates) a `# transcript: <first 5 words>` comment at the end of
   that define line.

REQUIREMENTS
------------
    pip install faster-whisper
    ffmpeg must be installed and on your PATH.

HOW TO USE
----------
1. Ensure VOICE_FOLDER points to your chapter folder (e.g. "game/audio/Chapter 10").
2. Run:  python voice_transcriber.py
"""

import os
import re
import sys

# =============================================================================
# CONFIG — EDIT THESE TWO PATHS FOR YOUR PROJECT
# =============================================================================

# Folder containing the .ogg voice files to transcribe.
# This will automatically scan ALL subfolders (character folders, route folders, etc.)
VOICE_FOLDER = r"game/audio/Chapter 6"

# Path to your central audio.rpy file containing all `define audio.xxx = ...` lines.
AUDIO_RPY_PATH = r"game/01_voice_lines.rpy"

# Whisper model size. Options (fastest -> most accurate):
#   "tiny", "base", "small", "medium", "large-v3"
WHISPER_MODEL = "base"

# faster-whisper compute type. "int8" is fastest on CPU.
COMPUTE_TYPE = "int8"

# "cpu" or "cuda" (if you have an NVIDIA GPU with CUDA installed).
DEVICE = "cpu"

# Number of words to keep from the transcript.
WORD_COUNT = 8

# If False, skips files that already have a "# transcript:" comment.
OVERWRITE_EXISTING = False

# Our comment marker
COMMENT_MARKER = "# transcript:"

# =============================================================================
# END CONFIG
# =============================================================================


def load_whisper():
    """Import and load the faster-whisper model."""
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
    """
    line = line.rstrip("\n")

    if COMMENT_MARKER in line:
        base = line.split(COMMENT_MARKER)[0].rstrip()
        return f'{base}  {COMMENT_MARKER} "{new_snippet}"\n'

    hash_index = line.find("#")
    if hash_index != -1:
        base = line[:hash_index].rstrip()
        existing_comment = line[hash_index:].rstrip()
        return f'{base}  {existing_comment} | {COMMENT_MARKER} "{new_snippet}"\n'

    return f'{line.rstrip()}  {COMMENT_MARKER} "{new_snippet}"\n'


def main():
    if not os.path.isdir(VOICE_FOLDER):
        print(f"ERROR: VOICE_FOLDER does not exist: {VOICE_FOLDER}")
        sys.exit(1)

    if not os.path.isfile(AUDIO_RPY_PATH):
        print(f"ERROR: AUDIO_RPY_PATH does not exist: {AUDIO_RPY_PATH}")
        sys.exit(1)

    # Recursively walk VOICE_FOLDER and every subfolder underneath it.
    # This includes Character Folders -> Route Subfolders.
    ogg_filepaths = {}
    duplicate_basenames = []

    print(f"Scanning '{VOICE_FOLDER}' and all subfolders for .ogg files...")
    for root, _dirs, files in os.walk(VOICE_FOLDER):
        for filename in files:
            if not filename.lower().endswith(".ogg"):
                continue
            if filename in ogg_filepaths:
                duplicate_basenames.append(filename)
                continue
            
            full_path = os.path.join(root, filename)
            # Store relative path for cleaner console output
            rel_path = os.path.relpath(full_path, VOICE_FOLDER)
            ogg_filepaths[filename] = (full_path, rel_path)

    if duplicate_basenames:
        print(f"\nWARNING: {len(duplicate_basenames)} filename(s) appeared in "
              f"more than one subfolder. Only the first one found is used:")
        for name in duplicate_basenames:
            print(f"    - {name}")

    ogg_files = list(ogg_filepaths.keys())

    if not ogg_files:
        print(f"No .ogg files found in {VOICE_FOLDER} or its subfolders. Nothing to do.")
        return

    print(f"Found {len(ogg_files)} .ogg file(s) total.\n")

    with open(AUDIO_RPY_PATH, "r", encoding="utf-8") as f:
        original_lines = f.readlines()

    audio_lines = list(original_lines)

    define_index = build_define_index(audio_lines)
    print(f"Found {len(define_index)} `define audio.xxx` line(s) in {AUDIO_RPY_PATH}.\n")

    model = None 
    updated_count = 0
    unmatched_files = []
    skipped_count = 0

    # Sort by relative path so files in the same folders are processed together
    sorted_ogg_files = sorted(ogg_files, key=lambda f: ogg_filepaths[f][1])

    for ogg_filename in sorted_ogg_files:
        filepath, rel_path = ogg_filepaths[ogg_filename]

        if ogg_filename not in define_index:
            unmatched_files.append(rel_path)
            continue

        line_idx = define_index[ogg_filename]
        current_line = audio_lines[line_idx]

        if not OVERWRITE_EXISTING and COMMENT_MARKER in current_line:
            print(f"Skipping (already transcribed): {rel_path}")
            skipped_count += 1
            continue

        if model is None:
            model = load_whisper()

        print(f"Transcribing: {rel_path}")
        snippet = transcribe_file(model, filepath)

        if snippet is None:
            print(f"  WARNING: no usable transcript for {rel_path}, skipping.")
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

    if updated_count == 0:
        print("\nNo new transcriptions were made. File left untouched.")
        return

    backup_path = AUDIO_RPY_PATH + ".bak"
    with open(backup_path, "w", encoding="utf-8") as f:
        f.writelines(original_lines)

    with open(AUDIO_RPY_PATH, "w", encoding="utf-8") as f:
        f.writelines(audio_lines)

    print(f"\nDone. Updated {updated_count} define line(s) in {AUDIO_RPY_PATH}.")
    print(f"A backup of the file before changes was saved to: {backup_path}")


if __name__ == "__main__":
    main()