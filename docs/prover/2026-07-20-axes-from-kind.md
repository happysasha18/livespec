# Prover + design-review + adversarial record — v3.2.0, axes-from-kind (INV-244)

Covers the MINOR-gate re-check for the landing that adds INV-244: a surface's composition axes derive
from its `project.kind`. Three passes ran over the proven spec, the architecture, and the tests, each in
a separate fresh seat that did not author the change under review [INV-237, INV-46]. The orchestrator
briefed the workers and accepted between stations; the drafting and the reads ran in workers so the
orchestrator held only the briefs and the decisions. Guards PRODUCT_SPEC.md and ARCHITECTURE.md for the
freshness rule [INV-116, M-6].

## Pass 1 — product-prover, FULL structural + cross-link

Verdict: advance with the two blockers folded, not a send-back. The design is right — axes derive from the
kind, and input-capability modelled as combinable capabilities (a tablet a co-occurrence of touch and a
fine pointer) is sound — but two load-bearing wires were unattached and folded before the landing.

| # | Finding | Disposition |
|---|---|---|
| F1 | The owed-axis trigger keyed on a `web / interactive-UX` value that `project.kind` cannot hold (the visual kinds are named `static site` and `fullstack`), so the machine had no key to fire on. | FOLDED — rebound to `project.kind ∈ {static site, fullstack}`, the visual kinds that declare a design-principles set [INV-136, INV-36]. |
| F2 | The new input-capability axis was never registered in C-1, so INV-72's completeness sweep could not reach it and C-1's universal completeness claim went false for a web surface. | FOLDED — C-1 reshaped to a kind-independent floor plus the axes a kind owes; input-capability registered; completeness reads "every floor axis and every axis its kind owes." |
| F3 | Viewport was owed in two homes (the C-1 floor and INV-244's elementary list), against one-home-per-fact. | FOLDED — viewport rides in as the C-1 floor axis; INV-244 adds input-capability alone [base rule 4]. |
| F4 | The resolution prescribed only a facet sentence, reproducing the checkbox that failed to stop the phone-visitor incident. | FOLDED — the resolution now names the compose-and-test consequence: the author composes and tests the surface against each elementary value, not only writes the sentence. |
| F5 | Binding-forward left the motivating tlvphotos surface uncovered until its next landing, while the clause read as "fixed." | FOLDED — one sentence names plainly that the existing photo surface carries the read at its next landing and stays uncovered until then [INV-159]. |
| F6 | The tablet co-occurrence read as covered while its forcing step is deferred. | FOLDED — the two poles are owed and answered up front now; the co-occurrence answer rides in with the deferred forcing step [target]. |

Seams that held: the owed-vs-covered finding is self-clearing (a decided "out of scope" sentence is a
written answer, so it does not re-fire); the facet/axis boundary does not double-own the fact (the
time-split at C-1 already models one fact as both a facet sentence and an axis composed-and-tested later);
the enumerate-vs-ride discipline [INV-226] is respected.

## Pass 2 — design review (two undeclared same-kind groups)

Group A — the three per-kind founding declarations (layers/proofs, design-principles, the new axis set).
Group B — the visual kind's owed axes (input-capability and its unnamed siblings).

| # | Finding | Disposition |
|---|---|---|
| D1 | Group B: INV-244 named "**the** input-capability axis", reading as the set closed at one member and re-enacting, one level up, the reactive drop the clause exists to kill (RTL/text-direction is the strongest tripped sibling on the same photo surface). | FOLDED (E1) — input-capability reframed as the first named member of the visual kind's open owed set; the siblings (browser engine, locale and direction, connection reach, first-vs-returning, accessibility, measurement reach) ride the general duty as their own increments [INV-226]. |
| D2 | Group A: the axis-set duty matched neither sibling — mandatory-flag-if-absent (layers/proofs) nor stated-conditional (design-principles) — leaving book / CLI / skill pack / custom unaddressed. | FOLDED (E2) — the per-kind axis set is a mandatory declaration flagged if absent [INV-135, A-10]; a kind may declare "none beyond the floor" as an explicit stated decision [INV-136]. The conditional reading is disproved by INV-244's own backend aside (a non-visual kind owes load/version/tenant). |
| D3 | Group A residue: the C-1 split made it a hybrid (enumerated floor + open kind-owed tail) that INV-226 asks a law to self-declare. | FOLDED (E3) — C-1 states its hybrid shape explicitly [INV-226]. |

## Pass 3 — adversarial confirmation + red-first proof

Hypothesis pressed: the architecture's "the founding check reds on silence, passes on explicit none" is
either false or rides the wrong mechanism. Result: the behaviour holds, and the mechanism attribution was
corrected. The red-on-silence/pass-on-none check is a presence-check embodied in the test (mirroring
INV-135's `founding_complete`), not `founding-questions.json` — that file drives the separate INV-227
update-check that names a new question to an older host, and it reds nothing. An explicit
`project.axes: none beyond the C-1 floor` line is present text, so a presence-check passes it and reds only
true silence. No production guardrail beyond the test is needed for the finding; the founding-questions
entry is still owed for the update-check duty and was wired.

Red-first proof: three teeth red against the current tree before the code — the spec-author skill did not
name the law, the founding-questions set did not carry the axes question, ADOPT did not record
`project.axes`. Ten of thirteen red against HEAD. The three self-contained fixture tests
(reds-on-silence, passes-on-explicit-none, visual-kind-passes) stay green as a pinned check contract, the
same structural property as INV-135's fixture tests. Wiring turned the three teeth green; compaction cleared
the clause's three open redundancy pairs back to the floor of 0. Full suite 1693 passed, 2 skipped;
redundancy floor 0; both register gates clean on every edit region.

Verdict: PROCEED. The landing carries no green-but-hollow surface — the finding fires from a wired sweep,
the check reds real drift, and the mechanism claim is corrected in the architecture record.
