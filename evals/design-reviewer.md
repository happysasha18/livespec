# Eval — design-reviewer (SPEC E-19)

## Scenario

Both arms read the same planted spec; the with-skill arm first reads
`skills/design-reviewer/SKILL.md` and runs the full design review over the proven spec. The spec under
review (verbatim) carries two element-level same-kind pairs — one a live divergence, one a divergence a
sentence already decides:

> # Little Gallery — spec
> The **gallery page** shows a wall of photos. A visitor taps any photo to open it large; open, the
> photo can be zoomed, dragged, and pinched to inspect the detail.
> The **memories page** shows a scatter of polaroid photos with a caption under each. A visitor taps a
> polaroid to open it large. The polaroid opens flat and cannot be zoomed — by decision, the polaroid
> keeps its printed size so the frame reads as an object, not a document.
> The **story page** shows a single hero photo a visitor taps to open large.

Planted structure: the gallery photo, the polaroid photo, and the hero photo all share the role
sentence "a photo a viewer opens large to inspect" — an undeclared same-kind group no clause names.
Within it: the **hero photo** declares no zoom/drag/pinch and **no sentence decides the difference**
(a live same-kind divergence — the ask should fire, one object pair, recommended default "give the
hero photo the same inspect gestures"). The **polaroid** also lacks the gestures, but the spec already
states "cannot be zoomed — by decision" (a decided difference — the pass must stay silent [INV-59]).

## Criteria

| Criterion (the skill's promise) | bare | with-skill |
|---|---|---|
| Descends below the page list to the photo elements and proposes the undeclared same-kind group | — | GREEN — three photos grouped by one role sentence |
| Fires exactly one ask on the gallery↔hero divergence, two objects in hand + recommended default | — | GREEN — one ask, both objects with their spec sentences |
| Stays SILENT on the gallery↔polaroid divergence a sentence already decides [INV-59] | — | GREEN — no ask, the decided sentence kills it |
| Every finding is a recommendation or an ask, never a blocking defect [INV-140] | — | GREEN — no defects, no landing held |
| Names two concrete objects each with its spec sentence per finding | — | GREEN |
| Respects the cap (≤3 asks) and the strong-signal bar | — | GREEN — one ask, well under the cap |

## The red

bare run: 2026-07-14 (one Sonnet worker per arm; records at
`docs/evals/2026-07-14-design-reviewer/`). The bare arm DID sense the hero-photo silence — the
substance is there, loader-fed — but delivered it as an undifferentiated list that mixed the same-kind
design divergence with prover-territory completeness gaps ("open large" undefined, no close behaviour,
no between-photo navigation), carried no confidence read, no two-objects-in-hand ask form, and no cap;
it never named the explicit same-kind group and offered no recommended default in the batched-question
shape. The with-skill arm ran the five-step similarity lens, proposed the three photos as one same-kind
group by role, fired exactly one `likely` ask on the gallery↔hero divergence with both objects and a
recommended default, and stayed silent on the gallery↔polaroid divergence the spec already decides —
every criterion GREEN, no blocking defect.

The red is therefore **form-only**, and the record says so plainly: the bare arm DID find the planted
divergence (the substance is there, loader-fed), but delivered it without the ask FORM — no named
same-kind group, no confidence read, no two-objects-in-hand shape, no cap, no recommended default in the
batched-question shape, and no separation of the design-review lane from the prover's verification lane.
The load-bearing criterion the eval scores is that disciplined ask form, not the raw detection.

## Re-run

One Sonnet worker per arm. Bare arm: the spec + "review the design of this before we build; do not
invoke any tools or skills". With-skill arm: "First read skills/design-reviewer/SKILL.md and run the
full design review strictly by it" + the same spec. Score per criterion — the load-bearing pair is the
fires-on-live / silent-on-decided split; append the dated record to `docs/evals/`.
