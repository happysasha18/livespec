> Archived 2026-07-12 s40 — landed as ROADMAP row 287 (SPEC INV-125). The cross-surface uniformity law lives in the composition clause, product-prover (cross-surface-policy lens), and build-pipeline (completeness guardrail). Broadened on his 2026-07-12 word to cover repeating state transitions and shared features / repeated elements.

# Wish — catch a policy that holds on one surface but not its siblings

From: tlvphotos window · 2026-07-12 · Alexander's word during a phone test.

## What happened (the real trigger)

tlvphotos has several sibling surfaces of the same interaction kind — the walk, the door,
the series side-room, the polaroid table. A gesture policy — "browser pinch-zoom is refused;
free zoom never happens here" — was decided and shipped, but the spec clause and the code
wrote it for **the walk** only (`touch-action` on the walk body; the clause literally opens
"the walk refuses browser pinch-zoom across the whole surface"). The door, the series room and
the polaroids kept the browser default, so pinch still zoomed there.

Every test was green and the earlier zoom/swipe sweep reported the class "swept", because the
suite asserted the policy on the walk — the one surface the clause named. The gap surfaced only
when Alexander pinched each surface by hand on a real phone. So the method shipped a policy that
was uniform in intent and non-uniform in fact, and nothing caught it.

## The gap in the method

When a policy or affordance is decided ("no pinch-zoom", "long-press shows the gracious line",
"a single input steps exactly one frame"), the method has no step that asks: *which surfaces are
of this kind, and does the policy hold on ALL of them?* The spec clause names the surface where
the decision was born; the prover checks the clause as written; the suite asserts what the matrix
rows cover. A sibling surface that should inherit the policy but was never named stays invisible
to all three.

## Candidate mechanisms (live-spec's call which is best — one, or a mix)

1. **A spec composition rule** — a cross-surface policy is stated at the surface-CLASS level, not
   on one surface: the clause enumerates the surfaces it governs (or names the class and its
   members), and a policy written for a single surface when siblings exist is a spec defect the
   prover flags. This puts the fix upstream, where it is cheapest.

2. **A product-prover check** — for each interaction policy, the prover enumerates the surfaces of
   that interaction kind (from the spec's surface registry) and flags any the policy's clause does
   not cover. This is the "prover writes itself a check" Alexander suggested.

3. **A mechanical guardrail** — the completeness family already scans the DOM for surfaces; extend
   it so a policy asserted for one surface is asserted DOM-wide (the touch-action / listener holds
   on every registered surface root), red until every sibling is covered. This catches it every
   commit, not once per review.

Alexander's steer: "let the prover write itself a check — or not the prover, let live-spec itself
decide what is best." He leaves the choice to the method. A spec-level rule feels like the root
(it moves the catch upstream of code), but a mechanical guardrail is what would have gone red the
day the walk-only fix landed. A composition of (1) + (3) may be the honest answer.

## Note

The tlvphotos side is being fixed under its own bug row this session (pinch/zoom uniformly off on
the door, series room and polaroids; the one allowed scale change is a chosen polaroid opening
slightly larger, which is our own layout, not a browser gesture). This wish is only the METHOD
lesson so the next project of this shape does not repeat it.
