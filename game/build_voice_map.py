#!/usr/bin/env python3
"""
build_voice_map.py
-------------------------------------------------------------------
Standalone tool (plain Python, no Ren'Py needed) that scans your
game's .rpy source files, finds every dialogue line, and builds two
JSON files consumed at runtime by 01_voice_autoplay.rpy:

    1. voice_line_ids.json
        "relative/path/script.rpy:123" -> "a1b2c3d4e5f6"
        Regenerated FRESH every run, so it always matches the CURRENT
        line numbers in your scripts. This is what lets the runtime
        hook find "what line is currently showing" -> "what ID is that".

    2. voice_map.json
        "a1b2c3d4e5f6" -> "audio/voice/a1b2c3d4e5f6.ogg"
        Only contains entries for which a matching audio file was
        actually found on disk. Lines with no recorded voice yet are
        simply absent, and play silently (no error).

    3. voice_report.csv
        A spreadsheet-friendly list of every dialogue line, its ID,
        character, a text preview, and whether audio exists yet.
        Hand this to voice actors / use it to track recording progress.

WHY A HASH INSTEAD OF LINE NUMBERS DIRECTLY?
-------------------------------------------------------------------
Line numbers shift constantly as you edit unrelated parts of a file.
If a voice file were tied directly to "line 340", inserting a single
line above it anywhere in the file would silently break the mapping.

Instead, each line's ID is a hash of:
    (file path, character tag, exact dialogue text, duplicate-index)

This ID only changes if the ACTUAL DIALOGUE TEXT changes (in which
case you needed a new recording anyway) or if the same character says
the exact same line more than once and their relative order in the
file changes. Unrelated edits elsewhere in the file, or in other
files, never affect existing IDs.

You still get a fresh, accurate {file:line -> ID} table every run
(voice_line_ids.json), so runtime lookups always match current line
numbers -- you just never have to maintain that table by hand.

USAGE
-------------------------------------------------------------------
    python build_voice_map.py /path/to/your/game

    Optional flags:
        --game-dir PATH        (default: <project>/game)
        --voice-dir PATH        Folder to search for recorded audio,
                                relative to game dir.
                                (default: audio/voice)
        --extensions ogg,mp3,wav,opus
                                Audio extensions to look for.
        --report FILE            Output CSV path (default: voice_report.csv,
                                written inside game dir)

Recorded audio files should be named "<ID>.<ext>", e.g.:
    game/audio/voice/a1b2c3d4e5f6.ogg

After recording, just re-run this script -- no manual bookkeeping.
-------------------------------------------------------------------
"""

import argparse
import csv
import hashlib
import json
import os
import re
import sys

# -----------------------------------------------------------------
# Keywords that can appear at the start of a Ren'Py statement line
# and look superficially like "identifier followed by a string" but
# are NOT dialogue. We skip lines starting with these.
# -----------------------------------------------------------------
NON_CHARACTER_KEYWORDS = {
    "if", "elif", "else", "while", "menu", "label", "jump", "call",
    "return", "scene", "show", "hide", "with", "play", "stop", "queue",
    "pause", "window", "define", "default", "python", "init", "transform",
    "screen", "style", "translate", "voice", "image", "persistent",
    "for", "in", "pass", "break", "continue", "extend", "nvl", "onlayer",
    "zorder", "at", "behind", "as", "config", "renpy", "$",
}

# Matches:  optional_identifier  "quoted text with \" escapes"  optional_trailer
DIALOGUE_RE = re.compile(
    r'^(?P<indent>\s*)'
    r'(?:(?P<who>[A-Za-z_][A-Za-z0-9_.]*)\s+)?'
    r'"(?P<text>(?:[^"\\]|\\.)*)"'
    r'(?P<trailer>.*)$'
)


def find_rpy_files(game_dir):
    for root, _dirs, files in os.walk(game_dir):
        for fn in files:
            if fn.endswith(".rpy"):
                yield os.path.join(root, fn)


def is_dialogue_line(who, trailer):
    """Filter out menu choices and non-dialogue matches."""
    trailer = trailer.strip()

    # Menu choices look like:   "Some option text":
    # i.e. the trailer starts with a colon.
    if trailer.startswith(":"):
        return False

    if who is not None and who in NON_CHARACTER_KEYWORDS:
        return False

    return True


def unescape(text):
    return text.replace('\\"', '"').replace("\\'", "'").replace("\\n", "\n")


def scan_file(path, rel_path):
    """
    Returns a list of dicts:
        {relpath, linenumber, who, text}
    in file order, for every dialogue line found.
    """
    results = []
    with open(path, "r", encoding="utf-8") as f:
        for lineno, raw_line in enumerate(f, start=1):
            stripped = raw_line.strip()
            if not stripped or stripped.startswith("#"):
                continue

            m = DIALOGUE_RE.match(raw_line)
            if not m:
                continue

            who = m.group("who")
            trailer = m.group("trailer")

            if not is_dialogue_line(who, trailer):
                continue

            text = unescape(m.group("text"))
            if not text.strip():
                continue

            results.append({
                "relpath": rel_path,
                "linenumber": lineno,
                "who": who or "narrator",
                "text": text,
            })

    return results


