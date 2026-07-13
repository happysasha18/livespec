# Wish: a visual-overlap lens — no two INTERACTIVE controls may share a spot

**From:** the tlvphotos window, 2026-07-13, carrying Alexander's find + his explicit "send this to
live-spec too — this you should have caught."

## What happened in the project

The exhibition has a floating audio player pinned top-right (`#ex-sound`, z-index 130) that rides
the whole walk. A separate feature — pinch a picture to inspect it — opens a full-screen zoom overlay
(`#ex-zoom`, z-index 120) whose own close (×) also sits top-right. Because the player's z-index is
higher than the overlay's, the player stayed **visible and pressable over the zoomed picture**, right
on top of the overlay's own × — two interactive controls competing for one spot in the corner.
Alexander found it by eye on his phone. The suite was green; every zoom test and every player test
passed; nothing in the spec or the prover flagged that two independently-correct controls occupy the
same screen place when one surface opens over another.

His framing (paraphrased): overlap of PASSIVE things is fine — a caption plaque may lie over the
picture, a tone plate under it. Overlap of INTERACTIVE controls is a defect — a thing a hand can
press (a player, a close, a link) must have a place of its own; two of them on one spot is broken.
And this is not a one-off: it should be a standing check for **any** visual interface.

## The wish (method side)

Add a **visual-overlap lens** to the prover / the review method, of the same family as the two wishes
already filed from this project — cross-surface policy uniformity (a policy true on one surface must
hold on its siblings) and paired-transition symmetry. The new lens:

1. **Classify every on-screen element by kind: interactive (a hand can press/aim at it — buttons,
   links, players, close controls, inputs) vs passive (decoration, text bands, plates, the artwork
   itself).**
2. **Assert that no two INTERACTIVE elements overlap on screen at the same time — including across
   layers.** The dangerous case is exactly the cross-surface one: surface B opens over surface A, and
   A's floating control still floats above B's own control. A per-surface review never sees it, because
   each surface is correct alone; the defect lives in the *composition* of two surfaces' controls in
   z-order and screen position.
3. **Passive-over-anything is allowed; interactive-over-interactive is the flag.** The boundary is by
   kind, not by position — a control moved aside still competes for the eye, so the fix is usually to
   RETRACT the lower surface's chrome while the covering overlay stands, not to nudge it.

The check wants a testable projection too: for each covering overlay a project defines, a browser-level
row that opens it and asserts every other interactive control is either not rendered or not pressable
(computed `pointer-events:none` / `opacity:0` / off-screen) while it stands. In tlvphotos this became
INV-77 (EX-CHROME): `faceSync` toggles an `ex-cover` class, the floating chrome hides under it, and
`tests/test_zoom.py` asserts the player is not pressable while the zoom is open (red-first proven — the
old code read `player {opacity:1, pointer-events:auto}` with the zoom open).

## Why it belongs in the method, not just this project

Every project the pack touches will grow floating chrome and modal overlays; the z-order collision of
their controls is a structural, recurring class, and it is invisible to a green suite and to a
surface-by-surface prover walk. This is the third cross-surface-composition gap this project has fed
back (after policy uniformity and transition symmetry) — they point at one missing capability: the
prover should reason about how two surfaces' elements compose on screen, not only about each surface's
own states.

## Provenance
The tlvphotos window, 2026-07-13. Filed as a wish, not applied to the pack — this window does not
write the pack tree. The product-side fix (INV-77) is already built, tested red-first, and landing in
tlvphotos.
