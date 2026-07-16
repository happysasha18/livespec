# Wish: an orientation/short-viewport facet in the standard sweep + a quantifier lens for the prover

From: the tlvphotos site window, 2026-07-16 ~23:26, on the owner's direct question ("why did neither
the prover nor the design review catch the landscape overlap earlier — did we miss something?").

## The incident (the key this wish carries)

The tlvphotos spec held a true-but-narrow layout law: "on a phone the caption zone must not cover the
work (it lives in the bottom margin band)". The implementation mapped "phone" to "viewport width
≤ 640px" — the CSS's only breakpoint. A rotated phone is a phone wider than 640, so it fell out of
both sentences: the law read it as not-a-phone, the styles gave it the desktop layout, and the caption
printed over the picture (the owner's landscape screenshot, 2026-07-16 ~22:45). The spec also carried
a rotation law (INV-86), but that one binds surviving STATE, and says nothing about layout.

No pass caught it beforehand because no lens ever pointed there: cross-link prover passes are
delta-scoped and the deltas were elsewhere; the claim itself was internally consistent, so a
consistency read had nothing to flag. The machinery is capable — the same night, with attention on
this surface, the scoped design review immediately found the exact sibling divergence (the caption's
landscape seat contending with the counter's corner, guarded only against the share rail).

## The two changes wished

1. **spec-author's standard-facet sweep grows one facet: orientation / short viewport.** The canonical
   list today has "phone/narrow layout" and sweeps by WIDTH; a landscape phone (wide AND short) is a
   distinct band that width-thinking misses. Every layout-bearing feature should end the sweep with a
   decided or [default] sentence for the short-viewport band too.

2. **A quantifier lens for the prover (and/or the design review's group pass):** every layout guarantee
   states its viewport quantifier explicitly — "on every viewport" or the named band — and a guarantee
   scoped to one band gets the standing question "and on the other bands?". A true-as-written but
   too-narrow claim is the class this lens exists to catch; the incident above is its key.

Fixed on the instance side already (tlvphotos SPEC now carries the caption-space law over every
viewport, proven and design-reviewed, 2026-07-16); this wish is the method-side class fix.
