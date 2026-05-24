"""
Dragon's Heart — Dialogue Line Scanner
=======================================
Scans a .rpy script file and finds every line where a character speaks.
Output shows each character, how many lines they have, line numbers,
and the first 5 words of each line for easier matching.

Usage: python scan_dialogue.py
(edit the FILE_PATH variable below, then run)
"""

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION — set the path to the .rpy file you want to scan
# ─────────────────────────────────────────────────────────────────────────────

FILE_PATH = r"D:\Renpy\dh_prologue ver 001\game\03_chapter_01.rpy"

# Output file — saved next to this script. Overwritten on every run.
import os
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dialogue_scan.txt")

# ─────────────────────────────────────────────────────────────────────────────
# Known character variable names in the script.
# Add or remove names here to match your game's character definitions.
# ─────────────────────────────────────────────────────────────────────────────

CHARACTERS = {
    "dorian", "yuxuan", "elara", "magnus", "svante", "chung", "aoi",
    "vasily", "cyrus", "olympia", "yk", "lucas", "sarah", "daniel",
    "jiang", "babala", "kristin", "lars", "pavel", "queen_ekaterina",
    "gustav", "sunwoo", "tianxun", "yuki", "boy_ald", "girl_ald",
    "prosperity_dragon", "taotie", "roboto", "roboto1", "tim", "weng",
    "niko", "man_1", "man_2", "woman_3", "female_guard", "door", "woman_2",
    # generic/narrator — uncomment if you want to track these too
    # "narrator", "mc",
}
# ─────────────────────────────────────────────────────────────────────────────

import re
from collections import defaultdict


def extract_preview(line_text):
    """Pull the first 5 words from the quoted dialogue text."""
    # Match the opening quote or paren-quote and grab everything after
    m = re.search(r'["(]"?(.+)', line_text)
    if not m:
        return ""
    raw = m.group(1).strip().strip('"\')')
    words = raw.split()
    preview = " ".join(words[:5])
    if len(words) > 5:
        preview += "..."
    return preview


def scan_file(path, output_path):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    # stores list of (lineno, preview) per character
    dialogue = defaultdict(list)
    pattern = re.compile(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s+[\(""]')

    with open(path, "r", encoding="utf-8") as f:
        for lineno, raw_line in enumerate(f, start=1):
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            match = pattern.match(raw_line)
            if not match:
                continue
            name = match.group(1).lower()
            if name in CHARACTERS:
                preview = extract_preview(line)
                dialogue[name].append((lineno, preview))

    chapter_name = detect_chapter_name(path)

    lines_out = []
    lines_out.append(chapter_name)
    lines_out.append("-" * len(chapter_name))

    if not dialogue:
        lines_out.append("No dialogue found.")
    else:
        for char in sorted(dialogue.keys()):
            entries = dialogue[char]
            lines_out.append(f"\n{char.capitalize()}: ({len(entries)} lines)")
            for lineno, preview in entries:
                lines_out.append(f"  * {lineno}  \"{preview}\"")

    output = "\n".join(lines_out) + "\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Done. Output written to: {output_path}")


def detect_chapter_name(path):
    """Try to read the label name from the file, fall back to the filename."""
    label_pattern = re.compile(r'^\s*label\s+(\w+)\s*:')
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                m = label_pattern.match(line)
                if m:
                    raw = m.group(1).replace("_", " ").title()
                    return raw
    except Exception:
        pass
    return os.path.splitext(os.path.basename(path))[0].replace("_", " ").title()


if __name__ == "__main__":
    scan_file(FILE_PATH, OUTPUT_PATH)