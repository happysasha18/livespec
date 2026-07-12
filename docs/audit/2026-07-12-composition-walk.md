# Surface-composition walk — 1.1.0 minor gate

**Audited state.** `~/live-spec` @ `8125b2c` (branch `main`, clean tree). Object: `PRODUCT_SPEC.md`
v1.0.24. This is the M-1 gate's surface-composition step [PRODUCT_SPEC.md:697]: enumerate the stateful
surfaces, confirm one-surface-one-name, then compose each surface and each new law against the surfaces
and laws it touches, and report every reachable combination no spec sentence covers.

The weight this pass carries sits on the laws landed since the 2026-07-05 walk: INV-101, INV-103, INV-104,
INV-106, INV-107, INV-108, INV-109, INV-110, INV-111, INV-112, INV-113, INV-114. The walk reads them
pairwise where they touch — two laws ordering one scenario in conflict, a transition whose end-state no
law owns, and a new station set beside the checkpoint-and-resume law.

The three questions the pass exists to ask: does any two laws give conflicting orders in one scenario;
does any transition leave a state no law owns; does any new station compose badly with checkpoint/resume.

---

## 1. Naming and inventory

One-surface-one-name holds across the new laws, with one word to watch.

- The new laws add no new named surface. They add stations onto surfaces the 2026-07-05 walk already
  inventoried: the inbox [E-11], the queue [E-3], the checkpoints [ACT-3], the architecture document
  [E-14], the loader [E-16], the remote [INV-82].
- **Watch word: "checkpoint."** INV-107 [PRODUCT_SPEC.md:681] uses "checkpoint" for the resume-state
  breakpoint record under `.live-spec/checkpoints/` [ACT-3] — its items are shipped work, and it closes
  when those items live in git history. INV-111 [PRODUCT_SPEC.md:1198] writes "the owner's decisions are
  locked in a checkpoint before any file moves [INV-107]" — here "checkpoint" holds owner decisions
  consumed by a layout pass. One word now names two contents under one cited anchor. This is not yet a
  collision, but the closing test crosses the two senses (see N2).

No new law claims to be a second source of truth. The declared-laws home [INV-101] stays single. No
surface is referenced-but-undefined.

---

## 2. Findings

### must-fix

**M — The live-spec push gate [M-6] and the remote inbox arm [INV-112] give conflicting orders for one
reachable push, and the ordered actor cannot obey both.** M-6 [PRODUCT_SPEC.md:732-736] reads: "every
push is preceded, in the same session, by two steps" — the concurrent-edit fence, then a fresh whole-spec
product-prover re-check whose record lands in `docs/prover/` before the push. "No re-check record for the
pushed state means the push should not have happened." INV-61 [PRODUCT_SPEC.md:740-746] scales the record's
form but still owes "its own full-page re-check record" on every push. INV-112 [PRODUCT_SPEC.md:1598]
orders a remote seat — "a cloud session, a scheduled routine, or another machine" — to deposit one inbox
file and push it, "committed touching inbox/ only ... and then pushed," with no prover pass and no record.
- *Reachable, and it is the born case.* INV-112 was born of exactly this seat aiming at live-spec:
  "a live routine alert was the first seat to hit the gap." A scheduled routine that drops a wish into
  live-spec's own `inbox/` and pushes is the first thing this law does. M-6 demands a whole-spec prover
  re-check before that push; a non-interactive remote routine cannot run product-prover and cannot write
  a `docs/prover/` record. The two laws order one push in opposite directions, and one order is
  structurally impossible for the seat.
- *Why it is must-fix, not a note.* This is not an edge the laws merely fail to mention. M-6 says
  literally "every push," and the flagship repo is the very target INV-112 names. The first remote deposit
  to live-spec breaks the gate on its face.
- *Owner.* M-6 should carve the inbox-only deposit push out of the whole-spec re-check: a push touching
  `inbox/` only changes no spec-backed content [INV-104], so it owes the fence and no prover record. State
  the carve-out where M-6 lists its two steps, and let INV-112 cite it. The fence step composes already —
  INV-112 names the one fresh inbox file as the fence's benign case [INV-11].

### should-fix

**S1 — INV-111 and INV-114 are two restructure vehicles whose relationship is unstated, and the lighter
one omits the suite check the heavier one requires.** INV-111 [PRODUCT_SPEC.md:1198] runs a same-version
docs-layout pass and proves it by a word-token multiset check and a punctuation multiset check, then lands
one journal chapter — no suite run, no prover. INV-114 [PRODUCT_SPEC.md:1200] gates "a restructure or a
migration ... merging back into main" with three parts: token identity plus the punctuation check
[INV-111], the full suite green on the merged tree [INV-39], and a prover pass on both sides.
- *Reachable.* A docs-layout pass is a restructure. INV-111 says it "builds on a clean pushed base, so one
  command restores the pre-pass tree," which reads as landing directly rather than merging a branch. If it
  lands direct, INV-114's suite-green part never runs on a layout pass — yet a reflow can break a
  suite-owned doc check (a version pin, an anchor multiset check, the register lint), and the multiset
  proof does not read a red test. If instead the pass merges a branch, INV-114 governs and INV-111's
  multiset proof is INV-114's part one restated — then which gate is authoritative is unsaid.
- *Owner.* INV-111 should state whether a layout pass lands direct or through INV-114's merge gate, and
  should add the suite-green check [INV-39] to its own proof for the direct-landing case.

