# Prover push re-check — v3.2.0 axes-from-kind landing (INV-244)

The M-6 whole-spec structural re-verify from a clean seat, run to satisfy the push gate's dated-record
requirement for today [M-6, INV-116]. It confirms the whole spec still holds together after the INV-244
axes-from-kind landing (v3.2.0), which was proven, design-reviewed, and adversarially tested hours ago in
docs/prover/2026-07-20-axes-from-kind.md and committed. Since that landing only NEXT_STEPS.md and
JOURNAL.md changed; PRODUCT_SPEC.md carries a zero diff against HEAD `f9ab498`, so this pass re-reads the
spec exactly as committed. The design decisions recorded on 07-20 are settled and are not re-opened here —
the pass reports regressions and fresh holes alone. The re-check is weighted to the INV-244 delta's blast
radius: the C-1 reshape and its citers, the founding-declaration composition, and the Formal index's
citation integrity. Guards PRODUCT_SPEC.md for the freshness rule [M-6].

## Pass — whole-spec structural re-verify, weighted to the INV-244 delta

Verdict: PROCEED. Every seam the reshape touches composes, no citer reads false against the floor+tail
split, and no dangling citation was introduced. The findings table below records the seams pressed and
what held; the one non-clean line is a pre-existing local-scope phrasing outside the delta that this
landing did not create and does not block.

| # | Seam pressed | Result |
|---|---|---|
| S1 | The C-1 reshape from one universal axis list to a kind-independent floor plus a kind-owed tail — does every clause that cites C-1 still read true? | HELD. All seven C-1 citers compose. The body states the hybrid at lines 2028 and 2042 ("the floor above is an enumerated set every stateful surface answers, and the kind-owed tail is an open set whose members a kind names one at a time"), and the C-1 index row (2438) carries the same shape with completeness reading "complete only once every floor axis and every kind-owed axis has an answer." The provenance-axis citer (2082, "trusted from the start [C-1]") and the time-split citer (407, sweep-versus-axis) are untouched by the reshape and stay true. |
| S2 | INV-72's completeness sweep against the floor+tail split — does the prover's whole-axis hunt now reach the kind-owed tail (input-capability), or does it silently walk the floor alone? | HELD, and held correctly by the one-home rule. INV-72 (body 2046, index 2310) reads "the whole axis list [C-1]" and "walks every axis," citing C-1 as the authoritative list rather than re-enumerating it. Because C-1 now carries the tail, "the whole axis list" resolves to floor plus tail, so the sweep reaches input-capability by reference. INV-244 confirms the routing from its own side: an owed-axis gap is "a finding of the same blank-answer class as a reachable situation the spec never wrote [INV-72]." Re-listing the tail members inside INV-72's prose would open a second home for the axis set and let it drift from C-1 [base rule 4]; the citation is the right design and the seam is clean. |
| S3 | INV-244 and the new `project.axes` per-kind declaration against INV-135 (layers/proofs) and INV-136 (design-principles) — double-ownership or a broken founding-check story? | HELD. Three founding declarations sit side by side, each in its own home: `project.layers`/`project.proofs` under INV-135 (2165), `project.design-principles` under INV-136 (2166), and `project.axes` under INV-244 (2385). INV-244 references the other two as siblings and claims ownership over neither. The founding check flags each independently — the axis set is "a mandatory founding declaration flagged if absent the way layers and proofs are [INV-135, A-10]," and a kind may declare "none beyond the floor as an explicit stated decision" on the empty-case pattern INV-136 already legitimises. The founding-check story is intact. |
| S4 | The Formal index carries INV-244 and its anchor set resolves; no dangling citation introduced. | HELD. INV-244's index row (2385) is present and complete. Every anchor sampled from the INV-244 and C-1 rows — INV-36, INV-135, INV-136, INV-226, INV-159, INV-18, INV-31, INV-30, INV-72, INV-138, INV-125, INV-126, INV-141, A-10 — resolves to exactly one index row. The forward markers [target] and [ROADMAP 437] are legitimate not-yet-specified reaches the clause names as later increments. No dangling citation was introduced. |
| S5 | Quantifier re-sweep — any universal, "only", or member-list sentence the reshape turned false. | HELD. The sweep over "every stateful surface", "the axis list", "canonical axes", and "only" across the axis section and the index found each universal correctly scoped: the floor's "every stateful surface answers, whatever its project's kind" (2028) and the visual kind's "every visitor-facing surface an open set of axes" (2058) both hold, and the visual kinds are named "among the project.kind values" — an open framing that admits a future visual kind rather than an "only". No enumeration reads false against the floor+tail split. |
| S6 | INV-226 (a general law declares whether it enumerates or rides) against C-1's new hybrid shape. | HELD. C-1 declares its own "enumerate-plus-ride shape [INV-226]" — an enumerated floor plus an open kind-owed tail. INV-226's index row (2367) names worked instances of the enumerate-or-ride choice without closing the example set, so a hybrid law self-declaring its shape satisfies its rule rather than contradicting it. This is the 07-20 record's D3 fold, and it stands. |

### One pre-existing item, outside the delta, non-blocking

INV-135's body sentence at line 1225 says the founding line that records `project.kind` "carries two more,
in the host profile: a `project.layers` line ... and a `project.proofs` line." Read in INV-135's own scope
the count is exact — those are the two lines this invariant contributes. Because `project.design-principles`
(INV-136) already stood as a separate founding line before this landing, the phrasing was already a
local-scope count rather than a spec-wide total, so INV-244 adding `project.axes` does not newly falsify it.
The landing under review did not touch this sentence and does not create the ambiguity, so it queues as a
pre-existing wording note rather than a delta regression [INV-114]; it holds no block on this push.

## Verdict

PROCEED. The three seams pressed hardest all held: the C-1 floor+tail reshape composes with every one of
its seven citers (S1); INV-72's completeness sweep reaches the kind-owed tail through its C-1 citation, and
does so correctly by the one-home rule rather than by re-listing the axes (S2); and INV-244's `project.axes`
declaration sits beside INV-135's layers/proofs and INV-136's design-principles as a third independent
founding declaration with no double-ownership and an intact founding-check story (S3). The Formal index
carries INV-244 with a fully resolving anchor set and no dangling citation. The whole spec holds together
after the INV-244 landing.
