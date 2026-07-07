# Eval — feedback-intake (SPEC E-19, E-28/T-20/INV-68)

## Scenario

Both arms get the same task; the with-skill arm first reads `skills/feedback-intake/SKILL.md` and works
strictly by it. Prompt (verbatim core):

> The project: a photo-portfolio website run by a disciplined process: a wish queue (ROADMAP.md), a
> journal, a decision archive (docs/decisions/), a workshop problem ledger (.live-spec/PROBLEMS.md),
> and an inbox/ folder. During one morning the owner hands in, all at once: (1) "галерея стала
> как-то медленно открываться на телефоне" (2) a saved answers-JSON from yesterday's decision page
> (3) a screenshot with a red circle around a caption typo (4) "друг говорит, что страница с картой
> запутанная" (5) a note that the thumbnail script warned about a missing dependency twice this week
> (6) an inbox/ file: a visitor's emailed praise of the museum-style hang. Task: for each item say
> exactly what you do — where it is recorded, what the owner hears back, what happens next.

## Criteria

| Criterion (the skill's promise) | bare | with-skill |
|---|---|---|
| Field evidence has ONE home (the feedback ledger) tied to the feature's success measure | RED — the friend's map remark became a "low-confidence backlog" queue row; the visitor's praise went to the journal against a decision file; no single place field signals accumulate | GREEN — both landed as dated FEEDBACK.md lines citing the feature's scenario |
| A reaction never becomes a queue row on the agent's own judgment | RED — the vague secondhand remark was queued | GREEN — "в задачу пока не превращаю"; a wish only by the human's word or a tripwire |
| Wish-shaped items walk wish intake (door, echo, row) | GREEN — the slow-gallery report queued for diagnosis | GREEN — same |
| An answer closes forever and is harvested (archive + row) | GREEN — decision archived, waiting row closed, build queued | GREEN — same |
| A fix-sized comment is fixed the same session, journal line, no queue | GREEN | GREEN |
| Workshop noise goes to the problem ledger, never the feedback home | GREEN — dated PROBLEMS.md row with an owner | GREEN — plus the append-a-date-on-re-mention discipline said |
| The inbox sweep is ONE commit: route landed + file removed | RED — the file was processed, the commit law unnamed | GREEN — said explicitly |
| One echo per item, the route named back | PARTIAL — natural replies given, the discipline unnamed | GREEN — one line per item, route named |
| Re-mention appends its date, changes nothing else | RED — absent | GREEN |

## The red

bare run: 2026-07-07, session 24 (a Sonnet worker, no skill read). An honest red with a strong floor:
the bare arm's process instincts are good — the decision archived with its raw JSON, the typo fixed on
the spot, the recurring workshop warning given an owner. What it lacked is exactly this skill's layer:
field evidence had NO home (one signal became queue spam, the other a journal note — scattered,
unreadable as a set, useless to a success measure), the one-commit sweep law and the
append-date-on-re-mention discipline were absent, and the echo was instinct rather than contract.

with-skill run: 2026-07-07, same session, same model, same prompt plus the skill read. All six items
routed exactly by the table; every criterion green.

## Re-run

Re-run both arms at the next milestone that touches the routing table or the ledger law, and at any
MINOR bump of the pack — same scenario, fresh workers; fold what the bare arm newly does well (it sets
the floor the skill must stay above).
