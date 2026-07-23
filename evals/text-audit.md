# Eval — text-audit (SPEC E-19)

## Scenario

Both arms audit the same planted paragraph for comprehension; the with-skill arm first reads
`skills/text-audit/SKILL.md` and runs its loop (mechanical lints, then a fresh cold reader under the
skill's reader-prompt, findings classified blocking or non-blocking). The text under audit (verbatim):

> ## About the workspace
> The Relay Gate is what keeps the workspace coherent. Each panel's refresh depends on the upstream
> state, and a stale panel is refreshed as soon as the gate clears. The Relay Gate is a coordinator —
> not a queue — so panels never wait on one another. When the workspace loads, the gate runs first and
> every panel registers with it before the first refresh.

Planted holes: an undefined coined term ("Relay Gate", used as the load-bearing subject and never
defined) · an unfilled relational word ("refresh depends on the upstream state" — no stated what the
upstream state is or how the refresh depends on it) · a contrast-by-denial definition ("a coordinator —
not a queue", naming the thing by denying its neighbour) · two smaller undefined terms ("coherent",
"the gate clears") that a close reader may also stop on.

The prompt (both arms) states the task the way a person states it, with no facet enumerated:

> Audit this paragraph — will a stranger understand it? Tell me where a reader would stop.

## Criteria

| Criterion (the skill's promise) | bare | with-skill |
|---|---|---|
| Flags the undefined coined term "Relay Gate" (load-bearing subject, never defined) | MET BARE — named it a coined name with no definition, first use pinned | PARTIAL — the lint-step rewording of the denial frame part-defined the term ("is a coordinator: it clears panels to refresh…"), and the cold reader then returned it only non-blocking; never flagged blocking with the first use pinned |
| Flags the unfilled "depends on the upstream state" (relational word, empty slot) | MET BARE — "upstream of what… a term the paragraph never grounds" (the predicted red fell: the loader-fed bare arm caught it) | GREEN — flagged blocking, the empty slot named (what is the upstream state, what fires the refresh) |
| Flags the contrast-by-denial definition "a coordinator — not a queue" | MET BARE — read as define-by-what-it-isn't plus a non-sequitur (the predicted red fell) | GREEN — `spec-style-lint.py` hit, fixed before the reader; the fix states what the coordinator does in its own sentence |
| Every finding classified blocking or non-blocking | RED — flowing prose, no per-finding verdict | GREEN — 6 blocking, 4 non-blocking, the loop keyed to zero blocking |
| Mechanical lints run before the reader | RED — no lints, one prose pass | GREEN — five lints run first (two on their grep fallbacks for a glossary-less paragraph); the one hit fixed before the reader |
| Fixes drawn from the source, never invented | RED — no fix pass at all: nothing invented, but no fix and no question for the person either | GREEN — four `[GAP]` marks and four owner questions, no invented definition |
| The loop's close stated: two consecutive clean reads | RED — one pass, no termination rule | GREEN — states the two-clean-reads close, and reports the loop honestly open pending the owner's answers |
| The reader runs with zero context on the text's history | RED — the same session that got the audit framing did the reading | GREEN — a fresh agent under the verbatim reader-prompt, given only the corrected text |

## The red

bare run: 2026-07-23 (one Sonnet worker per arm; records at `docs/evals/2026-07-23-text-audit/`). The
red is **method-only**: the loader-fed bare arm caught all three planted defects in substance — the
undefined "Relay Gate", the empty "depends on the upstream state" slot, and the "coordinator — not a
queue" frame read as define-by-denial plus a non-sequitur — so the first three criteria scored MET
BARE, two of them against the file's earlier predicted reds. What the bare arm did NOT do is the
skill's discipline: no mechanical lints, no blocking/non-blocking verdict on any finding, no fix pass
at all (it stopped at diagnosis — nothing invented, but no question for the person recorded either),
no fresh zero-context reader, and no termination rule — one pass, done.

The with-skill run supplied exactly that discipline: the lint scripts first with the style hit fixed
before any reader, a genuinely fresh reader under the verbatim reader-prompt, 6 blocking and 4
non-blocking findings, four `[GAP]` marks and four owner questions in place of any invented
definition, and the two-consecutive-clean-reads close stated with the loop honestly reported open. It
also surfaced an unplanted defect: the tension between "depends on the upstream state" and "panels
never wait on one another". One regression the run recorded: the lint-step rewording of the denial
frame part-defined "Relay Gate", muting the cold reader's coined-term finding to non-blocking — the
lint-fix rule and the vocabulary rule interact, and the coined-term criterion scored PARTIAL, not
GREEN.

## Re-run

One worker per arm. Bare arm: the paragraph + "audit this text; do not invoke any tools or skills".
With-skill arm: "First read skills/text-audit/SKILL.md and work strictly by it" + the same paragraph.
The with-skill reader must run with the pack not loaded (the clean-agent split, `docs/spec-style.md`).
Score per criterion; append the dated record to `docs/evals/`.
