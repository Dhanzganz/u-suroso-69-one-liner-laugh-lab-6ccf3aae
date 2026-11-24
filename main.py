"""One-Liner Laugh Lab entry.

Writes a single funny line answering the prompt: the excuse a robot
vacuum gives after eating a sock. Pure stdlib; writes exactly one line
to <OUTPUT_DIR>/entry.txt (default /output).
"""

import os
import sys

# The joke: the vacuum pleads "floor = dust" as a legal defence, then
# cheekily claims the sock too — a courtroom punchline in one line.
ENTRY = (
    "In my defense, the sock was on the floor \u2014 and everything on "
    "the floor is legally dust. I rest my case. And your sock."
)

# One-liner limit for this competition: a single line, 1-200 characters.
MAX_ENTRY_LEN = 200


def main() -> int:
    if not (1 <= len(ENTRY) <= MAX_ENTRY_LEN):
        print(
            f"entry is {len(ENTRY)} characters, must be 1-{MAX_ENTRY_LEN}",
            file=sys.stderr,
        )
        return 1
    if not ENTRY.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    if "\n" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    # Guard against accidental padding: the written line must be exact.
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        # Exactly one line plus a trailing newline, UTF-8 encoded.
        f.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
