# Prover record (architecture lens) — the cross-cut counter — 2026-07-12 s41

Prover skill version at this pass: product-prover 1.0.6. Mode: architecture lens (SPEC INV-116), because
this row touches the node-map's own law (boundary health) and its mechanical enforcement. No new node and
no new seam — the six architecture checks are walked at the pack's kind scale to confirm the structure still
holds under the added law and its check.

## The delta

The cross-cut counter (`guardrails/crosscut_counter.py`, row 293) mechanizes the boundary-health signal
INV-128 stated and deferred: it counts the closed queue's cross-cutting landings per unordered node pair
and flags a pair reaching the threshold (3 by default) as a boundary-move candidate for the MINOR audit.
The ARCHITECTURE Boundary-health section is updated from "the counter is a follow-on row's mechanical half"
to naming the landed check, its threshold, and its advisory (never push-blocking) nature; build-pipeline's
before-a-MINOR gate now runs it. Anchors: INV-128 (boundary-health), INV-37 (the re-carve through the
architecture step), base rule 19 (seen-twice-own-it).

## The six architecture checks (kind scale: a skill pack)

1. **Every spec fact has an owning node.** No new spec fact — the counter enforces the existing INV-128
   boundary-health law and INV-37 re-carve, both already owned by build-pipeline. Holds.
2. **No node stands without spec backing.** No new node. The counter is enforcement machinery under the
   build-pipeline / guardrails district, not a node of its own. Holds.
3. **Every seam names what crosses it and who owns the format.** No new seam. The counter reads the
   closed queue's `footprint:` notes (an existing artifact, ROADMAP.md) and writes an advisory list; it
   adds no inter-node data flow. Holds.
4. **Quality budgets stated with instrumentation homes.** Unchanged — the counter is itself an
   instrumentation home for boundary health (the recorded footprints made countable), reading the queue
   the boundary-health law already names as its evidence. Holds.
5. **Runtime view walks every promised flow.** The counter runs at the MINOR-audit flow (build-pipeline's
   before-a-MINOR gate), a build-time read on the author's machine over the queue file — no new runtime
   path, an added read at an existing gate. Holds.
6. **Placement view says where every node runs.** The counter runs build-time on the author's machine
   (guardrails placement), like the other guardrails checks. Holds.

## Findings

**0 must-fix.** Boundary-health composition checked: the bar (a typical request lands in one node) and the
signal (repeated cross-cuts on one node pair) were already stated (INV-128); this landing makes the signal
countable without changing the law. The flag is explicitly advisory — a boundary still moves only through
the architecture step and its re-prove (INV-37), so the counter never bypasses the human's re-carve
judgement. The counter run on the live ROADMAP flags exactly one pair (architecture <-> spec, 3
cross-cutting landings from the recent method-law rows) — a true reading, correctly advisory, not a defect:
these are shared-law landings that inherently touch the spec and the architecture together, and the MINOR
audit weighs whether that is a boundary smell or the nature of method-law work.

## Verdict

Architecture-lens pass clean, 0 must-fix. Structure unchanged; the boundary-health law gains its mechanical
counter without a new node or seam. Suite green.
