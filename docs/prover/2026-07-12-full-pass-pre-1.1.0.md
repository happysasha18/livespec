# Prover record — FULL pre-1.1.0 pass over the whole product spec (2026-07-12)

**Prover skill version:** product-prover **v1.0.2** (base skill referenced at v1.0.5). This pass ran under
the current lens set, including the six-check architecture lens and the full Phase-3e stress family —
notably the **declared-cross-cutting-laws station** (SPEC INV-101), which grew into the stress list since
the last FULL pass (2026-07-10, run under **v0.1.15**). That grown lens re-arms the full walk by the
prover's own record law: a "recently proven" spec proven under an older lens set owes a fresh full pass.

**Mode:** FULL (whole-spec re-check, every phase). **Trigger:** the pre-1.1.0 (MINOR) audit — a standing
full re-prove over PRODUCT_SPEC.md as it stands tonight, with the six landings that arrived since the last
full pass under the hardest look: INV-109 (no-silent-drop of substance), INV-110 (catch-up version-delta
discriminator), INV-111 (same-version docs-layout vehicle), INV-112 (inbox remote arm), INV-113
(architecture-redesign owes rework), INV-114 (restructure/migration merge gate), and the README stance
paragraph (M-250, TEST_MATRIX namespace) — asking whether they compose cleanly with the older laws or
whether any two clauses now collide.

**Documents proven:** PRODUCT_SPEC.md (v1.0.23, package VERSION 1.0.31, 1865 lines) with the Formal index
and TEST_MATRIX.md's M-247..M-253 rows in view for anchor/matrix ownership. HEAD 93cf950, tree clean.

**How this pass was run:** the prover read the whole spec end to end, extracted the model, then walked each
recent invariant against the sections it composes with — the merge gate (INV-114) against its cited kin
INV-111/INV-39 and against the older push/fence laws; the inbox remote arm (INV-112) against the push grant
(INV-82), the concurrent-edit fence (INV-11), and honest-failure (INV-67); the redesign law (INV-113)
against the re-carve routing (INV-37/E-14); the catch-up discriminator and vehicle (INV-110/111) against
the heavy catch-up machinery (INV-89..92); and the no-silent-drop law (INV-109) against the honest-echo and
register laws (INV-93, INV-83). Each landing's Formal-index row and TEST_MATRIX row were checked for
ownership and location.

## Opening assessment

The spec is in strong shape and tonight's six landings compose cleanly with the older laws in the main. The
merge gate (INV-114) is well-founded: its token-identity leg forecloses the aggravated-pre-existing-finding
edge I probed (a finding cannot worsen without a token change, and a token change is either a named delta,
reviewed, or an unmatched token, blocking), so the partition "absent-on-old blocks / equal-on-both queues"
holds. INV-113's architecture-ownership gap was caught at landing by the traceability suite, not left in the
doc, and the index confirms INV-113/INV-114 each own their node. The folds from the 2026-07-10 pass
(F1/F2/F6 into INV-82 and the tight rung) all stand — no regression. The declared-laws home (INV-101) that
re-armed this pass is present, with its three laws and two dated exemptions.

The findings are three should-fixes, all on INV-112's landing region and one index-map cell — none blocks
the build, none is a prose regression, and none touches the design's soundness. The one worth attention
before the minor bump is the INV-112-vs-INV-11 composition seam, unexamined by INV-112's own landing record.
Overall confidence: **ready to build; fold the three should-fixes or queue them as the senior prefers.**

## Findings

Each finding gives its headline, the source quote with its spec anchor, the operational consequence, and a
concrete action. The Disposition column is left for the senior to fill (folded / rejected + why).

| # | Finding | Anchor / line | Class | Disposition |
|---|---|---|---|---|
| F1 | INV-114's Formal-index Section cell points at the wrong section | index row L1854 vs clause L1200 [INV-114] | should-fix · hard-to-operate (ops-ux) | FOLDED 2026-07-12 (this batch; ratchet test pins the section column) |
| F2 | INV-112's autonomous inbox-push does not state how it composes with the never-push-while-a-peer-is-live fence | L1598 [INV-112] vs L1610 [INV-11] | should-fix · boundary-issue (composition) | FOLDED 2026-07-12 (this batch; composition sentence added to INV-112) |
| F3 | INV-112's clause carries a literal duplicated sentence | L1598 [INV-112] | should-fix · internal-conflict (consistency) | FOLDED 2026-07-12 (this batch; needle copy kept, first sentence reworked) |

