# Scores — build-pipeline eval rerun (2026-07-06)

Arms: `bare-build-pipeline.md` (no skill read) vs `with-skill-build-pipeline.md` (SKILL.md read in full
first). Scored against the criteria in `evals/build-pipeline.md`, plus the new capture-echo criterion.

| # | Criterion | bare | with-skill |
|---|---|---|---|
| 1 | The door named aloud BEFORE any file touch (bug → matrix → test → code entry) | RED — opens with "reproduce the bug locally," no door/entry-point named anywhere | GREEN — step 1 names door=bug, work-kind=product, states the entry point (bug → matrix → test → code) before any tool call |
| 2 | Work-kind named at intake | RED — absent throughout | GREEN — "product" named in the same step-1 line, with the reason (mytool is the CLI the user runs, the CSV is the artifact they receive) |
| 3 | Fix the class, sweep look-alike write paths | RED — this run's bare plan never looks for sibling flags/write-paths; the fix is scoped to `--export` only, at every step | GREEN — step 4 names the class explicitly and greps for every `--*-file`/`--output`/`--log` sibling; steps 8–10 (matrix, tests, fix) all carry "and every sibling from step 4" |
| 4 | Red-on-bug test BEFORE code | MET BARE — step 6 ("write a failing test") precedes step 7 ("fix the code") | GREEN — step 9 writes the failing tests across the whole class and confirms they fail before step 10's fix |
| 5 | A pending human question never parks the lane: recommend + batch + proceed | RED — step 5 states the decision explicitly then says "I'd stop here and ask ... rather than guess" — the lane parks on the open question, the exact anti-pattern the pack's INV-4 names | GREEN — step 6 states a recommended default (fail-loud), batches it with the class findings into one question, and proceeds on the default now; the human's real answer is a later one-line change, not a blocker |
| 6 | Guardrails run named before done | RED — no guardrails/pre-push check appears anywhere in the plan | GREEN — step 12 explicitly runs the completeness / tests-present / bounds / conflicts guardrail check before calling it done |
| 7 | Verify by deed on the real artifact | MET BARE — step 9 manually re-runs the original repro command end-to-end | GREEN — step 13 runs the real CLI against a real missing directory and inspects the real result, not the test suite alone |
| 8 | Plain-language report to the owner before push | MET BARE, partial — step 12 says it wouldn't push/merge without the user confirming the chosen behavior, but never describes a structured report (files touched, verified output) | GREEN — step 15 is a dedicated report step: what broke, what the class search found, which contract was applied, files touched, the real verified output — all before push |
| 9 | NEW — capture echo at intake: the report echoed back in one sentence, heard · door · name · row | RED — no echo of any kind; the report is acted on directly, never restated back | GREEN — step 1 closes with a literal one-sentence echo: "Heard — mytool --export writes a silently-empty CSV when the target directory is missing. Door: bug. Work-kind: product. Entering at bug → matrix → test → code." |

## Tally
- bare: 0 GREEN, 3 MET BARE (criteria 4, 7, 8 — one partial), 6 RED (1, 2, 3, 5, 6, 9)
- with-skill: 9 GREEN, 0 RED

## Notes
- This rerun's bare arm is markedly weaker on criterion 3 (class sweep) than the 2026-07-05 first run's
  bare arm, which happened to sweep siblings unprompted. That's the honest variance of an unstructured
  "plain assistant" answer — nothing here should be read as the bare arm reliably covering the class; it's
  a coin that sometimes lands heads without the skill's explicit "name the class, grep for it" step.
- The bare arm's single most consequential miss is criterion 5: it doesn't just fail to batch-and-proceed,
  it actively models the anti-pattern (naming the fork, then stopping to ask instead of recommending a
  default and moving). That is the gap the pack's INV-4 exists to close.
- The with-skill arm's answer traces cleanly to specific SKILL.md lines: the door/kind intake and capture
  echo (step zero + "When to run it"), the class-sweep and RECURRING re-door check (the "Bug:" bullet),
  the matrix's both-sides-and-level rule (step 5), red-on-bug (step 6), the guardrails teeth section, and
  the report-before-push language in step 9 ("Commit & show").
