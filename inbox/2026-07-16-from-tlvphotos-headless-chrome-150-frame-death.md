# The harness template's browser can go frame-dead: prefer chrome-headless-shell

From: the tlvphotos window, 2026-07-16
Kind: wish (test-infrastructure hardening)
Priority: medium-high — a whole machine's browser gates silently rot into false reds

## What happened

Chrome for Testing 150.0.7871.124 in `--headless=new` stopped producing compositor frames on this
Mac — `requestAnimationFrame` never fires, machine-wide, in every fresh launch. The page reports
`visibilityState: visible`; forcing damage, `Page.startScreencast`, device-metrics overrides, and the
anti-throttling flag trio all fail to revive frame production. The failure was intermittent in the
morning (the 08:08 gate ran 38/38 green on the same binary) and total by midday. Every test row that
waits on a rAF-gated paint (a `.show` class, a transition restore) reds falsely; rows reading
synchronous state stay green — a confusing half-red suite.

Chrome for Testing 151.0.7922.34 renders frames, but stalls loading any page from `127.0.0.1`
(`Page.navigate` never completes; `data:` URLs load fine) — a different fault, same outcome.

`chrome-headless-shell` 151 (the dedicated headless build) shows neither fault: frames from launch,
local pages load, both project gates green on it (tlvphotos 38/38, exhibition-engine 31/31).

## The wish

The pack's canonical harness (`templates/headless_harness.py`) resolves and launches a full Chrome
for Testing with `--headless=new`. Two hardening steps, in order of value:

1. **Prefer `chrome-headless-shell`** in the binary resolution
   (`~/.cache/puppeteer/chrome-headless-shell/*/chrome-headless-shell-mac*/chrome-headless-shell`,
   newest first), falling back to Chrome for Testing, then a system Chrome — and drop
   `--headless=new` when the shell is the pick (it is headless by construction). Install command:
   `npx @puppeteer/browsers install chrome-headless-shell@stable --path ~/.cache/puppeteer`.
2. **A launch-time frame probe** as a named guardrail: before trusting any suite, one throwaway page
   awaits a single rAF with a ~2s bound; a browser that cannot produce one frame fails LOUDLY with
   its own name ("the browser produces no frames — not a product red") instead of bleeding false
   reds through the suite.

The three hand-rolled harness copies on this machine (tlvphotos + exhibition-engine tests + the
engine's shipped harness) already carry fix 1; this note carries the find upstream so the template
and its consumers get it once, properly.
