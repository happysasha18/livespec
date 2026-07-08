#!/usr/bin/env python3
"""preshow-lint.py — the mechanical pre-show arm of the plain-language law (SPEC INV-28).

Why this exists: a human-facing line must open with the reader's outcome; internal handles —
spec codes (INV-28, M-176, T-9, E-14, S-0, A-3, ACT-2, D-2, C-1, B-2), row numbers, session
numbers — may only TRAIL in parentheses, never LEAD a sentence to the human. The law kept leaking
into chat reports anyway (a report led with "rows 166 …" and the reader could not parse it). Chat
has no file to gate, so this scans the human-facing TEXT a report/decision page/rendered artifact
carries, and flags a line that opens with an internal handle so the author rewrites it plainly
BEFORE the human sees it — a warning to clear, never a silent rewrite.

Scope: run on human-facing surfaces (a report, a decision page, a rendered doc's shown prose).
NOT on the spec/matrix/architecture internals, whose trailing anchors are legal by design.

Usage: preshow-lint.py FILE            (or: cat text | preshow-lint.py -)
Exit 0 = clean · exit 1 = a leading-handle line found (printed with its line number).
"""
import re
import sys

# an internal handle: a spec code (LETTERS-digits) or a row/session reference.
HANDLE = r"(?:INV|M|T|E|S|A|ACT|D|C|B)-\d+|rows?\s+\d+|sessions?\s+\d+"

# a line "leads with a handle" when, after optional markdown bullet/emphasis marks,
# its first word IS an internal handle. Anchors in parentheses or mid-sentence are fine.
LEAD = re.compile(r"^\s*(?:[-*>#]+\s*)*(?:\*+_?\s*)?(?:%s)\b" % HANDLE, re.IGNORECASE)


def lint(text):
    """Return a list of (line_no, line) that open with an internal handle."""
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if not stripped:
            continue
        # a line that is ONLY a handle-and-detail table cell or a code block is out of scope;
        # we flag prose lines that begin with a handle.
        if LEAD.match(line):
            hits.append((i, stripped))
    return hits


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage: preshow-lint.py FILE|-\n")
        return 2
    src = argv[1]
    text = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
    hits = lint(text)
    if not hits:
        return 0
    print("PRE-SHOW LINT (SPEC INV-28): a human-facing line must open with the reader's outcome,")
    print("not an internal handle. Rewrite these so the code only trails in parentheses:")
    for line_no, line in hits:
        print("  line %d: %s" % (line_no, line[:100]))
    print('{"severity":"advisory","code":"leading-handle","message":"a shown line opens with an '
          'internal handle","fix":"lead with the reader\'s outcome; let the code trail in parens"}')
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
