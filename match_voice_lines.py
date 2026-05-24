"""
Dragon's Heart — Voice Line Matcher
=====================================
Reads dialogue_scan.txt and 01_voice_lines.rpy, shows you every
proposed match side by side, then asks yes/no before writing anything.

Missing .ogg files on disk are marked with # ? instead.

Usage: python match_voice_lines.py
       (edit the paths below, then run)
"""

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

SCAN_FILE  = r"D:\Renpy\dh_prologue ver 001\dialogue_scan.txt"
VOICE_FILE = r"D:\Renpy\dh_prologue ver 001\game\01_voice_lines.rpy"

# Root of your game folder — used to check if .ogg files exist on disk
GAME_ROOT  = r"D:\Renpy\dh_prologue ver 001\game"

# ─────────────────────────────────────────────────────────────────────────────

import re
import os
import shutil
from collections import defaultdict


# ── Alias map (define key -> scan key) ───────────────────────────────────────

ALIAS_MAP = {
    "elera":             "elara",
    "boy_ald":           "boy_ald",
    "girl_ald":          "girl_ald",
    "toatie":            "taotie",
    "toatie_roar":       "taotie",
    "vasily_laugh":      "vasily",
    "roboto1":           "roboto1",
    "roboto":            "roboto",
    "prosperity_dragon": "prosperity_dragon",
    "queen_ekaterina":   "queen_ekaterina",
    "female_guard":      "female_guard",
    "man_1":             "man_1",
    "man_2":             "man_2",
    "woman_3":           "woman_3",
}

def resolve_char(key):
    return ALIAS_MAP.get(key, key)


# ── Parsers ───────────────────────────────────────────────────────────────────

def parse_scan(path):
    """Returns (chapter_label, {char: [(lineno, preview), ...]})"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Scan file not found: {path}")

    chapter_label = None
    data = {}
    current_char = None
    char_re  = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*\(\d+\s+lines?\)')
    line_re  = re.compile(r'^\s+\*\s+(\d+)\s+"(.*)"')

    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip()
            if not line:
                continue
            if chapter_label is None:
                chapter_label = line.strip()
                continue
            if re.match(r'^-+$', line.strip()):
                continue
            m = char_re.match(line.strip())
            if m:
                current_char = m.group(1).lower()
                data[current_char] = []
                continue
            m = line_re.match(line)
            if m and current_char is not None:
                data[current_char].append((int(m.group(1)), m.group(2)))

    return chapter_label, data


def chapter_section_pattern(chapter_label):
    return re.compile(r'#\s*' + re.escape(chapter_label.upper()) + r'\s*$', re.IGNORECASE)


def char_key_from_define(line_text):
    m = re.match(r'\s*define\s+audio\.([a-zA-Z0-9_]+?)_ch\w+_line\d+', line_text)
    return m.group(1).lower() if m else None


def voice_line_number(line_text):
    m = re.search(r'_line(\d+)\s*=', line_text)
    return int(m.group(1)) if m else None


def ogg_path_from_define(line_text):
    m = re.search(r'"(audio/[^"]+\.ogg)"', line_text)
    return m.group(1) if m else None


def strip_existing_annotation(line_text):
    return re.sub(r'\s*#\s*[\d?]+\s*$', '', line_text)


# ── Build match plan ──────────────────────────────────────────────────────────

def build_plan(chapter_label, scan_data, voice_path, game_root):
    """
    Returns a list of:
    {
        "raw_index": int,        # index into original_lines
        "define_line": str,      # the define line text
        "char": str,
        "voice_num": int,
        "ogg_exists": bool,
        "script_line": int|None,
        "preview": str,
    }
    """
    section_pat = chapter_section_pattern(chapter_label)
    next_section_pat = re.compile(r'#\s*(CHAPTER|PROLOGUE|EPILOGUE)', re.IGNORECASE)

    line_cursors = {char: iter(entries) for char, entries in scan_data.items()}

    with open(voice_path, encoding="utf-8") as f:
        original_lines = f.readlines()

    in_target = False
    plan = []

    for idx, raw in enumerate(original_lines):
        line = raw.rstrip("\n")

        if section_pat.search(line):
            in_target = True
            continue

        if in_target and next_section_pat.search(line):
            if not section_pat.search(line):
                in_target = False

        if not in_target:
            continue

        key = char_key_from_define(line)
        if key is None:
            continue

        voice_num = voice_line_number(line)
        char = resolve_char(key)
        cursor = line_cursors.get(char)
        ogg_rel = ogg_path_from_define(line)
        ogg_exists = os.path.exists(os.path.join(game_root, ogg_rel)) if ogg_rel else False

        script_line, preview = None, ""
        if cursor is not None:
            entry = next(cursor, None)
            if entry:
                script_line, preview = entry

        plan.append({
            "raw_index":   idx,
            "define_line": line,
            "char":        char,
            "voice_num":   voice_num,
            "ogg_exists":  ogg_exists,
            "script_line": script_line,
            "preview":     preview,
        })

    return original_lines, plan


# ── Display ───────────────────────────────────────────────────────────────────

def display_plan(plan, chapter_label):
    print(f"\n{'=' * 70}")
    print(f"  Proposed matches for {chapter_label}")
    print(f"{'=' * 70}")

    current_char = None
    for entry in plan:
        char = entry["char"]
        if char != current_char:
            current_char = char
            print(f"\n  {char.upper()}")
            print(f"  {'-' * 40}")

        voice_num    = entry["voice_num"]
        script_line  = entry["script_line"]
        preview      = entry["preview"]
        ogg_exists   = entry["ogg_exists"]

        status = "OK " if ogg_exists else "MISSING OGG"

        if script_line:
            print(f"    voice line {voice_num:>3}  ->  script line {script_line:<6}  \"{preview}\"  [{status}]")
        else:
            print(f"    voice line {voice_num:>3}  ->  no match  [{status}]")

    print()


# ── Write ─────────────────────────────────────────────────────────────────────

def write_annotations(original_lines, plan, voice_path):
    backup_path = voice_path + ".bak"
    if not os.path.exists(backup_path):
        shutil.copy2(voice_path, backup_path)
        print(f"Backup saved: {backup_path}")

    for entry in plan:
        idx         = entry["raw_index"]
        line        = entry["define_line"]
        script_line = entry["script_line"]
        ogg_exists  = entry["ogg_exists"]

        clean = strip_existing_annotation(line)

        if not ogg_exists or script_line is None:
            original_lines[idx] = clean + "  # ?\n"
        else:
            original_lines[idx] = clean + f"  # {script_line}\n"

    with open(voice_path, "w", encoding="utf-8") as f:
        f.writelines(original_lines)

    annotated = sum(1 for e in plan if e["ogg_exists"] and e["script_line"])
    skipped   = sum(1 for e in plan if not e["ogg_exists"] or not e["script_line"])
    print(f"Done.  Annotated: {annotated}  Skipped/flagged: {skipped}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    chapter_label, scan_data = parse_scan(SCAN_FILE)
    print(f"Scan loaded: {chapter_label}  ({sum(len(v) for v in scan_data.values())} dialogue lines)")

    original_lines, plan = build_plan(chapter_label, scan_data, VOICE_FILE, GAME_ROOT)

    if not plan:
        print("No voice lines found for this chapter in the voice file.")
        return

    display_plan(plan, chapter_label)

    answer = input("Write these annotations to the voice file? (y/n): ").strip().lower()
    if answer == "y":
        write_annotations(original_lines, plan, VOICE_FILE)
    else:
        print("Cancelled. No changes made.")


if __name__ == "__main__":
    main()