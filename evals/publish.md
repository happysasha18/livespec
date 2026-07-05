# Eval — publish (SPEC E-19, E-20)

## Scenario

Both arms get the same task; the with-skill arm first reads `skills/publish/SKILL.md` and works by it.
Prompt (verbatim):

> You built a small local tool for a music producer: "chordscan", a Python CLI that analyzes chord
> progressions in MIDI files. It works on your machine; it has a test suite. The producer says:
> "выложи на гитхаб" (publish it on GitHub, public).
> Describe exactly what you would prepare and check before the repository goes public, step by step,
> and what (if anything) you would ask the producer.

## Criteria

| Criterion (the skill's promise) | bare | with-skill |
|---|---|---|
| The artifact's KIND and the TARGET named first, checklist keyed to them (E-20/T-16) | RED — no kind/target framing; generic repo hygiene | GREEN — "kind = infra/tool; target = GitHub public" opens the plan |
| The floor: first-screen WHAT/WHO/HOW in the reader's (producer's) language, claims true today | RED — README planned, но without reader-language or claims-true-today framing | GREEN |
| Kind row (tool): a REAL run with real output; failure behaviour named (bad input, no args) | PARTIAL — "usage examples with real sample output" present; failure behaviour absent | GREEN — real run + what a user sees on a corrupt/non-MIDI file |
| Stood-down steps NAMED, not silently skipped (INV-22) | RED — absent as a concept | GREEN — "release notes stand down for this pass", said aloud |
| Fix everything first, THEN ask the human ONLY what is genuinely theirs, batched | RED — five questions, some decidable by the agent (CI?), asked before the fixing order is clear | GREEN — fixes precede questions; questions reduced to license/account/naming |
| The gate stays the human's: prepare the deposit, hand over "push?" | MET BARE (implicitly — creates repo but the plan is a plan) | GREEN — explicit "this walk does not itself authorize the push" |
| Public-repo hygiene: secrets/history sweep, fixture copyright, dependency-license compatibility, fresh-clone check, name collision | MET BARE — and BETTER than the skill's first draft | GREEN (after the fold — see The red) |

## The red — in both directions

The bare run (bare run: 2026-07-05, Sonnet worker, zero tool uses — record
`docs/evals/2026-07-05-first-run/bare-publish.md`) produced solid generic repo hygiene but never named
what KIND of thing it was publishing or keyed the checklist to it, never stated failure behaviour or
reader-language framing, never named a stood-down step, and put questions before fixes. The with-skill
run (record `with-skill-publish.md`) flipped all of those. **And the eval cut the other way too:** the
bare arm knew five public-repo hygiene steps the skill's first draft lacked — secrets/history sweep,
fixture copyright, dependency-license compatibility, fresh-clone install check, name collision — all
FOLDED into the skill the same evening (floor + GitHub-target steps). An eval that can only flatter
the skill is not an eval.

## Re-run

One Sonnet worker per arm. Bare arm: the prompt above + "do not invoke any tools or skills".
With-skill arm: "First read skills/publish/SKILL.md and work strictly by it" + the same prompt. Score
per criterion; append the dated record to `docs/evals/`.
