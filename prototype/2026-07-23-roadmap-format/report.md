# Conversion report — ROADMAP.md → queue-member format (row 480, PROTOTYPE)

Override table applied (rowconv.py, orchestrator triage 2026-07-23): row 99 → archive verbatim (stale in-work leader over a landed close); row 445 → archive with its status cell corrected to `**landed 2026-07-23 (v4.0.0)** — (status note: <old cell verbatim>)` (the spec-format conversion, shipped v4.0.0 2026-07-23, cell never updated at landing); row 69 → `*deferred* 2026-07-05 — revisit trigger: the next edit to the product-prover skill` (date = first git appearance, 810af02).

## Totals

- rows in (body data rows): 345
- archived: 227 (226 verbatim + row 445 with the corrected cell)
- live (normalized, ascending id order): 118
- live by status: queued 86 · in-work 3 · deferred 26 · far 3
- ambiguous / safe-default-live: 3  (235, 241, 424)

## Proof verdict

PASS — every word-token and punctuation difference between the OLD body and the NEW (live body + July archive) is attributed to a named delta class with matching signed counts; residual empty. Row 445's added landed-marker tokens stand as a named per-row delta. See out/proof-report.md.

## Validation

- queue_row_lint (SPEC INV-277), run via the REAL tests/test_traceability.py TestQueue with read repointed at out/: 118/118 live rows pass, reach line printed; fixtures, class-vocabulary test green.
- test_roadmap_in_work_cap (re-keyed by the orchestrator to the italic form): PASSES — counts rows 386, 412, 480 = 3, at the T-18 cap of 3.
- guardrails/check-doc-rotation.py --base out --doc ROADMAP.md: OK — nothing lost, no rotated row still live.

## Declared deltas (each counted)

- Closed rows moved to the July archive: 227 rows — 226 verbatim (cancel in the proof) + row 445's corrected status cell (adds `**landed 2026-07-23 (v4.0.0)** — (status note: )` around the old cell, tokenized and reconciled).
- Status normalized to `*word* DATE`, old status preserved verbatim in the wish cell's `(status note: …)`: 118 live rows; per row ADDED the wrapper (`status`,`note`; `(` `)` `:`) and the new status cell.
- Deferred rows carry a revisit-trigger clause: 26 rows (row 69's named by override, the rest `see the status note`).
- Sixth drift cell dropped: 27 live rows (removes `—` ×27 and `|` ×27); closed 6-cell rows keep theirs in the archive.
- Class re-vocabularying: row 411 far→surface; row 455 big→large (2 rows).
- Preamble replaced (old 212 word tokens → new ~534, excluded from the proof, reported); manifest keeps the 2026-07-18 line + one July line; archive header generated (excluded, reported).

## Flags for the orchestrator

- Ambiguous rows kept live (deferred): 235, 241, 424 — review whether each leg is truly still open.
- Dates pulled from the wish cell (status had none): 48, 49, 171, 302, 307, 308, 309, 332, 381.

