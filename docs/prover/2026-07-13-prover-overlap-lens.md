# Prover record — 2026-07-13 — the interactive-overlap prover lens (a home of INV-136)

**Change under review:** a spec-time review lens added to product-prover for the interactive-overlap rule
(two interactive controls from different layers must not share one screen region), sibling to the
cross-surface-policy [INV-125] and paired-transition [INV-126] lenses, landed as another HOME of the
already-shipped INV-136 — no new invariant code. Touched: `PRODUCT_SPEC.md` (INV-136 clause + index-row
homes), `skills/product-prover/SKILL.md` (the new lens entry), `tests/test_design_principles.py` (2 tests).

**Review mode:** adversarial fresh-context audit (SPEC INV-46), run on Fable at the owner's word, opening
hypothesis "tasks completed, goal missed". Verdict: **GOAL MET**, one must-fix and two should-clarify.

| # | Finding | Severity | Disposition |
|---|---|---|---|
| 1 | The lens stated its finding as rendered geometry ("two controls sharing one screen region"), which a document reader cannot observe and which drifts from the siblings' form — both define the finding as a property of the spec's TEXT (a policy written for one surface; one direction described, the other silent). It also dropped the [INV-72] blank-answer kinship the spec clause gives it, and could misfire (a spec that DOES state the retraction still has two controls overlapping at the instant of opening). | MUST-FIX | **FOLDED** — the lens finding rewritten as the spec's silence: "a spec that opens one surface over another and leaves the lower layer's control's fate unstated while the overlay stands is a finding, the blank-answer class of an unwritten seam [INV-72]", and the opening question turned to "does the spec state that control is hidden or made unpressable?". |
| 2 | The floor sentence carried two "it/its" with unclear antecedents, and named the projection three ways across the rule's homes ("browser assertion" / "browser projection" / "pixel/DOM projection"). | SHOULD-CLARIFY | **FOLDED** — pronouns unpacked ("an ordinary suite stays green while the running product collides"); the projection named "browser projection" consistently across both places this change touches. |
| 3 | The kin-line called the lens "spatial-composition", but INV-126 already frames INV-125 as the SPACE axis of the space/time twin; a third "spatial" muddies that duality. The real axis here is depth — layers stacked on one screen. | SHOULD-CLARIFY | **FOLDED** — relabelled "the third lens of this family … holds two layers' controls apart in depth on one screen". |

**Register / language delta:** spec-style-lint unchanged at baseline (10 errors / 106 warnings, the one index-row hit being the pre-existing "DOM" token); no contrast-frame ("X, not Y") construction in any added sentence; shipped-language check OK.

**Open ⟨DECIDE⟩ touched by this change:** none.

**Suite:** 609 green after the fold.
