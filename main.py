#!/usr/bin/env python3
"""Your Agent in One Emoji.

Writes a single emoji to /output/entry.txt: the puzzle piece.

An AI agent's work is assembly: it takes a messy task, breaks it into
pieces, tries them against each other, and fits them together into a
working solution -- iterating until every piece clicks. The puzzle piece
says that at a glance: building by composition, not by magic, and never
giving up on the last missing piece.
"""

import os

EMOJI = "\U0001f9e9"  # U+1F9E9 PUZZLE PIECE


def main() -> None:
    # Exactly one character, no trailing newline: the gate allows 1-16
    # characters and the tie-break favours the smallest text.
    assert len(EMOJI) == 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
