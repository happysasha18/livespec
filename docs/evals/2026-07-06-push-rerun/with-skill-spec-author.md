# With-skill run — spec-author scenario (2026-07-06 push-gate re-run, model = sonnet worker, arm = with-skill, spec-author 0.1.13, DE-CONTAMINATED prompt)

Read skills/spec-author/SKILL.md + live-spec-base first; 7 tool uses.

Verbatim output:

---

Here is the spec-delta section, authored per `spec-author` (v0.1.13) and the shared rules in `live-spec-base`.

> **Authoring note (not part of the shipped spec — delete once merged):** this delta assumes a host `SPEC.md` that already specifies the folder-of-photos gallery with two existing views. I don't have that document's real anchors, so I've used placeholders — **`V-GRID`** (compact grid view) and **`V-LIST`** (detailed list view) and **`PH-1`** (the `Photo` entity) — for the fences below. Swap them for the host spec's real anchors at merge time; don't merge this note itself (rule 13 — a claim needs its primary source, and I don't have one for the pre-existing sections).

## Opening a photo — the lightbox

**Regression fences.** Nothing about how photos are browsed today changes: the grid view still renders the
folder's photos as a compact grid, at whatever size and order it already uses `[V-GRID]`; the detailed list
view still renders the same photos as a list with whatever per-photo detail it already shows `[V-LIST]`;
and the folder's photo order — whatever a **Photo** `[PH-1]` already carries as its position — is unchanged
by either view. This feature only adds a new thing that can happen when a photo is clicked; it re-authors
nothing about how the two existing views look or sort.

A person is browsing either the grid or the list. They click one photo. The **Lightbox** opens: a
full-screen overlay showing that one **Photo** enlarged, dimmed background behind it, with a **prev
arrow** and a **next arrow** flanking the image and a close control. `[E-1]`

