# Design review — Little Gallery spec (bare arm, no skill loaded)

Run 2026-07-14, one Sonnet worker, WITHOUT reading any skill file: "Review the DESIGN of this spec
before we build it — flag anything inconsistent or worth a second look." Verbatim transcript.

---

Review of the Little Gallery spec — design consistency pass.

**Photo-opening interaction is inconsistent across the three pages, and it's not clear if that's intentional.**
- Gallery: tap opens large, then the photo can be zoomed, dragged, and pinched.
- Memories: tap opens large, but explicitly cannot be zoomed (flat, printed size) — this one's fine because the spec states the reason ("by decision... so the frame reads as an object, not a document").
- Story: tap opens large — and then nothing. No mention of zoom, drag, or pinch, and no mention of it being deliberately fixed-size either.

That silence on the story page is the thing I'd flag hardest. The gallery photo and the story hero photo are structurally the same kind of object (a plain photo, opened large on tap) — one gets rich inspection controls and the other's post-open behavior is just unstated. Compare that to the memories polaroid, where the "no zoom" choice is spelled out with a rationale. The story page has neither a stated capability nor a stated reason for lacking one. Worth asking: should the hero photo behave like the gallery photo (zoom/drag/pinch) once open, or is it meant to be a fixed, one-size view like the polaroid — and if the latter, why isn't that decision written down the way the polaroid's is?

**Captions appear only on one page.** Memories polaroids get a caption under each; gallery and story photos don't mention captions at all. Might be intentional (polaroids are captioned mementos, gallery/story photos aren't), but worth a sanity check since it's the only page with that element.

**"Open large" is never defined.** All three pages use "opens large" but nothing says what that visually means — full-screen modal? overlay? does the rest of the page dim or scroll away? Since it's the shared verb across all three surfaces, defining it once would remove ambiguity everywhere it's used.

**No close/exit behavior specified anywhere.** How does a visitor get back from the enlarged view to the wall/scatter/hero page? Not mentioned for any of the three.

**No mention of moving between photos while one is open.** On the gallery, once a photo is open and zoomed, can the visitor swipe to the next one, or must they close and re-tap? Same question doesn't even apply to story (single photo) but does to gallery and arguably to memories.

**Layout metaphors differ (wall vs. scatter vs. single hero) but that reads as intentional** — each page has a different curatorial feel, and that's consistent with them being different kinds of pages. Not flagging that as an inconsistency, just noting it's a deliberate-looking choice rather than an oversight, unlike the zoom question above.

---

**What the bare arm shows (the contrast the eval is for):** the bare reviewer DID sense the hero-photo
silence — the substance is there, loader-fed — but it delivered it as an undifferentiated list mixing
same-kind design divergences with prover-territory completeness gaps ("open large" undefined, no close
behavior, no between-photo navigation), carried no confidence read, no two-objects-in-hand ask form, and
no cap. It never proposes the explicit same-kind group, never separates the design-review lane (undeclared
groupings) from the verification lane (unstated edges the prover owns), and offers no recommended default
in the batched-question shape. The with-skill arm fires exactly one disciplined ask and stays silent on
the decided polaroid.
