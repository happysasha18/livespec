# With-skill run — spec-author scenario (2026-07-05, Sonnet worker, read the SKILL.md first)

Verbatim output:

---
Here is the spec-delta for the lightbox feature, authored per `spec-author`'s method (use-case-first, regression fences first, entities/states/transitions/invariants inside the walk, composed across the canonical axes, facet sweep woven in as sentences, closed by non-goals + a success measure). I did not open any other file — this was written from the SKILL.md alone, as instructed.

## Viewing a photo enlarged (the lightbox)

**Regression fences — what this change must leave standing.** Opening a photo must not change how the grid or the list already show and order photos: the grid still shows its compact tiles and the list still shows its detailed rows exactly as before this feature lands, and whatever ordering/sort each view already promises stays that view's ordering when the new lightbox reads from it (cite the existing ordering clause for each view when merging this delta — I don't have the base `SPEC.md`'s anchors in front of me, so this fence needs its real citation filled in rather than the placeholder above).

A viewer is looking at **the gallery** in either **grid view** (compact tiles) or **list view** (a detailed row per photo). Each row/tile shows **a photo** — a single image file with a name, a source location, and a position in whichever ordering the current view is showing.

**Clicking a photo opens it enlarged.** Clicking a tile in grid view, or a row's image in list view, opens **the lightbox**: a full-size view of that one photo, layered over the gallery. `CR-LB1`

**The lightbox has exactly two states — closed and open-on-a-photo.** While open, it always shows exactly one photo at a time; opening a different photo replaces the current one, it never stacks a second lightbox on top. `INV-LB1`

**Prev/next arrows walk the same ordering the viewer was already looking at.** Each side of the enlarged photo carries a control — "prev" and "next" — that moves to the adjacent photo in the ordering of whichever view (grid or list) was open when the lightbox was triggered. `CR-LB2` ⟨DECIDE⟩ At the first/last photo, does the arrow wrap to the other end, or does it disable/hide? Recommendation taken so the lane keeps moving: **disable the arrow at the ends, no wraparound** — the more common, less surprising convention. `[default]`

**Closing always returns to exactly where the viewer left off.** The close control (an "X"), the Escape key, a click on the dimmed backdrop, or the phone's back gesture, all close the lightbox and return to the originating view — grid stays grid, list stays list — at the same scroll position it had before opening; the underlying view is never reset to the top. `CR-LB3` No open of the lightbox is a dead end: every open eventually closes back to its origin. `INV-LB2` `[default]` (the exact close triggers are a reasonable default, not something the viewer asked to decide — flag for confirmation.)

**The viewer is the only actor.** Every transition here — open, prev, next, close — is user-initiated; nothing auto-advances (see non-goals).

### Composed across the axes

- **View (grid / detailed list):** both are entry points into the same lightbox; the photo shown and the prev/next ordering come from whichever view was open at the moment of the click, not a third global order.
- **Mode / tier:** not applicable to this surface — no read/edit or tiering distinction exists for viewing a photo. N/A.
- **Viewport size:** below desktop width, the lightbox goes full-screen; prev/next become swipe gestures (swipe left = next, swipe right = prev, swipe down = close) in addition to any on-screen arrows, since hover-sized arrow targets don't work on touch. `T-LB1` `[default]`
- **Persistence / reopen:** the lightbox's open/closed state is not written to storage and does not survive a page reload — refreshing the page always lands back on the grid or list, closed. `T-LB2` `[default]`
- **Concurrency (two windows open on the same gallery):** the lightbox's open/closed state and which photo it's showing are local to each window — opening a photo in one window has no effect on the other window's view, and each window discovers an unavailable photo independently rather than through any cross-window sync. `T-LB3` `[default]`

### The facet sweep

