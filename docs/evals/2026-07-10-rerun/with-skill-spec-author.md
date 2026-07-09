# With-skill run — spec-author scenario (2026-07-10 rerun, model = sonnet worker, arm = with-skill, spec-author 0.1.24)

Read skills/spec-author/SKILL.md directly (Read tool, not the Skill tool); 1 tool use.

Verbatim output:

---

Read the skill file directly (not via the Skill tool). Below is the spec-delta for the lightbox feature, written strictly by its method: use-case-first scenario, codes at line-ends, regression fences first, composition across the canonical axes, the facet sweep, the fit walk, and the two closing sentences — followed by the Formal-index rows this delta adds and the batched questions the method requires me to surface rather than silently answer.

One up-front flag: I don't have the actual PRODUCT_SPEC.md open (this is a dry run), so I can't cite the real anchors for the existing grid/list "click" behavior the fences below need to point at. I've written the fences in plain prose and marked exactly where a real anchor must be substituted before this lands in the live document.

---

## Looking closer: opening a photo in the lightbox `[feature: F-lightbox]`

The compact grid and the detailed list both show a folder's photos at a glance; neither, until now, lets a person see one photo enlarged. Clicking a photo in either view opens the **lightbox** — a full-screen overlay showing that one photo enlarged, centered, with a prev arrow and a next arrow that step through the same folder one photo at a time.

**The grid and the list keep their promises untouched.** Opening the lightbox changes nothing about the view underneath it: the grid's thumbnail order and scroll position, and the list's row order and scroll position, are exactly as they were the moment before the click ⟨cite pending — replace with the actual clause anchor for "the grid renders thumbnails in folder order" and its list counterpart, once read from the live spec⟩. Closing the lightbox returns the person to that same view, at that same scroll position, with no reflow. CR-LB-1

**The lightbox itself.** The **lightbox** is a new entity with two states: *closed* (the default — nothing overlays the grid or list) and *open on photo N*, where N is the clicked photo's position in the folder's current order. CR-LB-2

- **Opening**: clicking a photo (in either view) is the only trigger; it transitions the lightbox from closed to open-on-N, N being the clicked photo. CR-LB-3
- **Stepping**: from open-on-N, the next arrow moves to open-on-(N+1); the prev arrow moves to open-on-(N-1). CR-LB-4
- **Closing**: an explicit close control, clicking outside the enlarged photo, and the Esc key all transition open-on-N back to closed. CR-LB-5

**A state with no way out is a bug — say what happens at the ends of the sequence.** At the first photo, does prev disable, hide, or wrap to the last photo? At the last photo, does next do the mirror? This is a genuine taste call, not a default I can silently pick — see the batched questions below. ⟨DECIDE⟩ CR-LB-6

**Invariants.**
- *Safety*: the lightbox never shows a state for a photo that no longer exists in the folder — if the underlying file is gone or unreadable when stepped to, the lightbox shows an error state rather than a blank or stale image (see "a missing source" below). INV-LB-1
- *Liveness*: every open-on-N eventually reaches closed — there is no reachable state where the person is looking at the lightbox with no path back to the grid or list (the door↔room "no dead ends" invariant, applied here). INV-LB-2

