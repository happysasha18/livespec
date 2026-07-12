> Archived 2026-07-12 s40 — landed as ROADMAP row 288 (SPEC INV-126). The paired-transition symmetry law lives in the composition clause, the spec-author facet list, and product-prover (paired-transition check). The temporal twin of INV-125.

# Wish — a soft way IN with a hard way OUT is an asymmetry the method should catch

From: tlvphotos window · 2026-07-12 · Alexander's word during a phone test.

## What happened (the real trigger)

Opening the polaroid side-room plays a beautiful soft transition — the room dresses under a black
veil and is revealed in one breath. Closing it is a hard cut: one click and the room is gone,
no transition at all. The way in and the way out of the SAME surface do not match, and nobody
decided that on purpose — the entry got the crafted breath, the exit was left instant.

This is a sibling of the cross-surface uniformity gap already filed
([[2026-07-12-from-tlvphotos-cross-surface-policy-uniformity]]), but on a different axis. That one
was spatial: a policy that holds on one surface but not its siblings. This one is temporal: a
transition crafted for one direction of a paired state change (enter) but not its opposite (exit).
Both are the same root — a decision made for one member of a pair and silently not carried to the
other.

## The gap in the method

When a surface has a pair of opposite state changes — open/close, enter/exit, expand/collapse,
show/hide — the method has no step that asks: *do both directions get the same craft?* A soft,
designed entrance with an instant, undesigned exit passes every test (the exit "works" — the room
does close), reads fine in the spec (each direction may be described on its own), and only a human
feeling the asymmetry on a real device catches it.

Alexander's steer, verbatim in spirit: by default, unless asked otherwise, treat the two directions
as one thing that should be uniform; and at minimum, the method should ASK the user about such an
asymmetry rather than ship a crafted-in / instant-out pair silently.

## Candidate mechanisms (live-spec's call which is best — one, or a mix)

1. **A spec rule for paired state changes** — when a surface declares a transition on one direction
   of a paired state change, the spec must say what the OTHER direction does; "instant" is a valid
   answer, but it must be a stated, decided answer, not a silence. The prover flags a pair where one
   direction has a described transition and the opposite direction is unstated.

2. **A standard-facet sweep entry** — add "paired-transition symmetry" to the facet sweep the spec
   author already walks (phone layout, touch-vs-hover, empty/error, accessibility, performance): for
   every open/close-style pair, the sweep asks whether the exit mirrors the enter, and the answer
   ends as a spec sentence (mirror / a named shorter exit / deliberately instant), decided or asked.

3. **The default + the ask** — the method's default is symmetry (the exit mirrors the enter's feel
   unless a reason is stated), and where the author cannot decide, it is surfaced to the human as a
   real question, since motion feel is the human's own call and cannot be judged from code.

Alexander leaves the choice of mechanism to the method. Option 2 feels like the cheapest true home —
it rides a sweep the author already runs — with option 3's default-and-ask as its resolution rule.

## Note

The tlvphotos side is being fixed under its own row this session: the polaroid-room exit is being
made to mirror the soft entry (his stated default), and the actual feel is confirmed on his real
device (motion feel is his gate). This wish is only the METHOD lesson so the next project of this
shape does not ship a soft-in / hard-out pair without anyone deciding it.
