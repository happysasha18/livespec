# Bare run — test-author scenario (2026-07-10 rerun, model = sonnet worker, arm = bare)

No skill file read; zero tool uses.

Verbatim output:

---

# Test coverage — bug-lane scheduling feature

**Criterion 1 [T-9] — issue creates a marker at the correct time position on the ribbon**
- Test: render the widget with one synthetic detected issue at a known timestamp; query the DOM for the bug-lane marker; read its computed position (`getBoundingClientRect`/`left` or transform, not the source markup) and compare against the expected pixel position derived from the ribbon's known duration-to-width scale, within a small tolerance.
- HOW: browser-computed layout check — this criterion is a rendered-position fact, so string/DOM-text alone can't prove it.

**Criterion 2 [no anchor] — markers are visually distinct by severity**
- Test: render three issues of differing severities; assert each marker element carries a distinguishing class/attribute (e.g. `data-severity="high"`), and spot-check that the classes map to different computed colors.
- HOW: DOM-text/attribute check as the primary assertion (class name), with only a light computed-style check behind it. Proportionate to its unanchored status — real, but not pinned as tightly as the anchored criteria.

**Criterion 3 [no anchor] — clicking a marker opens/scrolls to its evidence panel**
- Test: render a marker tied to a known evidence panel; dispatch a real click event on it; assert the target panel's DOM state changes (visibility class toggles, or it receives focus/scroll).
- HOW: browser-computed interaction check — simulate the actual event and read the resulting DOM state, not just confirm a handler is attached.

**Criterion 4 [T-11] — markers never visually collide when issues are closely spaced**
- Test: place two synthetic issues inside the minimum-spacing window; render; read both markers' bounding rects; assert no horizontal overlap (or that the stacking/offset rule fired).
- HOW: pixel/bbox check via `getBoundingClientRect` — collision is inherently a rendered-geometry fact.

**Criterion 5 [T-18] — bug lane renders correctly empty when no issues exist**
- Test: render with zero issues; assert the bug-lane container exists in the DOM; assert it has zero marker children; assert no placeholder/error text leaks into it.
- HOW: DOM-structure check (existence + child count) — no rendering-precision needed since the claim is presence/absence, not position.

# Test coverage — run-page player feature

**Full run [INV-7] — full controls present, playhead synced across all charts**
- Test: render the full-run fixture (audio + stems); assert play/pause/seek/mute/solo controls exist and are enabled; advance playback time programmatically; read the playhead-linked position on every chart and assert they all move together.
- HOW: browser-computed, driven through an actual (simulated) playback advance — this is a cross-component invariant, not provable from static markup.

**Quick run — reduced controls, no per-stem mute/solo**
- Test: render the quick-run fixture (audio, no stem separation); assert per-stem mute/solo controls are absent or disabled; assert master play/seek controls are present.
- HOW: DOM-text/attribute check (element presence, `disabled` attribute).

**No-audio run — no player rendered at all**
- Test: render the no-audio fixture; assert zero matches for the player/playhead selector anywhere in the document; if the spec calls for a placeholder message, assert its exact text.
- HOW: DOM-structure check (absence), plus a plain string match only for the placeholder text if one is specified.

**Playhead on the time ribbon only [INV-9]**
- Test: render any run with audio; during simulated playback, query the whole document for all playhead-matching elements; assert the count is exactly 1; assert its ancestor chain terminates at the time-ribbon container and not any other chart's container.
- HOW: browser-computed structural check across a live playback window — needs to catch a stray duplicate playhead appearing dynamically, not just at initial render.

**Phone-width reachability**
- Test: set the browser viewport to a phone width; render; for each control (play/seek/mute/solo) read its bounding rect; assert each is fully inside the viewport (no clipping/overflow) and that no two controls' rects overlap.
- HOW: pixel/viewport-computed check — reachability is a physical/visual property, unprovable from markup alone.

# Overall testing approach

- Anchored criteria (T-9, T-11, T-18, INV-7, INV-9) get the heaviest assertion level available — computed position, bounding-rect, or count checks against a real render — since those are the facts the spec is pinned on.
- Unanchored criteria (bug-lane 2 and 3) still get real assertions, just lighter ones (class/attribute, click-triggered state change) — proportionate to their softer status, never skipped.
- Every test renders the actual offline HTML the Python script produces (or a fixture-driven equivalent) and inspects the real DOM/computed styles — no assertions against mocked markup standing in for the real artifact.
- Position- and collision-type claims (marker placement, marker spacing, phone-width control overlap) go through `getBoundingClientRect`/`getComputedStyle`, because the property being proven is a rendered-layout fact, not a source-text fact.
- Presence/absence claims (empty bug lane, missing stem controls in quick-run, missing player in no-audio run) use DOM existence/count checks — cheaper than pixel checks and sufficient for an is/isn't-there claim.
- The three run modes are each driven from their own fixture data, so the player's conditional rendering is tested against real mode-specific inputs rather than one fixture with toggled flags.
- Interaction-driven checks (click-to-evidence, playhead sync during playback) simulate the actual event or timeline advance and read the resulting DOM/state, rather than asserting a handler merely exists.
- Every test case traces back to its criterion by anchor code where one exists, and by criterion number where it doesn't, so a future spec edit points at exactly the tests that need review.
