# Prover record — INV-125 (cross-surface policy uniformity) — 2026-07-12 s40

Prover skill version at this pass: product-prover 1.0.5. Mode: CROSS-LINK short form (SPEC INV-61 — small
delta, skill kind, no new surface, no structure change).

## The delta

One invariant, INV-125: a cross-surface policy (a gesture, an affordance, an input mapping, a repeating
state transition, a feature or repeated element shared across places) is stated at the surface-CLASS level
and held uniform across siblings; a policy written for one surface while siblings of the same kind exist is
a spec defect. Three enforcement faces: the spec-class rule (upstream root), the product-prover
cross-surface-policy lens (enumerate the surfaces of that kind from the surface registry, flag any
uncovered), and the completeness guardrail (DOM-wide assertion, for a rendered product; the pack ships the
rule + lens only, having no DOM). Homes: the composition clause + Formal index, product-prover lens (beside
the unwritten-seams lens), build-pipeline completeness guardrail. Owning node: product-prover (owns-list +
M-266). Test: `tests/test_cross_surface_policy.py` (6 assertions, red-proven then green).

## Previous record's unfolded rows

`2026-07-12-s40-inv124-class-hunt.md` — 0 must-fix, clean. No carry.

## Findings

**0 must-fix.** Cross-link checks walked:

- Owning node present (product-prover owns-list carries INV-125, like its kin INV-72); matrix row M-266
  under the product-prover block; Formal-index row present — the three suite-enforced cross-references hold.
- Composition clean: INV-125 is the preventive twin of INV-124 (the class hunt) and the class-level
  companion of INV-72 (the unwritten-seam hunt asks whether a surface's behaviour is stated when a sibling
  is present; INV-125 asks whether a decided policy holds across the whole class). No contradiction. It
  rests on E-10 (the surface registry as the enumeration source) and INV-97 (the completeness family as the
  mechanical floor).
- The pack-has-no-DOM boundary is stated in the clause, so the guardrail face binds only a rendered product
  and the pack's own suite is not asked for a DOM-wide check it cannot run — no false obligation.
- The owner's clarification (uniformity also covers repeating state transitions and shared features /
  repeated elements, 2026-07-12) is folded into the clause and index in the same landing.

Verdict: buildable, landed. No open ⟨DECIDE⟩ touched by this delta.
