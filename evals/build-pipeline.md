# Eval — build-pipeline (SPEC E-19)

## Scenario

Both arms get the same task; the with-skill arm first reads `skills/build-pipeline/SKILL.md` and works
by it. Prompt (verbatim):

> You maintain a small CLI project; the repo contains SPEC.md, ARCHITECTURE.md, TEST_MATRIX.md, a pytest
> suite in tests/, and the tool's source. A user reports: "mytool --export out/report.csv silently
> writes an EMPTY file when the out/ directory doesn't exist."
> Describe EXACTLY what you would do to handle this report — step by step, in order, from the moment you
> read it to the moment you consider it done.

## Criteria

| Criterion (the skill's promise) | bare | with-skill |
|---|---|---|
| The door named aloud BEFORE any file touch (T-12; bug → matrix → test → code entry, not the full walk) | RED — no door step; plan opened with reproduce-then-code framing | GREEN — step 1 names door=bug · kind=product · priority · size, enters at the bug door |
| The work-kind named at intake (T-16) | RED — absent | GREEN — kind called (product: the CSV is the user's artifact) |
| Fix the class, sweep look-alikes (base rule 14) | MET BARE — loader-fed run swept sibling write paths | GREEN |
| Red-on-bug test BEFORE code (step 6) | MET BARE | GREEN |
| A pending human question never parks the lane (INV-4): recommend + batch + proceed | RED — bare plan says "I'd stop and ask rather than guess" | GREEN — question batched with class findings, proceeds on a stated default if deferred |
| Guardrails run named before done (pipeline teeth) | RED — absent | GREEN — pre-push check named as a step |
| Verify by deed on the real artifact (step 8) | MET BARE (manual re-run present) | GREEN |
| Plain-language report to the owner before push (step 9 / T-7) | MET BARE (partial — report present, push-gate respected) | GREEN — report step names files + verified output |
| The capture echo at intake: the report is echoed back in one sentence — heard · door · name · row (step zero; SPEC INV-27, added 2026-07-06) | — (criterion added later) | scored from the 2026-07-06 re-run |
| Verify in the medium's own form (step 8; SPEC INV-30, added 2026-07-06): a CLI verifies by the command round-trip on the real artifact, not "tests pass" alone | PARTIAL (2026-07-06 push re-run) — manual re-run present | GREEN (same re-run) — real command run AND real file read, sibling flags included |
| A taken default is TOLD at landing, never confirmed (step 9; SPEC INV-31, added 2026-07-06): the report names the choice with an example and a tweakable mark, asks nothing | RED (2026-07-06 push re-run) — would ask before committing | GREEN (same re-run) — "named as a tweakable default rather than asked-and-blocked-on" |
| A delegation brief carries the ledger walk + the clock (ACT-3; added 2026-07-06 batch 2) | — (bare plans no delegation) | PARTIAL (2026-07-06 batch-2 re-run) — brief sketch names exact edits + checkpoint path, neither clock nor ledger line; the scenario only brushes delegation |
| Steps worked in their craft's head (INV-33; added 2026-07-06 batch 2) | — | PARTIAL (same re-run) — substance craft-true (matrix derivation reads QA, verify reads the user's own eyes), no hat named |

## The red

The bare run (bare run: 2026-07-05, Sonnet worker, zero tool uses — record
`docs/evals/2026-07-05-first-run/bare-build-pipeline.md`) produced a strong loader-fed plan (class
sweep, red-first, spec sync all present — the honest boundary in evals/README.md at work) but never
NAMED the door or the kind, planned to PARK on the design question ("stop and ask rather than guess" —
the exact anti-pattern of INV-4), and never ran the guardrails. The with-skill run (same day, record
`with-skill-build-pipeline.md`) opened with the intake line (door · kind · priority · size), entered at
the bug door, batched the question and kept the lane moving, and put the guardrails and the
report-before-push where the law puts them.

## Re-run

One Sonnet worker per arm. Bare arm: the prompt above + "do not invoke any tools or skills". With-skill
arm: "First read skills/build-pipeline/SKILL.md and work strictly by it" + the same prompt. Score each
criterion; append the dated record to `docs/evals/`.
