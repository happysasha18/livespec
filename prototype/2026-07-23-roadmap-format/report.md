# Conversion report — ROADMAP.md → queue-member format (row 480, PROTOTYPE)

Source pinned to git 859dcfc; the orchestrator applied round-3 output at 6edcf32, and this final round supersedes it. Override table and the closed-leader→deferred rule recorded in rowconv.py (rationale per row).

## Totals

- rows in (pinned source body): 345
- archived: 228 (227 verbatim + row 445 with the corrected cell + delegation line)
- live: 117
- live by status: queued 82 · in-work 3 · deferred 29 · far 3
- ambiguous / safe-default-live: 3  (235, 241, 424)

## Proof verdict

PASS — word-token + punctuation multisets, OLD (859dcfc) vs NEW body + July archive, every difference attributed to a named delta class with matching signed counts; residual empty. See out/proof-report.md.

## Validation (all against out/)

- real TestQueue: queue_row_lint 117/117 with reach line; fixtures, class-vocabulary green.
- test_roadmap_in_work_cap (re-keyed to the italic form): PASSES — rows 386, 412, 480 = 3, at the T-18 cap.
- tests/test_delegation_line.py forward-landed scan: PASSES (row 445's corrected cell carries the Delegation (INV-103) line).
- guardrails/check-doc-rotation.py --base out: OK — nothing lost, no rotated row still live.

## Declared deltas (each counted)

- Closed rows to the July archive: 228 — 227 verbatim (cancel) + row 445's corrected status cell (named per-row delta).
- Status normalized `*word* DATE`, old status verbatim in the wish cell's `(status note: …)`: 117 live rows.
- Deferred revisit-trigger clauses: 29 rows (69/55/129/131 named by override, the rest `see the status note`).
- Sixth drift cell dropped: 27 live rows (`—` ×27, `|` ×27); archived 6-cell rows keep theirs.
- Class re-vocabularying: row 411 far→surface; row 455 big→large (2 rows).
- Preamble replaced (excluded, reported); manifest keeps the 2026-07-18 line + one July line; archive header generated (excluded, reported).

## Flags for the orchestrator

- Ambiguous rows kept live (deferred): 235, 241, 424 — review whether each leg is truly still open.
- Dates pulled from the wish cell: 48, 49, 171, 302, 307, 308, 309, 332, 381.