def compute_stable_id(relpath, who, text, dup_index):
    raw = "\x1f".join([relpath, who, text, str(dup_index)])
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:12]


def build(game_dir, voice_dir, extensions, report_path):
    game_dir = os.path.abspath(game_dir)
    voice_dir_abs = os.path.join(game_dir, voice_dir)

    all_lines = []
    for path in sorted(find_rpy_files(game_dir)):
        rel_path = os.path.relpath(path, game_dir).replace(os.sep, "/")
        # Ren'Py reports filenames relative to the project root and
        # usually prefixed with "game/" -- match that convention.
        renpy_relpath = "game/" + rel_path
        all_lines.extend(scan_file(path, renpy_relpath))

    # --- assign stable IDs, tracking duplicate occurrences per file ---
    seen_counts = {}
    voice_line_ids = {}
    rows_for_report = []

    for entry in all_lines:
        dup_key = (entry["relpath"], entry["who"], entry["text"])
        dup_index = seen_counts.get(dup_key, 0)
        seen_counts[dup_key] = dup_index + 1

        line_id = compute_stable_id(
            entry["relpath"], entry["who"], entry["text"], dup_index
        )

        key = "%s:%d" % (entry["relpath"], entry["linenumber"])
        voice_line_ids[key] = line_id

        rows_for_report.append({
            "id": line_id,
            "file": entry["relpath"],
            "line": entry["linenumber"],
            "character": entry["who"],
            "text_preview": (entry["text"][:80] + "...")
                if len(entry["text"]) > 80 else entry["text"],
        })

    # --- scan for existing audio files ---
    available = {}
    if os.path.isdir(voice_dir_abs):
        for root, _dirs, files in os.walk(voice_dir_abs):
            for fn in files:
                stem, ext = os.path.splitext(fn)
                if ext.lstrip(".").lower() in extensions:
                    rel_audio = os.path.relpath(
                        os.path.join(root, fn), game_dir
                    ).replace(os.sep, "/")
                    available[stem] = rel_audio

    voice_map = {}
    found_count = 0
    for row in rows_for_report:
        audio_path = available.get(row["id"])
        if audio_path:
            voice_map[row["id"]] = audio_path
            row["has_audio"] = "yes"
            found_count += 1
        else:
            row["has_audio"] = "no"

    # --- write outputs ---
    ids_path = os.path.join(game_dir, "voice_line_ids.json")
    map_path = os.path.join(game_dir, "voice_map.json")

    with open(ids_path, "w", encoding="utf-8") as f:
        json.dump(voice_line_ids, f, indent=2, ensure_ascii=False)

    with open(map_path, "w", encoding="utf-8") as f:
        json.dump(voice_map, f, indent=2, ensure_ascii=False)

    report_full_path = os.path.join(game_dir, report_path)
    with open(report_full_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["id", "file", "line", "character",
                           "text_preview", "has_audio"]
        )
        writer.writeheader()
        writer.writerows(rows_for_report)

    print("Scanned %d dialogue lines across .rpy files." % len(rows_for_report))
    print("  Voice files found:     %d" % found_count)
    print("  Missing voice files:   %d" % (len(rows_for_report) - found_count))
    print()
    print("Wrote:")
    print("  %s" % ids_path)
    print("  %s" % map_path)
    print("  %s" % report_full_path)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                      formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("project_dir", nargs="?", default=".",
                         help="Path to your Ren'Py project (containing a 'game' folder), "
                              "or pass the game folder itself with --game-dir.")
    parser.add_argument("--game-dir", default=None,
                         help="Explicit path to the 'game' folder. "
                              "Defaults to <project_dir>/game.")
    parser.add_argument("--voice-dir", default="audio/voice",
                         help="Folder (relative to game dir) to search for recorded audio. "
                              "Default: audio/voice")
    parser.add_argument("--extensions", default="ogg,mp3,wav,opus",
                         help="Comma-separated audio extensions to look for.")
    parser.add_argument("--report", default="voice_report.csv",
                         help="Output CSV filename, written inside the game dir.")
    args = parser.parse_args()

    if args.game_dir:
        game_dir = args.game_dir
    else:
        candidate = os.path.join(args.project_dir, "game")
        game_dir = candidate if os.path.isdir(candidate) else args.project_dir

    if not os.path.isdir(game_dir):
        print("Error: game directory not found: %s" % game_dir, file=sys.stderr)
        sys.exit(1)

    extensions = {e.strip().lower() for e in args.extensions.split(",") if e.strip()}

    build(game_dir, args.voice_dir, extensions, args.report)


if __name__ == "__main__":
    main()
