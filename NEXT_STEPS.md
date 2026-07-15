# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-15 09:30 — 1.6.0 SHIPPED, pushed, CI green; two reviews as one bounded loop + design review shipped alongside the prover + a flaky-test-is-a-defect law; pack v1.6.0)
**PACK v1.6.0** (1.5.0 at commit `bee657c`, CI green; 1.6.0 adds INV-155, suite 742). Three things landed
this session, all from Alexander's words, each proven by an independent adversarial pass that caught a real
design error before it shipped:

- **INV-154 — the two reviews as one bounded loop.** The prover and the design review settle to a fixed
  point. A round advances only on a human-accepted declaration; it rests in one of three named states —
  CONVERGES, WAITS, or STANDS DOWN (a kind with no element a person acts on) — capped at three progressing
  rounds; on the cap it stops and surfaces the unsettled groupings without holding a landing.
- **Design review shipped alongside the prover.** design-reviewer gained its own README + LICENSE;
  product-prover's README presents it as the younger sibling; a completeness guard locks both (M-300).
- **INV-155 — a flaky owned test is a defect fixed at its root.** Green means deterministic. A flake is
  routed by one question — is the nondeterminism removable in code the project owns? If yes it is a defect
  fixed at that root, masked by nothing (no retry, rerun-until-green, raised timeout, or "it passed this
  time"); if the external tool misbehaves at random it is workshop noise [INV-23]. A mechanical guardrail
  bans a retry/rerun plugin; the rest is the verify walk's discipline. (Alexander's "дерех а мелех" — the
  root/infrastructure fix first.)

Release mechanics of note: a version-home test that hard-pinned the previous release's literals was
rewritten to derive agreement from the VERSION file (root fix of a per-release hand-edit trap).

## Queue (ROADMAP)
- **321** feedback-collector sub-skill — on strong user emotion, OFFER (consent first) to send a distilled
  digest upstream; inbox destination, per-machine opt-out, distinct from feedback-intake. Open design Qs at
  build (Alexander 2026-07-15, "как дойдём добавим").
- **322** the forward-binding law is cited to two roots — unify to one.
- **323** declare the review-record class once (prover / design-review / skill-creator / verify records).
- **324** build-pipeline SKILL.md is 593 lines, over the 500 ideal — offload set-piece tables to references/.

## Standing habits / OWNER-HELD
- **Memory can be wiped** — the whole story is in JOURNAL + the prover/design-review records + ROADMAP.
- Version bumps are NOT owner-reserved (Alexander confirmed 2026-07-15): cut them on green; standing push
  authorization holds. The deep independent audit runs by default as quality, not on his word.
- On a failure: the root/infrastructure fix first, never a blind retry or a pointwise patch [INV-155 kin].
- Next free codes: INV-156, M-302.
