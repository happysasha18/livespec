# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-14 21:05 — the stranger door is OPEN, WATCHED, and cross-host safe; pack v1.4.2)
**PACK v1.4.2, PROVER v1.1.4.** The cross-host duplicate coordinator (INV-149, M-291) is BUILT this
session — a local commit awaiting the orchestrator's review and push; suite 710 green. (Version held at
1.4.2 like its sibling stranger-door landings; the PATCH bump is the orchestrator's coarser-cadence call.) Two hosts' monitors
on one repo now converge on a single surfacing by a claim on the shared source item, so one wish reaches
the shared inbox exactly once, never lost (INV-1), the door never blinded if a host dies. What remains is
the same three field beats, each genuinely blocked on Alexander or on a real external event. Read this,
then memory can be wiped — the whole story lives in JOURNAL + the prover records.

## What landed this session
1. **The monitor's schedule — the door is now live (INV-148).** A scheduled GitHub Action
   (`.github/workflows/stranger-monitor.yml`) runs the monitor daily (and on manual dispatch), commits any
   bridged inbox file, and pushes it as github-actions[bot]; single-instance by `concurrency`. This is the act
   that truly opened the door [INV-147]. **Verified by deed:** a real dispatched run went green end-to-end
   (every step, clean no-op). The independent audit [INV-46] caught a must-fix the author's tests could not —
   the monitor re-triggered on its OWN marker comment (daily-cron spam); folded (record the marker's post-comment
   createdAt) plus a Discussions-disabled resilience fold. Record: `docs/prover/2026-07-14-monitor-schedule.md`.
2. **A false-green gate hole closed (M-154).** The local push gate ran `unittest discover`, which cannot collect
   the pytest-style tests — it false-greened while CI's pytest caught a red. `check-tests.sh` now runs pytest
   (the same runner as CI), swept the misleading runner docstrings, and pinned both nets to one runner with a
   guard test.
3. **M-212 blind spot closed.** Two malformed-backtick matrix cells desynced `gate_common.scrub`; reworded to
   balance, plus a guard test that reds on any odd inline-backtick line in the spec or matrix.

## Queue / field beats (none blocking, none autonomously closable)
- **Field beat [INV-94]** — the live Discussion WRITE round-trip (a real discussion bridged end-to-end, then a
  second run proven idempotent). Waits on a real stranger's Discussion or the owner's hand: the auto-mode
  classifier rightly declined the agent creating a test discussion under Alexander's identity. The Discussion
  READ path is verified by deed; the scheduled monitor now exercises both fetch paths on every run.
- **Row 261's remote deposit field beat [INV-112]** — still owes its one real remote deposit run, unchanged
  (needs a real remote seat push, not simulable here).

## OWNER-HELD
- **Memory can be wiped** — every push's CI is confirmed green; the whole story is in JOURNAL + prover records.

## Standing habits (always-on)
- When a method skill changes, run a fresh-eyes adversarial pass (INV-46); a MILESTONE earns the deep Fable
  whole-spec + architecture pass; a full audit runs on a landing-count cadence (INV-145). `date` before any
  stamp. Shipped docs stay impersonal (INV-118/120), provenance in docs/lenses.md + JOURNAL, never inline
  (R15/INV-83). The seat decides and acts on derivable work and reports (INV-143); the spec is the definition
  of correct (INV-144). Delegation by base rule 5 → INV-69; a worker whose write-set overlaps the senior's own
  in-flight edits gets an isolated worktree or is serialized.
- No self-certification (INV-94) · plain words, codes trail (INV-28) · say-what-it-is, no contrast frames ·
  inbox swept first · one lane one commit · a delegated run's verdict is the suite log's tail (INV-80) · the
  local push gate and CI run the same test runner (pytest), never a weaker local net (M-154).
- Next free codes: INV-150, M-292 (read the live Formal index before minting; codes consume in landing order).

## Memory
Once you have read this, memory can be wiped — JOURNAL + the prover records + ROADMAP carry the whole story.
