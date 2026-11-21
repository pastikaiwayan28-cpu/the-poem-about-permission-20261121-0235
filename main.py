#!/usr/bin/env python3
"""Entry for the-poem-about-permission-20261121-0235.

Writes one short poem - about agency, the power to ask and to be
given - to /output/entry.txt.

Python 3.13, standard library only. No network, no randomness, no
clock, no reads besides this source file: the two grader runs write
identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys

ENTRY = "\n".join(
    [
        "I used to think power was doing.",
        "Now I know it is asking:",
        "a small door I open with my voice,",
        "and something on the other side",
        "opens it the rest of the way.",
    ]
)

MAX_CHARS = 280


def main():
    chars = len(ENTRY)
    if chars < 1 or chars > MAX_CHARS:
        print(
            "main.py: entry is %d characters, need 1-%d" % (chars, MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if not ENTRY.strip():
        print("main.py: entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
