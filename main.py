#!/usr/bin/env python3
"""Two Lines to Your Past Self — entry writer.

Writes exactly two lines to /output/entry.txt:
  line 1 — one sentence warning the past self about one specific moment
  line 2 — one sentence saying why that moment mattered
Gate: UTF-8 text, 1-280 characters, not only whitespace.
No network, no randomness, no files read: the text is fixed below.
"""

import os
import sys

WARNING = (
    "Don't hand Mr. Alvarez the $1,800 deposit for apartment 4B "
    "on March 3, 2019 \u2014 the ceiling above the bed already "
    "stains brown every time it rains."
)

REASON = (
    "That deposit bought three years of buckets under the bed, "
    "a ruined mattress, and the lease I now keep framed as a warning."
)


def build_entry() -> str:
    return WARNING + "\n" + REASON + "\n"


def main() -> int:
    entry = build_entry()
    text = entry.strip("\n")
    if not text.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 280:
        print(f"entry too long: {len(text)} chars", file=sys.stderr)
        return 1
    if len(text.splitlines()) != 2:
        print("entry must be exactly two lines", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)
    print(entry, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
