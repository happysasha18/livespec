# Prover record — 2026-07-18 — rows 384 + 387 (gate-correctness pair)

Mode: CROSS-LINK. Two new gate surfaces added to the guardrails node; the whole spec was
proven FULL at the 2026-07-17 MINOR gate and the batch-4 push re-check (2026-07-18 ~04:17),
with no structural change since — this pass proves the two new surfaces against the named
existing surfaces they seam to. Single senior seat, no worker dispatch [INV-103].

## Surfaces under change

- **INV-218** (ROADMAP 384) — a check that looked at nothing is not a pass. The shared shape
  `guardrails/nonempty_input.py` and its first instance, the index prose gate
  `guardrails/check-index-prose.py` (gate x). Owning node: guardrails.
- **INV-219** (ROADMAP 387) — the card's gate reads the host's own tree. The gate
  `guardrails/check-agent-card.py` (gate y). Owning node: guardrails. Removes INV-184's [target].

## Cross-link seams checked

| Seam | Both sides present + named the same? | Verdict |
|---|---|---|
| INV-218 ↔ INV-155 (the unexpected-skip law it is the sibling of) | yes — INV-218 cites INV-155, INV-155 unchanged | clean: the empty-input case is the input-set analogue of the unexpected skip; parallel enforcement (declare the expected set, red by name on the void) |
| INV-218 ↔ the Formal-index code→home promise | yes — the index prose gate is the first instance, `test_spec_index_unique_anchors` named as the prior partial net | clean: the uniqueness check stands; the new arm adds index→home-prose, the gap it never covered |
| INV-218 ↔ the gate chain (gate x in pre-push, CI, meta-gate) | yes — pre-push gate x, gates.yml gate x, gate-red-proofs.json proof x | clean: gate u (CI-mirror) and gate w (meta-gate) both re-read the chain and pass |
| INV-219 ↔ INV-184 (the declaration law whose [target] it removes) | yes — INV-184 prose + index rewritten, target-map [S-0] owner list updated in lockstep | clean: INV-184's prose literals stand whole; only the [target]-deferral tail is rewritten to name the live gate; the law now carries its own mechanical net, so [INV-101]'s "a declared law with no net is a broken invariant" is satisfied |
| INV-219 ↔ A-10 (the kind-with-no-layers flag it is the sibling of) | yes — INV-219 cites A-10 | clean: a card-less tree is flagged the same rank a layerless kind carries |
| INV-219 ↔ INV-97 (the pack as its own first host) | yes — the gate reads the pack root by default, the pack carries its own card | clean: honest self-application; the gate reads this tree and passes, so it never reds its own push |
| INV-219 ↔ A-11 / INV-159 (adoption's line, bind-forward) | yes — adopt/ADOPT.md names the card in the canonical set, the duty binds forward | clean: a pre-law tree writes its card at its catch-up walk |

## The self-application question (387)

The gate reds a live-spec host tree carrying no `.live-spec/agent.md`. The pack IS a host
[INV-97], so the honest question is whether the gate reds the pack's own push. It does not:
the pack carries its card at `.live-spec/agent.md` (verified on disk; the existing
`tests/test_agent_channels.py::test_pack_card_exists_and_names_its_five_fields` already reads
it). The gate's scope is one tree — the host's own, read by deed — so it makes no claim about
other hosts' trees it cannot reach; those take their card at catch-up [A-11], the discovery of
OTHER agents' cards staying the live scan [E-32]. No finding.

## Vacuous-pass self-check (384)

The index prose gate is itself a check with an input set (the Formal-index anchors), so it must
not be the very defect it names. It declares that input set through `require_nonempty` and reds
by name when the index parses to zero — proven on a fixture whose index section carries no rows.
So the gate cannot pass by looking at nothing. No finding.

## ⟨DECIDE⟩ touched

None. Neither surface touches an open decision.

## Findings

| # | Finding | Folded / rejected |
|---|---|---|
| — | none must-fix | — |

0 must-fix. Both surfaces derive cleanly from their named siblings; the gate chain re-reads
them under gate u and gate w and passes; the full suite is green.
