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
