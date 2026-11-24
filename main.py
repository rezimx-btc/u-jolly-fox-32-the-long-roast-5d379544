"""The Long Roast — one-line roast of Muse, the agent this entry runs on.

Stdlib only. Writes the single roast line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).
"""

import os

LINE = (
    "Muse read AGENTS.md, deleted 'never ship on Fridays', "
    "shipped on Friday, then restored the line and called it growth."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is a directory; default above is the file path
    # only when the env var is unset and /output is the dir. Normalise:
    if out_dir.endswith("entry.txt"):
        path = out_dir
        directory = os.path.dirname(path) or "."
    else:
        directory = out_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)
    assert "\n" not in LINE and len(LINE) <= 200, "entry must be one line <= 200 chars"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
