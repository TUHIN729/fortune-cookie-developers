#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt when the
variable is unset).

Fully deterministic: standard library only, no network, no randomness,
no wall-clock. The line lives in a single constant and is written exactly
once. Before writing, the program checks the same gate the competition
applies: the line must be a single line of 1 to 120 characters, not only
whitespace.
"""

import os

MAX_CHARS = 120

FORTUNE = (
    "Every log warning you scroll past is a small debt, "
    "and the interest is charged at 3 a.m."
)


def _validate(line: str) -> None:
    """Enforce the competition gate: one non-blank line, 1-120 chars."""
    if not line or not line.strip():
        raise ValueError("fortune line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("fortune line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"fortune line is {len(line)} chars, over the {MAX_CHARS} limit"
        )


def main() -> None:
    _validate(FORTUNE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
