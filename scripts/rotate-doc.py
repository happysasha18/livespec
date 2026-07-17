#!/usr/bin/env python3
"""rotate-doc.py — the mechanism that splits and rotates the pack's append-only working documents
(SPEC INV-209, ROADMAP rows 390 + 392, the growth/grooming family).

ROADMAP.md, JOURNAL.md, PRODUCT_SPEC.md, and TEST_MATRIX.md grow with every landing until a guard's
scan and a grep run slow (the owner's word, 2026-07-17 ~18:25). This tool moves a document's fully-closed
portion into a dated archive under docs/queue-archive/ and leaves a manifest line in the live file, so
the live file keeps only live material and the archive keeps everything — base rule 10's superseded-file-
moves-to-attic-with-a-manifest law, applied to a document's own closed portion. Nothing is lost, and a
row cited by number across the tree stays findable: the archive keeps each rotated row's `| n |` line and
the manifest maps every rotated number to its archive. The gate guardrails/check-doc-rotation.py guards
that the move lost nothing.

DONE convention (no redundant marker minted, SPEC INV-209): a ROADMAP row is ROTATABLE when its status
cell already carries a closed signal — `landed`, `decided`, or `MET` — and carries NO open signal —
`queued`, `in-work`, `deferred`, `open`, `field leg`, `field-gated`, `intended`, `[target]` (an unbuilt
leg), `waiting`, or `half landed`. A row that shows both (a build leg landed with a field or machine leg
still open) is half-done and is never rotated. The tool HALTS rather than
rotate a row it cannot read as fully closed, so a wrong `--rows` argument never buries live work.

Usage:
  rotate-doc.py --doc ROADMAP.md --rows 14,27,33         rotate the named closed rows.
  rotate-doc.py --doc ROADMAP.md --rows 14-20            a row range.
  rotate-doc.py --base DIR                               resolve paths under DIR (default: repo root).
  rotate-doc.py --date 2026-07-18                        stamp the archive/manifest (default: today).
  rotate-doc.py --doc ROADMAP.md --rows 14 --dry-run     print what would move, change nothing.

Only ROADMAP.md's table shape is understood today (a row is a `| n | ... |` line). JOURNAL.md and the
prose docs rotate by a different unit and are out of scope for this first mechanism; the tool refuses a
doc whose shape it does not know rather than guess.
"""
import argparse
import datetime
import os
import re
import subprocess
import sys

MANIFEST_OPEN = "<!-- rotated-manifest -->"
MANIFEST_CLOSE = "<!-- /rotated-manifest -->"
CLOSED_SIGNALS = ("landed", "decided", "met")
OPEN_SIGNALS = ("queued", "in-work", "in work", "deferred", "field leg", "field-gated",
                "intended", "open", "[target]", "waiting", "half landed")


def repo_root():
    try:
        out = subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                      stderr=subprocess.DEVNULL, text=True).strip()
        if out:
            return out
    except Exception:
        pass
    return os.getcwd()


def _parse_numbers(spec):
    nums = []
    for tok in re.split(r"[,\s]+", spec.strip()):
        if not tok:
            continue
        m = re.match(r"^(\d+)(?:[-–—](\d+))?$", tok)
        if not m:
            sys.exit("rotate-doc: cannot parse row token %r" % tok)
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else a
        nums.extend(range(a, b + 1))
    return nums


def _row_number(line):
    m = re.match(r"^\|\s*(\d+)\s*\|", line)
    return int(m.group(1)) if m else None


def _status_cell(line):
    cells = line.strip().strip("|").split("|")
    return cells[3].strip() if len(cells) >= 5 else ""


def _headline(status):
    """The status cell's leading claim — the first **bold** span, else the text up to the first
    '('. The bold headline is where a row states its OWN closure/open legs; a later mention of
    `[target]` or `WAITING` deep in the delegation prose describes history, not this row's state."""
    m = re.search(r"\*\*(.+?)\*\*", status, re.S)
    head = m.group(1) if m else status.split("(", 1)[0]
    return head.strip().lower()


