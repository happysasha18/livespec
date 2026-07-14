# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-14 23:24 — four lanes pushed + CI green, Discussion field beat CLOSED; a MINOR release awaits Alexander's word; pack v1.4.2)
**PACK v1.4.2, PROVER v1.1.4.** Three lanes landed on origin this session, every push's CI green (`gh run`),
suite 724 green: (1) the cross-host duplicate coordinator (INV-149, M-291); (2) property routing between the
prover and the design review (INV-150 + INV-125/INV-126 sharpened, M-292/M-293/M-294) — each declared
cross-cutting law names its enforcing net, one of three kinds (a mechanical gate naming a real guardrail/test;
the prover's judgment station; or the design review's recommendation), verified at the INV-101 station, with a
net-floor test that reds on a netless law; the class trigger catches a kind-general rule homed on one member;
the paired-transition law grew its reversibility-of-means half (a blocking obligation, promoted from a soft
recommendation — named to Alexander as a bar-change, kept isolated so it can be softened), binding any
continuous-gesture opening; the inbox openable-faces wish is realized and harvested; four fresh-eyes findings
folded before push; (3) a monitor idempotency fix (M-295) that a LIVE round-trip exposed — the monitor
re-surfaced an item because GitHub bumps `updatedAt` past its own marker comments, now the activity generation
reads from non-marker comments on both channels. **The request-layer classifier (INV-151/152/153, M-296/297/298)
is PUSHED** (`bccfad3`, CI green) — suite 736 green: the door set is written CLOSED at build-pipeline's door
step with the entry-layer criterion + the one-plain-question fallback, the deferral-must-justify-itself clause
is base rulebook rule 29, and the unification is stated once (INV-153). Its mandatory fresh-eyes adversarial
pass ran and its one real finding was folded before push (the intake back-check test was vacuous — now
red-first on a phrase unique to the new wiring; design-reviewer added to the base-pin guard).

**A MINOR release awaits Alexander's word.** The session added five invariants of new capability
(INV-149 through INV-153), which is a MINOR bump by semver (1.4.2 → 1.5.0). The bump and its deep Fable
whole-spec + architecture audit are held for Alexander: he reserved the version/pin alignment for his own word
(row 231), and the deep Fable pass runs only on his word. Everything is landed, green, and CI-confirmed at
1.4.2; the release is one word away. Read this, then memory can be wiped — the whole story lives in JOURNAL +
the prover/design-review records.

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

## Queue / field beats
- **Discussion WRITE round-trip — CLOSED this session.** A live round-trip on the real repo exposed a real
  idempotency bug (the monitor re-surfaced a discussion because GitHub bumps `updatedAt` past its own marker
  comments), fixed and pushed (M-295, both channels; record
  `docs/prover/2026-07-14-monitor-idempotency-updatedat-skew.md`). A FRESH live round-trip after the fix then
  confirmed exactly-once end-to-end: run 1 deposited one inbox file plus its claim/confirm markers, run 2
  deposited nothing and added no comment. Test discussions created and deleted, tree clean, origin untouched.
- **Remote deposit field beat [INV-112]** — still owes its one real remote deposit run (needs a real remote
  seat push from another machine or a cloud session, not simulable from this local seat).

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
- Next free codes: INV-154, M-299 (INV-151/152/153 and M-296/297/298 consumed by the request-layer classifier
  lane, built locally this session; read the live Formal index before minting; codes consume in landing order).

## Memory
Once you have read this, memory can be wiped — JOURNAL + the prover records + ROADMAP carry the whole story.
