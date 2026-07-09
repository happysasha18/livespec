# [Project Name] — SPEC (v0.1, [date])

> How to read: each section is a scenario — what a person does and what they see. The short codes in
> brackets are quiet machine anchors (for the prover, the test matrix, and transcript greps); the Formal
> index at the end maps every anchor to its home section. Edit history lives in JOURNAL.md; this spec
> states today's truth.

**Founding answers (B-2).** personal-vs-reusable: ⟨DECIDE⟩ · asked of the human or read from their
profile at founding. Never inferred from examples. Add the other answers that shape this product.

**Current vs target.** [If anything below is designed but not yet shipped, say so here and mark those
sections `[target]` — the spec never claims shipped what isn't. Keep this block honest at every edit;
remove it only when everything stated is real.] [S-0]

## What [product] is

[One paragraph, plain words: why the product exists and its whole value to the person using it. Introduce
the main nouns in **bold** as you go — each first appearance is where that entity is defined (attributes,
unit/valid range if it's a measure) and gets its anchor.] [E-1]

## [The main scenario — name it by what the person DOES: "Analysing a track", "Throwing a wish", …]

[Walk it as prose: what the person does, what they see, what the system does underneath. Weave the formal
content into the walk. Never split it out into separate Entities/States/Actors chapters:]

[Each **entity** is defined in bold where the walk first meets it, with its attributes and states. [E-2]]

[Each lifecycle move is told as a step of the walk — which action, which actor, what triggers it. A state
with no way out is a bug; say what exits it. [T-1]]

[What is ALWAYS true while the scenario runs gets its own plain sentences — safety (what must never
happen) and liveness (what must eventually happen, within what bound):]
- [Plain-language invariant sentence — exact condition trails in the detail. [INV-1]]

## [The edge scenario — what happens when it goes wrong or is interrupted: "When a bug cuts the line", …]

[Every failure, interruption, and exception path the system can reach is a scenario too: what the person
sees, what the system guarantees, how the normal path resumes. An edge the spec doesn't walk is a gap,
even if the code "handles" it. [T-2] [INV-2]]

## Who decides what

[**The human** owns: taste, thresholds only they can pick, irreversible calls, … [ACT-1]]
[**The system / the agent** owns: … [ACT-2]]
[Every transition told above must trace to an actor named here. Decisions the spec can't make alone are
marked ⟨DECIDE⟩ inline and listed under Open decisions.]

## Composing across axes

[For every stateful surface, compose it across the canonical axis list: **view · mode · tier · viewport
size · persistence/reopen · concurrency** (where real). One surface = one name everywhere. For each axis
value: is the surface's state still visible, still reversible; does the transition preserve, reset, or
block it? If the surface persists state, walk the older-stored-value × current-code case too. Close with
the composition invariant as one plain sentence. [C-1]]

## Open decisions

- ⟨DECIDE⟩ [A call only the human can make — one line, with the leading question and the current pick if
  work proceeds on a recommendation. [D-1]]

## Formal index

Machine handles → home section. The prose above is the meaning; this table is only the derived map —
re-derive it whenever anchors change; it must never drift into a second truth.

| Anchor | One line | Section |
|---|---|---|
| S-0 | shipped vs target marked honestly | header |
| E-1 | [entity, one line] | What [product] is |
| E-2 | [entity, one line] | [main scenario] |
| T-1 | [transition, one line] | [main scenario] |
| T-2 | [transition, one line] | [edge scenario] |
| INV-1 | [invariant headline] | [main scenario] |
| INV-2 | [invariant headline] | [edge scenario] |
| ACT-1 | [the human: what they own] | Who decides what |
| ACT-2 | [the system/agent: what it owns] | Who decides what |
| C-1 | [composition rule] | Composing across axes |
| D-1 | [open decision] | Open decisions |

---

*Authored via spec-author (use-case-first shape: scenarios lead, codes trail as anchors, the Formal index
closes the doc). Review with product-prover before deriving the test matrix or writing code.*
