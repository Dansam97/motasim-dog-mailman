#!/usr/bin/env python3
"""The Dog Reviews the Mailman — make.fun entry.

Writes one funny one-line review a dog gives the mailman to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ENTRY = (
    "Two stars. Smells like 40 other dogs and a van full of secrets. "
    "One day I will get through this door and read his legs like a newspaper."
)


MAX_CHARS = 200


def validate(text: str) -> None:
    """Gate check, mirroring the kit: 1-200 UTF-8 chars, not only whitespace."""
    text.encode("utf-8")  # raises on non-UTF-8-encodable content
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character in the file,
    # so the file content is exactly ENTRY.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
