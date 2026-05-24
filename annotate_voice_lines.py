"""
Dragon's Heart — Voice Line Annotator
======================================
Reads the dialogue_scan.txt output and annotates the matching character's
voice lines in 01_voice_lines.rpy with the corresponding script line numbers.

Only modifies lines under the chapter section that matches the scan output.
All other chapters are left untouched.

Usage: python annotate_voice_lines.py (edit the paths below, then run)
"""
import re
import os
# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

# The dialogue_scan.txt produced by scan_dialogue.py
SCAN_FILE   = r"D:\Renpy\dh_prologue ver 001\dialogue_scan.txt"

# Your full voice lines .rpy file
VOICE_FILE  = r"D:\Renpy\dh_prologue ver 001\game\01_voice_lines.rpy"

# The voice file is edited in place. A backup is saved alongside it on first run.
# ── Helpers ──────────────────────────────────────────────────────────────────
def parse_scan(scan_path):
    """
    Parse dialogue_scan.txt into:
      chapter_label : str  e.g. "Chapter 1"
      data          : dict  { "elara": [218, 219, ...], "dorian": [...], ... }
    """
    if not os.path.exists(scan_path):
        raise FileNotFoundError(f"Scan file not found: {scan_path}")

    chapter_label = None
    data = {}
    current_char = None

    line_re  = re.compile(r'^\s+\*\s+(\d+)')
    char_re  = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*\((\d+)\s+lines?\)')

    with open(scan_path, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip()
            if not line:
                continue

            # First non-blank line is the chapter name
            if chapter_label is None:
                chapter_label = line.strip()
                continue

            # Separator line (dashes) — skip
            if re.match(r'^-+$', line.strip()):
                continue

            # Character header e.g. "Elara: (68 lines)"
            m = char_re.match(line.strip())
            if m:
                current_char = m.group(1).lower()
                data[current_char] = []
                continue

            # Line number entry e.g. "  * 218"
            m = line_re.match(line)
            if m and current_char is not None:
                data[current_char].append(int(m.group(1)))

    return chapter_label, data


def chapter_section_pattern(chapter_label):
    """
    Build a regex that matches the chapter section header comment in the
    voice lines file, e.g. for "Chapter 1" it matches lines like:
        # CHAPTER 1
    """
    # "Chapter 1" -> "CHAPTER 1"
    upper = chapter_label.upper()
    # Also accept variations like "CHAPTER 1" / "Chapter 1" in the comment
    escaped = re.escape(upper)
    return re.compile(r'#\s*' + escaped + r'\s*$', re.IGNORECASE)


def voice_line_number(line_text):
    """
    Extract the sequential voice line number from a define statement.
    e.g. "define audio.elera_ch1_line42 = ..." -> 42
    Returns None if not a voice line define.
    """
    m = re.search(r'_line(\d+)\s*=', line_text)
    if m:
        return int(m.group(1))
    return None


def char_key_from_define(line_text):
    """
    Extract the character key from a define statement.
    e.g. "define audio.elera_ch1_line1 = ..." -> "elera"
    We strip the chapter suffix: elera_ch1 -> elera
    """
    m = re.match(r'\s*define\s+audio\.([a-zA-Z0-9_]+?)_ch\d+_line\d+', line_text)
    if m:
        return m.group(1).lower()
    return None


def strip_existing_annotation(line_text):
    """Remove any previously added # NNN comment at end of line."""
    return re.sub(r'\s*#\s*\d+\s*$', '', line_text)


# ── Normalise character key aliases ──────────────────────────────────────────
# Maps the key as it appears in the define (e.g. "elera") to the canonical
# name used in the scan output (e.g. "elara").  Add entries here if needed.

ALIAS_MAP = {
    "elera":            "elara",
    "boy_ald":          "boy_ald",
    "girl_ald":         "girl_ald",
    "toatie":           "taotie",
    "toatie_roar":      "taotie",
    "vasily_laugh":     "vasily",
    "roboto1":          "roboto1",
    "roboto":          "roboto",
    "prosperity_dragon":"prosperity_dragon",
    "queen_ekaterina":  "queen_ekaterina",
    "female_guard":     "female_guard",
    "man_1":             "man_1",
    "man_2":             "man_2",
    "woman_3":           "woman_3",
}


def resolve_char(key):
    return ALIAS_MAP.get(key, key)


# ── Main ─────────────────────────────────────────────────────────────────────

def annotate(scan_path, voice_path):
    chapter_label, scan_data = parse_scan(scan_path)
    print(f"Scan loaded: {chapter_label}")
    for c, lines in scan_data.items():
        print(f"  {c}: {len(lines)} lines")

    if not os.path.exists(voice_path):
        raise FileNotFoundError(f"Voice file not found: {voice_path}")

    # Make a backup before first edit (only if backup doesn't exist yet)
    # backup_path = voice_path + ".bak"
    # if not os.path.exists(backup_path):
    #     import shutil
    #     shutil.copy2(voice_path, backup_path)
    #     print(f"Backup saved: {backup_path}")

    section_pat = chapter_section_pattern(chapter_label)
    next_section_pat = re.compile(
        r'#\s*(CHAPTER|PROLOGUE|EPILOGUE)',
        re.IGNORECASE
    )

    line_cursors = {char: iter(nums) for char, nums in scan_data.items()}

    with open(voice_path, encoding="utf-8") as f:
        original_lines = f.readlines()

    in_target_chapter = False
    output_lines = []
    annotated = 0
    unmatched = 0

    for raw in original_lines:
        line = raw.rstrip("\n")

        if section_pat.search(line):
            in_target_chapter = True
            output_lines.append(line)
            continue

        if in_target_chapter and next_section_pat.search(line):
            if not section_pat.search(line):
                in_target_chapter = False

        if in_target_chapter:
            key = char_key_from_define(line)
            if key is not None:
                voice_num = voice_line_number(line)
                char = resolve_char(key)
                cursor = line_cursors.get(char)

                if cursor is not None and voice_num is not None:
                    script_line = next(cursor, None)
                    clean = strip_existing_annotation(line)
                    if script_line is not None:
                        output_lines.append(f"{clean}  # {script_line}")
                        annotated += 1
                    else:
                        output_lines.append(clean + "  # ?")
                        unmatched += 1
                    continue

        output_lines.append(line)

    with open(voice_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines) + "\n")

    print(f"\nDone.")
    print(f"  Annotated : {annotated} lines")
    print(f"  Unmatched : {unmatched} lines (marked with # ?)")
    print(f"  File updated: {voice_path}")


if __name__ == "__main__":
    annotate(SCAN_FILE, VOICE_FILE)