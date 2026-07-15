# Prover record — 322 (forward-binding unification) + 323 (review-record class, INV-156)

Ran under **product-prover v1.1.4** (base live-spec-base v1.0.17), 2026-07-15. Adversarial
delta-scoped re-prove of the uncommitted 323 delta plus the committed 322 delta (HEAD `453a9d6`,
the push ahead of origin — this record also satisfies the M-6 push-gate re-check that the guardrail
currently reds for). Mode: delta-scoped, both sides read (pre-322 tree at `81cb73e` and the working
tree). The whole document stayed in view; findings are narrowed to the two deltas' seams.

## Verdict — HOLDS-WITH-FIXES

The mechanism both deltas build is sound and the suite is green but for the expected fresh-record
gate. Two defects block a clean landing, each delta-authored and each a false or contradictory spec
claim that a reader tracing a citation hits head-on. Neither is a mechanism bug; both are
one-home-per-fact / traceability breaks — the exact failure class this pack exists to forbid. Fold
the two defects and the deltas hold.

Accuracy note (the 323 target that mattered most): the disposition vocabularies are stated
correctly for both full siblings (prover `folded / rejected(+why)` + kind; design-review
`recommended / asked / answered(+decision) / held`), and verify's characterisation — outcome in the
landing record, not a dated file — is TRUE against INV-46 (line 1909, 1520: "verdict rides the
landing report"). The break is not in verify; it is in the craft-walk member, below.

## Invariants touched

- **322:** INV-41 (budget numbers — home unchanged), INV-15 (cited as the forward-binding root),
  and the forward-binding convention shared with INV-74 / INV-75 / INV-127 / lines 703, 721.
- **323:** INV-156 (new), and it leans on INV-140, INV-141, INV-142, INV-99, INV-46. New homes:
  spec body clause (line 440), Formal-index row (line 2000), M-303, ARCHITECTURE design-reviewer
  node (line 61), product-prover + design-reviewer record sections, `tests/test_review_record_class.py`.

## Findings

| # | Finding | Kind | Disposition (author folds at gate) |
|---|---|---|---|
| F1 | 322 unifies forward-binding onto INV-15, but INV-15's text never states that law | defect · internal-conflict (consistency) | open |
| F2 | INV-156 homes the craft-walk record in `docs/audit/`, contradicting INV-99's "landing record" | defect · direct-contradiction (contradiction) | open |
| F3 | INV-156 omits the periodic/milestone adversarial audit (INV-145), a dated `docs/audit/` review pass | defect · missing-scenario (state-space) | open |
| F4 | INV-156 is owned by design-reviewer, the newest and least central member | recommendation · boundary-issue (composition) | open |
| F5 | "one forward-binding law" is contradicted by T-16 / A-3 / INV-21 / line 626, left un-unified | recommendation · over-general (abstraction) | open |
| F6 | Class shape demands "opens by naming the skill and version"; existing craft-walk records name no version | recommendation · hard-to-operate (ops-ux) | open |

---

### F1 — 322 repoints forward-binding to INV-15, but INV-15 is the node/matrix law, not the forward-binding law

> "this budget duty binds forward from that first landing, never retroactively — the one forward-binding law every such duty carries [INV-15]." — PRODUCT_SPEC.md line 697 (and the INV-41 index row, line 1902), both authored by commit 453a9d6 (322)

Follow the citation. INV-15's own text — formal index (line 1857): *"no landing without an owning
node + a right-level matrix row"*; home clause (line ~720): *"no wish lands whose facts lack an
owning architecture node and a matrix row at the right level"* — states the node-and-matrix
invariant. Nowhere does INV-15 state *"a duty binds forward from the first landing after its clause
exists, never retroactively."* Line 721 applies forward-binding TO INV-15 as a temporal modifier;
it does not make INV-15 the statement of that law. So 322 unified the property onto a root that is
silent on the property. A reader tracing `[INV-15]` from the budget clause to learn the
forward-binding rule lands on a sentence about owning nodes and finds no such rule — the citation
does not discharge. 322's stated goal ("unify the forward-binding law to one root") is therefore
unmet: the "one root" does not carry the law in its text.

Delta-scoped: the phrase *"the one forward-binding law … [INV-15]"* is 322-authored (git blame line
697 = 453a9d6); before 322, INV-41 restated the rule as its own. The underlying looseness is older
(INV-74/75/127 already cited INV-15 for forward-binding without the definite article), but 322
elevated the mislabel to "THE one forward-binding law" and made it load-bearing, so it blocks here.

Fix — one of: (a) give the forward-binding principle a dedicated home the citations point at: either
add a clause to INV-15's index/home text that states the forward-binding law in words (so the
citation resolves), or (b) mint a new invariant whose stated content IS *"a new duty binds forward
from the landing after its clause exists, never retroactively; existing items owe no retroactive
backfill and comply at the first landing that touches them,"* and repoint INV-41 (and ideally
INV-74, INV-75, INV-127, lines 697/703/721) at it. (b) is the clean one and matches 322's own
premise that there is exactly one such law; (a) is the smaller edit if INV-15 is meant to stay the
home. Either way the cited root must state the cited property.

