# Incident wish — one project's test-Chrome cleanup kills another project's live run

- **From:** track-coach window, 2026-07-15 ~21:50
- **Kind:** wish / incident (a cleanup-scoping rule the pack should state and enforce)
- **Severity:** medium-high — it reaches into a SEPARATE live session's work and can silently red or abort its run

## What happened

While verifying track-coach, the agent cleared what looked like orphan test browsers with a path-scoped
kill: `pkill -9 -f '.cache/puppeteer/chrome'`. At that moment a DIFFERENT session (tlvphotos, working in
`~/exhibition-engine`) was running its own test suite, driving its own headless Chrome. Both projects launch
Chrome for Testing from the SAME install path, `~/.cache/puppeteer/chrome/...`, so the path-scoped pattern
matched the other project's LIVE browsers too and knocked them out mid-run. A hung `run_all.py` cleared in the
same pass may also have belonged to that session. The tlvphotos run recovered on its own, but the cleanup had
reached across the window boundary into another project's active work.

## Why the existing laws did not prevent it

- This is the exact blind spot LEFT OPEN by the sibling wish
  `2026-07-15-from-tlvphotos-test-cleanup-killed-users-real-chrome.md`. That wish's fix — "kill only by the
  test-browser install path `~/.cache/puppeteer/...` instead of a bare `chrome` pattern" — protects the human's
  REAL browser, and it is correct for that. It does NOT protect a second PROJECT: every project's test Chrome
  lives under that same shared install path, so path-scoping still hits all of them at once.
- Nothing states that a cleanup must be scoped to the OWNING RUN, so a discriminator good enough to spare the
  user's browser (install path) is still too broad to spare a sibling project's live run.
- One host, several concurrent sessions (each its own window/project) is a normal state here, and the pack has
  no rule keeping one window's teardown inside its own project's boundary.

## Suggested rule for the pack to state (owner decides)

- **Test-Chrome cleanup is scoped to the run that owns it, not to the shared install path.** The only safe kill
  target is the harness's own recorded PID / process group (the row-327 process-group reap, already the right
  mechanism). When a manual sweep of strays is unavoidable, resolve each candidate browser's owning project by
  its parent process's working directory (`lsof -a -p <pid> -d cwd`) and kill only those under THIS window's
  project tree.
- **Age is the liveness signal.** A browser whose age is ~0s belongs to an ACTIVE run and is never a stray; a
  process at 0% CPU with no disk writes for many minutes is genuinely hung and safe to clear. Any stray-sweep
  states this test so it cannot abort a healthy neighbour.
- **Cross-window boundary is explicit in the cleanup rule.** Fold this into the same harness-safety line as the
  real-browser wish (INV-157/158 family) and the worker-briefing guidance: a session's teardown never reaps a
  process it does not own, and "own" is decided by process group or project cwd, never by the shared
  `~/.cache/puppeteer` path. The two wishes together give the full discriminator — the install path spares the
  human's browser, the process-group / cwd scope spares a sibling project's run.

The track-coach side is fixing itself now (path-plus-cwd scoping adopted, a memory written so it never
recurs). This wish is the pack-level rule the owner may want to fold so no host repeats it across windows.
