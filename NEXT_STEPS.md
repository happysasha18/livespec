# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-15 09:07 — 1.5.0 SHIPPED, pushed, CI green; the two reviews are now one bounded loop, the design review ships alongside the prover; pack v1.5.0)
**PACK v1.5.0** (commit `bee657c`, pushed, CI green, suite 738). Two stories landed this session as one
MINOR release, from Alexander's wish "include the design review in the prover pack":

- **Story A — INV-154, the loop.** The prover and the design review form a bounded loop that settles to a
  fixed point. A round is one prover re-read plus one design-review re-read; only a human-accepted
  declaration (a class sentence or a decided sentence) advances it. The loop rests in one of three named
  states — CONVERGES, WAITS (on the human's answer), or STANDS DOWN (a kind with no element a person acts
  on, recorded by name). It is capped at three progressing rounds; on the cap it stops and surfaces the
  unsettled groupings with a best-effort cause, and it never holds a landing. Proven three times, rewritten
  twice: an independent adversarial prove folded seven within-clause findings, then the MINOR-gate
  whole-spec prover and full design review each found the same deeper gap from a different side (a confident
  recommendation fitting no resting state; a stood-down pass falsely reading as converged on a UI-less kind
  like live-spec itself), both folded into the three-state model.
- **Story B — the shopfront.** design-reviewer ships its own README + LICENSE; product-prover's README
  presents it as the younger sibling with a cross-reference; a completeness guard locks both (M-300).
- **Release + a root fix.** VERSION/plugin/spec-header → 1.5.0; design-reviewer 1.0.1, build-pipeline
  1.0.30; the stale v1.3.0 stamp removed from product-prover's README. A version-home test that hard-pinned
  the previous release's literals (a per-release hand-edit trap) was rewritten to derive agreement from the
  VERSION file (Alexander's "дерех а мелех" — root fix over a patch), so it stays current on its own.

## In flight this session (under /loop, autonomous)
- **ROADMAP 325 — flaky tests root-fixed, never tolerated or retried** — building NEXT as its own lane
  into test-author + build-pipeline's green definition (Alexander 2026-07-15; the infrastructure/root fix
  first, never a blind retry or patch).

## Queue (ROADMAP)
- **321** feedback-collector sub-skill — on strong user emotion, OFFER (consent first) to send a distilled
  digest upstream; inbox destination, per-machine opt-out, distinct from feedback-intake. Open design Qs at
  build (Alexander 2026-07-15, "как дойдём добавим").
- **322** the forward-binding law is cited to two roots — unify to one.
- **323** declare the review-record class once (prover / design-review / skill-creator / verify records),
  default is to declare.
- **324** build-pipeline SKILL.md is 593 lines, over the 500 ideal — offload set-piece tables to references/.

## Standing habits / OWNER-HELD
- **Memory can be wiped** — the whole story is in JOURNAL + the prover/design-review records + ROADMAP.
- Version bumps are NOT owner-reserved (Alexander confirmed 2026-07-15): cut them on green, standing push
  authorization holds. The deep independent MINOR-gate audit runs by default as quality, not on his word.
- Next free codes: INV-155, M-301.
