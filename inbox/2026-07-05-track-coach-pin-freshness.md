# Wish: file:line pins need a freshness mechanism (pin-by-symbol, or a drift guardrail)

## The wish (plain words)
ARCHITECTURE.md's `file:line` pins (ADOPT Phase 5 / E-14) go stale on EVERY commit that inserts lines
above a pin in the pinned file — silently. The method prescribes the pins but no mechanism keeps them
honest. Two remedies, either or both:

- **Pin by symbol, line as cache:** the normative pin is the named thing (`_web_panel_html`, a
  `PLAYER_LOGIC_START` marker comment, a CSS selector), and the `:line` is a convenience that may lag.
  A reader resolves the symbol; a checker can too.
- **A drift guardrail (mechanical!):** a small check that, for each pin, greps the named symbol at/near
  the pinned line and reports drifted/broken pins. It slots straight into the pre-push gate family —
  this is exactly the kind of check a cheap worker or 20-line script does perfectly.

## Why (what broke / what was missing)
track-coach's ARCHITECTURE.md pins were verified in its s56 audit; ONE working session later (s57, a
~25-line cosmetic change to build_widget.py), **7 of 17 pins had drifted** (up to +20 lines). Nothing
flagged it — a worker re-verify ordered by hand caught it during the adoption pass (2026-07-05). Any
host that pins and then keeps coding will rot the same way; a drifted pin is worse than no pin because
it asserts a wrong location with confidence.

## Who threw it
The track-coach session, live-spec adoption pass, 2026-07-05 (Alexander's "сделай все по лайвспеку" run).
