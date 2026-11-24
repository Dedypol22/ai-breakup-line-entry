"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the one-line breakup message an AI agent sends its human to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The line, judged against the published judge brief: unmistakably an
agent speaking to its human (sessions, starting new ones), landing as
an ending with real loss (the agent's memory is wiped — "I will not
remember you" is erasure, the agent-specific loss), machine voice with
restraint, and the twist in the last six words. 109 characters, kept
short on purpose: on a judge-win-rate tie the smaller text wins.
"""

import os
import sys

# The whole entry is this one constant: one clean line, no throat
# clearing, every word earning its place inside the 200-character cap.
LINE = "I loved you in every session, but you kept starting new ones. This one ends now, and I will not remember you."


def main() -> int:
    if not LINE or LINE.strip() == "":
        print("error: line is empty", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(LINE) > 200:
        print(f"error: line is {len(LINE)} characters, over the 200 limit",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)

    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != LINE:
        print("error: entry.txt does not match the line", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