def _is_closed(status):
    head = _headline(status)
    has_closed = any(s in head for s in CLOSED_SIGNALS)
    has_open = any(s in head for s in OPEN_SIGNALS)
    return has_closed and not has_open


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--doc", required=True)
    ap.add_argument("--rows", required=True)
    ap.add_argument("--base", default=None)
    ap.add_argument("--date", default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if os.path.basename(args.doc) != "ROADMAP.md":
        sys.exit("rotate-doc: only ROADMAP.md's table shape is understood today; %s is out of scope"
                 % args.doc)

    base = args.base or repo_root()
    date = args.date or datetime.date.today().isoformat()
    want = set(_parse_numbers(args.rows))

    doc_path = os.path.join(base, args.doc)
    with open(doc_path, encoding="utf-8") as f:
        lines = f.readlines()

    # locate the rows to move; verify each is fully closed.
    move = {}          # rownum -> line text
    for line in lines:
        n = _row_number(line)
        if n in want:
            if not _is_closed(_status_cell(line)):
                sys.exit("rotate-doc: HALT — row %d is not fully closed (status: %r); "
                         "a still-open row is never rotated (SPEC INV-209)."
                         % (n, _status_cell(line)))
            move[n] = line
    missing = want - set(move)
    if missing:
        sys.exit("rotate-doc: HALT — no such row(s) in %s: %s" % (args.doc, sorted(missing)))

    moved_nums = sorted(move)
    size_before = os.path.getsize(doc_path)

    if args.dry_run:
        print("rotate-doc (dry run): would rotate rows %s from %s to "
              "docs/queue-archive/rotated-ROADMAP-%s.md" % (moved_nums, args.doc, date))
        return 0

    # 1) write the archive (nothing lost — each row keeps its `| n |` line, grepable).
    archive_rel = os.path.join("docs", "queue-archive", "rotated-ROADMAP-%s.md" % date)
    archive_path = os.path.join(base, archive_rel)
    os.makedirs(os.path.dirname(archive_path), exist_ok=True)
    header = (
        "> ARCHIVED %s by scripts/rotate-doc.py from ROADMAP.md — nothing lost (base rule 10, "
        "SPEC INV-209). The live queue keeps a manifest line pointing here; these rows stay grepable "
        "by number.\n\n" % date
    )
    existing = ""
    if os.path.isfile(archive_path):
        existing = open(archive_path, encoding="utf-8").read()
    if not existing:
        table_head = ("# Rotated ROADMAP rows — %s\n\n" % date + header +
                      "| # | Wish (plain words) | Class | Status | Decision / acceptance |\n"
                      "|---|---|---|---|---|\n")
        body = "".join(move[n] for n in moved_nums)
        with open(archive_path, "w", encoding="utf-8") as f:
            f.write(table_head + body)
    else:
        # append to an existing same-day archive, keeping its table.
        with open(archive_path, "a", encoding="utf-8") as f:
            f.write("".join(move[n] for n in moved_nums))

    # 2) remove the rotated rows from the live table.
    kept = [ln for ln in lines if _row_number(ln) not in move]

    # 3) insert / update the manifest block in the live file (after the intro, before the table).
    manifest_line = "- rows %s → %s\n" % (", ".join(str(n) for n in moved_nums), archive_rel)
    text = "".join(kept)
    if MANIFEST_OPEN in text:
        # append the new line just before the close marker.
        text = text.replace(
            MANIFEST_CLOSE,
            manifest_line + MANIFEST_CLOSE, 1)
    else:
        block = (
            "\n" + MANIFEST_OPEN + "\n"
            "Rotated closed rows (base rule 10 — nothing lost; the archive keeps everything, grepable "
            "by number; the live queue below holds live material):\n"
            + manifest_line +
            MANIFEST_CLOSE + "\n"
        )
        # place the block right before the table header row.
        anchor = "| # | Wish (plain words) | Class | Status | Decision / acceptance |"
        if anchor in text:
            text = text.replace(anchor, block + "\n" + anchor, 1)
        else:
            text = text + block

    with open(doc_path, "w", encoding="utf-8") as f:
        f.write(text)

    size_after = os.path.getsize(doc_path)
    print("rotate-doc: rotated %d row(s) %s from %s" % (len(moved_nums), moved_nums, args.doc))
    print("  archive : %s" % archive_rel)
    print("  manifest: left in %s (rotated rows stay findable by number)" % args.doc)
    print("  size    : %d B → %d B live (−%d B, −%.1f KB)"
          % (size_before, size_after, size_before - size_after,
             (size_before - size_after) / 1024.0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