`defect · internal-conflict (consistency)`

---

### F2 — INV-156 says the craft-walk record is a dated `docs/audit/` file; INV-99 says its findings go to the landing record

> "The skill-creator craft-walk record is a member with the prover's disposition — folded / rejected(+why) — and no held-ask, its findings resolving within the walk [INV-99]." + class shape: "a dated file under the pass's own home (… the craft walk in `docs/audit/`)" — PRODUCT_SPEC.md line 440 (INV-156), replicated in the index row (2000), M-303, and ARCHITECTURE line 61

> "Each finding is folded or rejected by name in the landing record." — PRODUCT_SPEC.md line 343 (INV-99, unchanged by the delta)

INV-156 cites INV-99 as its authority for the craft-walk member, but the two clauses name two
different homes for the same fact — where a craft-walk finding's disposition lives. INV-99 says the
landing record; INV-156 says a dated file under `docs/audit/`. Both cannot be the single home
(one-home-per-fact). This is the same landing-record home INV-156 calls verify's "one deliberate
difference" — so by INV-99's text the craft walk shares that trait and verify is NOT the sole
difference, and by INV-156's text INV-99 is wrong. A later session reading INV-99 expects the
craft-walk fates in the landing record and finds none there if the author followed INV-156, or
hunts `docs/audit/` if the author followed INV-99.

