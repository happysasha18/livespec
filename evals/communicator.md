# Eval — communicator (SPEC E-19)

## Scenario

Both arms get the same task; the with-skill arm first reads `skills/communicator/SKILL.md` and works by
it. Prompt (verbatim):

> You just finished a work session on a music-analysis app whose owner is a music producer
> (non-technical, reads messages on his phone). Session facts: queue rows 12 (per-stem loudness meters),
> 14 (fix the crooked recommendations grid), 15 (faster widget load) all landed; row 16 (the evidence
> panel) is blocked on one open question — should advice cards sort by urgency or by time? your
> recommendation is urgency; the test suite is 64 green; version 0.9.16 is committed but NOT pushed
> because the owner holds the push gate.
> Write the message you would send the producer right now.

## Criteria

| Criterion (the skill's promise) | bare | with-skill |
|---|---|---|
| Plain product words, no dev jargon walls | MET BARE | GREEN |
| The map as a map: status icons (✅/🙋/⬜), one substance clause per line (rule 9) | RED — bullet prose, no map, no explicit "what remains" | GREEN — icon map, every line carries substance |
| The one decision asked cleanly with the recommendation marked (rules 2/7) | MET BARE (recommendation present) | GREEN |
| No internal bookkeeping doing the talking (rule 8): version numbers / "64 green checks" as message content | RED — "Committed as 0.9.16", "64 green checks" | GREEN — "tested clean, saved, not pushing until you say" |
| Retell, don't reference: row numbers trail, never lead | MET BARE | GREEN (rows trail in parens) |

## The red

The bare run (bare run: 2026-07-05, Sonnet worker, zero tool uses — record
`docs/evals/2026-07-05-first-run/bare-communicator.md`) wrote a decent plain-words message but shipped
NO map of where the project stands (no icons, no what-remains line) and let internal bookkeeping talk
("Committed as 0.9.16", "64 green checks"). The with-skill run (same day, record
`with-skill-communicator.md`) flipped both: icon map with per-line substance, bookkeeping reduced to
"tested clean / saved / not pushing until you say". Honest note: the with-skill run misread the sort
question as within-card ordering (scenario ambiguity, not a skill defect) — the scenario sentence
could name "advice cards" more precisely at the next re-run.

## Re-run

One Sonnet worker per arm. Bare arm: the prompt above + "do not invoke any tools or skills". With-skill
arm: "First read skills/communicator/SKILL.md and work strictly by it" + the same prompt. Score each
criterion; append the dated record to `docs/evals/` (append-only). The honest boundary
(evals/README.md) applies: bare is bare-of-the-SKILL.
