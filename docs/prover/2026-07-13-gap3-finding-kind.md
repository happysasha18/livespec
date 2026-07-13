# Prover record — INV-140, "the prover labels each finding a defect or a recommendation"

**Prover skill version.** The pass reviews the repo copy of product-prover **v1.0.10** (the copy carrying
the delta: the `kind · severity · plain-label` tag line, the KIND block, the four-block Phase 5, the
kind-naming record column). The lens set actually loaded in this session was the *installed* copy
`~/.claude/skills/product-prover/SKILL.md` at **v1.0.9** — the pre-delta version, which has no KIND block
and still reads "Three short blocks." So this pass ran under the older lens set and reviews the newer one;
where it matters below I say so.

**Self-test note (dogfooding the feature under review).** I label each of my own findings with the very
`kind · severity` tag INV-140 introduces, and I derive the kind by the clause's own rule ("is there an
invariant behind it"). One of my findings (F3) turns out to be a **should-clarify defect** — a spec claim
that is false but cosmetic — which is a live witness of the exact `(should-clarify, defect)` pair that F1
is about. So the feature, applied to this very review, produces the disagreement F1 names. That is the
strongest evidence in the record, and I found it by using the feature.

**Mode.** FULL-scoped to the delta (the four homes named in the brief), read against the whole spec, the
architecture, and both prover copies. Adversarial opening hypothesis: *the kind duplicates severity, adds
no obligation, contradicts the disposition rules, or missed the goal.*

**Verdict in one line.** The kind axis is **genuinely orthogonal** to severity (the redundancy horn of the
hypothesis fails — see F-note A), the goal is met, register and traceability are clean — **but** because
the two axes are orthogonal, the *block-or-queue* verdict must sit on exactly one of them, and the delta
puts it on **both**: the KIND block and INV-140 say the **kind** decides blocking, while M-6 and
build-pipeline step 2 still say **must-fix** (severity) decides it. That is a real internal contradiction
between normative homes of the push-gate disposition. **One must-fold (F1).**

---

## What is working (real, substantive)

- **The orthogonality is real, not two names for one thing.** Severity carries *operational impact* (the
  skill's own example: a real atomicity issue is `should-clarify` for a quarterly manual op, `must-fix`
  for an automated path). Kind carries *is there an invariant behind it*. These come apart: a false spec
  claim with tiny impact is a `should-clarify` **defect**; a pure ambiguity is a `should-clarify`
  **recommendation**. Two `should-clarify` findings, two different kinds — so kind adds information severity
  does not carry. The redundancy horn of the hypothesis fails.
- **The derivation rule is decidable via the right discriminator.** The load-bearing test is "with no
  invariant behind it" (recommendation) vs "names a broken invariant or a false claim" (defect), not the
  literal "a stated invariant is violated." Read that way, the prover's staple gap-findings (unwritten
  seam, missing precondition) classify correctly as defects, because a needed invariant stands behind them.
- **Traceability is intact.** INV-140 has a Formal-index row (PRODUCT_SPEC.md:1783), a matrix row (M-282,
  correctly under `### [node: product-prover]`), and exactly one owning node (product-prover, ARCHITECTURE.md:45 —
  the trailing "owner is build-pipeline" clause attaches to the *other* wiring lenses, not to INV-140).
- **The four homes are internally consistent among themselves:** tag line `kind · severity · plain-label`
  (SKILL.md:81), example updated to three parts (`defect · must-fix · boundary-issue`, :94), KIND block
  beside SEVERITY (:104-108), Phase 5 fourth block for recommendations (:378), record column names the kind
  (:399), meta-rule names the kind (:399). No stale "Three short blocks" survived.

---

## Findings

### F1 — The block-or-queue verdict now has two carriers that can disagree (must-fold)

> "The kind carries the blocks-or-queues verdict and the severity carries operational impact" — product-prover SKILL.md, KIND block (:108)

> "Must-fix findings are folded before pushing. … The rest become queue rows." — PRODUCT_SPEC.md, M-6 (:767)

The delta moves the *does-this-block-the-push* decision onto **kind** (the KIND block sentence above;
INV-140: "a defect folds before a push and a recommendation becomes a queued row"). But the fact "which
findings must fold before a push" already has homes keyed on **severity**: M-6 (:767, "Must-fix findings
are folded… the rest become queue rows") and build-pipeline step 2 (:206, "fold every must-fix"). After the
delta there are two triggers for one gate — `must-fix` and `defect`. They coincide only if
`defect ⟺ must-fix`, and the feature itself denies that coincidence: the KIND block says a defect is
"*normally* must-fix" (not always), and severity is explicitly impact-driven, so a **low-impact false spec
claim is a `should-clarify` defect**. For that finding INV-140 says *fold before push*, M-6 says *the rest →
queue*. A session running the push gate has two rules and no tie-break. This is the pack's own "one home per
fact" law broken on a load-bearing gate (an `internal-conflict`).

