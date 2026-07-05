# Bare run — spec-author scenario (2026-07-05, Sonnet worker, tool uses: 0)

Contamination note: the scenario prompt enumerated facet hints (two views, phones, two windows,
renamed/deleted files) — see evals/spec-author.md; the axis coverage below is partly prompt-fed.
Honest-boundary note: the "Formal index"/INV-style structure is loader-fed (evals/README.md).
The scored RED stands regardless: roughly ten product decisions taken silently — no ⟨DECIDE⟩, no
`[default]` tags, no questions to the author, no fences, no non-goals, no success measure.

Verbatim output:

---
## Lightbox view

### Overview

From either view of the gallery — the compact grid or the detailed list — clicking (or tapping) a photo opens it enlarged, centered over the page, with the rest of the gallery dimmed behind it. Prev/next arrows step through the same set of photos the person was just browsing, in the same order, without closing and reopening the lightbox. `LB-1`

The lightbox is a transient overlay, not a page: it does not replace the grid/list, it sits on top of it. Closing it (arrow-away, Escape, tap outside, back gesture) returns the person to the exact scroll position and view they were in. `LB-2`

### Scenarios

**Opening from either view**
Person clicks/taps a photo in the grid — the lightbox opens showing that photo enlarged, at the size that fits the screen without cropping. Person does the same from the list view — same lightbox, same behavior. The view the photo was opened from does not change what the lightbox looks like; it only changes what "next" means (see below). `LB-3`

**Stepping through photos**
Person clicks the next/prev arrow, or on desktop presses the right/left arrow key, or on a phone swipes left/right — the lightbox shows the next or previous photo in the current sort order (the same order visible in the grid/list at the moment the lightbox was opened). The image swaps in place; the lightbox itself does not close and reopen. `LB-4`

**Reaching the ends**
Person is on the first photo and presses/swipes "prev": nothing happens, or the arrow is visibly disabled. Same for "next" on the last photo. The lightbox never wraps silently from last back to first — that reads as a jump, not a boundary. `LB-5`

**Closing**
Person presses Escape (desktop), taps outside the enlarged photo, taps an explicit close control, or uses the phone's back gesture/button. The lightbox closes and the underlying grid/list is exactly as the person left it — same scroll position, same view. `LB-6`

**Two windows open on the same gallery**
Person has the gallery open in two browser windows (e.g. one on grid, one on list, or the same view twice). Opening a lightbox in one window has no effect on the other — each window's lightbox is that window's own state. Navigating prev/next in window A does not move window B. `LB-7`

**A photo is renamed or deleted by another tool while the app is open**
Person is browsing the lightbox (or has it closed) while a separate tool on the same machine renames or deletes files in the gallery's folder.
- If the currently-displayed photo becomes unavailable, the lightbox shows a clear "this photo is no longer available" state instead of a broken image, and prev/next still work to move to a photo on either side that still exists. `LB-8`
- If the person advances to a photo that turns out to be renamed/gone by the time the lightbox requests it, the same fallback applies rather than a silent blank or a crash. `LB-9`
- Renumbering caused by deletions elsewhere in the set does not skip or repeat neighboring photos for a lightbox session already in progress — "next" is resolved at the moment it's pressed, not pre-computed once at open time. `LB-10`

**Desktop vs phone**
On desktop: arrow icons are visible on hover/always-visible over the enlarged photo, left/right arrow keys step through photos, Escape closes. On a phone: arrows are tap targets sized for touch, and left/right swipe on the photo itself steps through photos; there is no keyboard, so swipe and tap are the only step controls. The lightbox fits the viewport in both cases without requiring the person to pinch-zoom just to see the whole photo. `LB-11`

**Loading**
If the enlarged photo takes a moment to load (large file, slow connection — more likely on a phone), the lightbox shows a lightweight loading state in place rather than a blank frame or a layout jump once the image lands. `LB-12`

---

### Formal index

**Entities**
- `Photo` — identified by a stable id the app assigns, distinct from filename (filenames can change externally).
- `GallerySet` — the ordered sequence of photos backing the current grid/list view at the moment the lightbox opened.
- `LightboxSession` — one instance of the lightbox open in one browser window: current photo id, the `GallerySet` order it is stepping through, and open/closed state.

**States** (per `LightboxSession`)
- `Closed`
- `Open(photo: Photo, position: index in GallerySet)`
- `Open-Unavailable(position: index)` — current position's photo no longer resolves to a file.

**Transitions**
- `Closed → Open(p, i)` — person activates photo `p` at position `i` from grid or list.
- `Open(p, i) → Open(p', i+1)` — next, where `p'` = photo currently at position `i+1` in `GallerySet`, re-resolved at press time.
- `Open(p, i) → Open(p'', i-1)` — prev, symmetric.
- `Open(p, i) → Open(p, i)` (no-op) — next pressed at last position, or prev pressed at first position.
- `Open(p, i) → Open-Unavailable(i)` — the file backing `p` is renamed/deleted externally and re-resolution at position `i` fails.
- `Open-Unavailable(i) → Open-Unavailable(i±1)` / `Open(p, i±1)` — prev/next still resolve from an unavailable state, using the same re-resolve-at-press-time rule.
- `Open(*) → Closed`, `Open-Unavailable(*) → Closed` — close via Escape, outside tap, close control, or back gesture.

**Invariants**
- `INV-1` One `LightboxSession` per browser window; sessions in different windows over the same gallery never share or mutate each other's state. (LB-7)
- `INV-2` Closing a `LightboxSession` never mutates the grid/list scroll position or active view. (LB-2, LB-6)
- `INV-3` Position resolution ("what photo is at index i") is evaluated at the moment prev/next is pressed, never cached from lightbox-open time — external renames/deletes are reflected on the next step, not just on reopen. (LB-9, LB-10)
- `INV-4` `next` at the last position and `prev` at the first position are no-ops (no wraparound). (LB-5)
- `INV-5` An unresolvable photo renders the explicit unavailable state, never a broken image, blank frame, or thrown error. (LB-8, LB-9)
- `INV-6` The `GallerySet` order used by a session matches the order of the view (grid or list) it was opened from at open time. (LB-3, LB-4)
---
