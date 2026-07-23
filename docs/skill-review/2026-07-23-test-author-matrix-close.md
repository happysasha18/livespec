# Skill review — test-author (skill-creator review of the matrix-close reteach, row 477)

`SKILL-REVIEW`

Skill: test-author
Date: 2026-07-23
Reviewer: skill-creator review, applied over the delta at the TEST_MATRIX format conversion.

Verdict: passes — the close instruction (step 8) was re-taught from a hand-walked coverage checklist
to the mechanical gates, and the new text reads as one coherent step, agrees with
`docs/test-matrix-format.md` and every shipped gate it names, and leaves no stale reference to the
retired checklist. No fix-worthy finding.

## What changed

Step 8 of the derivation principles, "Close by walking the coverage checklist", becomes "Close by the
mechanical gates, not a hand-walked list" — the checklist retires and its facts move to the row lint,
the generated Reference gate, and a standing interface-coverage suite check, with the matrix
`## Reference` named as generated-not-hand-edited output. (The same working tree also carries a pure
version-stamp bump 4.0.1→4.1.0, exempt from review by the gate's stamp carve-out.)

## Findings

- Coherence: the reworded step 8 is one coherent close procedure — it names what retires, why (the
  hand-walk let a missing level or a bare happy-path row slip), and the three mechanical homes that
  now hold each fact. Reads clean in place among the numbered principles. No defect.
- Agreement with the format doc and the shipped gates — all four named artifacts exist and do what the
  step claims:
  - `test_matrix_rows_have_level_and_negative_side` in `tests/test_traceability.py` reds a row that
    pins no ladder level or states no never side and NAMES the offending row (verified in the test
    body and its red-proof `test_row_lint_names_a_levelless_or_one_sided_row`). Matches the doc's
    "## The row lint" section.
  - `guardrails/check-matrix-reference.py` reds a body anchor missing from the Reference and a
    Reference anchor no body row carries (verified in the gate's THE LAW block). The step summarizes
    the two coverage-relevant faults; the gate's third fault (committed Reference vs a fresh build) is
    the hand-edit guard the step covers separately via "never hand-edited". Accurate, not a misstatement.
  - `scripts/build-matrix-reference.py` exists and builds the `## Reference`; the step's
    "generated output, the way the spec's own code-to-location table is" matches the doc.
  - `tests/test_interface_coverage.py` holds the interface-level-row-per-block and
    layer-to-level (P8, P9) rules; its module header names "P8+P9" and its tests enforce both. Matches.
- No stale reference to the retired hand-walked checklist anywhere in the skill body: the only
  "checklist" mention is step 8's own announcement of the retirement (the one other hit is the pack
  footer's line about the publish skill, unrelated).
- Trigger and structure sound: the frontmatter description and the skill's structure are untouched by
  this delta; the change is confined to one numbered principle. The suite's own needle-phrase
  assertions against this skill (`tests/test_interface_coverage.py`: the layer-to-level rule, the
  interface-test requirement, and the coverage-checklist-gains-both check) all still resolve against
  the reworded body (verified against the whitespace-flattened text the suite reads).

none fix-worthy — no suggested edit for the orchestrator to apply.
