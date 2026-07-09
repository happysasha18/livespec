# With-skill run — test-author scenario (2026-07-10 rerun, model = sonnet worker, arm = with-skill, test-author 0.1.2)

Read skills/test-author/SKILL.md directly (Read tool, not the Skill tool); 1 tool use.

Verbatim output:

---

I read the file directly (not via the Skill tool) at `/Users/sashaabramovich/live-spec/skills/test-author/SKILL.md`. Below is the derivation, following its method: state-space named before cells, both sides per row, level pinned by what breaks visibly, matrix-local rows for anchor-less criteria citing their parent, geometry facts widened per INV-78, ladder capped at the real device per INV-77, and the closing approach bullets.

One explicit assumption, flagged rather than guessed silently: the player feature lists three behavior clauses against two anchors (INV-7, INV-9) without naming which clause is unanchored (unlike the bug-lane section, which named criteria 2–3 directly). I assigned INV-7 to the full/quick/no-audio behavior and INV-9 to playhead-on-ribbon, and treated phone-width reachability as the deliberately-unanchored one, parented to INV-9 since it's the same transport control's contract.

## State space (named before cells)

**Bug-lane scheduling** — axes: overlap-depth data state (0 / 1 / 2-concurrent / 3+-stress / simultaneous-start tie) × run-type view state (full / quick / no-audio, for the comparison-consistency criterion).

**Run-page player** — axes: run-type data state (full / quick / no-audio) × viewport view state (desktop / phone width) × playback view state (paused-at-0 / mid-playback / at-end).

## Test cases — bug-lane scheduling

| Row | Anchor | Cell | Does / Never | Level | HOW it asserts |
|---|---|---|---|---|---|
| BL-1 | T-9 | 2 concurrent bugs, same lane | Does: rendered on separate sub-rows. Never: overlapping bounding boxes. | browser-computed | Render in a real browser engine, read both bug elements' `getBoundingClientRect()`, assert their vertical ranges don't intersect. |
| BL-2 | no anchor (parent T-9, tie-break mechanic) | 2 bugs, identical start timestamp | Does: deterministic stack, shorter above. Never: same row, or order varying across identical re-renders. | browser-computed | Render the same fixture twice, read each bug's rect both times, assert shorter-above and identical ordering across both renders. |
| BL-3 | no anchor (parent T-9, layout-growth mechanic) | 4+ concurrent bugs (stress) | Does: lane grows to fit max depth. Never: any bug rect clipped by the lane container. | browser-computed | Render the stress fixture, read the container's computed rect and every bug rect, assert every bug rect lies fully inside the container's. |
| BL-4 | T-11 | lane with 0 bugs | Does: lane omitted/collapsed. Never: empty lane rendered occupying visual space. | browser-computed | Render bug-free vs. bugs-present fixtures side by side, read the empty lane's computed bounding box, assert zero rendered height/no layout — not just empty `innerHTML`. |
| BL-5 | T-18 | same bug data across full/quick/no-audio | Does: same row assignment across all three. Never: row order reassigned between run-type variants for identical data. | browser-computed | Render all three run-type fixtures from one shared dataset, read each bug's row index by y-position in each render, assert identical ordering across all three. |

## Test cases — run-page player

| Row | Anchor | Cell | Does / Never | Level | HOW it asserts |
|---|---|---|---|---|---|
| PL-1 | INV-7 | full run | Does: working player, scrubbing enabled. Never: dead play control while audio is present. | browser-computed | Render the full-run fixture, assert play control is not `[disabled]`, invoke play, assert `currentTime` advances after a tick. |
| PL-2 | INV-7 | quick run | Does: audio-only player, no stem controls (no stem data). Never: stem-mute control with nothing behind it. | DOM-text for stem-control absence (a presence fact); browser-computed for the play control's enabled state | Render the quick-run fixture, assert no stem-mute element exists in the document; separately re-run PL-1's computed-enabled check. |
| PL-3 | INV-7 | no-audio run | Does: no player / disabled transport. Never: a play button that does nothing when clicked. | browser-computed | Render the no-audio fixture, assert either no play element exists or it's `[disabled]`; if clicked anyway, assert no `currentTime` advance and no playing-state flip. |
| PL-4 | INV-9 | mid-playback, desktop width | Does: playhead tracks `currentTime` on the ribbon. Never: a playhead duplicated on any other chart/panel. | browser-computed | Start playback, sample `currentTime`, read the ribbon playhead's computed x-position and assert it matches `currentTime/duration` within tolerance; query every other panel for a playhead element and assert zero matches. |
| PL-5 | INV-9, geometry per INV-78 | playhead position at 2 viewport widths, after N sequential seeks | Does: position stays correct relative to the ribbon's own bounds at both sizes and after repeats (no drift). Never: an absolute-pixel computation that only matches one viewport/one step. | browser-computed | At each of two viewport widths, perform N seeks; after each, read playhead and ribbon rects, assert `(playhead.center − ribbon.left)/ribbon.width` stays within ε of `currentTime/duration` at every step. |
| PL-6 | no anchor (parent INV-9, reachability mechanic) | phone-width viewport, transport controls | Does: every control's tap target sits fully in-viewport and unoccluded. Never: a control partly/fully off-screen or covered at phone width. | browser-computed (static reachability only — see bullet below) | Render at a pinned phone width, read each control's rect, assert it's inside `[0, viewportWidth] × [0, viewportHeight]`, and assert `elementFromPoint()` at its center returns the control itself. |

## Overall testing approach

- Axes were named before any cell was filled — overlap-depth/tie/run-type for the bug lane, run-type/viewport/playback-state for the player — so the empty-lane state and the quick-run-has-no-stems state each got their own row instead of hiding inside a flat element-by-view grid.
- Levels are pinned by what a user would see break: overlap, visibility, position, and reachability facts sit at browser-computed (BL-1 through BL-5, PL-1, PL-3 through PL-6); a pure element-presence fact (PL-2's stem panel) is legally DOM-text; nothing here is a string-level wiring fact.
- The three anchor-less rows (BL-2, BL-3, PL-6) are matrix-local, citing their parent anchor rather than being flagged missing — they're node-level mechanics (a tie-break rule, a growth rule, a reachability contract on an already-anchored control), which the method names as the legal case for "matrix id absent from the spec." A criterion with no anchor and no such parent relationship would instead be a genuine derivation defect, routed back to spec-author before the row is written.
- Every row states both sides: BL-4's never-side (no empty-shell lane) and PL-3's never-side (no dead play button) are exactly the regression fence the ladder exists for — a happy-path-only row for either is fixed here, before a user could find it.
- PL-5 is written relative, at two viewport widths, over N repeated steps (SPEC INV-78) because the playhead is a positioning fact — a one-viewport, one-step, absolute-pixel check would stay green while drifting further off on every next seek.
- PL-6 stops at browser-computed because static layout reachability is checkable headless; if "phone-width reachability" turns out to mean touch-gesture reachability rather than layout, that slice moves to a real-device walk row per INV-77 rather than being faked in a headless browser.
- Every new row is proven red against the current build before its fix lands, and the skip-set is pinned exactly (e.g., no-audio run legitimately skips the `currentTime`-advance check in PL-3 — that skip is expected, not silent); traceability then stands as its own enforced test, failing the suite on any row citing a missing test, duplicate id, or an anchor with zero rows against it.