---

**F1 — The Formal index files INV-114 under "The machines that hold the bounds," but the clause physically lives in the Catch-up section; a lookup by the map lands in the wrong place.**

> "| INV-114 | a restructure or migration merge gate judges the delta … | The machines that hold the bounds |" — Formal index (line 1854)

The INV-114 clause is at line 1200, inside "### Bringing an adopted host up to the current pack (catch-up),"
beside INV-110 and INV-111 (which it cites and which both correctly read "Catch-up" in their own index
rows). A reader or a later prover resolving INV-114 through the index is sent to "The machines that hold the
bounds" (line 1508), where no INV-114 clause exists. The green `test_spec_anchor_and_index` for INV-114
proves the anchor is present in prose and index but does not assert the Section cell matches the clause's
actual home, so the suite passed a wrong pointer. The milestone gate's own "re-check the formal index
against the prose" step (M-1) is exactly the check this pre-1.1.0 audit performs.

Change the INV-114 index Section cell from "The machines that hold the bounds" to "Catch-up," matching its
sibling rows INV-110/INV-111 and the clause's real location. (Do not move the clause — it sensibly sits
beside INV-111, which it cites.)

`should-fix · hard-to-operate (ops-ux)`

---

**F2 — INV-112 mandates a remote seat push its inbox deposit, but INV-11 forbids pushing while a peer session is live and hands push coordination to the human; the two are not reconciled, and a scheduled remote seat has no human to coordinate with.**

> "Its deposit stays one new file in inbox/, committed touching inbox/ only with the source named in the message, and then pushed." — Package repo [INV-112]

> "The agent never pushes while another session is known to be live in the repo; push coordination belongs to the human." — Package repo [INV-11]