- **Loading and error states:** while the enlarged image is loading, the lightbox shows an explicit loading state (not a blank flash); if the enlarged image fails to load, it shows an explicit error state, never a broken-image icon standing in silently. `T-LB4`
- **A missing source — the photo gets renamed or deleted by another tool while the gallery is open:** if the photo currently shown in the lightbox becomes unavailable, the lightbox shows an explicit "this photo is no longer available" message with the option to close or move to the next available photo — it never guesses a replacement or silently disappears. `INV-LB3 (safety)` ⟨DECIDE⟩ this depends on how the gallery identifies a photo elsewhere in the spec: does it track a photo by a stable id/path (so a rename is detected as a rename), or only by filename (so a rename looks identical to delete-plus-new-file)? That answer isn't in front of me and changes whether "renamed" ever shows a distinct message from "deleted" — needs the author's call.
- **Accessibility:** the lightbox is reachable and operable by keyboard alone — arrow keys move prev/next, Escape closes — and traps focus while open so tabbing never silently leaves it; the enlarged image carries the same alt text as its source, and controls hold sufficient contrast against the dimmed backdrop. `T-LB5`
- **Performance envelope:** the next and previous photos are preloaded once the lightbox opens, so navigating through a large gallery doesn't stall waiting on each image; the gallery's full photo set is never bulk-loaded just because one lightbox opened. `T-LB6`
- **Visual hierarchy:** the backdrop dims the gallery behind it enough that the enlarged photo and its controls read as the one active layer; close/prev/next controls are sized and spaced from the same scale as the rest of the app, not ad hoc.

### Non-goals

Editing, cropping, or deleting a photo from inside the lightbox — it is look-only, not this time. Pinch-zoom or panning within the enlarged photo — not this round. An autoplay/slideshow mode — not this round. A shareable/deep link directly to one open photo — not this round.

### Success measure

A viewer can go from any thumbnail or row to seeing it enlarged, move through the neighboring photos without returning to the grid/list, and always land back exactly where they started when done. `[default]` As a number: the share of lightbox opens that end in an explicit close action (X / Esc / backdrop / back-gesture) rather than a stuck or broken state — target ~100%. `[default]`

### Formal index (delta — merge into the existing table, renumber to avoid collision)

| Anchor | One line | Home |
|---|---|---|
| CR-LB1 | Clicking a photo in grid or list opens the lightbox on that photo | Viewing a photo enlarged |
| CR-LB2 | Prev/next move to the adjacent photo in the current view's order | Viewing a photo enlarged |
| CR-LB3 | Closing returns to the originating view at its prior scroll position | Viewing a photo enlarged |
| INV-LB1 | Lightbox shows exactly one enlarged photo at a time, never stacked | Viewing a photo enlarged |
| INV-LB2 | Every open eventually closes back to its originating view | Viewing a photo enlarged |
| INV-LB3 | An unavailable photo shows an explicit message, never a silent guess | Viewing a photo enlarged |
| T-LB1 | Below desktop width: full-screen lightbox + swipe gestures | Viewing a photo enlarged |
| T-LB2 | Lightbox state does not persist across reload | Viewing a photo enlarged |
| T-LB3 | Lightbox open/closed state is independent per browser window | Viewing a photo enlarged |
| T-LB4 | Explicit loading and error states for the enlarged image | Viewing a photo enlarged |
| T-LB5 | Keyboard-reachable with trapped focus; alt text carried through | Viewing a photo enlarged |
| T-LB6 | Next/prev photo preloaded; no bulk-load of the whole gallery | Viewing a photo enlarged |

**Open questions / marked defaults, surfaced as required (batched, not one ping each):**

1. ⟨DECIDE⟩ **How does the gallery identify a photo** (stable id/path vs. filename)? This decides whether a rename shows a distinct message from a delete in the lightbox's "no longer available" state — I couldn't find this in what I read, it needs the author's call.
2. `[default]` **No wraparound** — prev/next disable at the ends of the list rather than looping. Confirm or override.
3. `[default]` **Close triggers**: X button, Esc, backdrop click, and back-gesture all close. Confirm the full set is wanted (e.g., is backdrop-click-to-close actually desired, or too easy to trigger by accident?).
4. `[default]` **Swipe gestures on phone**: left/right = next/prev, down = close. Confirm this matches the app's existing touch conventions elsewhere, if any exist.
5. `[default]` **No persistence across reload**, and **lightbox state is per-window, not synced** between two open windows on the same gallery. Confirm this matches how the rest of the app already treats two-window concurrency (I don't have visibility into whether other surfaces already promise cross-window sync — if they do, this default should follow suit instead).
6. **Fence citations are placeholders** — I don't have the existing `SPEC.md` in hand, so the exact anchors for "the grid's/list's existing ordering promise" need to be filled in by whoever merges this delta, per the fence rule (a fence must cite a real clause, not float free).
---