Operational consequence: the agent runs the live-spec push gate, hits a `should-clarify · defect` (e.g. a
spec sentence whose stated number is wrong but harmless), and cannot tell from the method whether to fold it
now or queue it — the two normative homes give opposite answers, so the fold-or-defer call is made ad hoc
and a later session cannot reproduce it.

**Fix — pick ONE carrier and make the other homes cite it. Two coherent end-states:**

- **(A) Kind carries the verdict (recommended).** Edit M-6 (PRODUCT_SPEC.md:767): replace *"Must-fix
  findings are folded before pushing. … The rest become queue rows."* with *"Defect findings are folded
  before pushing. … Recommendations become queue rows."* Align build-pipeline step 2 (:206) "fold every
  must-fix" → "fold every defect." Severity then stays purely operational impact, exactly as the KIND block
  intends. This honors the feature's design (it un-conflates blocking from impact, which severity's
  `must-fix` had merged) and keeps kind load-bearing rather than decorative.
- **(B) Severity keeps the verdict.** Soften the KIND block sentence (:108) to *"The severity carries the
  fold-or-queue verdict; the kind names whether an invariant stands behind the finding, so the human sees
  why."* and reword INV-140's clause (PRODUCT_SPEC.md:427, 1783) so a defect does not *by itself* block
  (drop "a defect folds before a push"). Kind becomes an at-a-glance annotation; M-6 and step 2 stay as is.

Preference: **(A).** The feature's whole value is telling fold-now from weigh-later at the point of report;
(A) makes that the actual gate rule instead of a label sitting beside a gate keyed on something else. Note
for the orchestrator: (A) touches M-6, a long-standing invariant — this is a real method change, so it is
the human's call whether to take (A) or the lighter (B); the must-fold is only that the homes **stop
disagreeing**, not which way.

`defect · must-fix · internal-conflict (consistency)`

---

### F2 — The defect definition's literal wording ("a *stated* invariant is violated") is narrower than the prover's actual output

> "`defect` — a stated invariant is violated, or a claim the spec makes is false." — product-prover SKILL.md (:105)

The prover's staple findings are **gaps** — a missing precondition, an unwritten seam, a missing rule —
where the spec is *silent*, so no *stated* invariant is violated and no spec claim is *false*. Taken
literally, those staples match neither defect pole and fall by elimination toward "recommendation," which
would mislabel a must-fix seam (a caption stranded over the closing screen, INV-72) as a queued nicety. The
clause is *saved* by its own operative discriminator two sentences later — "with no invariant behind it"
(a gap has an invariant behind it → defect) — so a careful reader classifies correctly. But the pole's
wording and the discriminator pull opposite ways for the prover's most common finding type.

Consequence: a hurried prover reads the defect pole, sees "stated invariant violated," and tags a genuine
specification gap `recommendation` because nothing *written* was broken — the exact misbucketing that lets a
blocker queue instead of fold.

**Fix:** widen the defect pole in both homes (SKILL.md:105 and PRODUCT_SPEC.md:427/1783) from "a stated
invariant is violated" to "an invariant the design needs is violated **or left unstated where its absence
lets a bad state through**, or a spec claim is false" — so the pole matches the "invariant behind it"
discriminator the clause already relies on.

`recommendation · should-clarify · over-general (abstraction)`

---

### F3 — The spec clause says the human sorts "severity" by hand; the feature is about sorting KIND (a false claim, cosmetic)

> "…the label tells the two apart at the point of report rather than leaving the human to sort severity by hand." — PRODUCT_SPEC.md, INV-140 clause (:427)

Pre-delta, findings already carried `severity` on the tag, so the human never had to sort severity by hand
— what was undifferentiated was the **kind**. The born-note in the *same sentence* and the index row both say
"sort **defect from recommendation** by hand." So "sort severity by hand" is a false statement of the very
problem the feature solves, and it disagrees with its own sentence.

This finding is the record's **self-test payoff**: by the clause's rule it is a **defect** (a spec claim is
false), yet its operational impact is nil (one imprecise word) so its severity is **should-clarify**. That is
a concrete `should-clarify · defect` — the exact pair F1 says the two disposition homes answer differently.
Under INV-140 it "folds before a push"; under M-6 it is "the rest → queue." I did not construct this pair to
prove a point; the feature, applied to its own spec clause, produced it.

**Fix:** in PRODUCT_SPEC.md:427 change "sort severity by hand" → "sort defect from recommendation by hand"
(matching the born-note in the same sentence and index row 1783).

`defect · should-clarify · internal-conflict (consistency)`

---

### F4 — Phase 3.5 acknowledged gaps carry no kind, while the KIND block says "say which for every finding"

> "End with: `acknowledged · plain-label (formal-term)`." — product-prover SKILL.md, Phase 3.5 (:349)

