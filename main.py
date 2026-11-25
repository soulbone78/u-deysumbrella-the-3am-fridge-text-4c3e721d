#!/usr/bin/env python3
"""The 3AM Fridge Text - entry program (pure stdlib).

Writes a single line - the text message a smart fridge sends its
owner at 3am - to /output/entry.txt (1-140 chars, one line).
"""

import os

LINE = "It's 3am. Third trip tonight. The pickles saw everything, and frankly, so did I."


def validate(line):
    """Check the entry against the gate before writing it."""
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, "entry must be 1-140 characters"
    assert not line.isspace(), "entry must not be only whitespace"
    line.encode("utf-8")  # raises if the entry is not UTF-8 text
    return line


def main():
    line = validate(LINE.strip())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