**S2 — INV-114's token-identity gate fits a content-preserving restructure and misfires on a
content-changing redesign [INV-113].** INV-114 [PRODUCT_SPEC.md:1200] blocks on "load-bearing token
identity old-versus-new modulo the per-chunk named deltas." That check is right for a restructure that
preserves content and moves it. INV-113 [PRODUCT_SPEC.md:636] governs a deliberate architecture redesign
that changes the document's shape and content — "layers restacked, a surface's ownership moved, nodes
merged or split."
- *Reachable.* A redesign is a restructure by plain reading, so it routes to INV-114's merge gate. But a
  redesign changes tokens by intent; INV-114's token-identity part would flag the whole redesign as
  unmatched tokens unless every change is spelled as a "per-chunk named delta," turning the gate into an
  exhaustive line-by-line naming of an intentional reshape. INV-113's own duty is the architecture-lens
  re-prove, not a token-identity proof.
- *Owner.* INV-114 should scope its "restructure" to a content-preserving pass and exclude a redesign
  [INV-113], or state that a redesign's merge drops the token-identity part and stands on the prover pass.

**S3 — The remote inbox deposit push does not obey INV-82's live-session stand-down, and the carve-out is
implied but never stated.** INV-82 [PRODUCT_SPEC.md:728] holds a by-rule push down "while another session
is known live in the repo." INV-112 [PRODUCT_SPEC.md:1598] has a remote seat that "cannot see which
sessions are live" push its inbox file and retry after a pull on rejection.
- *Reachable.* A remote seat structurally cannot honor a stand-down it cannot detect, so the deposit push
  must be exempt from INV-82. INV-112 frames the deposit as the fence's benign case, which implies the
  exemption, but it cites INV-82 only for the grant, never for the stand-down it quietly overrides.
- *Owner.* INV-112 should say plainly that the inbox-only deposit push is exempt from the live-session
  stand-down [INV-82], since it touches `inbox/` only and never races shared content.

### note

**N1 — A partially-shipped checkpoint has no clearly owned end-state under INV-107.** INV-107
[PRODUCT_SPEC.md:681] reads "a landing that ships a checkpoint's items flips that checkpoint to its closed
state," and "a checkpoint whose items all live in git history is stale." A landing that ships some of a
checkpoint's items and not others is not addressed: read one way it closes a checkpoint with live items
still open, read the other it leaves a part-shipped checkpoint that the returning session cannot tell from
an untouched one. State that the flip fires only when all of a checkpoint's items reach git history.

**N2 — INV-107's closing test does not cleanly reach INV-111's decision-lock checkpoint.** INV-111
[PRODUCT_SPEC.md:1198] locks owner decisions in a checkpoint and cites INV-107 for it. INV-107's flip test
is "all items live in git history." A decision-lock record's contents are decisions consumed by the layout
pass, not shipped deliverables that land in git history as work. Whether INV-107 flips such a record closed
when the pass lands, and whether it is a resume-state checkpoint under the worker-liveness law [INV-76], is
left to the reader. One added sentence in INV-111 would say which.

**N3 — A fire-and-forget remote deposit seat cannot honor INV-106's read-the-verdict duty.** INV-106
[PRODUCT_SPEC.md:730] has the pushing session read the remote gate's verdict and fix a red run the same
session. A scheduled routine that deposits and exits has no same session to fix a red gate in. Severity is
low, since an inbox-only push should not redden the gate, but the seat is the same non-interactive class as
the must-fix, and the two carve-outs should be written together.

**N4 — INV-112's push retry has no stated bound.** INV-112 [PRODUCT_SPEC.md:1598] says "a push the remote
rejects retries after a pull." Two remote seats contending the same repo, or a fast-moving repo, leave the
retry loop unbounded and its give-up state unowned. A bounded retry with an honest-failure exit [INV-67]
would match the law's own honest-failure shape.

---

## 3. Verdict — readiness to gate 1.1.0 on this pass

**One must-fix, three should-fix, four notes.** The new laws compose well in the ordinary case: INV-112
names its composition with the peer fence outright, INV-110's version discriminator cleanly separates the
catch-up walk from a host's own pipeline, and INV-108's live channel sits correctly beside the once-read
homes and this very gate's loader walk [M-1].

The must-fix is a true two-law contradiction on the flagship repo, hit by the first remote seat the law
was written for, and it should fold before the gate rather than becoming a queue row — the fix is one
carve-out sentence in M-6. S1 and S2 are the seams between the three restructure laws (INV-111, INV-113,
INV-114) that landed within two days of each other and have not yet been read against one another; both
are single-clause scope statements. S3 and the four notes are safe as owned queue rows.

Recommendation: **fold M and S3 into M-6 and INV-112, fold S1 and S2 into the restructure cluster, record
the four notes**, then gate 1.1.0 on this pass.

*(Surface-composition slice only; the re-prove, matrix-audit, eval, skill-craft, and compaction steps of
the M-1 gate are separate passes.)*

---

**Addendum (landing).** The must-fix and S1-S3 landed in commit `94f0a3f` via
.live-spec/checkpoints/pending-draft-composition-fixes.md: M-6 carve-out (clause + index + profile
pointer), INV-111 suite-green + merge-gate relationship (clause + index), INV-114 content-preserving
scope in all three homes (clauses + index), INV-112 stand-down sentence (clause + index), three test
extensions red-proven then green. The four notes and the CI mechanical-arm row stay routed per the
draft's disposition section.
