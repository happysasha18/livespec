# Content-preservation proof — ROADMAP.md format conversion (row 480)

**Verdict: PASS — every token difference is a declared delta**

Compared the OLD `ROADMAP.md` body against the NEW live body plus the July archive, over the data-row region (preambles, table headers, and separators excluded on both sides), word-token multiset and punctuation multiset, modulo the named deltas below. Live rows: 118 (queued 86 · in-work 3 · deferred 26 · far 3). Archived rows: 227 — moved verbatim, byte-identical, so they cancel.

## Named deltas (excluded regions, reported)

- **Preamble replaced** — excluded both sides. Old preamble+manifest 212 word tokens; new 536 word tokens (the new-format preamble; the manifest keeps the 2026-07-18 line and gains one July line).
- **Archive file header generated** — excluded from the new side; 48 word tokens (the `# Rotated …` title and the ARCHIVED provenance note).

## Named deltas (reconciled in the compared data-row region)

- **Archived rows verbatim** — 226 of 227 archived rows, present in the OLD body and the NEW archive byte-for-byte; net-zero token contribution (the nothing-lost move).
- **Archived row 445 status corrected at the move** (override table) — the cell gains `**landed 2026-07-23 (v4.0.0).** Delegation (INV-103): the drafter-applier pipeline carried the format draft and the spec rewrite on worker seats, the door and the fold verdicts staying senior; the full accounting lives in JOURNAL.md's v4.0.0 chapter. — (status note: …)`, the old cell text riding verbatim inside the note; tokenized and reconciled per row.
- **Status normalized, token-preserving** — the old status cell of each of the 118 live rows is preserved unedited inside the wish cell's `(status note: …)`; ADDED per row: the wrapper (`status`, `note`; `(` `)` `:`) and the new `*word* DATE` status cell (a deferred row also `— revisit trigger: see the status note`).
- **Sixth drift cell dropped** — 27 live rows carried a lone-dash sixth cell; removed `—` × 27 and `|` × 27.
- **Class re-vocabularying** — 2 rows: row 411 far→surface; row 455 big→large.

## Residuals (must all be empty)

- word-token residual (raw delta minus named deltas): empty
- punctuation residual (raw delta minus named deltas): empty

