# Conversion report — ROADMAP.md → queue-member format (row 480, PROTOTYPE)

Source pinned to git 859dcfc. Round 7: the three-cell sweep — the classifier reads wish + status + acceptance per live row, catching landings recorded off the status cell. Verdict table in mapping.md ('Round 7 sweep'); SWEEP_OVERRIDES and the sweep rules recorded in rowconv.py.

## Totals

- rows in: 345
- archived: 231 (rounds 1-6: 228, incl. 99/128 by override and 445 corrected; round-7 sweep: 3 — rows 130, 279, 420)
- live: 114
- live by status: queued 75 · in-work 3 · deferred 33 · far 3
- round-7: queued→deferred 4 (133, 190, 261, 436) · re-triggered 3 (134, 140, 141) · ambiguous 0 · acceptance rewrites 1 (row 54 'stays in-work'→'stays open')

## Proof verdict

PASS — OLD (859dcfc) vs NEW body + July archive + status-notes entries; every difference a named delta with matching signed counts; residual empty. Round-7 deltas: sweep archives cancel verbatim; sweep-deferred trigger text counted inside the per-row status-cell addition (copy-not-move, notes stay verbatim); the rule-5 rewrite counts word `in-work`→`open` and the departing hyphen.

## Validation (against out/)

- real TestQueue: lint 114/114 with reach; in-work cap = 386, 412, 480 = 3; class vocab + fixtures green.
- delegation + footprint forward-landed scans: green (sweep-archived rows carry no `**landed`-immediate token ≥ 2026-07-12; notes file harmless).
- rotation gate: OK.

## Flags for the orchestrator

- NEEDS-TRIGGER remaining: 143, 144 — no named event anywhere in their cells.
- Round-7 verdicts open to veto: the three archives (130, 279 — my rule-6 read, 420 via SWEEP_OVERRIDES) and the four queued→deferred rows.

