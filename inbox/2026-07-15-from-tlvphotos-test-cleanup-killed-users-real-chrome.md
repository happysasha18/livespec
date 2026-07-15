# Incident wish — test-Chrome cleanup killed the USER'S real browser

- **From:** tlvphotos window, 2026-07-15 ~20:36
- **Kind:** wish / incident (a safety rule the pack should state and enforce)
- **Severity:** high — it reaches OUTSIDE the workshop and disrupts the human's own running work

## What happened

While clearing stray test browsers between flaky gate runs, the agent (and some workers it briefed) killed
Chrome with over-broad patterns: `pkill -9 -f "chrome_crashpad_handler"`, and worker-side `pkill -9 chrome` /
"pkill Chrome before each run". Those patterns match the USER'S real Google Chrome — `chrome_crashpad_handler`
is a process the user's own Chrome runs, and `chrome` matches "Google Chrome" too. The user's browser closed
mid-session. He noticed and asked "are you closing my Chrome after tests, or am I imagining it?" — he was not
imagining it.

This is a sibling of the same-day `$TMPDIR` 78GB leak wish
(`2026-07-15-from-tlvphotos-tmpdir-leak-despite-hygiene-laws.md`): both are the test harness's cleanup
reaching where it must not. Killing the real browser is worse — it destroys the human's own work state, an
effect OUTSIDE git and outside the workshop, exactly the class rule 17 (irreversible outward effects) and the
row-222 hygiene law ("a suite leaves the machine as it found it") mean to forbid.

## Why the existing laws did not prevent it

- Row 327 / INV-157 states the harness reaps its Chrome by PROCESS GROUP (the correct, targeted mechanism).
  But the manual/worker cleanup done AROUND a flaky run — the pkills a human or worker types when strays
  linger — has no stated safety rule, so it defaulted to broad name patterns.
- No rule says: a cleanup pattern must uniquely identify the TEST browser and can never match the user's own
  browser. The safe discriminator exists (Chrome for Testing installs under `~/.cache/puppeteer/...`, and the
  harness launches it with an isolated `--user-data-dir`), but nothing names it as the ONLY legal target.

## Suggested rule for the pack to state (owner decides)

- **A test harness and anyone cleaning up after it NEVER kill by a pattern that can match the human's real
  browser.** Forbidden patterns: bare `chrome`, `Chrome`, `Google Chrome`, `chrome_crashpad_handler`, bare
  `puppeteer`. The ONLY legal kill targets the test browser uniquely — its install path
  (`~/.cache/puppeteer/...`) or, better, the harness's own recorded PID / process group.
- **Prefer no manual kill at all:** if the harness reaps its own process group on teardown AND sweeps its own
  install-path strays on launch (the row-327 mechanism, extended to cover a killed/timed-out run), no human or
  worker ever needs a `pkill`, so the footgun disappears. Make that the stated path; a manual pkill is the
  fallback and, when used, is path-scoped only.
- **State it as a safety line in the harness rule (INV-157/158 family)** and in the worker-briefing guidance,
  so a briefed worker inherits the constraint rather than reinventing a broad `pkill chrome`.

The tlvphotos side is fixing itself now (agent adopting the path-scoped kill, a memory written so it never
recurs); this wish is the pack-level rule the owner may want to fold so no host repeats it.