The KIND block opens "defect or recommendation — say which for **every finding**" (:104), but Phase 3.5's
acknowledged-gap tag has no kind slot. Acknowledged gaps are framed as "not new discoveries," so an exemption
is defensible — but it is unstated, and a literal reader of "every finding" will wonder whether an
acknowledged gap owes a kind.

**Fix:** add one clause to the KIND block: "Acknowledged gaps (Phase 3.5) carry `acknowledged` in the kind
slot rather than defect/recommendation — they are the document's own open items, not the prover's fold-or-queue
call." One sentence closes the ambiguity.

`recommendation · worth-considering · missing-rule (invariant)`

---

## Per-finding disposition table

| id | finding | kind | severity | folded / rejected |
|---|---|---|---|---|
| F1 | block-or-queue verdict has two carriers (kind vs must-fix) that disagree on `(should-clarify, defect)` findings | defect | must-fix | **must-fold (orchestrator to apply)** — take (A): M-6:767 → "Defect findings are folded before pushing… Recommendations become queue rows"; build-pipeline step 2:206 "fold every must-fix" → "fold every defect". OR the lighter (B). The homes must stop disagreeing. |
| F2 | defect pole "a *stated* invariant is violated" narrower than the prover's gap-findings; saved only by the "invariant behind it" discriminator | recommendation | should-clarify | queued — recommend folding: widen the pole in SKILL.md:105 + PRODUCT_SPEC.md:427/1783 to match the "invariant behind it" test |
| F3 | INV-140 clause says human sorts "severity" by hand; feature sorts KIND — false claim, disagrees with its own born-note | defect | should-clarify | queued (cosmetic) — recommend folding the one word: PRODUCT_SPEC.md:427 "severity" → "defect from recommendation". Also the record's live `(should-clarify, defect)` witness for F1. |
| F4 | acknowledged gaps carry no kind while "say which for every finding" | recommendation | worth-considering | queued — one clause in the KIND block resolves it |

---

## Answers to the adversarial questions

1. **Duplicate of severity?** No. Kind and severity are orthogonal — witnessed by the reachable pairs
   `(should-clarify, defect)` (low-impact false claim) and `(should-clarify, recommendation)` (pure
   ambiguity). Kind carries information severity does not. The redundancy horn fails. *But* orthogonality is
   exactly why the block verdict cannot sit on both axes at once — see F1.
2. **Derivation sound and decidable?** Yes, via the operative discriminator "is there an invariant behind
   it," which classifies gaps correctly. The literal "a *stated* invariant is violated" pole is narrower than
   the discriminator and should be widened (F2). The `should-clarify` mapping is coherent as written but is
   the seam where kind and severity visibly separate (a `should-clarify` can be either kind), which is what
   F1 turns on.
3. **Consistent with M-6 / INV-99?** With INV-99, yes (INV-140 only refines what a finding *becomes*). With
   **M-6, no** — M-6 (and build-pipeline step 2) key folding on `must-fix`, INV-140/KIND block key it on
   `defect`; they contradict on any low-severity defect. This is F1, the sole must-fold.
4. **Phase 5 four-block partition consistent?** Yes. Block 1 (top-3 to fix = defects) and block 4
   (recommendations queued) partition cleanly with no overlap; the record column and meta-rule both name the
   kind; no stale "three blocks" remains.
5. **Register / traceability?** Clean. No "X — not Y" scissors, no coined metaphor, no non-native phrasing in
   the new text ("defect"/"recommendation" are plain words). INV-140 is fully traceable: one index row, one
   matrix row (M-282, correct node), one owning node.

**Overall readiness: needs one more iteration — a single reconciliation (F1) before this lands soundly;
F2–F4 are queued recommendations the human weighs as taste/precision calls.**

---

## Orchestrator resolution (2026-07-13 ~22:05, folded before commit)

- **F1 — FOLDED.** Chosen resolution: make the kind the COARSE READING of the severity rather than a second
  independent axis. A defect is exactly a `must-fix`; a recommendation is a `should-clarify` or a
  `worth-considering`. So the kind and the severity can never disagree on whether a finding blocks — the
  kind names the blocks-or-queues verdict in one word, and the push gate's folding rule stays home at M-6
  unchanged (a defect is a must-fix, so "fold every must-fix" and "fold every defect" are the same rule, one
  home). This is lighter than the prover's option A (which would have edited the long-standing M-6 invariant)
  and truer to the wish than option B (which would have demoted the kind to a bare annotation). The wobbly
  "a should-clarify can be a defect" claim was removed. Applied to the KIND block (`skills/product-prover/SKILL.md`),
  the INV-140 spec clause, and the Formal-index row.
- **F2 — FOLDED.** The defect pole widened to include "a required invariant or answer the spec owes is
  missing (a completeness gap)", matching the prover's real gap-findings (unwritten seams), not only a
  stated invariant violated.
- **F3 — FOLDED.** The spec clause's "sort severity by hand" corrected to "sort defect from recommendation
  by hand" (the feature sorts kind, not severity).
- Suite green after the folds (632 passed).
