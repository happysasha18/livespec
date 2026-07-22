# Gaps — where PRODUCT_SPEC.md does not answer

A gap is a place where a criterion in `sample.md` names a judgment, and the spec does not say who judges it or by what measure. Per LAW 3, the criterion names the plainest honest actor and carries a `[GAP]` line. Inventing the missing behaviour is forbidden; a gap line is the correct output for a real hole.

## GAP 1 — the effort-and-value measure behind the quick-win mark

**Criterion:** R3.11.

**What the spec gives.** PRODUCT_SPEC.md line 98 defines a quick win as "low effort, immediate value, no design decision inside." The third test — no design decision inside — is checkable. The first two — low effort, immediate value — are evaluative.

**What is missing.** The spec does not define how the intake classifier measures a request's effort, nor how it measures a request's value, for the quick-win mark. No unit, threshold, or procedure is stated.

**GAP line as written in sample.md:** *the spec does not define how the intake classifier measures a request's effort or a request's value for the quick-win mark.*

## GAP 2 — how a request's effort is weighed against its benefit at scope negotiation

**Criterion:** R5.2.

**What the spec gives.** PRODUCT_SPEC.md line 102 and line 289 say a request "larger than its worth" or "too big for its worth" is negotiated in scope. T-15 (line 2158) repeats the phrase. The procedural response — cut the scope or split into stages — is defined.

**What is missing.** The spec never defines who weighs a request's effort against its benefit, or by what measure, to reach the judgment "larger than its worth." The trigger is used as a given.

**GAP line as written in sample.md:** *the spec does not define who weighs a request's effort against its benefit, or by what measure, at scope negotiation.*

## GAP 3 — the entry routes of two disagreement outcomes

**Criterion:** R4.7.

**What the spec gives.** PRODUCT_SPEC.md line 319 names the three owners of a three-source disagreement: "a bug row for code past spec, a spec fix for a moved pin, a restructure row for a missing node." The bug row's route is stated by its name, and INV-37 (line 2249) binds the restructure row to the architecture step's re-check. Line 2155 (T-12) closes the route set at five: feature, bug, refactor, docs-only, skip.

**What is missing.** The spec never names which of the five entry routes the spec-fix item and the restructure item take. "Restructure" shares no word with "refactor", and a spec fix names no route at all.

**GAP line as written in sample.md:** *the spec does not name the entry routes for the spec-fix and restructure backlog items; of the three disagreement outcomes, only the bug item's route is stated.*

---

The first two gaps sit on the same missing thing: a stated way to measure a request's effort and its value. The spec uses the judgments (quick win, larger than its worth) without defining the scale behind them. The third gap is a routing hole: two of the three disagreement outcomes have an owner but no named entry route.

Checked and settled without a gap: the batched report and the delivery report are one artifact (the batched section of the delivery report — lines 399 and 518); size "bug" and the bug entry route share one word on purpose, one call stated once (line 291); a defect of the product goes to the bug route (line 1113).