**Composed across the canonical axes.**
- **View** (compact grid / detailed list): the lightbox is a third layer on top of whichever view was active at the click; it carries no separate "grid-flavored" or "list-flavored" lightbox — one lightbox, either origin. Closing returns to the originating view, unchanged. INV-LB-3
- **Mode**: no read/edit split exists yet on either view, so this axis is N/A here — stated explicitly rather than silently skipped.
- **Tier**: no tiering concept has been introduced elsewhere in the product as I have it in context; N/A, stated explicitly rather than skipped. ⟨DECIDE⟩ if a tier concept exists elsewhere in the real spec, this line needs revisiting.
- **Viewport size**: below desktop width, the lightbox stays a full-screen overlay (see the facet sweep's phone-layout entry).
- **Persistence / reopen**: the lightbox's open/closed state and current photo are **not** persisted across a reload — a refresh always lands on the grid or list, closed. `[default]` CR-LB-7
- **Concurrency**: single-user, no shared/concurrent-write state involved; N/A, stated explicitly.
- **Every other live surface**: while the lightbox is open, the grid or list behind it is inert (not scrollable, not clickable) but still rendered and unchanged underneath — this is the "hold" answer for the sibling surface, named so a reviewer can check it. INV-LB-4

**The facet sweep** (every visible surface owes this list a sentence — SPEC T-13):

- **Layout on a phone or narrow window** — the lightbox is a full-viewport overlay; the enlarged photo scales to fit the shorter of width/height with no crop, and prev/next arrows sit at the left/right edges rather than floating over the image center. `[default]`
- **Touch where the design assumed a mouse** — a horizontal swipe on the enlarged photo steps prev/next, the same as clicking the arrows; a tap outside the photo closes the lightbox, the same as the click-outside on desktop. `[default]`
- **Empty, error, and loading states** — loading: the enlarged photo shows a blurred low-res placeholder (already available from the grid thumbnail) swapped for the full image once it loads, so the overlay is never a blank rectangle. Error: if the full image fails to load (missing/renamed file), the lightbox shows a plain "this photo can't be shown" message in place of the image, keeps the arrows live so the person can step past it, and keeps the close control live. Empty: N/A — the lightbox never opens without a clicked photo, stated explicitly rather than skipped. `[default]`
- **Accessibility** — Esc closes; left/right arrow keys step prev/next; the close control and both arrows are reachable by Tab and have a visible focus state; the enlarged photo's alt text is the photo's existing filename or caption, whichever the grid/list already use as its accessible label. `[default]`
- **The performance envelope** — the low-res placeholder paints within 150 ms of the click; the full-resolution photo replaces it within 2 s on a cold visit. `[default]` — flagged as a number I picked rather than one confirmed; see batched questions.
- **Visual hierarchy** — the overlay dims the grid/list behind it so the enlarged photo is the only strong element on screen; the arrows and close control render smaller and lower-contrast than the photo itself, never competing with it for attention. `[default]`
- **Two windows at once** — the lightbox's open/closed state is local to its own window/tab; opening the lightbox in one window does nothing to a second window open on the same folder (no shared state exists to desync, since nothing persists — see the persistence axis above). CR-LB-8
- **A missing source** — covered above under invariants/error state: a photo gone or renamed by the time it's stepped to shows the error state, never a guess at what it might have been.

**The fit walk** (product/UX kind — SPEC INV-29):

- **Arrival**: the only entry to the lightbox, today, is clicking a photo in the grid or the list — no direct link/URL entry exists yet. `[target]` a shareable/deep-linkable lightbox URL is a named future surface, not specified for build now.
- **What they do here**: look at one photo enlarged, step to neighboring photos, close.
- **Where they go next from every state**: from open-on-N, the paths are prev, next, or close — all three always available except at the sequence's ends, which is exactly the ⟨DECIDE⟩ above.
- **What a return visit changes**: nothing — no seen-state or last-viewed-photo memory is kept (ties to the `[default]` no-persistence line above). `[default]`
- **Feel against an approved prototype**: no prototype has been shown or approved for this feature in what I have; this clause is text-born and carries no `norm:` pointer. If a mockup exists, open it before building and this section gets the pointer at that point.
- **What next feature this invites**: a slideshow/autoplay step-through, and photo actions from inside the lightbox (download, rotate, delete) are natural next asks. `[target]` both named, neither specified now.

**Non-goals.** Editing, deleting, downloading, or rotating a photo from the lightbox; a slideshow/autoplay mode; a deep-linkable URL to a specific photo — all wait for a later pass. CR-LB-9

**Success measure.** A person who opens the lightbox can reach the next or previous photo in one action, and always has a working path back to the view they came from, with no dead end. `[default]` — a numeric target (e.g., a session-analytics threshold) is not confirmed; see batched questions.

### Formal index — new rows this delta adds

| anchor | one line | home |
|---|---|---|
| `F-lightbox` | the lightbox feature as a whole | Opening a photo in the lightbox |
| CR-LB-1 | opening the lightbox leaves the grid/list unchanged underneath | Opening a photo in the lightbox |
| CR-LB-2 | the lightbox entity: closed / open-on-N | Opening a photo in the lightbox |
| CR-LB-3 | click opens the lightbox on the clicked photo | Opening a photo in the lightbox |
| CR-LB-4 | prev/next step to N-1/N+1 | Opening a photo in the lightbox |
| CR-LB-5 | close control, click-outside, Esc all close | Opening a photo in the lightbox |
| CR-LB-6 | behavior at the first/last photo (undecided) | Opening a photo in the lightbox |
| INV-LB-1 | safety: never shows a gone photo without an error state | Opening a photo in the lightbox |
| INV-LB-2 | liveness: every open state has a path to closed | Opening a photo in the lightbox |
| INV-LB-3 | view axis: one lightbox, either origin, closes back to it | Opening a photo in the lightbox |
| INV-LB-4 | every-other-surface axis: grid/list held inert but rendered underneath | Opening a photo in the lightbox |
| CR-LB-7 | no persistence of open/photo state across reload | Opening a photo in the lightbox |
| CR-LB-8 | two-window independence (nothing shared to desync) | Opening a photo in the lightbox |
| CR-LB-9 | non-goals for this pass | Opening a photo in the lightbox |

(This table must be merged into the real document's single end-of-doc Formal index, not kept as a second one — flagging per the pack's "an index that drifts" anti-pattern.)

---

### Batched questions / ⟨DECIDE⟩ points surfaced, not silently filled

1. **CR-LB-6 — sequence ends.** At the first photo, does prev disable, hide, or wrap to the last photo? Mirror question for next at the last photo. I did not silently pick this because "no dead ends" is satisfied by either disable-with-visible-affordance or wrap — it's a genuine taste call, not a triviality.
2. **Fence citations.** CR-LB-1 needs the real anchors for the existing "grid renders in folder order" / "list renders in folder order" (or equivalent) clauses from the live PRODUCT_SPEC.md — I don't have that document open in this exercise, so I left a cite-pending marker instead of inventing an anchor.
3. **Performance number.** The 150 ms / 2 s budget is my own default, not a confirmed target — worth confirming against the folder sizes and image weights this product actually expects.
4. **Success-measure number.** I wrote a qualitative measure with no analytics target attached. If the product already tracks engagement, a real number (e.g., "% of lightbox opens that use prev/next before closing") would replace the `[default]` tag.
5. **Tier axis.** I marked tier N/A on the assumption this product has no tiering concept anywhere else — confirm that's still true before this ships.
