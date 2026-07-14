# Design review — property routing between the prover and the design review, 2026-07-14

**Skill version:** design-reviewer 1.0.0.

**Scope:** this pass reviews a change to the design review's OWN method (work-kind skill), so it runs in the
pack's own kind form: the elements it inventories are the pack's review passes and the properties they own,
and the same-kind check is whether the two reviews partition the cross-cutting properties cleanly. It does
not run the browser element inventory (the pack has no DOM of its own).

**Input:** the delta that declares INV-150 (each cross-cutting law names its net), sharpens INV-125 (the
sentence-form trigger), and declares INV-126's reversibility-of-means half — realizing the inbox case
`2026-07-14-tlvphotos-openable-face-exit-symmetry.md`.

## The same-kind group under review

The two review passes — the prover and the design review — are a same-kind pair: each reads a proven spec
and reports on a cross-cutting property. The design question the delta settles is whether every such
property has exactly one owning pass at every moment, with none owned twice and none dropped.

## Parity check

| property | before the delta | after the delta | owned twice or dropped? |
|---|---|---|---|
| presence of a close (a state entered and not left) | prover (dead-end/liveness; INV-72 where unmodeled) | unchanged | owned once (prover); the design review's parity table is a welcome incidental second net |
| continuity of a paired transition | prover (INV-126, continuity half) | unchanged | owned once (prover) |
| reversibility of the opening means | design review (undeclared parity question) | prover (INV-126 means half, blocking) | promoted cleanly; the design review no longer owns it |
| a kind-general rule homed on one member | fell through — enumeration presupposed the kind was declared | prover (INV-125 sentence-form trigger) | closed; the prose-law form now has a prover home |
| cross-sibling propagation, declared class | prover (INV-125) | unchanged | owned once (prover) |
| cross-sibling propagation, undeclared grouping | design review (INV-141) | unchanged | owned once (design review) |
| net-of-record assignment for a declared law | unowned (nothing recorded a law's enforcer) | prover station verifies the net field (INV-150) | closed; a netless law is now a broken invariant |

## Finding

**Confident — the partition is now clean and the routing split is stated on the design review's own side.**
Before the delta, two properties from the openable-faces case had no prover home: the missing inverse
gesture (no declared facet) and the divergence from a sibling's stated mirror principle (the group never
declared, the class-general sentence never lifted). The delta gives both a prover home. The design-reviewer
skill now carries the declaration-status routing split explicitly, so the design review claims only
genuinely undeclared groupings and the prover claims the declared ones and the class-general sentences. No
property is left owned by both passes, and none is dropped. This is written as a recommendation-grade
confirmation, since it stands on the spec text alone and blocks nothing (INV-141).

No `likely` finding rides to the human this pass: the deciding facts here are settled by the spec text and
the audit, so no question meets the strong-signal bar.

## Outcome

| finding | confidence | outcome |
|---|---|---|
| the property partition between the two passes is clean after the delta | confident | recommended (a confirmation; blocks nothing) |

The pass holds no landing. The routing split it confirms lives at INV-150 (spec) and in the design-reviewer
skill's "How the answer closes the loop" section.
