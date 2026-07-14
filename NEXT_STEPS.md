# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-14 22:11 — property routing between the two reviews is DECLARED, four review findings folded; pack v1.4.2)
**PACK v1.4.2, PROVER v1.1.4.** Property routing between the prover and the design review is BUILT this
session (INV-150 + INV-125/INV-126 sharpened, M-292/M-293/M-294) — a local commit awaiting the
orchestrator's review and push; suite 721 green. Each declared cross-cutting law now names its enforcing
net, one of three kinds (a mechanical gate — a named guardrail script or test; the prover's judgment station;
or the design review's recommendation), verified at the INV-101 station; the pack's three laws are mechanical
gates naming their real guardrails/tests. The cross-surface trigger catches a kind-general rule homed on one
member; the paired-transition law grew its reversibility-of-means half (a blocking obligation, promoted from a
soft recommendation — named to Alexander as a bar-change, kept isolated so it can be softened), now binding
any continuous-gesture opening (the "over everything" narrowing removed). A net-floor test reds if any
declared law names no net. This realizes and harvests the inbox openable-faces wish. A THIRD local commit
(this worker) fixes a monitor idempotency bug a live round-trip exposed (M-295): the monitor re-surfaced an
item because GitHub bumps `updatedAt` past its own marker comments — now the activity generation is read from
non-marker comments, both channels, suite 724 green. Three local
commits now await the orchestrator (this one, the cross-host coordinator INV-149 M-291, and the M-295 fix). The
request-layer classifier the same audit covers is a SEPARATE lane the orchestrator builds next. Field beats
below are unchanged, each genuinely blocked on Alexander or a real external event. Read this, then memory
can be wiped — the whole story lives in JOURNAL + the prover/design-review records.

## What landed this session
0. **Property routing between the two reviews (INV-150, INV-125/INV-126, M-292/M-293/M-294).** Each declared
   cross-cutting law names its net; the class trigger fires on a kind-general rule homed on one member; the
   paired-transition law reads as two halves (continuity + reversibility of means). Records:
   `docs/prover/2026-07-14-property-routing.md`, `docs/design-review/2026-07-14-property-routing.md`. Inbox
   openable-faces wish harvested. One must-fix folded (the watch-level net's dated reason), one recommendation
   queued (whether INV-150 states the presence-versus-rightness split explicitly or by reference). Four review
   findings folded in a later worker pass: the means-half "over everything" narrowing removed; the net
   vocabulary given three kinds (mechanical gate / prover station / design review) with the pack's three laws
   named as mechanical gates; the orphan `test_cross_sibling_routing_split` cited in M-292; a net-floor test
   (`test_pack_declared_laws_each_name_a_net`) added, red-first proven.
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
- **Field beat [INV-94]** — the live Discussion WRITE round-trip was RUN (a real discussion bridged
  end-to-end, then a second run) and it EXPOSED a real idempotency bug: the monitor re-surfaced the same
  discussion into a second inbox file because GitHub bumps `updatedAt` strictly past the monitor's own marker
  comments. Fixed this session (M-295): the activity generation is read from non-marker comments, both
  channels; suite 724 green; record `docs/prover/2026-07-14-monitor-idempotency-updatedat-skew.md`. A local
  commit awaiting the orchestrator's review + push. A fresh live round-trip on the real repo (Discussion or
  Issue) to re-confirm exactly-once end-to-end still waits on a real stranger's item or the owner's hand.
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
- Next free codes: INV-151, M-296 (M-295 landed this session for the monitor idempotency fix; read the live
  Formal index before minting; codes consume in landing order).

## Memory
Once you have read this, memory can be wiped — JOURNAL + the prover records + ROADMAP carry the whole story.
