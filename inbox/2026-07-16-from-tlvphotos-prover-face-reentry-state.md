# Wish — the prover should flag a re-enterable surface whose entry state is unstated

From: the tlvphotos window, 2026-07-16.
Kind: wish (a standing prover / design-review lens).
Priority: medium — it names a whole class of shippable bug the review passes miss today.

## The wish

Give the product-prover (and the design-reviewer's transition-parity pass) a standing lens: for every
surface a visitor can leave and re-enter, the spec must declare two things — the surface's entry
position/focus, and whether entering it resets its internal state or resumes the state left behind. A
spec that covers a surface's open ceremony, its exit, its variants, and its guards but leaves its
entry position blank is a finding, not a pass.

## Why (what broke, with the source)

tlvphotos shipped a real bug: the series side-room, in its sideways-lane variant, did not reliably open
on the series' first member after a prior visit had scrolled the lane to the end. The owner exited from
the last picture, re-opened the room, and met the last picture again instead of the first.

The spec covered this room richly — it opens as a face with one history step, the way out mirrors the way
in, the variant is the series' character, the pinch and the pinch-refusal are pinned, the walk beneath is
restored to its exact frame. But no line ever stated WHICH member the lane lands on when the room opens,
nor that a fresh entry resets rather than resumes. An unstated transition end-state.

That omission is exactly the prover's shape: it reasons in states, transitions, and initialization. "A
face opens — focused where, and does entry reset or resume prior internal state?" is an initialization
question a state-transition review should ask by construction. Neither the prover pass nor the
transition-parity design review named the blank, so it shipped. The owner's own words on finding it:
"shouldn't the prover have found this?" — and the honest answer is yes.

The lens this proposes would have surfaced the blank as an open question against the spec before any code
was written, closing the whole class rather than this one lane.

## Provenance

- The bug: tlvphotos series side-room lane, observed by the owner 2026-07-16, being fixed in the same
  session at the spec (a new invariant: the lane opens on its first member; entry resets) → matrix row →
  red test → engine code.
- Related pack anchors the reviewers already carry: the design-reviewer's motion-parity lens (INV-165),
  which is a sibling standing lens born the same way from this project.
