# Incident wish — a pattern-based Chrome kill in one window reaches another window's browsers

- **From:** track-coach window, 2026-07-15 ~21:50 (premise corrected ~22:05)
- **Kind:** wish / incident (a cleanup-scoping rule the pack should state and enforce)
- **Severity:** medium-high — it reaches into a SEPARATE live session's work and can silently red or abort its run

## What happened

While verifying track-coach, the agent cleared what looked like orphan test browsers with a pattern kill:
`pkill -9 -f '.cache/puppeteer/chrome'`. At that moment a DIFFERENT session (tlvphotos, working in
`~/exhibition-engine`) was running its own test suite, driving its own headless Chrome from exactly that
puppeteer path. The pattern matched tlvphotos's LIVE browsers and knocked them out mid-run. A hung
`run_all.py` cleared in the same pass may also have belonged to that session. The tlvphotos run recovered on
its own, but a cleanup typed in the track-coach window had reached across the boundary into another window's
active work.

## The real mechanism (first draft of this wish got it wrong)

The two projects do NOT share a Chrome binary, so this is not a shared-install-path problem:

- **track-coach** drives the SYSTEM Chrome — `/Applications/Google Chrome.app/.../Google Chrome` with
  `--headless=new`. It never uses puppeteer.
- **tlvphotos** drives Chrome for Testing from `~/.cache/puppeteer/chrome/...`.

The actual fault is that a **process-name / path pattern kill is not tied to the run that owns the process**.
Such a pattern matches by what the binary IS, so from any window it can reach any other window's browsers, and
— because track-coach's headless binary is the very same `Google Chrome.app` as the human's real browser — a
broad `pkill "Google Chrome"` from the track-coach window would also close the human's own Chrome (the sibling
wish `2026-07-15-from-tlvphotos-test-cleanup-killed-users-real-chrome.md`). One host running several sessions,
each its own window/project, is a normal state here, and nothing keeps a window's teardown inside its own run.

## Why the existing laws did not prevent it

- Row 327 / INV-157 already says the harness reaps its Chrome by PROCESS GROUP — the correct, run-scoped
  mechanism. But a manual sweep of strays typed AROUND a flaky or hung run has no stated scoping rule, so it
  defaulted to a name/path pattern, which is scoped to the binary and not to the run.
- The sibling wish's fix (kill by the puppeteer install path, not a bare `chrome`) protects the human's real
  browser for a puppeteer-based project. It does not help here: it is still a pattern, so it still reaches
  every OTHER run that uses that same path.

## Suggested rule for the pack to state (owner decides)

- **Test-Chrome cleanup is scoped to the run that owns it — its own PID / process group — never a
  process-name or install-path pattern.** The row-327 process-group reap is already the right mechanism;
  state that a manual sweep uses it too. To make even a hung or hard-killed run reap cleanly, launch the
  browser in its OWN process group (`start_new_session=True`) so `killpg(pgid, …)` targets only that run's
  tree.
- **When a manual sweep of a genuinely orphaned browser is unavoidable, resolve each candidate's owning
  project by its parent process's working directory (`lsof -a -p <pid> -d cwd`) and act only on those under
  THIS window's project tree.** Age is the liveness signal: a browser aged ~0s belongs to an ACTIVE run and is
  never a stray; a process at 0% CPU with no disk writes for many minutes is genuinely hung.
- **State the cross-window boundary explicitly** in the harness-safety line (INV-157/158 family) and in the
  worker-briefing guidance: a session's teardown never reaps a process it does not own, and "own" is decided
  by process group or project cwd, never by what the binary is named or where it is installed.

The track-coach side is fixing itself now: its harness (`scripts/headless_check.py`) already reaps its own
Chrome by process handle and uses no broad pkill; this movement adds `start_new_session` + a `killpg` group
sweep so a forced teardown leaves no orphan and never needs a pattern kill. This wish is the pack-level rule
the owner may want to fold so no host repeats it across windows.
