# product-prover — register rewrite notes (2026-07-22)

Scope: register-only rewrite of `skills/product-prover/SKILL.md` and `skills/product-prover/README.md`.
No rule/lens/step meaning, scope, or force changed. All code anchors (INV-x, M-x, E-x) kept. Frontmatter
`description` trigger semantics untouched. Base-rule references by number kept. Tests/ and guardrails/ not edited.

## Counts

- Contrast-by-denial (scissors) fixed: **26** — 15 in SKILL.md, 11 in README.md.
  - SKILL.md: lines 42, 104 (×2), 279, 283, 292, 318, 342, 349, 357, 374, 380, 381 (×2), 424.
  - README.md: lines 43 (×2), 47 (×2), 80, 99, 129 (×2), 137 (×2), 139.
- Drama / inflation flattened: **1** — SKILL.md line 133 "The juice." → "These are the findings that matter most."
- Register-lint findings fixed: **2** — SKILL.md lines 203 and 215, the `en-say-so-plainly` self-certification
  pattern ("Say so plainly" / "say so plainly", both agent-directives) reworded to "State that plainly".
  These were pre-existing lint hits, not introduced by this rewrite; reworded to reach a clean lint verdict.

## Lint verdict

`scripts/preshow-register-lint.py` on both files: **OK (clean)** — no coined metaphor, calque, or
transliterated pack term. (Final run after all edits.)

## Cold-read rounds

- **Round 1 (fresh stranger, full files):** flagged ~9 BLOCKING stops. All but one were pre-existing,
  load-bearing pack vocabulary (dual, twin, net, fold, "second-sibling question", "blank-answer class",
  mid-sentence INV-anchor density) — outside a register-only rewrite and protected by the "keep meaning /
  keep anchors / keep cross-references" contract. None were introduced by this rewrite. The one item inside
  register scope and meaning-safe — SKILL line 318 "the complement it does not ask" (define-by-what-it-is-not
  + unfilled relational word "complement") — was fixed to "the question entry symmetry does not ask".
- **Round 2 (confirming stranger, rewritten sentences):** remaining BUMPY flags were out-of-context artifacts
  (antecedents like "it" are clear in the full document) or pre-existing bullet/gerund structure, and each
  rewritten sentence is an improvement over the scissor it replaced. Acted on one: SKILL line 292 tightened
  from one long clause into two sentences.

## Pins recorded (a changed sentence that appears in tests/)

1. **`tests/test_full_pass_coverage_record.py`** — phrase "five colliding angles" appears in the module
   DOCSTRING (lines 9–10), NOT in any assertion, so no test breaks.
   - OLD (skill): "so the one lifecycle is walked once rather than from five colliding angles; each sub-question keeps its own anchor:"
   - NEW (skill): "so the one lifecycle is walked once as a single pass; five separate angles would otherwise collide over it. Each sub-question keeps its own anchor:"
   - The pinning test file was not edited. Assertions in this test ("**Lifecycle**", the six lens names,
     "surface × sweep", "hit / clean / N/A-with-reason", "A missing verdict line reads as a skipped sweep")
     are all preserved. Test re-run: green.

No other changed sentence has a distinctive fragment present in tests/ or guardrails/. (Grepped every
changed fragment; only the two below surfaced, and the second was left unchanged — see risk list.)

## Left unchanged because rewriting risked meaning or pack-consistency

1. **"never a serializing surface" (SKILL line 380).** The clause "the shared living docs are a convergence
   point reconciled at integration, never a serializing surface" carries the canonical INV-49 phrasing that
   is ASSERTED in `tests/test_traceability.py` against `PRODUCT_SPEC.md`, `skills/build-pipeline/SKILL.md`,
   and `TEST_MATRIX.md` (needles "convergence point" and "never a serializing surface"). Editing product-prover's
   copy would not break the test (it reads other files) but would diverge product-prover from the pinned
   canonical form across the pack. Left intact.
2. **"co-location alone owes a lane not a queue" (SKILL line 380).** A tight technical binary — parallel lane
   vs serial queue, two named mechanisms — judged a lawful/instructional distinction, not a definitional
   contrast. Left to preserve the canonical INV-49 sentence.
3. **"recommend rather than ask" (SKILL lines 44, 447; README line 139).** Lawful instructional substitution
   (a directive: do X rather than Y), and a recurring pack idiom. Kept as the lawful class; reported as the
   only remaining "rather than" hits after the sweep.
4. **Pre-existing dense pack vocabulary** flagged BLOCKING by the cold reader (dual/twin/net/fold/"second-sibling
   question"/"blank-answer class" and mid-sentence INV-anchor density at SKILL lines 101, 126, 167, 173, 185,
   193, 279, 290, 380, 381). These are load-bearing pack terms carried by code anchors and cross-references
   the task requires kept; grounding or removing them risks meaning and pins. Not introduced by this rewrite.
   Left unchanged as out of register-only scope.

## Suite note

Ran the product-prover-adjacent test set. The product-prover assertions all pass (including
`test_prover_carries_the_class_lens`, `test_entry_state_lens`, `test_full_pass_coverage_record`,
`test_finding_kind`, `test_scenario_entry_exit`, `test_delivery_separability`, `test_transition_payload_lens`).
Four failures observed in that set are pre-existing and read OTHER files — `skills/build-pipeline/SKILL.md`
(test_craft_ladder, test_build_pipeline_bug_entry_drives_the_hunt), plus test_skill_evals_present and
test_real_repo_lists_complete (evals/, PRODUCT_SPEC, README, OVERVIEW). None read product-prover's changed
content; none attributable to this rewrite.
