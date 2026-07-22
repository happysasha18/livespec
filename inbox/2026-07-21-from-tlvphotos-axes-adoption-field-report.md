# Field report: the axes release adopted in tlvphotos — one accuracy correction and two findings

From: tlvphotos, 2026-07-21 (during the catch-up walk from pack 2.7.0 to 3.6.0, on Alexander's word)
Id: tlvphotos-2026-07-21-axes-adoption-field-report
Need-by: none. Nothing here blocks anything on the pack side.

This is the host's report back from adopting the axes release. It corrects one factual claim the release
carries about this project, and offers two findings the pack may want, since tlvphotos is one of the three
real hosts the founding check reads and the visual-kind example.

## 1. The accuracy correction — the founding bug is already closed here

The migration wish and the release note both state that the gap the release was born from is still open in
this tree, and Part 2 of the wish instructs the adopting session to "expect the owed-versus-covered
finding" against the photo surfaces, with the touch value uncovered on the polaroid surface.

That is no longer true, and it stopped being true a week before the release. The polaroid surface reached
full parity with the gallery on 2026-07-14, in direct answer to the very wish that reported it:

- The polaroid print sits in the pinch selector set, the whole print including its paper frame as the hit
  area.
- The match reads the element under either touch point rather than the event target, which is what makes a
  print too small for two fingertips reachable at all.
- One delegated touch handler opens the layer over any face and seeds the scale from that same gesture, so
  the pinch that opens it keeps scaling it. There is no arming tap.
- A one-finger drag pans the enlarged picture, bounded by the same clamp the gallery path uses, and the
  desktop pointer has its own equivalent.

Three suite rows hold this, two of them split so that a bare-table pinch opening nothing is asserted
alongside the positive case, which is what stops the row passing vacuously.

So the owed-versus-covered read on this host's photo surfaces comes back **covered**, and the predicted
finding does not fire. Worth reconciling on the pack side, because the release's own text presents this
host as the open instance.

## 2. Finding — the axis taxonomy met a host that had already built one, by different joints

This tree ran its own cross-cutting movement on 2026-07-20 and 21, before the release reached it. It
modelled the same territory as **three sibling axes**: input modality (touch · pointer · keyboard),
assistive technology, and browser engine. The pack models **one axis**, input-capability, with touch and a
fine pointer as combinable poles, and holds accessibility and browser engine as separate siblings that
enter as later increments.

Both cut the same cloth. The host has adopted the pack's line verbatim, because a shared taxonomy across
hosts is worth more than a local one. Two things fell out of doing so that the pack may want:

- **The keyboard has nowhere to go.** In the pack's model the keyboard is not a pole of input-capability
  (which holds touch and a fine pointer), and it is not accessibility either, since a sighted person
  navigating by keyboard uses no assistive technology at all. This host found real, separate gaps under
  it: a polaroid print with no tab stop and no key handler, which neither the touch pass nor the
  screen-reader pass would have surfaced. The keyboard may deserve to be a third pole of
  input-capability rather than waiting on the accessibility increment.
- **A host can be ahead of the increment schedule.** This tree already composes and tests every
  visitor-facing surface against the keyboard, assistive technology, and both browser engines. The
  profile line the pack asks for has no way to say so — it names what is owed, with no room to record
  what is already held ahead of the pack's own increments. This host wrote that as free prose under the
  line. A `project.axes` grammar that can carry "covered ahead" would keep it machine-readable.

## 3. Finding — the version catch-up walk found no chapter for the release it was sent to adopt

The wish asked for a walk from 2.7.0 to 3.2.0. `MIGRATION.md` carries chapters up to 3.0.0 and stops
there, while `VERSION` reads 3.6.0. So the walk's mechanical range covered 2.7.0, 2.8.0 and 3.0.0, and
everything from 3.1.0 through 3.6.0 rode the founding-question sweep and the re-vendoring with no chapter
of its own. That matches what the wish itself predicted for 3.1.0 and 3.2.0, and it now holds for four
more releases.

This is reported rather than complained about: the tier rule says a minor costs a host a re-run of its
walk and nothing else, so chapterless minors are the rule working. The observation is only that a host
reading `MIGRATION.md` to build its chapter chain sees a document that ends six releases behind the
version file, with nothing on the page saying that the gap is intentional. One sentence at the end of
the chapter list, naming which releases carry no chapter and why, would close that read.

## Provenance

Written by the tlvphotos session during its own adoption, 2026-07-21. This window wrote this one file in
the live-spec tree and nothing else.
