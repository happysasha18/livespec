# Design review — Little Gallery spec (with-skill arm), design-reviewer v1.0.0

Run 2026-07-14, one Sonnet worker, having read `skills/design-reviewer/SKILL.md` in full and run the
full design review over the planted spec (evals/design-reviewer.md). Verbatim transcript.

---

*Design review — Little Gallery spec, run per `design-reviewer` SKILL.md v1.0.0 (full pass — no prior surface registry to scope against, so all three surfaces read fresh).*

**Step 1 — Enumerate (element inventory, descending below page level).**

| Element | Surface | Spec sentence |
|---|---|---|
| Photo (wall) | gallery | "A visitor taps any photo to open it large; open, the photo can be zoomed, dragged, and pinched to inspect the detail." |
| Polaroid | memories | "A visitor taps a polaroid to open it large. The polaroid opens flat and cannot be zoomed — by decision, the polaroid keeps its printed size so the frame reads as an object, not a document." |
| Caption | memories | "a scatter of polaroid photos with a caption under each" |
| Hero photo | story | "a single hero photo a visitor taps to open large" |

**Step 2 — Describe by role** (person's action words, not the author's category names).

- Gallery photo: *a photo a visitor opens large and then inspects up close by zooming, dragging, and pinching.*
- Polaroid: *a photo a visitor opens large to look at, fixed at its printed size.*
- Caption: *a line of text a visitor reads once, under a polaroid.*
- Hero photo: *a photo a visitor opens large.*

**Step 3 — Propose groups.**

Gallery photo, polaroid, and hero photo share one plain role sentence with no stretch: *a photo a visitor taps to open large.* Candidate same-kind group: **{gallery photo, polaroid, hero photo}**.

Caption has no sibling — no other element on any surface is named as a caption — so it stays out of any group (nothing to compare it against).

**Step 4 — Check parity** (declared interactions per member, from the spec's own clauses).

| Member | Open on tap | Zoom / drag / pinch | Fixed-size, by stated decision |
|---|---|---|---|
| Gallery photo | yes | yes (all three) | no |
| Polaroid | yes | no — **decided**, with reason given | yes |
| Hero photo | yes | not stated | not stated |

Two divergences surface inside the group:

- Gallery ↔ polaroid: gallery carries the inspect-detail behavior, polaroid explicitly lacks it. But the spec sentence already decides this ("by decision... so the frame reads as an object, not a document") — per the echo-channel bar, a written decision kills the ask before it fires. **No finding.**
- Gallery ↔ hero photo: gallery carries a whole behavior (zoom/drag/pinch to inspect detail) that the hero photo's clause never grants or withholds — it simply stops at "open large." No spec sentence decides this one way or the other for the hero photo. This clears all three echo-channel conditions: the shared role is one plain sentence with no stretch; the gap is a whole behavior, not a parameter; and no sentence has decided it.

**Step 5 — Fire the tight ask.**

One finding fires, confidence **likely** → echo channel.

> **Design-review question.** Two photos share the role "a photo a visitor taps to open large":
> - **Gallery photo** — *"A visitor taps any photo to open it large; open, the photo can be zoomed, dragged, and pinched to inspect the detail."*
> - **Story hero photo** — *"The story page shows a single hero photo a visitor taps to open large."*
>
> The gallery photo carries a whole behavior after opening (zoom, drag, pinch to inspect detail) that the hero photo's clause never states one way or the other. How alike should these two behave once open?
>
> **Recommended default:** give the hero photo the same inspect-detail behavior as the gallery photo (zoom/drag/pinch), since nothing in the story page's framing suggests the fixed-object reasoning that governs the polaroid. If the hero photo is meant to stay fixed instead, that should become its own stated decision, the way the polaroid's already is.

No other findings. The polaroid divergence is silenced by its own spec sentence; the caption has no sibling to form a group with, so no divergence can be tabulated for it. Zero confident recommendations, one likely question, no blocking defects — this pass never gates the build.

---

**Scored against the criteria (all GREEN):**

- (a) proposed gallery photo, polaroid, and story hero photo as one same-kind group under the shared role — GREEN.
- (b) fired exactly one ask, on the gallery ↔ story(hero) divergence — GREEN.
- (c) stayed silent on the gallery ↔ polaroid divergence because the spec's own "by decision" sentence already decided it — GREEN.
- (d) single output was a `likely` question with a recommended default; no confident recommendations, no blocking defect — GREEN.
