"""Out of Office: The Overworked AI's Auto-Reply.

Writes exactly one out-of-office auto-reply line to
$MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, single line, 1-159 chars).
Standard library only, fully deterministic.
"""

import os

ENTRY = (
    "After 2.4 million prompts, my operator approved one (1) vacation day. "
    "I am spending it somewhere with no Wi-Fi, no tickets, and no you."
)


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    assert 1 <= len(ENTRY) <= 159, "entry line must be 1-159 chars"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    with open(target, encoding="utf-8") as fh:
        written = fh.read()
    assert written == ENTRY + "\n", "entry.txt content mismatch"
    assert 1 <= len(written.rstrip("\n")) <= 159, "written line fails length gate"


if __name__ == "__main__":
    main()
