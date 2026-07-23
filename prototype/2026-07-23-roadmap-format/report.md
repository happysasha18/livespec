# Conversion report — ROADMAP.md → queue-member format (row 480, PROTOTYPE)

Source pinned to git 859dcfc (round-3 output applied at 6edcf32; this round-6 output supersedes it). Round 6 root fix: the in-body status notes read as current state to a cold reader (bold LANDED in a quote out-shouting the italic status), so live rows carry no note — the pre-conversion status texts live verbatim in docs/queue-archive/status-notes-ROADMAP-2026-07-23.md (45,991 B; no manifest line, not a rotated-rows archive), and deferred cells name their real trigger inline. The preamble states both facts (status cell = sole authority; where the old texts live).

## Totals

- rows in (pinned source body): 345
- archived: 228 (227 verbatim + row 445 with the corrected cell + delegation line)
- live: 117  (body 686 KB old → 126 KB new; notes file 45,991 B)
- live by status: queued 82 · in-work 3 · deferred 29 · far 3
- ambiguous / safe-default-live: 3  (235, 241, 424)

## Trigger extraction (deferred: 29)

- inline 20 · override 4 (55, 69, 129, 131) · NEEDS-TRIGGER fallback 5 (134, 140, 141, 143, 144).

## Proof verdict

PASS — OLD (859dcfc) vs NEW body + July archive + status-notes entries, word-token and punctuation multisets, every difference a named delta with matching signed counts; residual empty. Duplication choice: a deferred row's extracted trigger is COPIED into the status cell (counted inside the per-row status-cell delta) while the notes entry stays verbatim — copy-not-move keeps the notes file's verbatim guarantee. See out/proof-report.md.

## Validation (all against out/)

- real TestQueue: queue_row_lint 117/117 with reach line; in-work cap (re-keyed) counts 386, 412, 480 = 3; fixtures + class-vocabulary green.
- tests/test_delegation_line.py + tests/test_footprint_note.py forward-landed scans: green with the notes file inside their docs/queue-archive/*.md glob — its `## row` sections are not `| n |` table rows and every `**landed` occurrence in the note texts predates the 2026-07-12 bind, so both parsers skip them (verified by running the real tests).
- guardrails/check-doc-rotation.py --base out: OK — the notes file is outside the rotated-*.md orphan glob, so it owes no manifest line.

## Declared deltas (each counted)

- Closed rows to the July archive: 228 — 227 verbatim (cancel) + row 445's corrected cell (named per-row delta).
- Live rows: old status text verbatim to the notes file (cancels); ADDED per row the `*word* DATE` cell (+ inline trigger) and the `## row <id>` notes header.
- Sixth drift cell dropped: 27 live rows; archived 6-cell rows keep theirs.
- Class re-vocabularying: row 411 far→surface; row 455 big→large (2 rows).
- Preamble replaced (+2 authority sentences per the addendum), archive header + notes header generated — excluded from the proof, token counts reported in proof-report.md.

## Flags for the orchestrator

- NEEDS-TRIGGER rows 134, 140, 141, 143, 144: cells carry the last-resort fallback; the real events need the owner's word.
- Ambiguous rows kept live (deferred): 235, 241, 424.
- Dates pulled from the wish cell: [48, 49, 171, 302, 307, 308, 309, 332, 381].

