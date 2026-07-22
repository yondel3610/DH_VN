"""
voice_tag_remover.py
====================
A simple script to remove all `voice audio.xxx` lines from chapter .rpy files.

WHAT THIS DOES
--------------
1. Scans one or more chapter .rpy files and removes ALL `voice audio.xxx` lines.
2. Writes a new file with "_unvoiced" suffix (or overwrites original if configured).

WHY USE THIS
------------
- If you want to start fresh with voice tagging
- If you're rolling back voice tags to re-run the inserter
- If you accidentally inserted voice tags into the wrong file

SAFETY
------
By default this script does NOT overwrite your original file. It writes a
new file next to it with a "_unvoiced" suffix (e.g. chapter_05.rpy ->
chapter_05_unvoiced.rpy) so you can diff/review before replacing.
Set OVERWRITE_ORIGINAL = True below once you trust the output.

HOW TO USE
----------
1. Edit CHAPTER_FILES below to point to your chapter .rpy files.
2. Run:  python voice_tag_remover.py
3. Review the console output.
4. Open the _unvoiced.rpy file(s), confirm the voice lines are removed.
"""

import os
import re

# =============================================================================
# CONFIG — EDIT THESE FOR YOUR PROJECT
# =============================================================================

# List of chapter files to scan and remove voice tags from.
CHAPTER_FILES = [
    r"game/04_chapter_02.rpy",
    # Add more files as needed
]

# If True, overwrites the original chapter file directly instead of writing
# a "_unvoiced.rpy" copy. Leave False until you've reviewed the output.
OVERWRITE_ORIGINAL = False

# =============================================================================
# END CONFIG
# =============================================================================


def remove_voice_tags(lines):
    """
    Remove all voice audio.xxx lines from the given lines.
    Returns (new_lines, count_removed, removed_lines).
    """
    new_lines = []
    removed_count = 0
    removed_lines = []
    
    # Pattern to match voice lines with optional indentation
    voice_pattern = re.compile(r'^\s*voice\s+audio\.\w+\s*$')
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a voice line
        if voice_pattern.match(line.rstrip()):
            removed_count += 1
            removed_lines.append(line.rstrip())
            i += 1
            continue
        
        new_lines.append(line)
        i += 1
    
    return new_lines, removed_count, removed_lines


def process_chapter_file(chapter_path):
    """Remove voice tags from a single chapter file."""
    
    print(f"\n{'=' * 70}")
    print(f"Processing: {chapter_path}")
    print(f"{'=' * 70}")

    if not os.path.isfile(chapter_path):
        print(f"  ERROR: file not found, skipping.")
        return

    with open(chapter_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines, removed_count, removed_lines = remove_voice_tags(lines)

    if removed_count == 0:
        print("  No voice tags found in this file.")
        return

    print(f"  Removed {removed_count} voice tag(s):")
    for removed in removed_lines[:10]:  # Show first 10 as preview
        print(f"    - {removed}")
    if removed_count > 10:
        print(f"    ... and {removed_count - 10} more")

    if OVERWRITE_ORIGINAL:
        out_path = chapter_path
        print(f"  WARNING: Overwriting original file!")
    else:
        base, ext = os.path.splitext(chapter_path)
        out_path = f"{base}_unvoiced{ext}"

    with open(out_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"  Wrote cleaned file to: {out_path}")


def main():
    print("=" * 70)
    print("VOICE TAG REMOVER")
    print("=" * 70)
    print(f"OVERWRITE_ORIGINAL: {OVERWRITE_ORIGINAL}")
    print(f"Files to process: {len(CHAPTER_FILES)}")
    print("=" * 70)

    for chapter_path in CHAPTER_FILES:
        process_chapter_file(chapter_path)

    print(f"\n{'=' * 70}")
    print("Done!")
    if not OVERWRITE_ORIGINAL:
        print("Check the '_unvoiced.rpy' output files before replacing your originals.")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()