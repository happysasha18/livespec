# Prover record — INV-46 trigger broadened (audit as a standing station) — 2026-07-12 s40

Prover skill version at this pass: product-prover 1.0.8. Mode: short form (SPEC INV-61 — small skill-kind
delta sharpening one existing invariant, no new surface, no structure change). This change EDITS a method
invariant, so by the very rule it lands it owes a fresh-context adversarial audit — a FABLE pass runs beside
this prover pass and folds before the landing (dogfooding the new trigger on its own first act).

## The delta

INV-46's mandatory trigger broadens from one case to three, each one where a single head both makes and
judges the work: (1) the code step was delegated AND the delta is surface-sized (the old case); (2) the
change edits the method itself — a new or changed invariant — because the author is blindest to a
contradiction with the pack's own existing law; (3) the only reviewer is the author (self-built +
self-proven, no independent read). Born of today's INV-128 landing: the author's own prover pass read it
clean, and a fresh Fable context caught a real contradiction with the door law (INV-16). Homes: the spec
INV-46 clause + Formal index, build-pipeline's verify step, the M-144 matrix row. No new invariant code — a
sharpening in place (one home per fact: the trigger lives in INV-46). Test: `test_adversarial_verify_option`
extended for the three cases, red-proven against the pre-delta build-pipeline copy then green.

## Findings (product-prover pass)

**0 must-fix from this pass.** Checks walked:

- The sharpening stays in INV-46's one home; the spec clause, build-pipeline text, matrix row, and test all
  carry the three cases (no drift between homes).
- The distinction from the product-prover pass holds: the prover reads the DOCUMENT for gaps; the INV-46
  audit is a FRESH-CONTEXT re-derivation from the spec sentences with the "goal missed" hypothesis — a
  different check, now required exactly where the author's own review shares the blind spot.

## Open question carried to the Fable audit

The one real risk I want the fresh eyes on: case (2) makes the audit mandatory for EVERY new or changed
invariant, and this pack lands invariants in batches (five today). Does that create an unworkable burden — a
spawned agent for a one-word invariant tweak — and does the law need a proportionality escape (the senior
may satisfy it with a genuinely fresh re-read for a small law edit, reserving a spawned fresh agent for a
surface-sized or high-stakes change)? The Fable audit's answer folds here before the landing.

## Fable adversarial audit — findings folded before landing (2026-07-12)

The change edits a method invariant, so by its own new rule it owed a fresh audit — this is that dogfood. A
Fable pass read the spec clause + index, build-pipeline, M-144, the test, and the neighbouring laws
(INV-45/61/16). Verdict: sound in intent, but shipped one meaning-inverting sentence pinned green by its own
test and two definitional gaps that made the trigger either evadeable or near-universal. All folded:

- **F1 (must-fix) — the briefing phrase "primary sources only, apart from the worker's summary or your own
  plan" read as its own opposite, and the test pinned the broken string.** This was pre-existing text in the
  INV-46 build-pipeline clause, swept here as part of the same law (fix-the-class). FOLDED: reworded to
  "primary sources only: never the worker's summary, never the senior's own plan"; the test needle updated
  in lockstep.
- **F2 (should-clarify) — case (2) had no proportionality floor: a one-word invariant tweak forced a spawned
  worker.** FOLDED: "edits the method" now means a rule whose MEANING changed (a wording-only edit that
  changes no meaning is not a method edit), and one fresh checker per landing batch covers every law in the
  batch (INV-61 scales the audit's form, never its freshness). The escape is explicitly NOT "the senior does
  a fresh re-read" — the motivating incident is a same-head review passing clean.
- **F3 (should-clarify) — "the only reviewer is the author" both leaked and swallowed.** FOLDED: the trigger
  is redesigned as high-stakes AND author's-own-review — "high-stakes" is surface-sized OR method-meaning-
  changing, and "the author's own review" means no independent read, where an independent read is defined as
  a differently-contexted head briefed from the primary sources on the goal-missed hypothesis (a same-context
  prover pass never counts, delegation never makes it independent). This kills the swallow (self-built alone
  no longer fires it) and the leak (a spawned same-hypothesis prover cannot be passed off as independent).
- **F4/F5 (worth-considering) — the "single head" frame over-claimed for a delegated-then-reviewed method
  edit; recursion bounded but unrecorded.** FOLDED by the redesign (the trigger now turns on "no independent
  read", so a genuinely independently-reviewed method edit does not fire it) and by this record (the audit of
  the audit-law is recorded here; the checker produces findings not method edits, so the chain terminates).

Verdict after fold: the trigger is proportionate (meaning-change threshold + one-checker-per-batch),
non-evadeable (independent-read defined), and non-universal (high-stakes AND author-only). 0 open must-fix.
