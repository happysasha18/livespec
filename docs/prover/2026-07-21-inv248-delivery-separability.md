# Prover record — INV-248, the delivery-separability lens (2026-07-21)

PROVER-RECORD

Prover skill version: product-prover under live-spec-base v3.5.0.
Mode: FULL adversarial pre-push review of the INV-248 delta (ROADMAP 438), run in a FRESH independent
context — not the seat that authored the clause (SPEC INV-237). Opening hypothesis: "tasks completed,
goal missed." The new lens was self-applied to its own introducing documents (INV-237 self-application).

Verdict: **PASS with two recommendations, the strong one folded before this record.** No must-fix. The
opening "goal missed" hypothesis was refuted — every claimed home carries substantive text, the tests
are genuinely red-then-green against HEAD 4dd3857, INV-248 is owned exactly once, and M-433 sits under
the spec-author node citing the seven real test defs, all green.

## The delta judged

- PRODUCT_SPEC.md — the INV-248 clause beside INV-244 + the Formal-index row.
- skills/product-prover/SKILL.md — the lens bullet after the INV-49 lens + the dual-discovery habit.
- skills/spec-author/SKILL.md — the authoring duty (state the delivery answer where an owed axis adds runtime code).
- ARCHITECTURE.md — owned by the spec-author node, carried by the product-prover node (the INV-49 precedent).
- TEST_MATRIX.md — M-433 under [node: spec-author].
- tests/test_delivery_separability.py — 7 tests.

## Findings

**F1 — the viewport example could invite over-application (RECOMMEND, FOLDED).** The illustrative axis
list named the viewport — the canonical pure-CSS/media-query axis — as an axis the lens reaches, without
the reminder that the lens fires only where covering the axis ships runtime code. A careless prover could
over-apply to responsive CSS. Folded: the clause and the lens bullet now say each axis is reached "only
where covering that axis ships runtime code," a viewport answered by a media query or a locale by a
logical property drawing no delivery question. The top-level runtime-code gate was already explicit; this
removes the trap in the example.

**F2 — the general dual-discovery habit rides a specific invariant (RECOMMEND, ACCEPTED as-is).** The
dual-discovery habit is a general prover practice yet is homed inside INV-248, where a reader hunting the
prover's dual practice would not look. Accepted as the habit riding its originating clause: it was found
AS this lens's dual, so its birth home is honest, and it lives in the product-prover skill prose (not the
spec as an enforceable invariant), which is the right register for a habit. Left as-is by decision.

## Distinctness from INV-244 (the redundancy charge)

Refuted. INV-244 flags a COVERAGE gap — an owed axis value the code leaves unhandled, the visitor falling
through. INV-248 flags a DELIVERY-SHAPE gap — every axis value bundled into one artifact with no named
reason, the visitor getting too much. Orthogonal: a monolith can fully cover every axis value (INV-244
green) and still ship every value's code to every visitor (INV-248 concern). Behaviour-split versus
artifact-split is a genuine second obligation.

## The "senior read, never a gate" stance

Consistent with the tests. The tests assert only that the documents CARRY the lens and habit text; they
never mechanically fire the lens on a sample spec — correct, since the lens is an un-executable senior
judgment, so there is nothing to fire and no false-green risk.

## INV-237 self-application

Confirmed correct and vacuous. live-spec's own kind is a skill pack, which declares `project.axes: none
beyond the C-1 floor` (.live-spec/profile.md) — an explicit stated decision that it owes no composition
axis. INV-248's trigger therefore has no runtime-code composition axis to fire on in the pack's own
documents, so the lens finds nothing to flag in its introducing docs — the right self-application result.
Stronger confirmation of the clause's "some duals fold into a lens already run": the one place the pack
ships runtime code, the guardrail/gate kit, is delivered along the pack-to-host axis, whose delivery
decision (centralize versus ship-the-shape) is already owned by INV-163/INV-172 — a dual folded into an
existing lens.

## Register, stubs, traceability

No banned contrast-frame scissors in the new clauses; the one comma form ("reads the design's own reason,
not a diff") mirrors the sibling INV-49 lens verbatim, the established house idiom. No sentence leads with
an internal code. No TODO/FIXME/placeholder/stub in the delta. Seven cited test defs equal seven file
defs, all green; INV-248 owned once; M-433 correctly homed.
