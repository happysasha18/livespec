# Wish: a new prover lens — delivery separability along a declared composition axis (+ the dual-lens heuristic)

From: tlvphotos, 2026-07-21 (Alexander's catch + follow-up, mid input-modality-axis movement)
Note: this file was raced/truncated once by a concurrent live-spec inbox sweep; this is the full atomic rewrite.

Lived: the input-modality composition axis shipped as a delivery monolith. Focus-trap, live-region, long-press, keyboard, and alt code all ride the single walk bundle to every visitor, touch and desktop alike. Evidence: ARCHITECTURE.md labels the 21-fragment client assembler "infrastructure, owns no spec anchor", and records the JS bundle size as "none wired; a budget with no watcher", so no spec decision stands behind monolithic delivery (~97 added source lines, ~1-2KB gzip on an ~87KB bundle).
Id: tlvphotos-2026-07-21-delivery-separability
Need-by: none

## 1. The lens (his catch, sharpened)
When a spec declares a cross-cutting COMPOSITION axis (here: input modality — touch / pointer / keyboard), the
composition lens checks that BEHAVIOUR decomposes along the axis: every capability reachable under every pole.
There is a DUAL question the prover never asks: does the shipped ARTIFACT decompose along that same axis, or is
it a monolith? The input-modality axis added focus-trap, live-region, long-press, keyboard, and alt code that
all ship in the single walk bundle to EVERY visitor, touch and desktop alike. The axis exists in behaviour and
is absent in delivery — a monolith; every visitor loads poles they never use.

This is NOT the atomicity lens (that is runtime all-or-nothing / no observable partial state). It is a new lens
— delivery separability along the composed axis, the dual of composition: composition asks "does behaviour
split along the axis?"; this asks "does the delivered artifact split along the axis, or ship as one monolith?"

The ask: add a standing lens to product-prover — when a spec declares a cross-cutting composition axis that adds
runtime code, ask whether the delivered artifact is partitioned along that axis or monolithic. A monolith is a
valid answer ONLY when it is a NAMED, justified architectural choice. The finding is when the monolith is an
UNEXAMINED default: force the design to state "ships monolithically because X" or "owes a platform-split /
lazy-load road". Absence of that statement is the finding. Byte-budget is a downstream consequence, not the
root; the root is separability. (Generalises past input modality: any declared axis — AI on/off, engine,
viewport — raises the same dual.)

## 2. Concrete evidence from tlvphotos (why this would have bitten at prove time)
- ARCHITECTURE.md labels the client assembler (21 fragments joined into one exhibition.js) "infrastructure —
  owns no spec anchor". No spec decision stands behind monolithic delivery.
- It records the client JS bundle size as "none wired; a budget with no watcher" — a budget with nothing
  enforcing it.
- "One page" (INV-70) is the runtime document shape under overlays, NOT a delivery choice.
So the monolith is a live unexamined default. A first attempt to "close the seam" by NAMING the monolith
deliberate was itself wrong (Alexander caught it: "монолит точно осознанный?"). The lens must ask whether the
deliberateness is REAL, not let the design assert it. (Real growth was tiny — ~97 source lines, ~1-2KB gzip on
an ~87KB bundle — so no split was warranted here; the point is the prover should have RAISED it and made the
design name it honestly.)

## 3. Follow-up idea — lenses come in complementary pairs; use the DUAL as a discovery heuristic
The delivery-separability lens was FOUND as the dual of composition. That raises a bigger question: should each
lens have a complementary one? Partly the pack already lives this — safety ↔ liveness is the canonical dual
pair (nothing bad ever ↔ something good eventually), and state ↔ transition is a dual (nodes ↔ edges). So
"lenses pair up" is already embodied in places.

NOT proposed as a hard law "every lens must have a dual". Two failure modes argue against a mandate:
- Some duals COLLAPSE into an existing lens: the dual of an invariant ("what always holds") is a variant (a
  decreasing progress measure), which is just the liveness/termination lens re-discovered.
- Some duals are definable but rarely bite, so a standalone lens does not earn its keep.

On atomicity (floated as dual-less): it is arguably NOT dual-less — its dual is isolation (atomicity is temporal,
no partial state across a transition; isolation is concurrent, no partial state visible to other actors), the A
and I of ACID; idempotency and reversibility are further companions. That the "exception" is itself debatable is
the best argument for a heuristic over a law.

The ask: add to product-prover a generative prompt, not a completeness rule — "for each lens you apply, ask
whether its DUAL bites here." The dual's value is as a way to FIND the missing lens (exactly how
delivery-separability surfaced), not a requirement that every lens ship with a partner.
