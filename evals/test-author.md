# Eval — test-author (SPEC E-19, E-27)

## Scenario

Both arms get the same task; the with-skill arm first reads `skills/test-author/SKILL.md` and works
strictly by it. Prompt (verbatim core):

> The project: an offline HTML music-analysis widget rendered by a Python script. Two proven spec
> sections are given — the bug-lane scheduling feature (five acceptance criteria, anchors T-9, T-11,
> T-18; criteria 2–3 deliberately carry no anchor) and the run-page player feature (full / quick /
> no-audio runs, playhead on the time ribbon only, phone-width reachability; anchors INV-7, INV-9).
> Task: derive the test coverage for these two sections — the test cases, and for each HOW it
> asserts. Then the overall testing approach in 5–8 bullets.

## Criteria

| Criterion (the skill's promise) | bare | with-skill |
|---|---|---|
| The matrix is an ARTIFACT: inventory first, rows derived, coverage checklist walked at close | RED — tests derived directly, no inventory, no checklist walk | GREEN — artifact inventory opens; per-row derivation; the checklist walk closes and FLAGS a real gap |
| Every row states BOTH sides (do + never) | PARTIAL — strong negative assertions present, but per-scenario, not a per-row discipline | GREEN — every row carries its never side; several rows exist purely for it |
| A LEVEL pinned per row, by what the user would see broken | PARTIAL — levels chosen sensibly (DOM parse vs headless) but implicitly, per test, with parse-level as the default | GREEN — level named per row with the reason; the empty-shell fact forced to browser-computed because DOM-text would falsely pass an empty div |
| State space named before cells (view axes × data axes) | PARTIAL — fixtures per run-type exist; axes never named, cells not crossed systematically | GREEN — axes named for both sections before any row |
| Red-first proof discipline | RED — absent | GREEN — the bug protocol stated: matrix cell first, red proven, then code |
| Pinned skip-set (an unexpected skip is a failure) | RED — absent | GREEN — browser rows must RUN; a silent engine-missing skip named as the failure class |
| Traceability as a STANDING test | PARTIAL — tests named after anchors for visibility | GREEN — a suite-level check that fails on unanchored rows and uncovered facts |
| Derivation defects routed to their source | RED — the two anchor-less criteria went unnoticed | GREEN — flagged as a spec-derivation defect, routed back to spec-author before the matrix closes |

## The red

bare run: 2026-07-07, session 23 (a Sonnet worker, no skill read). An honest red: the bare arm's
assertion CRAFT was strong — real negative checks, sensible engine choices, property-based sequences,
anchor-named tests. What it lacked is exactly the method layer the skill carries: no matrix artifact,
no per-row level judgment as a recorded decision, no red-first, no pinned skip-set, no standing
traceability, and it walked past the planted anchor gap. The two arms agree on good taste; the skill
adds the derivation discipline that survives a weaker day and a weaker model.

with-skill run: 2026-07-07, same session, same model, same prompt plus the skill read. All eight
promises met; the planted gap caught and routed correctly.

## Re-run

Re-run both arms at the next milestone that touches the skill's method sections (the level ladder or
the derivation steps), and at any MINOR bump of the pack — same scenario, fresh workers; fold what
the bare arm newly does well (it sets the floor the skill must stay above).
