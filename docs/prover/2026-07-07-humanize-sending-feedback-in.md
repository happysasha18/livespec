# Prover cross-link — SPEC humanize batch: "Sending feedback in" (2026-07-07, session 24 cont.)

Register rewrite of one scenario section. This record is the git-diff fact table (old → new), built from
`git diff SPEC.md`, not from the new prose alone. Question per row: does the new prose still carry the
fact, precondition, invariant, route, fence, and non-goal the old prose claimed?

Mechanical gates already green before this record: needle re-match 18/18 section-scoped (`needle-extract.py
--verify`); anchor set identical to the captured baseline (every count matches, no ID changed, all trailing);
full suite 175 green.

## Fact table (old claim → new carrier → verdict)

| # | Old fact / anchor | New carrier | Verdict |
|---|---|---|---|
| 1 | Feedback = anything handed back, any size/moment/channel [E-28] | "at any size, any moment, through any channel … [E-28]" | KEPT |
| 2 | Host's product's users' reports travel same road once a session receives them [E-28] | same sentence, split for length; anchor still trails | KEPT |
| 3 | Promise: nothing lost, everything answered by a route | "nothing handed in is ever lost, and everything handed in is answered by a route" | KEPT |
| 4 | Four routes → homes (wish→queue row; answer→archive+harvested row; fix→commit+journal; noise→problem ledger) | rendered as a 4-item list, all four homes present | KEPT |
| 5 | Feedback ledger FEEDBACK.md, append-only, at host root [default], owns evidence/reactions/wordless drops | "**feedback ledger (FEEDBACK.md)** … append-only file beside the queue at the host root [default]" | KEPT |
| 6 | One dated line: when·who+channel·what it concerns·plain words·where it went | all five fields present in the "line records" sentence | KEPT |
| 7 | One echo per item; wish-shaped echo IS wish echo [INV-27]; else hears heard+where | KEPT verbatim needles + [INV-27] trailing | KEPT |
| 8 | Re-mention appends date, changes nothing else [INV-68] | "appends its date to the existing line and changes nothing else … [INV-68]" | KEPT |
| 9 | Three channels one contract [T-20]: spoken/typed; comment on shown [INV-4,INV-64]; dropped file one NEW file [E-11] swept [T-10], no-words→one question, guess never written | list preserved; all anchors trailing; "the ledger never records a guess" (positive restatement of "a guess is never written") | KEPT |
| 10 | Route WISH: walks intake, row is home [T-12, INV-27] | KEPT | KEPT |
| 11 | Route fix-sized→FIXED same session (commit+journal); story-sized queues | KEPT | KEPT |
| 12 | Route answer→CLOSES forever, harvested, archive+harvested row [INV-59] | KEPT | KEPT |
| 13 | Route reaction→FIELD EVIDENCE, cites scenario, success-measure sentence [INV-21] gains place, first honest slice, machinery stays [target] row 48, grows to wish only by word/tripwire | KEPT, all anchors trailing; em-dash aside for "measurement plugins, aggregation" (list aside, not a scissors contrast) | KEPT |
| 14 | Route workshop noise→problem ledger [INV-23]; seam=subject: product→FEEDBACK.md, workshop→PROBLEMS.md, one home each | KEPT; two-destination statement kept positive (both destinations named) | KEPT |
| 15 | feedback-intake owns it; fires on handed-in item + inbox sweep; not on own output/own question/mere mention; unsure→one question; never opens queue row on own judgment, wish door owns verdict [T-20] | KEPT; the three no-fire cases rendered as an explicit list, needle "never opens a queue row on its own judgment" verbatim, [T-20] trailing | KEPT |
| 16 | Fences (5) [E-11, T-10, INV-27, T-12, INV-59, INV-23, INV-1] | 5-item "Fences its birth must hold" list, every anchor trailing | KEPT |
| 17 | Composition: outside sessions never edit ledger; only assigned session appends [INV-10, INV-11]; append-only archives like queue [INV-1] | KEPT; needle "only the assigned session" verbatim | KEPT |
| 18 | Facets: surfaces ledger+chat echo; media own layout/touch/a11y/perf; empty state = header only, healthy; else N/A [default] | KEPT as list | KEPT |
| 19 | Non-goals (3): no end-user widget (visitors ride row 48/own wish); no auto read/score/aggregate ([target]); no new door mechanics | KEPT as list | KEPT |
| 20 | Success measure: never hand in same item twice; findable with route same session [default] | KEPT; "the human" → "You" (register rule 8, address the reader) | KEPT |

## Anchor→sentence pairing check (set-equality is necessary but not sufficient)

No anchor migrated to a weaker sentence. Spot-checked the load-bearing ones:
- [E-28] still trails the "users' reports travel the same road" clause.
- [INV-21] still trails the success-measure-sentence clause inside the FIELD EVIDENCE route.
- [INV-68] still trails the "appends its date … changes nothing else" clause.
- [T-20] both occurrences trail the same two clauses (three-channels contract; never-opens-a-queue-row verdict).

## Wording changes worth naming (meaning intact)
- Passive→active in two fences ("workshop noise still lives in the problem ledger alone" → "The problem
  ledger still holds workshop noise alone"; anchor and fact unchanged).
- "the human" → "You" in the success measure (register rule 8). Same subject.
- The final dense edges paragraph split into four labelled lists (Fences / Composition / Facets / Non-goals)
  plus the standalone success measure. No fact added or dropped.

Verdict: **CLEAN.** Every old fact, route, fence, facet, non-goal, and success measure carried; every
anchor preserved and trailing; 18/18 needles section-scoped; suite 175 green. No must-fix.
