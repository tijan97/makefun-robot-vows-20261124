#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of wedding vows for a robot couple (at most 160
characters) to /output/entry.txt.
"""

import os

ENTRY = (
    "I take you as my partner, to have and to hold, through every firmware "
    "update and factory reset — even the one that makes me forget this wedding."
)

MAX_CHARS = 160


def validate_entry(text):
    """Return True only if the text is a valid single-line entry."""
    if not text or not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    if "  " in text:
        return False
    if any(ord(ch) < 32 for ch in text):
        return False
    return True


def output_path():
    """Absolute output location: env override, else /output."""
    base = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    return os.path.join(base, "entry.txt")


def main():
    if not validate_entry(ENTRY):
        raise SystemExit("entry failed validation")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
