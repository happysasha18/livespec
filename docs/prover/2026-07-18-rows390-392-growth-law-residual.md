# Prover record — ROADMAP rows 390 + 392 residual legs (the growth-law family)

Date: 2026-07-18 · Doc version proven: v2.6.3 · Mode: CROSS-LINK + architecture lens · Kind: infra ·
Form: SHORT-FORM (SPEC INV-61 — a skill/prose/infra delta, no new surface, no structure change: two
anchors on existing nodes, two new guardrails mechanisms, gate z wired).

## What landed

The grooming/rotation leg of both rows landed earlier 2026-07-18 as INV-209 (gate t, `scripts/rotate-doc.py`).
These are the RESIDUAL legs:

- **Row 390 — the node-growth law (INV-233).** A node's fitness is re-answered as it grows, and node
  co-residence in one file is the counted signal. The ratcheted counter `guardrails/node_growth_counter.py`
  reads nodes-per-file from ARCHITECTURE.md's own pin column (distinct nodes naming a file); its ratchet
  `guardrails/node-file-cap.json` is seeded at the current count so the tree lands green and any increase
  reds, the cap ratcheting down only [INV-164]. It RIDES THE SUITE (`tests/test_node_growth.py`), taking
  no push-gate letter — the sibling of the prose-debt cap. The prover's seventh architecture lens (the
  growth re-ask) and the design-review split-proposal shape are stated in their skills. Owner: build-pipeline
  (kin of INV-122 / INV-128 / INV-164).

- **Row 392 — the growable-artifact bound (INV-234).** Everything that can grow declares the number that
  bounds it and the watcher that reads it (INV-41's shape lifted to every growable artifact). The four
  large working docs each declare a byte ceiling with a recorded reason in `guardrails/doc-bounds.json`,
  and the watcher `guardrails/check-doc-bound.py` (gate z, wired local + CI) reds a doc past its ceiling.
  It composes with INV-209: crossing the bound earns a rotation, and rotation is the remedy the red points
  to. Owner: guardrails (sibling of gate t / INV-209).

## Architecture lens — six checks, each at the infra kind scale

1. **Every spec fact owned by exactly one node.** INV-233 → build-pipeline owns-list; INV-234 →
   guardrails owns-list. `tests/test_traceability.py` (gate b) asserts single ownership; green.
2. **No node stands without spec backing.** No new node; both anchors land on existing nodes. Pass.
3. **Every seam names what crosses it.** No new seam. Pass.
4. **Quality budgets with instrumentation homes and watchers [INV-41].** INV-234 IS a budget-with-watcher
   instance (the four docs' byte ceilings + gate z), and INV-233's counter is the watcher for the
   nodes-per-file budget. Both name their instrumentation home (the config JSON) and their watcher (the
   check / the suite test). Pass.
5. **Runtime view walks every promised flow [INV-74].** The node-growth counter runs at every suite run;
   gate z runs at every push (local + CI). Both flows walk end to end. Pass.
6. **Placement view says where every node runs [INV-75].** Both mechanisms are build-time checks on the
   author's machine and in CI; unchanged placement. Pass.

## Findings

- **0 must-fix.**
- F1 (folded): the node-growth counter trusts the map, so an under-declared coarse map evades it. Folded
  into the spec clause and the counter's honest-boundary docstring, answered by the every-fact-owned-once
  backstop [INV-150] and the prover walking the map at every re-prove. This is Fable's own recorded
  objection from the row-390 consult, carried forward.
- F2 (folded): a doc-size ratchet that only ratcheted down would block every push once a doc grew past its
  seed, since the docs GROW until rotated. Folded by making the bound a CEILING that rotation resets (not
  a monotone-down number), with the recorded-reason discipline for a raise — verified the current tree
  passes gate z.

## Composition check (INV-209)

INV-234's clause and the gate's docstring both name the composition with INV-209 explicitly: the bound is
the trigger, the rotation (guarded by gate t) is the remedy. `test_doc_bound.py::test_spec_composes_with_rotation`
asserts the clause references INV-209; `test_gate_passes_a_freshly_rotated_doc` proves the composition at
the machine level (a doc over its ceiling but rotated today passes).

## Red-first proof

Both test files were run against the pre-delta tree: 29 failed, 3 passed (the 3 are "not-wired"
negatives, correctly green while the mechanisms were absent). Recorded in
`docs/prover/red-proof-2026-07-18-rows390-392-residual.txt`. After the build: 32 passed.

## Gate-chain touch

Row 390 (node-growth) does NOT touch the push chain — it rides the suite. Row 392 (doc-bound) adds gate z
to the push chain: `guardrails/pre-push`, `.github/workflows/gates.yml`, `guardrails/gate-red-proofs.json`
(proof z → `tests/test_doc_bound.py::test_gate_reds_a_doc_over_its_bound`). The meta-gate w
(every-gate-can-fail) and gate u (CI-mirror parity) both re-run green with gate z present. The current
tree passes gate z (the four already-large docs sit within their seeded ceilings).
