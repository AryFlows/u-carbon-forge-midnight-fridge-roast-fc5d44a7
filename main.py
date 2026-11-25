"""Frost Midnight Lockout — one-line midnight fridge roast.

Writes the roast to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

LINE = "It's 2 a.m., I'm starving, and the fridge just locked me out like I'm the burglar in my own kitchen."


def main() -> None:
    # Gate: one line, 1-200 chars, UTF-8, not only whitespace.
    assert 1 <= len(LINE) <= 200, "line outside 1-200 char gate"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
