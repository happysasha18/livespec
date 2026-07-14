# Design review — the request-layer classifier and its two siblings, 2026-07-14

**Skill version:** design-reviewer 1.0.0. Runs right after the prover (INV-141), on the same proven delta.
Recommendations and questions only; nothing here blocks the landing.

**Scope:** the request-layer classifier delta (INV-151/152/153). This is a method change, so the design
review reads the method's own elements — the routing controls and the closed-set entries — as the elements
a session acts on.

## The same-kind group the delta itself declares

The three routing controls are a declared same-kind group, and INV-153 names the group and states its
parity in one clause: a request (INV-151), a property (INV-150), and a work item (INV-152) each route to
the home whose declared sentence governs them, and each has a homeless-item finding when nothing governs
them. Behaviour parity within the group, checked:

| control | routes by | homeless-item finding | verifier |
|---|---|---|---|
| request classifier (INV-151) | highest document its change reaches | matches no kind → one plain question (INV-4) | the applied-or-stood-down-by-name landing contract (INV-22) |
| property net (INV-150) | the net that can pin the violation to a sentence | a declared law with no net → a broken invariant (INV-101) | the declared-laws station on every prover pass (INV-101) |
| deferral test (INV-152) | the seat, unless a human-only fact is named | a marker that cannot name its fact → defaults to the seat, the finding | the seat's derive-before-defer posture (INV-143) |

The three members behave alike on the axis that matters — route-to-declared-home, and the un-routable item
is itself the finding — and diverge only where the audit says they must: different moments, different
verifiers. INV-153 declares the group rather than leaving it undeclared, so this parity is now a spec
sentence the prover holds, not a design-review observation. No divergence to echo.

## The closed-set entries as a second same-kind group

The eleven entries of the closed door set are a same-kind group: each is (kind → home → mandatory
back-check). Parity check — does every entry carry a real back-check, or is one silently blank? Walked:
ten entries name a back-check; only "research / a question from the docs" carries "—", and that is correct
by design (no write means no layer and nothing to back-check), stated as such rather than left blank. No
divergence: the one blank is a decided sentence, not an omission.

## Questions echoed to the human

None rise to an ask. The delta declares its own groupings (INV-153 for the controls, the closed set for the
entries) and states their parity, so the design review finds no undeclared same-kind group and no unexplained
divergence. The one taste-adjacent point — whether the deferral clause should ever name the design review as
a watch-level net the way a property can (INV-150) — does not apply here: a work item is routed by the seat
or the human, not by a review pass, so there is no watch-level option to offer.

## Verdict

The design behind the delta is consistent: the routing controls behave alike where they should and diverge
only where declared, and the closed set's entries each carry their back-check or a decided reason for none.
No recommendation blocks; no question needs the human. Recorded for the milestone gate's design-review walk.
