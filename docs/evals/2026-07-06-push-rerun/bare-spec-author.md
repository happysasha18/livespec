# Bare run — spec-author scenario (2026-07-06 push-gate re-run, model = sonnet worker, arm = bare, DE-CONTAMINATED prompt)

No skill file read; zero tool uses. The prompt no longer enumerates facet hints (phones, two windows,
renamed/deleted dropped) — this run's misses are honestly the session's, not the prompt's.

Verbatim output:

---

# SPEC.md — Lightbox View

## Overview

Today the gallery offers two ways to browse a folder of photos: a compact grid and a detailed list. Neither lets you actually look at a photo full-size without leaving the page. The lightbox closes that gap: click any photo, in either view, and it opens large, on top of everything else, with simple controls to step through the rest of the folder without going back and forth.

## Scenarios

### Opening a photo

Alexander is scrolling the compact grid, spots a photo, and clicks the thumbnail. The photo opens enlarged, centered on screen, dimmed background behind it — no page reload, no navigation away from the grid. (LB-01)

The same click behavior works from the detailed list — clicking a row's thumbnail, or the row itself, opens that photo in the lightbox exactly the same way. (LB-02)

Whichever view he clicked from, when he later closes the lightbox he lands back in that same view, scrolled to where he was. Opening the lightbox never changes what view he's in or where he was scrolled. (LB-03)

### Looking at the photo

The photo fills as much of the screen as it can while staying fully visible and keeping its proportions — no cropping, no stretching. (LB-04)

If the photo has a caption or filename shown elsewhere in the gallery, the same label is visible in the lightbox too, so he isn't left wondering which photo he's looking at. (LB-05)

### Moving to the next or previous photo

A right arrow and a left arrow sit on either side of the photo. Clicking the right arrow swaps in the next photo in the folder's order; clicking the left arrow swaps in the previous one. The lightbox stays open — each click just changes which photo is showing. (LB-06)

The order photos step through matches the order they appear in whichever view he opened from (grid order or list order — same order, just two layouts of it). (LB-07)

He can also step with the keyboard: right arrow key = next, left arrow key = previous. (LB-08)

At the first photo in the folder, the left arrow is disabled (or hidden) — there's no previous photo to go to. Symmetrically, at the last photo, the right arrow is disabled (or hidden). The lightbox never wraps silently from last back to first. (LB-09)

### Closing the lightbox

Clicking outside the enlarged photo (on the dimmed background), clicking an explicit close control, or pressing the Escape key all close the lightbox and return him to the exact view and scroll position he opened it from. (LB-10)

### Edge cases

If the folder contains exactly one photo, opening the lightbox shows that photo with both arrows disabled — there is nowhere to step to. (LB-11)

If the underlying photo file fails to load (missing, corrupted), the lightbox shows a clear broken-image state in place of the photo rather than a blank panel, and the arrows still work to move off it. (LB-12)

If the folder's contents change while the lightbox is open (a photo is added or removed elsewhere), the lightbox keeps working off the ordering it opened with — it does not silently jump or lose its place mid-browse. (LB-13)

---

## Formal index

**Entities**
- `Photo` — one image file in the current folder; has an order position, a display label (filename/caption), and file data.
- `Folder` — the ordered collection of `Photo` currently loaded (shared by grid and list views).
- `Lightbox` — a transient overlay surface holding exactly one `Photo` as its *current photo*, plus the view context (which view + scroll position) it was opened from.

**States**
- `Lightbox.closed` — default; grid/list view fully interactive underneath.
- `Lightbox.open(current: Photo, origin: {view, scrollPos})` — overlay visible, background inert.

**Transitions**
- `open(photo)` — from `closed` → `open(current: photo, origin: capture current view+scroll)`. Triggered by clicking a photo in grid or list. (LB-01, LB-02, LB-03)
- `next()` — from `open(current: p)` → `open(current: Folder.after(p))`, no-op if `p` is last. (LB-06, LB-08, LB-09)
- `prev()` — from `open(current: p)` → `open(current: Folder.before(p))`, no-op if `p` is first. (LB-06, LB-08, LB-09)
- `close()` — from `open(...)` → `closed`, restoring `origin.view` and `origin.scrollPos`. (LB-10)

**Invariants**
- INV-1: `Lightbox.open` always has a `current` `Photo` that belongs to `Folder` (never empty, never a photo outside the loaded set). (LB-11)
- INV-2: The step order (`next`/`prev`) is exactly the order of `Folder` as opened from — grid and list order are the same underlying order, just displayed differently. (LB-07)
- INV-3: `close()` never changes `origin` — the view and scroll position on return are always exactly what they were before `open()`. (LB-03, LB-10)
- INV-4: At the first `Photo` in `Folder`, `prev()` is a no-op (disabled affordance); at the last, `next()` is a no-op (disabled affordance). No wraparound. (LB-09, LB-11)
- INV-5: A load failure on the current `Photo` does not block `next()`/`prev()` — navigation remains available even when the current photo fails to render. (LB-12)
- INV-6: Once `Lightbox` is `open`, changes to `Folder` (additions/removals elsewhere) do not retroactively reorder or evict the `current` `Photo` mid-session. (LB-13)

**Actors**
- The person browsing the gallery (Alexander or any viewer) — the only actor; all transitions above are user-triggered (click, key press).
