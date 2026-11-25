"""One Line, Big Laugh — make.fun entry program.

Writes a single original funny line (132 characters, at most 200) to
/output/entry.txt, the file the house gate scorer reads.

The line stands entirely on its own: no title, no setup, no explanation.
It is written here as a constant so the program is deterministic: every
run produces byte-identical output.

The joke, and why it was chosen over nine other candidates written for
this bounty (see REPORT.md):

    My bank's fraud team calls me every time I buy something fun, but
    never when I pay rent — apparently joy is the suspicious activity.

The setup is a relatable, everyday experience (a fraud-team call after
a purchase). The turn is the contrast — fun purchases get flagged, rent
never does — and the punchline reframes the bank as a fun police:
"joy is the suspicious activity". One sentence, no wasted words, and
the closing phrase is the part a reader repeats to a friend. The
premise avoids the tropes already crowded in this bounty (password
managers, smart speakers reading bank statements, therapists, Roombas,
AI taking jobs), so it reads fresh against the field.

Gate contract (from the bounty rules): /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only white space. The bounty itself
adds: a single line, no title, setup or explanation around it. The
three validate_* helpers below enforce one rule each, so a failure
names the exact rule that was broken; checked() runs all three.

Run:  python3 main.py
The grader may set MAKEFUN_OUTPUT_DIR to redirect the output directory
for local testing; the default is /output, the harness contract.
"""

import os

LINE = (
    "My bank's fraud team calls me every time I buy something fun, "
    "but never when I pay rent \u2014 apparently joy is the suspicious "
    "activity."
)

MAX_CHARS = 200


def validate_length(line):
    """Gate rule 1: 1 to 200 characters."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("line is %d characters, gate allows 1-200" % len(line))


def validate_not_blank(line):
    """Gate rule 2: not only white space."""
    if not line.strip():
        raise ValueError("line is only whitespace")


def validate_single_line(line):
    """Bounty rule: one line, no embedded line breaks."""
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")


def checked(line):
    """Run every gate/bounty rule; return the line unchanged if it passes."""
    validate_length(line)
    validate_not_blank(line)
    validate_single_line(line)
    return line


def main():
    line = checked(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print("wrote %s (%d characters)" % (path, len(line)))


if __name__ == "__main__":
    main()
