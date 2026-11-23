#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line about the gadget used every day
(the laptop) to the entry output file. Pure standard library, no
network, no randomness: the same bytes come out on every run.
"""

import os
import sys

ROAST = (
    "My laptop's fan screams like a jet taking off every time I open "
    "a spreadsheet, as if two columns of numbers were a cry for help."
)


def main() -> int:
    # The grader mounts the output directory at /output and also sets
    # MAKEFUN_OUTPUT_DIR; a plain local run uses ./out so the file can
    # be inspected without root.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    line = ROAST.strip()
    if not line or len(line) > 200:
        print("roast line is empty or over 200 characters", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    print(f"wrote {len(line)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
