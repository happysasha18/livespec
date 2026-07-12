# Prover record — INV-126 (paired-transition symmetry) — 2026-07-12 s40

Prover skill version at this pass: product-prover 1.0.6. Mode: CROSS-LINK short form (SPEC INV-61 — small
delta, skill kind, no new surface, no structure change).

## The delta

One invariant, INV-126: both directions of a paired state change (open/close, enter/exit, expand/collapse,
show/hide) get the same craft or a stated reason they do not; the default is symmetry, and because motion
feel is the human's own gate an undecidable pair is surfaced to him rather than shipped as a crafted-in and
instant-out pair silently. It rides the standard-facet sweep as its own facet (the canonical list's home is
spec-author), and the prover flags a pair with one direction described and the opposite unstated. Homes: the
composition clause + Formal index, the spec-author facet list, product-prover's paired-transition check.
Owning node: spec-author (owns-list + M-267). Test: `tests/test_paired_transition.py` (6 assertions,
red-proven then green).

## Previous record's unfolded rows

`2026-07-12-s40-inv125-cross-surface-uniformity.md` — 0 must-fix, clean. No carry.

## Findings

**0 must-fix.** Cross-link checks walked:

- Owning node present (spec-author owns-list carries INV-126, beside INV-18 the facet sweep it rides);
  matrix row M-267 under the spec-author block; Formal-index row present.
- Composition clean: INV-126 is the temporal twin of INV-125 (that holds a policy uniform across sibling
  surfaces in space, this holds a transition uniform across the two directions of one change in time). It
  rests on INV-18 (the facet sweep it rides), INV-31 (defaults told, not asked), INV-30 (motion feel is the
  human's gate, so the undecidable pair is surfaced), and INV-72 (the blank-answer finding class). No
  contradiction: the facet joins the canonical list carrying its named incident, satisfying the
  curated-list rule.
- The default-and-ask resolution matches the pack's facet discipline exactly (a facet ends as a decided or
  `[default]`-tagged sentence, silence is not an option), so no new asking machinery is introduced.

Verdict: buildable, landed. No open ⟨DECIDE⟩ touched by this delta.