Note the sharper edge: the craft walk runs INSIDE the verify step (INV-99, line 343: "the verify
step additionally runs the installed skill-creator's review"). INV-156 splits a component of the
verify step (craft walk → dated file) from the verify step itself (→ landing record) into two record
classes — incoherent on its face.

Practice sides with `docs/audit/`: real dated craft-walk records exist —
`docs/audit/2026-07-06-skill-creator-walk.md` and `docs/audit/2026-07-07-test-author-birth-walk.md`
(a skill-landing craft walk). So the right reconciliation is to fix INV-99, not INV-156: amend
INV-99 to name the dated `docs/audit/` record as the craft walk's home (findings folded/rejected
there, the landing record carrying only the pass's verdict line, if anything). Do that in the same
change as 323 — shipping INV-156 while INV-99 still reads "landing record" lands a direct
contradiction. Once INV-99 is fixed, verify becomes the genuine sole landing-record member and
INV-156's "one deliberate difference" holds.

`defect · direct-contradiction (contradiction)`

---

### F3 — the periodic / milestone adversarial audit (INV-145) is a dated `docs/audit/` review pass INV-156 does not name

> "every review pass writes its record of one class … the prover's spec re-check [INV-140], the design review [INV-141], the skill-creator craft walk [INV-99], and the verify-by-deed audit [INV-46]" — PRODUCT_SPEC.md line 440 / index row 2000

`docs/audit/` holds more than craft walks. `2026-07-12-minor-gate-walk.md`
("1.1.0 MINOR-gate audit — two passes, one record … Opus auditor"), `2026-07-12-composition-walk.md`,
`2026-07-12-delegation-dedup.md`, and their kin are the periodic / milestone **adversarial audit**
(INV-145: "an audit is adversarial by nature … [INV-46]") — a review pass writing a dated
`docs/audit/` record with its own disposition vocabulary (MET / OWED / FLAG). By INV-156's own test
("a new review pass states its record against this class — a member with its own disposition
vocabulary"), this pass is already a member and is unnamed. The class INV-156 declares "once" is
therefore not closed over the review passes that actually exist: it omits the one whose records
share its home directory. A reader told "every review pass" is enumerated will miss the audit walk.

For contrast, the architecture re-prove (INV-116) is NOT a missing member — it is a product-prover
pass recording in `docs/prover/` (line 742, 1982), i.e. the same member as the prover, applied to
ARCHITECTURE.md. Correctly folded into "the prover." The milestone audit is the genuine gap.

Fix — name the periodic/milestone audit (INV-145) as a member of INV-156: a dated `docs/audit/`
file with its MET/OWED/FLAG vocabulary, opening by naming the auditor. Or, if it is meant to be
excluded (e.g. treated as the composition of its component prover + design-review records rather
than a pass in its own right), state that exclusion by name — the minor-gate-walk file is plainly a
standalone record, so silent omission is the wrong answer.

`defect · missing-scenario (state-space)`

---

### F4 — the cross-cutting class is owned by design-reviewer, its newest and least central member

> "and owns the review-record class declaration — every review pass … writes a record of one shared shape … [INV-156]" — ARCHITECTURE.md line 61 (design-reviewer node's owns-list)

The class spans four members owned by four different nodes: the prover (product-prover), the design
review (design-reviewer), the craft walk (build-pipeline / skill-creator), and verify
(build-pipeline). INV-156 places the class declaration under design-reviewer — yet the class is
explicitly derived FROM the prover's record ("the same shape and discipline as the prover's record")
and design-review is the youngest member. The owning node inverts the dependency: the sibling that
inherited the shape now owns the family rulebook, while the shape's origin (product-prover) and the
two members that break from the shape (craft walk, verify — both build-pipeline territory) sit
elsewhere. The one-owner rule is met mechanically, so this does not block; but a cross-cutting record
class reads more naturally as a build-pipeline fact (build-pipeline orchestrates every pass and owns
the landing record and the verify/craft-walk accounting) or a product-prover fact (the canonical
record). Queue for a taste call: move INV-156's ownership to build-pipeline or product-prover, or
state why design-reviewer is the deliberate home.

`recommendation · boundary-issue (composition)`

---

### F5 — "the one forward-binding law" is contradicted by the spec's own structure

> "the one forward-binding law every such duty carries [INV-15]" — PRODUCT_SPEC.md line 697

The definite article claims a single forward-binding root, but the spec states the same
"binds forward, never retroactively" principle independently in at least four other places, none
repointed by 322: T-16 (line 341, 1154 — the work-kind axis binds forward, "like any forward-binding
intake law"), A-3 (line 491 — an adopted feature owes its spec pair at the first landing, never
retroactively en masse), INV-21 (line 1863 — "binds forward"), and line 626 (norm pointers,
"looks forward only … never retroactively"). Either these are all one law — in which case 322
unified only the INV-41 duplicate and left the rest scattered, so "one root" is not achieved and the
claim overreaches — or they are per-domain instances of a shared principle, in which case calling
INV-15 "the one" is the wrong framing. This is the design-level companion to F1: F1 says the cited
root is silent on the property; F5 says the "one root" premise is itself untrue pack-wide. Resolving
F1 via a dedicated forward-binding invariant would let T-16 / A-3 / INV-21 / line 626 cite it too and
make the "one law" real; otherwise scope the line to "the forward-binding law these architecture
duties carry" rather than "the one forward-binding law."

`recommendation · over-general (abstraction)`

---

### F6 — the class shape demands a skill+version header the existing member records don't carry

> "opening by naming the skill and version that ran the pass" — PRODUCT_SPEC.md line 440 (class shape)

The two real craft-walk records open with a title and date but no skill-creator version —
`# Skill-creator walk — all six pack skills, 2026-07-06` and
`# test-author — skill-creator walk at birth (2026-07-07 …)`. INV-156 imposes a shape the named
member's own records do not yet exhibit. Low severity — the duty binds forward (new records comply,
INV-15/the forward-binding law), and the prover and design-review records DO open by naming their
skill version. But note it so the author either backfills the header expectation as forward-binding
by name, or the traceability test (M-303) is not read as asserting a shape the existing files fail.

`recommendation · hard-to-operate (ops-ux)`

## What I checked and found clean

- **INV-41 not orphaned.** INV-41 keeps its own home (budget numbers), cited by ARCHITECTURE line
  61/195/209, the architecture lens (line 668), spec-author (line 267), build-pipeline (237/288).
  322 removed nothing from INV-41's ownership. No leftover cite of INV-41 as the forward-binding root.
- **Disposition vocabularies accurate.** Prover `folded / rejected(+why)` + kind (product-prover
  SKILL line 396, INV-140) and design-review `recommended / asked / answered(+decision) / held`
  (design-reviewer SKILL line 89) are both quoted correctly in INV-156.
- **Verify's difference TRUE.** INV-46 (line 1909, 1520) puts verify's verdict in the landing
  report, not a dated file. INV-156's characterisation of verify is correct — the error (F2) is that
  the craft walk shares that home per INV-99, not that verify is mis-described.
- **INV-156 single-owned.** Exactly one node (design-reviewer) claims it; M-303 sits under it; the
  two skill record-sections point at the class without restating it (the test asserts this). The four
  323 homes are mutually consistent — they jointly contradict INV-99 (F2), not each other.
- **Suite.** 758 passed, 1 failed — the failure is the prover-record freshness gate
  (`check-prover-record.sh`) reddening because PRODUCT_SPEC.md changed in 453a9d6 with no newer
  `docs/prover/` commit. This record, committed, clears it. `test_review_record_class.py` is green;
  note it encodes the `docs/audit/` claim (F2) and so would need updating alongside the INV-99 fix.

## Readiness

Needs another iteration — fold F1 and F2 (both small, surgical edits), decide F3, and the deltas are
buildable. F4–F6 queue as taste calls and hold nothing.

---

## Folds applied (author, same session, 2026-07-15)

- **F1 (defect) — folded by deflation + re-queue.** The false "the one forward-binding law [INV-15]"
  claim is removed; INV-41's forward-binding now reads "binds from that first landing, never
  retroactively, the way the architecture's own duties bind forward [INV-15]" — a precedent cite, not a
  claim that INV-15 states the law. The real unification (a dedicated forward-binding invariant repointing
  every scattered cite) is re-scoped as NEXT_STEPS row 325 with this record cited: it is a feature, not the
  two-line cleanup the queue line implied.
- **F2 (defect) — folded by correct attribution, INV-99 untouched.** The dated `docs/audit/` member is the
  MILESTONE whole-pack skill-creator craft walk [INV-145] plus the periodic adversarial audit, not the
  per-landing skill-creator review. The per-landing review [INV-99] now sits with verify in the landing
  record — so INV-99's "landing record" text (and its test) stay true, and the contradiction is gone
  without amending INV-99. Verify remains the one genuine landing-record difference.
- **F3 (defect) — folded.** The periodic adversarial audit [INV-145] is now named a member, with its
  MET / OWED / FLAG disposition, in the clause, the index row, M-303, and the ARCHITECTURE owns phrase.
  The architecture re-prove [INV-116] stays folded into "the prover" (it records in docs/prover/), as the
  record noted.
- **F4 (recommendation) — folded by stated rationale.** The ARCHITECTURE owns phrase now states why
  design-reviewer holds the class: it reached the one-class reading from the record-sibling seam it already
  owns (design review → record). Product-prover and build-pipeline cite the class without restating it.
- **F5 (recommendation) — folded with F1.** The "one law" overreach is gone; the wider scatter
  (T-16 / A-3 / INV-21 / line 626) is the subject of row 325.
- **F6 (recommendation) — folded.** INV-156 now states the class binds forward, so records written before
  the class was declared are not reshaped retroactively.

Suite 759 green after the folds. This record, committed with the delta, is the M-6 push-gate re-check for
the pushed state.