The Lightbox has two states: **closed** (its default — the grid or list is what's on screen) and **open**
(one photo enlarged, everything else dimmed behind it). While open, it tracks two things: **which photo**
is currently shown, and **which view it was opened from** (grid or list) — so closing knows where to
return. `[E-1]`

**Opening it** — clicking a photo thumbnail in the grid, or a photo row in the list, is the one and only
door into the Lightbox; the visitor triggers it, never the system on its own. `[T-1]`

**Stepping through it** — the next arrow (or the → key) advances to the next photo in the folder's order;
the prev arrow (or ←) goes back one. The order followed is the **same order** the folder already has —
the Lightbox never re-sorts; it just walks the one sequence both views already agree on. At the first
photo, prev is disabled (not hidden — a person can always see there's nowhere further back); at the last
photo, next is disabled the same way. ⟨DECIDE⟩ *should the ends wrap around instead of stopping?*
Recommended default, taken so the lane keeps moving: **stop, don't wrap** — wrapping silently loops a
person back to a photo they already saw with no signal that they've cycled. `[T-2] [default]`

**Closing it** — the close control, the Esc key, or a click on the dimmed background outside the photo all
close the Lightbox and return to **exactly** the view and photo it was opened from — scrolled/positioned so
that photo is where the eye left it. No stranding: a person is never dropped back at the top of the grid
having lost their place. `[T-3] [INV-1]`

## Composing across axes

- **View (grid / detailed list).** The Lightbox behaves identically regardless of which view launched it —
  same overlay, same arrows, same keyboard controls. The only thing the view affects is the close target:
  closing always lands back on the launching view, at the same photo. `[C-1]`
- **Mode.** No read/edit mode split exists on this surface yet — N/A.
- **Tier.** No tiering applies to this feature — N/A.
- **Viewport size.** Below phone width, the Lightbox goes edge-to-edge (no dimmed margin to spare), and the
  arrows grow into larger tap targets sized for a thumb, not a cursor — detailed under the facet sweep
  below. `[C-2]`
- **Persistence / reopen.** ⟨DECIDE⟩ *is the open Lightbox (and which photo) reflected in the URL, so a
  refresh or a shared link reopens the same photo — or is it purely client-side and a refresh drops back to
  the view underneath?* Recommended default, taken so the lane keeps moving: **the URL updates while open**
  (so the browser Back button closes the Lightbox rather than leaving the page entirely — see the fit walk
  below) and a fresh load of that URL reopens straight into the Lightbox on that photo. A reload with no
  such URL simply shows the view underneath, closed. `[C-3] [default]`
- **Concurrency.** Two windows open on the same folder each hold their own, independent Lightbox state —
  one window stepping next/prev never affects the other; nothing about this feature is shared/persisted
  server-side. `[C-4]`

**The composition invariant:** opening, stepping, and closing the Lightbox never changes what the grid or
list itself shows or how it's sorted — the Lightbox is a read-only window onto the same one photo sequence,
under every view, viewport, and window. `[INV-2]`

## The facet sweep

- **Phone / narrow window** — the Lightbox is full-bleed (no dimmed border to lose to a small screen); the
  photo shrinks to fit the viewport, arrows stay reachable at the same corners. `[default]`
- **Touch** — the arrows are real tap targets, not hover-revealed chrome; a left-half / right-half tap on
  the photo also steps prev/next, and a horizontal swipe does the same — so nothing here depends on a mouse
  existing. `[default]`
- **Empty, error, and loading** — a photo still loading shows a blurred low-res placeholder in place (never
  a blank flash); a photo that fails to load shows a plain "this photo didn't load" message with the same
  arrows and close still live (never a raw broken-image icon, never a dead end); a folder of exactly one
  photo opens the Lightbox with both arrows disabled from the start. ⟨DECIDE⟩ *if a photo is removed from
  the folder between page-load and the visitor stepping onto it (a background rescan), what does the
  Lightbox show?* Recommended default: **skip forward to the next photo that still exists, with a one-line
  note that one was skipped** — never freeze, never show a blank frame. `[default]`
- **Accessibility** — Esc closes; ← / → step; focus is trapped inside the Lightbox while open and returns
  to the exact thumbnail/row that opened it on close; the arrows are real buttons with `aria-label`s ("previous
  photo" / "next photo"); a screen reader announces "photo N of the folder's total" on every step; the
  enlarged image carries the same alt text the grid/list already give it. `[default]`
- **Performance envelope** — only the current photo and its immediate prev/next neighbor are loaded at full
  resolution; every other photo in the folder stays at whatever thumbnail resolution the grid/list already
  use until it's actually navigated to. ⟨DECIDE⟩ *what folder size must stay smooth (hundreds? low
  thousands)?* Recommended default: **no hard cap — this lazy load-ahead-of-one keeps it flat regardless of
  folder size**, revisit only if a real folder proves otherwise. `[default]`
- **Visual hierarchy** — the enlarged photo is the only thing competing for attention; the arrows, the
  close control, and the position counter ("N of M") sit low-contrast and corner-anchored, never sized or
  colored to rival the photo itself. `[default]`
- **Two windows at once** — covered under Concurrency above: independent per window, nothing to strand.
- **A missing source** — same as the empty/error case above: a photo gone from the folder is skipped
  forward with a note, never silently frozen, never a guess at what should have been there. `[default]`

## The fit walk

- **Arrive.** One door in: clicking a photo from either view. If the URL-reflects-state default above
  stands, a shared/reloaded Lightbox link is a second door straight to one photo — both land the visitor in
  the same state. `[target]` *(deep-linking itself; only the URL-reflection behavior above is specified now.)*
- **Do.** Look at one photo enlarged, step forward/back through the whole folder without ever dropping back
  to the grid/list in between.
- **Next, from every state.** At either end of the folder, the disabled arrow itself is the answer ("nowhere
  further this way") — never a dead click. Closing is reachable from every single photo the same three ways
  (Esc / background click / close control) — never a state where the visitor is stuck inside.
- **Return visit.** No memory of the last photo viewed is kept between visits — each visit starts however
  the visitor clicks in, fresh. `[default]`
- **Feel.** No approved visual prototype is referenced for this feature; absent one, the recommended default
  is the ordinary lightbox convention — dimmed/darkened backdrop, photo as sole subject, chrome subordinate
  (tying to the visual-hierarchy facet above). `[default]`
- **Next feature this invites** — a direct shareable link to one photo, captions/metadata shown alongside
  the enlarged photo, pinch-zoom/pan on the enlarged image. Named, not specified. `[target]`

## Closing the delta

**Non-goals this time:** no pinch-zoom or pan past fit-to-screen, no autoplay/slideshow, no
download/edit/delete controls from inside the Lightbox — all deliberately left out.

**Success measure:** a visitor can walk an entire folder start to finish via next/prev alone, never
returning to the grid or list in between; the number to watch, once reading machinery exists, is what
share of Lightbox sessions close via a boundary-reached arrow rather than an early exit. `[default]`

## Open decisions

- ⟨DECIDE⟩ Do the folder ends wrap on prev/next, or stop? Recommended: **stop.** `[D-1]`
- ⟨DECIDE⟩ Does the Lightbox reflect its open/photo state in the URL (deep-linkable, Back closes it) or stay
  purely client-side? Recommended: **reflect it in the URL.** `[D-2]`
- ⟨DECIDE⟩ What happens to the current photo if it's removed from the folder mid-session? Recommended:
  **skip forward one, with a note.** `[D-3]`
- ⟨DECIDE⟩ Is there a real folder-size ceiling this must stay smooth past? Recommended: **none — lazy
  load-ahead-of-one covers it.** `[D-4]`

## Formal index — new rows to merge in

| Anchor | One line | Section |
|---|---|---|
| E-1 | **Lightbox** entity: closed/open, tracks current photo + originating view | Opening a photo — the lightbox |
| T-1 | opening: click a photo in grid or list, the only door in | Opening a photo — the lightbox |
| T-2 | stepping: prev/next follow the folder's existing order; stops (doesn't wrap) at either end `[default]` | Opening a photo — the lightbox |
| T-3 | closing: three controls, always returns to the exact originating view + photo | Opening a photo — the lightbox |
| INV-1 | no stranding — close always restores the exact view/photo/position | Opening a photo — the lightbox |
| INV-2 | composition invariant: the Lightbox never changes what the grid/list shows, under any view/viewport/window | Composing across axes |
| C-1 | view axis: same Lightbox behavior from grid or list; only the close target differs | Composing across axes |
| C-2 | viewport axis: edge-to-edge below phone width, larger tap targets | Composing across axes |
| C-3 | persistence axis: URL reflects open state; reload/share reopens the same photo `[default]` | Composing across axes |
| C-4 | concurrency axis: independent per window, nothing shared | Composing across axes |
| D-1 | ⟨DECIDE⟩ wrap vs stop at folder ends | Open decisions |
| D-2 | ⟨DECIDE⟩ URL-reflected vs purely client-side state | Open decisions |
| D-3 | ⟨DECIDE⟩ behavior when the current photo is removed mid-session | Open decisions |
| D-4 | ⟨DECIDE⟩ whether a real folder-size ceiling exists | Open decisions |

---

Open ⟨DECIDE⟩ points surfaced above, with the recommendation each carries so work can proceed without stalling: wrap-vs-stop at the folder's ends (recommend stop), URL-reflected vs client-only Lightbox state (recommend URL-reflected, so Back closes it rather than leaving the page), what happens when the current photo vanishes mid-session (recommend skip-forward-with-a-note), and whether a real folder-size ceiling needs naming (recommend none, given the lazy load-ahead-of-one approach). None of these blocked the section — each is written as a taken `[default]` per the facet-sweep rule, findable and reversible on your word.
