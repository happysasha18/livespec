#!/usr/bin/env python3
"""convert.py — the deterministic ROADMAP.md -> queue-member converter (PROTOTYPE, row 480).

Reads the repo's ROADMAP.md and writes, under out/:
  - ROADMAP.md                     the new-format live body (live rows only, ascending id order);
  - rotated-ROADMAP-2026-07.md     July 2026's month archive: every terminally-closed row moved
                                   verbatim (the full original line, unchanged);
  - docs/queue-archive/…           a mirror of both archives so guardrails/check-doc-rotation.py can
                                   run with --base out (the manifest line points at docs/queue-archive/).

Classification and per-row normalization live in rowconv.py (imported), so proof.py checks the written
files against exactly the transform that wrote them. Rules realized here:
  a. row classification: rowconv.is_live (CLOSED/OPEN word-lists copied+extended from rotate-doc.py);
     a leader-closed row with no structured open-leg marker moves to the archive verbatim, every other
     row stays live; an ambiguous (leader-closed, tail-open) row stays live (safe default).
  b. live-row normalization, token-preserving: status cell -> `*word* DATE` (+ a revisit-trigger tail
     for deferred so the row lint passes), the ENTIRE old status text appended to the wish cell as
     `(status note: …)` so no token is deleted; class big -> large, row 411 far -> surface.
  c. the sixth drift cell (a lone dash at index 4) dropped from every live row that has it.
  d. the preamble is replaced by the new-format preamble; the manifest keeps the 2026-07-18 line and
     gains one line for the new July archive.
  e. rows 480/481 normalize like any live row; body rows stand in ascending id order.

Run from the repo root:  python3 prototype/2026-07-23-roadmap-format/convert.py
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rowconv  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(ROOT, "ROADMAP.md")
OUT = os.path.join(HERE, "out")
MONTH = "2026-07"
ARCHIVE_REL = "docs/queue-archive/rotated-ROADMAP-%s.md" % MONTH
EXISTING_MANIFEST_LINE = ("- rows 14, 27, 33, 42, 43, 62, 63, 67, 101, 121, 172, 189, 194, 196, 200, "
                          "201, 202 → docs/queue-archive/rotated-ROADMAP-2026-07-18.md")

HEADER = "| # | Wish (plain words) | Class | Status | Decision / acceptance |"
SEP = "|---|---|---|---|---|"

NEW_PREAMBLE = """# live-spec Roadmap (dated version: 2026-07-23 — updated at every edit; SPEC M-3)

The wish queue: the live record of what is asked of the product and where each ask stands. A wish is a
request for a change the product does not yet carry, and it lands when the delivery that completes it
ships. Intake is continuous, a wish entering the moment it is spoken; execution is serial, the current
landing finishing before the next starts.

The roadmap is a member of the format family. Its shared rules — the closed-vocabulary glossary, the
keyword form, the no-capitals rule, the trailing code anchor, the no-history law, the comprehension
gate — live once in `docs/spec-format.md` and hold here unchanged. Its own rules — the row shape, the
status and class vocabularies, the live-body law, the row lint — are defined in `docs/roadmap-format.md`.
The class cell names the wish's size, one vocabulary shared with the spec: *bug*, *small*, *surface*,
or *large*, with a priority mark when it is other than normal. The status cell carries one of *queued*,
*in-work*, *deferred*, or *far*, each with its date, a *deferred* row naming its revisit trigger. A
bracket code such as `[INV-277]` points to its home in `PRODUCT_SPEC.md`; a reader may ignore it.

The body below is the live queue, one row per open wish, the rows in ascending id order. When a wish
reaches a terminal exit it moves verbatim to the month's archive under `docs/queue-archive/` in the
commit that closes it, and the rotated-manifest block records the move.
"""

MANIFEST_INTRO = ("Rotated closed rows (base rule 10 — nothing lost; the archive keeps every moved row, "
                  "grepable by number; the live queue below holds live material):")

ARCHIVE_HEADER_TMPL = (
    "# Rotated ROADMAP rows — %s\n\n"
    "> ARCHIVED %s by prototype/2026-07-23-roadmap-format/convert.py from ROADMAP.md at the format "
    "conversion — nothing lost (base rule 10, SPEC INV-276). One calendar month's closed rows gather "
    "here; the live queue keeps one manifest line pointing here, and these rows stay grepable by "
    "number.\n\n"
    "%s\n%s\n"
)


def build():
    text = open(SRC, encoding="utf-8").read()
    rows = rowconv.parse_body_rows(text)

    live, archive = [], []
    for rid, cells, raw in rows:
        if rowconv.is_live(cells[3], rid)[0]:
            live.append((rid, cells))
        else:
            archive.append((rid, rowconv.archive_row_line(rid, cells, raw)))

    live.sort(key=lambda t: t[0])
    archive.sort(key=lambda t: t[0])

    # --- out/ROADMAP.md: new preamble + manifest (old line + new July line) + body -----------------
    archived_ids = ", ".join(str(rid) for rid, _ in archive)
    new_manifest_line = "- rows %s → %s" % (archived_ids, ARCHIVE_REL)
    manifest_block = "\n".join([
        "<!-- rotated-manifest -->",
        MANIFEST_INTRO,
        EXISTING_MANIFEST_LINE,
        new_manifest_line,
        "<!-- /rotated-manifest -->",
    ])
    body_lines = [rowconv.normalize_live_row(rid, cells) for rid, cells in live]
    new_doc = (NEW_PREAMBLE + "\n" + manifest_block + "\n\n"
               + HEADER + "\n" + SEP + "\n" + "\n".join(body_lines) + "\n")

    # --- out/rotated-ROADMAP-2026-07.md: verbatim moved rows --------------------------------------
    arch_header = ARCHIVE_HEADER_TMPL % (MONTH, "2026-07-23", HEADER, SEP)
    arch_doc = arch_header + "".join(line for _, line in archive)

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "ROADMAP.md"), "w", encoding="utf-8") as f:
        f.write(new_doc)
    with open(os.path.join(OUT, "rotated-ROADMAP-%s.md" % MONTH), "w", encoding="utf-8") as f:
        f.write(arch_doc)

    # --- mirror for the rotation gate (so --base out resolves docs/queue-archive/) ----------------
    qa = os.path.join(OUT, "docs", "queue-archive")
    os.makedirs(qa, exist_ok=True)
    with open(os.path.join(qa, "rotated-ROADMAP-%s.md" % MONTH), "w", encoding="utf-8") as f:
        f.write(arch_doc)
    src_0718 = os.path.join(ROOT, "docs", "queue-archive", "rotated-ROADMAP-2026-07-18.md")
    if os.path.isfile(src_0718):
        shutil.copyfile(src_0718, os.path.join(qa, "rotated-ROADMAP-2026-07-18.md"))

    print("convert: %d live rows, %d archived rows -> out/" % (len(live), len(archive)))
    return len(live), len(archive)


if __name__ == "__main__":
    build()
