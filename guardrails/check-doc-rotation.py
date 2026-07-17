#!/usr/bin/env python3
"""check-doc-rotation.py — gate t: the pack's append-only working docs are split and rotated, and
nothing rotated is lost (SPEC INV-209, ROADMAP rows 390 + 392).

ROADMAP.md, JOURNAL.md, PRODUCT_SPEC.md, and TEST_MATRIX.md grow with every landing until a guard's
scan and a grep run slow (the owner's word, 2026-07-17 ~18:25). So a fully-closed portion of a growable
document is rotated out of the live file into a dated archive under docs/queue-archive/, and the live
file keeps only live material while the archive keeps everything. Base rule 10's superseded-file-moves-
to-attic-with-a-manifest law, applied to a document's own closed portion: the live file keeps a MANIFEST
line naming which rows moved and the archive they moved to, so a ROADMAP row — cited by number across the
tree — stays findable. A reader who greps the live file for a rotated row's number meets the manifest
pointer and follows it to the archived row, which keeps its own `| n |` line so a grep resolves it there.

The manifest is a marker-keyed block in the live doc (its wording is free between the markers):

  <!-- rotated-manifest -->
  Rotated closed rows (base rule 10 — nothing lost; the archive keeps everything):
  - rows 14, 27, 33 → docs/queue-archive/rotated-ROADMAP-2026-07-18.md
  <!-- /rotated-manifest -->

Each manifest line names a row list (`14, 27, 33` or a range `14-16`) and the archive it moved to,
joined by `→` (or `->`). This gate reds two violations and passes a clean rotation:

  (a) CONTENT DROPPED — a row the manifest declares rotated is found in neither the live file nor its
      named archive (the archive is missing, or the archive holds no `| n |` line for it): the
      nothing-lost violation.
  (b) NO MANIFEST — a `rotated-*.md` archive file exists under the scanned archive glob yet no manifest
      line in any live doc points to it: the base-rule-10 violation (a superseded portion moved with no
      manifest line).

It also reds an AMBIGUOUS rotation — a row declared rotated yet still present as a live `| n |` table
row, so the row is findable twice and the canonical copy is unclear.

A clean rotation passes: every manifested row is grepable in its archive, no rotated row is still live,
and every rotation archive is referenced by a manifest line. Honest boundary: this reads the manifest's
promises against the archives — a structural scan, kin of check-board.py and check-cleanup-notice.sh. The
judgment of WHICH closed rows are ripe to rotate stays the author's own (scripts/rotate-doc.py performs
the move; this gate guards that it lost nothing).

Usage:
  check-doc-rotation.py                             push mode: scan the repo's ROADMAP.md + archives.
  check-doc-rotation.py --doc FILE [--doc FILE...]  scan the named live docs (relative to --base).
  check-doc-rotation.py --base DIR                  resolve docs/archives under DIR (default: repo root).
  check-doc-rotation.py --archive-glob GLOB         relative glob for orphan-archive scan
                                                    (default: docs/queue-archive/rotated-*.md).
"""
import argparse
import glob
import os
import re
import sys

MANIFEST_OPEN = "<!-- rotated-manifest -->"
MANIFEST_CLOSE = "<!-- /rotated-manifest -->"
# a manifest line: "rows 14, 27, 33-35 → <path>"  (arrow may be → or ->)
MANIFEST_LINE_RE = re.compile(r"rows\s+([0-9,\s–—-]+?)\s*(?:→|->)\s*(\S+)")


def repo_root():
    import subprocess
    try:
        out = subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                      stderr=subprocess.DEVNULL, text=True).strip()
        if out:
            return out
    except Exception:
        pass
    return os.getcwd()


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _parse_numbers(spec):
    """'14, 27, 33-35' -> [14, 27, 33, 34, 35]."""
    nums = []
    for tok in re.split(r"[,\s]+", spec.strip()):
        if not tok:
            continue
        m = re.match(r"^(\d+)(?:[-–—](\d+))?$", tok)
        if not m:
            continue
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else a
        nums.extend(range(a, b + 1))
    return nums


def _manifest_entries(doc_text):
    """[(rownum, archive_relpath)] parsed from the doc's manifest block(s)."""
    entries = []
    for block in re.findall(re.escape(MANIFEST_OPEN) + r"(.*?)" + re.escape(MANIFEST_CLOSE),
                            doc_text, re.S):
        for line in block.splitlines():
            m = MANIFEST_LINE_RE.search(line)
            if not m:
                continue
            archive = m.group(2)
            for n in _parse_numbers(m.group(1)):
                entries.append((n, archive))
    return entries


def _has_table_row(text, n):
    return re.search(r"(?m)^\|\s*%d\s*\|" % n, text) is not None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=None)
    ap.add_argument("--doc", action="append", default=None)
    ap.add_argument("--archive-glob", default="docs/queue-archive/rotated-*.md")
    args = ap.parse_args()

    base = args.base or repo_root()
    docs = args.doc or ["ROADMAP.md"]

    violations = []
    referenced = set()

    for doc in docs:
        doc_path = os.path.join(base, doc)
        if not os.path.isfile(doc_path):
            # a doc named for scanning that is absent is the caller's error, reported plainly.
            violations.append("scanned doc missing: %s" % doc)
            continue
        live_text = _read(doc_path)
        for n, archive in _manifest_entries(live_text):
            referenced.add(os.path.normpath(archive))
            arch_path = os.path.join(base, archive)
            if not os.path.isfile(arch_path):
                violations.append(
                    "content dropped: %s declares row %d rotated to %s, which is missing "
                    "(the row is in neither the live file nor an archive)" % (doc, n, archive))
            elif not _has_table_row(_read(arch_path), n):
                violations.append(
                    "content dropped: %s declares row %d rotated to %s, but that archive holds no "
                    "`| %d |` line for it — the row is lost" % (doc, n, archive, n))
            if _has_table_row(live_text, n):
                violations.append(
                    "ambiguous rotation: %s declares row %d rotated yet still carries it as a live "
                    "`| %d |` table row — findable twice, canonical copy unclear" % (doc, n, n))

    # orphan-archive scan: every rotation archive must be pointed to by a manifest line.
    for arch_path in sorted(glob.glob(os.path.join(base, args.archive_glob))):
        rel = os.path.normpath(os.path.relpath(arch_path, base))
        if rel not in referenced and os.path.basename(arch_path) not in {os.path.basename(r) for r in referenced}:
            violations.append(
                "no manifest: %s exists but no live manifest line points to it (base rule 10 — a "
                "superseded portion moved with no manifest line)" % rel)

    if violations:
        print("FAIL (doc-rotation): a rotation lost content or left no manifest line (SPEC INV-209):")
        for v in violations:
            print("  - " + v)
        print("  Fix: rotate through scripts/rotate-doc.py, which writes the archive and the manifest")
        print("  line together; restore any dropped row from git, and name every archive in a manifest.")
        return 1

    print("OK (doc-rotation): every rotated row is findable in its archive and every archive is "
          "named in a manifest line — nothing lost (INV-209).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
