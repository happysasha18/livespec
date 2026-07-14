# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-14 — the stranger door landed + pushed; pack v1.4.1)
**PACK v1.4.1, PROVER v1.1.4.** The stranger door (rows 261 + 315) is COMMITTED (`4278681`) and PUSHED to
origin/main; local == origin. Suite 692 green, all local gates green. The remote CI run (`gates`, push
`4278681`) was in flight at hand-off — **on resume, confirm it went green** (`gh run list --limit 1`); a red
verdict is this session's own immediate bug to fix before anything else (INV-106). Read this, then memory can
be wiped — the whole story lives in JOURNAL + ROADMAP (rows 261/315) + `docs/prover/2026-07-14-stranger-door.md`.

## What landed
A stranger (a contributor with no push rights and no per-repo grant — a private-repo read-only collaborator
or anyone on a public repo) opens a templated GitHub Issue or Discussion requesting a source; the monitor
`scripts/stranger-wish-monitor.py` bridges each open un-surfaced item into ONE committed inbox/ file and
records the item's update generation on a marker comment, so from that file on it is an ordinary inbox wish
under the git-atomic harvest already proven safe [T-10, INV-11]. INV-146 (the door) + INV-147 (the monitor),
both channels served (Issue over `gh issue`, Discussion over GraphQL). Two independent adversarial passes
(INV-46) folded 9+ holes incl. two must-fix. Row 315 rode along: 17/18 TEST_MATRIX provenance cells swept to
docs/lenses.md, the gate widened to cover the matrix.

## ⟨FIRST ON RESUME⟩ — the door is open but unwatched
The Issue/Discussion templates are live in the repo, so a stranger can open a wish NOW — but no schedule runs
the monitor yet, and the spec requires a schedule where the door is open [INV-147]. **Set the monitor's
schedule** (this is the act that truly "opens" the door). Recommended shape: a GitHub Action (`.github/workflows/`)
on a cron (e.g. daily) that runs `python3 scripts/stranger-wish-monitor.py` with `contents:write`, `issues:write`,
`discussions:write` permissions — build it through the pipeline (it is a new autonomous writer to main, so it
owes its own prove: two overlapping scheduled runs, what token it commits under). Until it is set, the
maintainer runs the monitor by hand (`python3 scripts/stranger-wish-monitor.py` — verified a clean no-op today).

## Queue / field beats (none blocking)
- **Field beat [INV-94]** — the live Discussion WRITE round-trip (a real discussion bridged end-to-end, then
  a second run proven idempotent). Waits on a real stranger's Discussion or the owner's hand: the auto-mode
  classifier rightly declined the agent creating a test discussion under Alexander's identity. The Discussion
  READ path is verified by deed.
- **Cross-host duplicate** — INV-147 states the bound: the single-instance lock holds within one host; two
  hosts' monitors on one repo can surface one wish twice (a duplicate the maintainers drop, never a wish lost
  [INV-1]). The cross-host coordinator is a named later stage, not built.
- **M-212 markdown glitch** (found by row 315's sweep) — an escaped backtick inside a code span in one
  TEST_MATRIX cell desyncs `gate_common.scrub`'s backtick pairing, a latent lint blind spot; left untouched,
  its own small row's worth.
- **Row 261's old remote deposit field beat** (INV-112) still owes its one real remote run, unchanged.

## OWNER-HELD
- **Memory can be wiped** once CI is confirmed green.
- `~/.claude/CLAUDE.md` "seven→eight working skills" — DONE this session (Alexander's word: fix obvious things,
  don't ask).

## Standing habits (always-on)
- When a method skill changes, run a fresh-eyes adversarial pass (INV-46); a MILESTONE earns the deep Fable
  whole-spec + architecture pass; a full audit runs on a landing-count cadence (INV-145). `date` before any
  stamp. Shipped docs stay impersonal (INV-118/120), provenance in docs/lenses.md + JOURNAL, never inline
  (R15/INV-83). The seat decides and acts on derivable work and reports (INV-143); the spec is the definition
  of correct (INV-144). Delegation by base rule 5 → INV-69; before spawning a worker whose write-set overlaps
  the senior's own in-flight edits, give it an isolated worktree or serialize (the row-261/315 fence slip).
- No self-certification (INV-94) · plain words, codes trail (INV-28) · say-what-it-is, no contrast frames ·
  inbox swept first · one lane one commit · a delegated run's verdict is the suite log's tail (INV-80).
- Next free codes: INV-148, M-290 (read the live Formal index before minting; codes consume in landing order).

## Memory
Once CI confirms green, memory can be wiped — the whole story lives in JOURNAL + ROADMAP + the prover record.
