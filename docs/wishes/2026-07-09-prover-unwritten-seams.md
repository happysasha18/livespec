# Wish: the prover should catch a stateful surface whose states aren't fully described

**From:** the tlvphoto host conversation (Alexander), 2026-07-09.

## The wish, in plain words

Teach `product-prover` to flag a **stateful surface whose behaviour is not described for every
situation it can actually reach** — especially the situation "another surface is present / active."
Today the prover reliably catches a missing cross-link only when both surfaces are named and their
seam is written; it does not actively hunt for the seam that nobody wrote. Alexander's ask: if the
prover can SEE that a state graph is incomplete, it should say so — an unreachable-from-the-spec but
reachable-at-runtime state is a hole, the same class as an unowned fact.

## Why — the incident that motivates it (primary source)

On tlvphoto's live walk, the caption zone (`#exh-cap`, a stateful surface that speaks the focused
work's title + story) kept showing the PREVIOUS work's title and story once the visitor reached the
closing screen (the finale, `.exh-fin`). Root cause in code: the caption updates only when an
`.exh-frame` intersects; the finale is not a frame, so nothing clears the caption — it strands the
last work's text over the finale, and the change reads as a jump rather than a transition.

This is a textbook cross-section composition hole (the caption surface × the finale surface), exactly
the class the prover is built for — yet it shipped. It shipped because the compose-across-axes step
was never run for that pair: the caption and the finale were each specced alone, and "what does the
caption show when the finale is in view?" was never written, so there was no seam for the prover to
check. The prover read a spec that looked complete because the missing state was invisible in it.

Alexander's framing: the prover should notice that a surface's states are "не до конца описаны" —
not fully enumerated — rather than only checking the seams an author remembered to write.

## What a fix might look like (for the live-spec session to shape, not a spec here)

- A prover phase that, for each stateful surface, enumerates the surfaces/contexts it co-exists with
  (siblings on the same page, the surfaces reachable before/after it in the flow) and asks for each:
  "is this surface's behaviour stated WHEN that other one is present/active?" A pair with no written
  answer is a finding, not a pass.
- Possibly a spec-authoring counterpart: the compose-across-axes checklist should include "every OTHER
  live surface" as an axis for a persistent/fixed surface, so the author writes the finale×caption
  sentence before the prover ever runs.

Bundle the two tlvphoto siblings that came from the same root (both are "an already-present surface's
behaviour under a change nobody composed"): the door re-running its entry fade on a viewport
aspect-ratio change (door × viewport-size axis) is the same class — an already-shown surface with no
stated behaviour for a relayout.
