# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-16 ~23:08 — v2.3.0 ready to push)
Rows 361–364 built, accepted, MINOR gate run whole (prover + design review + fresh adversarial
audit, all records with same-day addenda). The 21:47 session died on server 529s mid-audit-fold; the
resumed session verified all four audit folds complete in the tree (findings 1/4/5/6 — socket.timeout
kinship on Py<3.10, probe-failure browser reap, fallback-leg bound, deleted-test-file false red —
each red-proven), wrote the audit record (docs/audit/2026-07-16-2.3.0.md), queued finding 2 as row
366, amended the JOURNAL chapter. Full suite 961 green in 106.9 s, budget watcher green, freeze
green. REMAINS: commits by lane (363 skills / 364 template / 361+362 guardrails / docs+version),
push, CI verdict, mirror walk. Then row 365, row 366.

## PRIOR STATE (2026-07-16 ~18:17 — v2.2.0 SHIPPED)
Rows 359 + 360 landed, pushed 26fc256, mirror synced and walked live. Story in JOURNAL.md.

## ON RESUME — the queue
- **Row 365 — every stated quality budget owes a watcher** (the 2.3.0 design review, finding 2):
  INV-41 grows the watcher duty, the architecture template's budget table gains the column, the
  prover's architecture lens asks for it; red-proven.
- **Row 366 — the scoped reach road vs enumerating tests** (the 2.3.0 audit, finding 2): either a
  suite-hygiene net (an enumerating test over an infra dir reds unless pinned into the scoped set)
  or a decided spec sentence stating the by-name limit of INV-40's scoped claim.
- **Adoption follow-through (his windows):** tlvphotos — ratchet wired and live (checked 15:07).
  promoter — manifest present, `guardrails/pre-push` absent: the wiring step is unfinished there
  (its own window's work). track-coach — adopted with a local hand-fix matching the pack's row-358
  fix; after the 2.3.0 push its update watcher will propose the re-install roads.
- After the 2.3.0 push, hosts that adopted at 2.x see the update watcher name the stale vendored
  files (headless_harness.py among them — the frame-death fix reaches them through the update);
  each window re-installs on its own word.

## Standing word / OWNER-HELD
- Do the whole movement solo, push on green; plain English in docs, plain Russian in chat. Gates
  mandatory everywhere.
- CONCURRENCY: multiple windows share ~/live-spec. Commit narrowly by explicit path, never `git add -A`;
  re-check HEAD before writing (fence). A co-located deposit is the FILE ALONE — no staging, no commit
  (INV-174); the commit-time fence also stops a staged file carrying unstaged edits (INV-175).
- Next free codes: INV-182, M-347 (M-341..M-346 spent), next ROADMAP row 367. Memory can be wiped once
  pushed — story in JOURNAL.md (the v2.3.0 chapter) + the 2026-07-16 prover/design-review records with
  addenda.