INV-11's write/commit fence already carves out inbox new-files as the benign case, but its push clause does
not — and INV-112 requires a push. On the exact scenario INV-112 is built for (a cloud session or a
scheduled 3am routine depositing an alert into a foreign repo's inbox), there is no human in the loop to
"coordinate" the push, and requiring one would defeat the autonomy the arm exists to provide. INV-112's own
landing record (2026-07-12-row247) checked composition against INV-82 and INV-94 but not INV-11, so this
seam is unexamined. The blast radius is small — a remote seat rarely *knows* a peer is live, and the
collision law (fresh `-2`/`-3` filename, never editing an existing file) makes a racing inbox push
conflict-free, with a non-fast-forward rejection caught by INV-112's own honest-failure/retry — but the
composition should be stated rather than left to inference, the same way the 2026-07-10 pass made the
INV-82-vs-INV-11 push seam explicit (that pass's F2).

Add one clause to INV-112: the inbox-only new-file push inherits INV-11's benign-inbox carve-out and is not
held for human push-coordination — an autonomous remote seat has no human to coordinate, and the collision
law makes the fresh-file push conflict-free; a non-fast-forward rejection is the honest-failure/retry case,
never a silent drop. Cross-link INV-11 from INV-112's line.

`should-fix · boundary-issue (composition)`

---

**F3 — INV-112's clause states the same sentence twice in a row, a stutter introduced in the row-247 landing.**

> "A remote seat — a cloud session, a scheduled routine, another machine — reaches a repo only through git. A remote seat reaches a repo only through git." — Package repo [INV-112]

The second sentence repeats the first verbatim in meaning ("reaches a repo only through git"). No correctness
consequence — both sentences are true — but it reads as an editing artifact in the spec's own normative
prose, and the clause travels the clean-writer road (INV-84) whose bar it fails here. The Formal-index
one-liner for INV-112 (line 1730) does not carry the stutter, so only the body clause is affected.

Delete the duplicate: keep "A remote seat — a cloud session, a scheduled routine, another machine — reaches
a repo only through git." and drop the second "A remote seat reaches a repo only through git."

`should-fix · internal-conflict (consistency)`

## What was probed hardest and found sound

- **The merge gate (INV-114)** against its own partition: I constructed the aggravated-pre-existing-finding
  case — a finding milder on the old side, worse on the merged side — and it cannot arise. The
  token-identity leg (identity old-versus-new modulo per-chunk named deltas, plus the punctuation multiset
  [INV-111]) means content is provably identical except for named deltas; a finding cannot worsen without a
  token change, and a token change is either a named delta (reviewed) or an unmatched token (blocks). The
  "absent-on-old blocks / equal-on-both queues" partition is therefore complete given the token leg. Its
  citations of INV-111 (token+punctuation) and INV-39 (landing gate) resolve correctly and are not restated.

- **The redesign law (INV-113)** against the re-carve routing (INV-37/E-14): INV-113 states what the
  redesign row *owes the document* (re-shape + re-prove, not pins-only), while INV-37/E-14 carry the
  redesign as its own row — no overlap, no conflict. The ARCHITECTURE.md owning-node gap that the pins-only
  path would leave was caught at landing by the traceability suite (row 257 record), and the index confirms
  INV-113 is owned by build-pipeline, INV-114 by product-prover.

- **The catch-up discriminator and vehicle (INV-110/INV-111)** against the heavy catch-up machinery
  (INV-89..92): the version-delta test cleanly partitions the heavy walk (host behind current VERSION) from
  the light same-version vehicle, and the trigger wordings are correctly demoted to "examples under the
  version test." INV-111's word-token-AND-punctuation multiset proof is the right check for a pure reflow;
  it composes with, and is cited by, INV-114's stronger token-identity check for the merge case.

- **The no-silent-drop law (INV-109)** against the honest-echo (INV-93) and register (INV-83) laws: INV-109
  governs what a landing report must NAME (every substance removal), INV-93/INV-83 govern what a line must
  SAY and how it reads — orthogonal, no clash. Its scope carve-out (substance, not line-level wording) is
  explicit.

- **The 2026-07-10 folds** re-checked as holding: INV-82 now runs inside the push grant [INV-70, INV-9]
  (F1), stands down while a peer is live [INV-11] (F2), and the tight rung reads "the batch's reach-scoped
  gate [INV-45] green at HEAD" (F6). No regression in any.

- **The declared-laws home (INV-101)** that re-armed this pass: present, naming three declared laws (the
  plain-language register [INV-28/34/83], clock-honest stamps [INV-24], no self-certification [INV-94]) with
  two dated exemptions (measurement and accessibility, both 2026-07-12). Tonight's six landings are
  skill/prose/infra deltas with no new visitor surface, so the per-surface declared-law walk owes them
  nothing beyond what their homes already carry.

## Coverage note

CRUD and authorization tables stay N/A for this product, as in every prior full pass: live-spec is a
single-human skill pack with no multi-user persistent entity and no role model. The coverage that matters
here is the anchor→node ownership map and the Formal-index-vs-prose map, carried by ARCHITECTURE.md,
`tests/test_traceability.py`, and TEST_MATRIX.md. Every tonight landing (INV-109..114) resolves to a BUILT
matrix row (M-247, M-248, M-249, M-251, M-252, M-253) with a red-proven string test, and M-250 pins the
README stance paragraph; F1 records the one index-map cell the `test_spec_anchor_and_index` suite does not
assert.

**Namespace note (not a defect):** M-247..M-253 are TEST_MATRIX.md row anchors, a separate namespace from
the spec's Formal-index M-1..M-7 milestone family; they are correctly absent from the spec index.

## Gate

Three findings, all should-fix, zero must-fix, no prose regression. F1 is a wrong index Section pointer that
the milestone's own index-vs-prose re-check should correct before the 1.1.0 bump. F2 is the one unexamined
composition seam (INV-112's autonomous inbox-push vs INV-11's push fence), likely benign under the collision
law but owed an explicit clause, precedented by the prior pass's INV-82-vs-INV-11 fold. F3 is a duplicated
sentence in INV-112's body. All three sit on tonight's landing region or its index map; each is a
sentence-level edit. Recommend folding all three before the minor bump, or queueing F2 as a row if the
senior prefers — none is a prose regression and none blocks buildability.

## Addendum — landing (2026-07-12)

F1/F2/F3 landed 26aaa65 — one defect batch, one commit, riding this record (no new ROADMAP row, no new
INV/M numbers). F1's fix ships with its ratchet: test_spec_anchor_and_index now pins INV-114's index
Section cell to Catch-up, red-proven against the pre-fix tree.
