# Prover record — INV-137, "the orchestrator reads to decide, not to discover"

Ran under **product-prover v1.0.10** (references live-spec-base v1.0.9). Mode: CROSS-LINK / delta-scoped,
fresh-context reviewer, not involved in authoring. Date 2026-07-13.

Opening hypothesis (adversarial): *a new law was added that contradicts an existing pack law, or the goal
was missed.*

## Triage

PROCEED. The delta is a normative rule + spec invariant with clear structure (a seat, an input it governs,
a bounded exception, a visibility mechanism) — analyzable against the existing routing/delegation laws it
sits beside.

## What I read (primary sources, not summaries)

- `skills/live-spec-base/SKILL.md` — rule 25 (lines 246–257), rule 5 (46–56), the description (line 3).
- `PRODUCT_SPEC.md` — INV-137 prose (1477), INV-103 (1475), INV-69 (1434–1473), Formal-index rows under
  "Who decides what" (INV-69 1877, INV-103 1913, INV-137 1914), the reconciled hook line (160).
- `skills/build-pipeline/SKILL.md` — the delegation-accounting echo naming reads dispatched (537–543).
- `ARCHITECTURE.md` — build-pipeline node owns-list (line 46, INV-137 present).
- `TEST_MATRIX.md` — M-279 (line 243). Ran `tests/test_orchestrator_read_discipline.py` → **5 passed**.

## Verdict on the hypothesis

Rejected. INV-137 does **not** contradict rule 5 / INV-69 or the delegation accounting (INV-103); it is a
clean third face of one seat's discipline, explicitly distinguished in its own text (input/context-hygiene
vs work-produced vs reported). The goal is met: the law is stated, traceable, tested green, and the prior
hook misattribution is reconciled. One must-fold defect (a stale rule count the delta introduced) and a
few should-clarify seams remain.

## Findings

| id | finding (headline) | severity | folded / rejected(+why) |
|---|---|---|---|
| F1 | Base-skill description still says "twenty-four rules in the body" — the body now has 25 | must-fix | **must-fold (orchestrator to apply)** — the delta added rule 25 but left the count in `SKILL.md` line 3 stale; this is a one-home/freshness defect caused by this change (rules 4, 9). Exact fix: in `skills/live-spec-base/SKILL.md` line 3, change "twenty-four rules in the body" → "twenty-five rules in the body". Sweep-checked (rule 14): this is the only stale count string in the pack — `grep` for "twenty-four/twenty-three/24/25 rules" hits nothing else. |
| F2 | The boundary between "dispatch reads past a glance / read the distillation, not raw bodies" and verify-by-deed (rule 11) / primary-source reading (rule 13) is left implicit | should-clarify | **should-fold** — the title ("reads to **decide**, not to discover") and the body's scoping to reads done "to UNDERSTAND or DESIGN" do carve verify/decide reads OUT of the dispatch duty, so there is no literal contradiction. But the body never names rules 11/13, and its line "the lead reads the distillation, not the raw file bodies" can be over-read as covering a fact-verifying read — which would collide head-on with rule 13 ("read the actual source line… never rest a claim on a summary") and rule 5's raw-output clause ("a worker's green is a lead the lead ACCEPTS by re-checking it"). Recommend one clause: a verify/decide read stays with the lead, and where such a read is large enough to dispatch, the worker returns RAW evidence the lead re-checks (rule 5/13's delegation face), not a bare distillation. |
| F3 | Base body grew a rule but the skill metadata stays `version: 1.0.9` | worth-considering | **flag to orchestrator** — freshness re-reads (rule 8) key on a version change; a body edit with no version move can slip past a resuming session's re-read. Confirm whether this delta should carry a base-skill version bump (and update the "written against v1.0.9" pointers in the working skills if so). Not blocking the law's soundness. |
| F4 | Rule 25's parenthetical "(rule 5, SPEC INV-69)" on the "workers locate their own anchors" sentence points to homes that don't state it verbatim | worth-considering | **flag** — the reconciliation correctly moves the claim's home to rule 25 (the hook now cites rule 25, good). But rule 25 itself attributes the anchor-locating sentence to rule 5 / INV-69, and neither states it in those words — INV-69's worker contract only implies it ("the files its brief names"). A reader chasing the anchor into rule 5 finds nothing, a faint residual of the very misattribution this change cured. Optional: add "the brief carries the anchors" to INV-69's worker contract so the pointer resolves, or drop the rule-5 cite. |

## Adversarial questions — settled

1. **Contradicts rule 5 / INV-69, or extends?** Extends, cleanly. INV-137 explicitly says it "governs the
   lead's own reading (the input side) where [INV-69] governs the work it produces and [INV-103] what it
   reports; the three are one seat's discipline seen from three sides." No double-home, no overlap. No
   finding.
2. **Contradicts the ask/verify/delegation laws?** No literal contradiction (see F2). Rule 25 is scoped to
   reads done "to understand or design" (discover); verify-by-deed (rule 11) and primary-source reads
   (rule 13) are decide-reads the title keeps with the lead. The seam is real but the rule is followable as
   written — the gap is that it doesn't affirmatively state the carve-out. Should-clarify, F2.
3. **Is "a glance is bounded" actionable?** Yes. "Small file / a handful of targeted lines" is fuzzy on its
   own, but the operative test is functional — "whose result IS the deliverable (a version string, one
   clause to quote)" vs a read done to understand/design. That functional criterion carries it past a line
   count. No finding; the only softness ("small file" has no size) is absorbed by the functional test.
4. **Traceable and complete?** Yes. Owning node present (ARCHITECTURE.md build-pipeline row, INV-137).
   Formal-index row present (spec 1914, "Who decides what", single occurrence). Matrix row present (M-279)
   citing five tests, all present in `tests/test_orchestrator_read_discipline.py` and green. Homes list
   ("base rule 25 + this clause + delegation accounting [INV-103] + chat-law hook's routing-line reminder")
   is accurate — each home exists and carries its part; the reads-dispatched visibility lives in the
   build-pipeline echo (537–543) and INV-137's own clause.
5. **Does the reconciled hook match rule 5 / rule 25?** Yes. Hook line 160 cites "base rule 25, SPEC
   INV-137" for "workers locate their own anchors" (now genuinely stated in rule 25, line 254) and "the
   routing law [INV-69]" for "routes work to the cheapest sufficient tier" (rule 5 / INV-69). The prior
   defect — claiming the anchor rule as rule 5, which never stated it — is cured. Residual pointer nit in
   F4.

## What's working

- The three-sided framing (read-input / work-output / report) is the right decomposition and is stated in
  the clause itself, which is exactly what prevents the double-home the hypothesis feared.
- Full traceability with a red-first-proven, now-green enshrining test across all five homes (M-279).
- The visibility mechanism reuses the existing delegation-accounting channel (INV-103) rather than
  inventing a new one — the same cure that finally held the routing rule.

## Readiness

Sound to land after F1 is folded (a one-word count fix the delta itself caused). F2 is the one seam worth
closing in the same pass; F3/F4 are optional polish. Needs one small fold, not another iteration.
