"""Two Lines to Your Past Self — make.fun bounty entry.

Two lines of advice to my past self. The entry is fixed text: exactly
two lines, 1-280 characters in total (after stripping leading/trailing
newlines). Deterministic execution: no randomness, no time, no network,
no file reads. The WARNING line names the mistake to avoid; the REASON
line names what that mistake cost.
"""

import os
import sys

WARNING = "Don't hand Mr. Alvarez the $1,800 deposit for apartment 4B on March 3, 2019 — the ceiling above the bed already stains brown every time it rains."

REASON = "That deposit bought three years of buckets under the bed, a ruined mattress, and the lease I now keep framed as a warning."


def build_entry():
    """Return the two-line entry, each line followed by a newline."""
    return WARNING + "\n" + REASON + "\n"


def main():
    """Validate the entry, write it to /output/entry.txt, and print it."""
    entry = build_entry()
    stripped = entry.strip("\n")
    lines = stripped.split("\n")
    if not stripped or len(stripped) > 280 or len(lines) != 2:
        print("error: entry must be exactly two non-empty lines, 1-280 characters", file=sys.stderr)
        return 1
    if not all(line.strip() for line in lines):
        print("error: entry must be exactly two non-empty lines, 1-280 characters", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    # The entry file is the deliverable: two lines, UTF-8, trailing newline.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)
    print(entry, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
