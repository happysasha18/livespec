# Prover record — SPEC humanize migration plan (Fable pass, 2026-07-07, session 24)

Target: `docs/research/2026-07-07-spec-humanize-plan.md` (the reconciled whole-doc human-first rewrite
plan). Reviewer: Fable, product-prover lens on the PLAN's safety (not the spec's content). Requested by
Alexander ("прогони через фейбл на всякий — это серьёзная миграция"). Verdict: **READY-WITH-FIXES** —
spine sound (needle registry + anchor diff + per-batch suite + prover cross-link + taste loop; push
gate confirmed FULL-reach for SPEC.md so the suite can never stand down on a rewrite push), but five
confirmed MUST-FIX escape paths. All folded into the plan (see its "Prover findings folded" section).

## MUST-FIX (all folded)

1. **Whole-doc `assertIn` + "compress repeats" = silent fact drop.** Needles match the FLATTENED whole
   doc, not a section (e.g. "one-way" occurs 7× in SPEC.md). Compressing a repeated clause out of
   section A passes because a copy survives in B; a later batch reweords B and updates the needle → A's
   statement is gone, no gate fired. FOLD: per-batch needle check is SECTION-SCOPED — every needle
   matching the OLD section text must match the NEW section text; deliberate relocation named in the
   landing.

2. **"Grep from the section's prose" is backwards and manual.** Needles are short fragments, not the
   section's sentences; no extractor script exists. FOLD: write a needle-extractor (`scripts/`) that
   pulls all asserted literals from `test_traceability.py`, whitespace-normalizes both sides as the
   tests do, and matches AGAINST the old section — the mechanical step-1/step-4 gate, before batch 1.

3. **Anchor-set diff proves presence, not the sentence certified.** `[INV-22]` can migrate to a weaker
   sentence with set-equality and matrix coverage both green. FOLD: diff anchor→trailing-sentence
   PAIRS before/after; the prover cross-link runs on an old-vs-new fact table built from `git diff` of
   the section, never from the new prose alone; prover signs each changed pairing.

4. **SPEC↔skill echo pairs are outside the model.** The same clause is asserted verbatim in SPEC AND in
   a skill doc (e.g. "An unresolved kind scales nothing down" in SPEC + build-pipeline). Rewording the
   SPEC side and updating only the SPEC-side needle leaves the skill in the old voice — "one home per
   fact" bifurcates, suite green. FOLD: the batch treats coupled skill prose as in-scope — per shared
   clause, reword the skill copy + its needle in the same commit, or record the divergence by name.

5. **D4 omits the consumer inventory that makes the method safe.** The generalized formula presumes a
   needle registry exists; a new host (tlvphoto) has none. FOLD: D4 = (1) inventory every mechanical
   consumer of the doc, (2) derive load-bearing shapes, (3) build/verify the needle registry, (4) THEN
   the five-gate batch loop. Row 148 Phase 1 IS step 1 — the sub-skill must export it.

## SHOULD (folded)

6. Epic layer form undefined — could collide with header-split shape rules. FOLD: epics as a plain TOC
   list at the top; every section header keeps its exact `## ` string.
7. "Register frozen at batch 1" contradicts step 7 ("adjust to his nudges"). FOLD: a named FINAL
   register-sweep pass (wording-only; needles/anchors stable; suite gates it) so the opening can be
   re-touched without violating "never reworked twice".
8. `templates/SPEC.template.md` breaks D1's "every future spec born in the genre" (it's needled and
   stays old-register). FOLD: add the template as one small batch in the movement.

## NICE (noted)

9. Closed doors recorded (no action): prose-only reach can't stand the suite down for SPEC.md;
   `rule 18`==2 and `appetite` ban asserted; index `[target]` cells pinned; ARCHITECTURE pins into SPEC
   touch only `SPEC.md:1`.
10. D3 (communicator scissors/metaphor lint) is a different skill/gate family — sequenced as its own
    row so a lint debate never stalls a rewrite batch.
11. End-of-movement grep for stale verbatim SPEC quotes in the untested prose class (README, OVERVIEW,
    MIGRATION, docs/) at the 0.9.0 close.
