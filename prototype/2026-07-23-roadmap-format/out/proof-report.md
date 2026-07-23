# Content-preservation proof — ROADMAP.md format conversion (row 480)

**Verdict: PASS — every token difference is a declared delta**

Compared the OLD `ROADMAP.md` body (git 859dcfc) against the NEW live body plus the July archive plus the status-notes file's entries, over the data-row region (preambles, table headers, separators, and the notes file's prose header excluded and reported), word-token multiset and punctuation multiset, modulo the named deltas below. Live rows: 117 (queued 82 · in-work 3 · deferred 29 · far 3). Archived rows: 228 — moved verbatim, byte-identical, so they cancel.

## Named deltas (excluded regions, reported)

- **Preamble replaced** — excluded both sides. Old preamble+manifest 212 word tokens; new 578 word tokens (the new-format preamble; the manifest keeps the 2026-07-18 line and gains one July line).
- **Archive file header generated** — excluded from the new side; 48 word tokens (the `# Rotated …` title and the ARCHIVED provenance note).
- **Status-notes file header generated** — excluded from the new side; 72 word tokens (what the file is; not a rotated-rows archive, no manifest line).

## Named deltas (reconciled in the compared data-row region)

- **Archived rows verbatim** — 227 of 228 archived rows, present in the OLD body and the NEW archive byte-for-byte; net-zero token contribution (the nothing-lost move).
- **Archived row 445 status corrected at the move** (override table) — the cell gains `**landed 2026-07-23 (v4.0.0).** Delegation (INV-103): the drafter-applier pipeline carried the format draft and the spec rewrite on worker seats, the door and the fold verdicts staying senior; the full accounting lives in JOURNAL.md's v4.0.0 chapter. — (status note: …)`, the old cell text riding verbatim inside the note; tokenized and reconciled per row.
- **Status normalized, token-preserving** — each of the 117 live rows' pre-conversion status text stands verbatim in the status-notes file (so it cancels against the old cell); ADDED per row: the new `*word* DATE` status cell (a deferred row with its real inline `— revisit trigger: …` clause) and the notes entry's `## row <id>` header (`row`, the id; `#` × 2).
- **Deferred trigger duplication (the declared choice: copy, not move)** — a deferred row's extracted trigger clause is COPIED into the status cell while the notes entry stays verbatim, so the duplicated tokens are counted inside the per-row status-cell addition above; moving the clause out of the note would have broken the notes file's verbatim guarantee.
- **Sixth drift cell dropped** — 27 live rows carried a lone-dash sixth cell; removed `—` × 27 and `|` × 27.
- **Class re-vocabularying** — 2 rows: row 411 far→surface; row 455 big→large.

## Residuals (must all be empty)

- word-token residual (raw delta minus named deltas): empty
- punctuation residual (raw delta minus named deltas): empty

