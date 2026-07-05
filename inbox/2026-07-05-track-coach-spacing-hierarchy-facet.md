# Wish: feature-intake should sweep VISUAL HIERARCHY as a standard facet (spacing + type)

## The wish (plain words)
When a feature adds or changes any visible surface, the intake should also sweep **visual hierarchy** —
the same way row 72 already sweeps responsive / touch-vs-hover / empty-error-loading / a11y / performance.
It is one more "standard facet a layman can't name but instantly sees when it's wrong." Two concrete sub-rules
to state and default-and-report:

- **Spacing hierarchy:** the gap BETWEEN separate things must be larger than the gap WITHIN one thing
  (inter-group > intra-group). Nesting depth drives spacing, not per-element guesswork.
- **Brightness / type hierarchy:** a heading is never dimmer or smaller than the body it heads; sizes come
  from one scale, not scattered ad-hoc values.

Proposal: add a "visual hierarchy" line to row 72's swept-facet list, each item either specified by the
human or defaulted-and-reported as a plain-words tradeoff (same mechanism as the other facets).

## Why (what broke / what was missing)
In track-coach, a multi-panel surface (the reference read + web-info + evidence drawer) shipped with
per-panel margins picked by eye (10 / 24 / 30 px). That produced an INVERTED spacing hierarchy — the gap
between two top-level panels (24px) was SMALLER than the gap between sub-panels nested inside one drawer
(30px). The eye reads that as "broken," but no checklist item forced the check, so it slipped through the
whole spec→prove→matrix→test→code pipeline and only surfaced when Alexander eyeballed the render.
Root cause = the intake has no explicit "visual hierarchy" facet; spacing/type hierarchy is exactly the
kind of thing a producer notices but can't name up front. Same family as the row-72 "standard facets"
incident. Fix in track-coach = a two-role spacing split (`--gap` within a group, `--rhythm` between
sections) + a brightness/type scale; the GENERAL lesson belongs here in the method, not in one project.

## Who threw it
The track-coach session (Alexander's review, 2026-07-05). He asked directly: "why wasn't this automatic —
this should be written down somewhere; if it's live-spec, send it to the inbox."
