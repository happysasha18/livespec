# Prover record — INV-72 (prover hunts the unwritten seam) + C-1 "every other live surface" axis

**Date:** 2026-07-09 · **Mode:** CROSS-LINK on the delta against the whole spec · **Reviewer:** product-prover (senior)
**Delta under review:** PRODUCT_SPEC.md — new axis in the canonical list (C-1, "### Composing across axes")
and new invariant INV-72. Wish: docs/wishes/2026-07-09-prover-unwritten-seams.md.

## Opening assessment
The delta extends the existing cross-section-composition law rather than competing with it: C-1 already
required composing a stateful surface across a fixed axis list; this adds "every other live surface" as a
member and makes the prover derive the reachable situations for itself instead of trusting the author to
have filled each. It composes cleanly with INV-18 (facet sweep) and INV-31 (silence is consent) — the
prover reports the gap, the author writes the sentence, the human is asked nothing. No contradiction, no
must-fix. Four should-clarify/worth-considering sharpenings below, all folded in-pass, so the invariant
owns exactly one node and derives one clean matrix row.

## Findings

| # | Severity · category | Finding | Disposition |
|---|---|---|---|
| F1 | should-clarify · boundary (composition) | INV-72 said the author writes the seam sentence "[default]-tagged, exactly as the facet sweep does [INV-18]" — but "every other live surface" is an AXIS (C-1), not a facet (INV-18/T-13 device list). Line 357 already splits them: the sweep authors facet sentences at first-spec; the axes compose "once the surface exists." An author couldn't tell whether a finale×caption sentence is a facet row (E-15) or a C-1 composition-invariant row, nor when it is authored. | **FOLDED** — INV-72 now names the discharge explicitly: the author writes it "as a composition invariant [C-1]", tagged the same way the facet sweep tags its own [INV-18]. The `[default]` tell is shared; the home is C-1's axis composition, not a new facet row. |
| F2 | should-clarify · abstraction | "every axis change it undergoes while already shown (a relayout, a reopen)" restated the viewport axis and the reopen axis, which C-1 already lists. Read literally it looked like INV-72 adds duplicate axes. The real new thing is the ACTIVE enumeration discipline applied to the WHOLE list, of which "every other live surface" is the one new member. | **FOLDED** — INV-72 reframed as "reads the whole axis list [C-1] actively, deriving each surface's reachable situations for itself." The door×viewport incident is now plainly the active hunt on the EXISTING viewport axis; finale×caption is the hunt on the NEW axis. No duplication. |
| F3 | should-clarify · boundary (actors/ownership) | INV-72 as first written bundled two owners: the prover's hunt (product-prover node) AND "the author writes the sentence" (spec-author/C-1). The architecture step requires every fact owned by exactly one node (test_architecture_owns_every_anchor_once); a two-owner invariant fails clean derivation. | **FOLDED** — INV-72 now OWNS only the prover's hunt + its disposition (reports gap, invents nothing, asks nothing). The authoring half is CITED ([C-1], [INV-18]), not restated as INV-72's own law. Architecture: INV-72 → product-prover node; the axis + authoring → spec-author node under C-1. |
| F4 | worth-considering · missing-scenario (state-space) | The motivating case is caption (stateful) × finale (a static end screen — "not a frame," per the wish). If "every other surface" is read as "every other STATEFUL surface," the prover/author would skip the finale — exactly the surface that stranded the caption. | **FOLDED** — the C-1 bullet now reads "whether or not that other surface holds state ... (a static end screen counts)," so a non-stateful co-present surface is in scope. |

## What's working
- INV-72 reuses the existing E-14 "fact no node owns" equivalence for "a reachable state the spec omits" —
  one class, one mental model for the reader, no new vocabulary.
- The silence-is-consent fence (INV-31) is held explicitly: the prover asks the human nothing, so the new
  hunt cannot regress the facet sweep into a confirmation-request machine (the wish's stated regression fence).
- Both motivating incidents (finale×caption, door×viewport) map onto the folded text without strain.

## Open ⟨DECIDE⟩ touched by this delta
None. No ⟨DECIDE⟩ marker sits on the compose/prover sections.

## Verdict
Ready to derive. All four findings folded in-pass; the fold stays local to C-1 + INV-72 and does not re-trigger
the gate. Next: architecture (INV-72 → product-prover node, C-1 axis → spec-author node), then the matrix row.
