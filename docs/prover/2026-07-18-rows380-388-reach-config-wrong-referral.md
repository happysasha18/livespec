# Prover record — 2026-07-18 — rows 380 + 388 (reach classes as config · the wrong referral named)

Mode: CROSS-LINK. Two surfaces changed — one on the guardrails node (INV-224), one on the
base-rulebook node (INV-225). The whole spec was proven FULL at the 2026-07-17 MINOR gate and
re-checked on the 2026-07-18 batches, with no structural change since; this pass proves the two
surfaces against the named existing surfaces they seam to. Single senior seat, no worker dispatch
[INV-103]. Previous prover records' unfolded rows: none open.

## Surfaces under change

- **INV-224** (ROADMAP 380) — the reach map's directory classes are host config. The infra
  directories, prose files, and referrer directories move from `guardrails/check-push-reach.sh`
  body constants into `guardrails.config.json` under `reach_classes`, the pack's values shipped
  as the default; the script reads them, a host adopts via its own declared layers [INV-135].
  Owning node: guardrails. Extends the existing reach gate — no new gate letter.
- **INV-225** (ROADMAP 388) — a wrong referral is named as the finding. When a referral points at
  a zone that does not own the target, the exchange loops back over the same pair and the escalation
  names the wrong referral rather than the neutral "could not settle". Owning node: base-rulebook.
  A suite-riding checker `guardrails/check-wrong-referral.py`, not a push gate.

## Cross-link seams checked

| Seam | Both sides present + named the same? | Verdict |
|---|---|---|
| INV-224 ↔ INV-45 (the reach map it lives under) | yes — INV-224 sits in INV-45's clause region, cites the scoped middle road | clean: the classification LOGIC is unchanged; only the source of the class lists moves from body to config. The default config reproduces every INV-45 / M-142 / M-344 verdict (asserted by the untouched reach tests, all green) |
| INV-224 ↔ INV-135 (project.layers) | yes — INV-224 cites INV-135, which already carries "the footprint check and the test-level rule read the project's declared categories rather than a hardcoded code list" | clean: the reach classes are the same per-project knowledge project.layers names; INV-224 is that principle reaching the reach gate's own class lists |
| INV-224 ↔ the conservative floor (INV-45's "conservative by construction") | yes — a config with no classes leaves every file unclassified → FULL | clean: the floor is preserved and strengthened; a missing/empty config can only over-run, never false-green scope. Red-proven by `test_reach_default_config_reproduces_todays_verdicts`'s empty-config arm |
| INV-224 ↔ the suite-hygiene net (ROADMAP 366, TestScopedReachHygiene) | yes — the net's `_infra_dirs_from_config` now reads referrer_dirs from the config's one home | clean: the "one home, never a second copy" property the net's own docstring asserts is now literally true — script and net read the same config key |
| INV-225 ↔ INV-196 (the two-crossing bound) | yes — INV-225 refines INV-196's cap event | clean: INV-196 counts the same-pair re-crossing and escalates; INV-225 makes that escalation NAME the wrong referral. INV-196's prose stands whole; INV-225 adds the naming beneath it |
| INV-225 ↔ INV-190 (the referral direction) / INV-150 (the honest split) | yes — INV-225 cites both | clean: the referral still travels back to the asker [INV-190]; whether the target falls inside a zone's claim stays the sweep's and prover's judgment [INV-150], and the checker reads only the exchange SHAPE |
| INV-225 ↔ INV-83 / INV-222 (chat surface not gatable, the far-tier sibling) | yes — INV-225 names the checker as riding the suite not the push chain | clean: the exchange is a status-report surface with no committed file to gate, the exact shape check-far-tier.py already takes; no new gate letter, no gate-red-proofs entry owed |

## The mechanical-distinguishability question (388 — the STOP condition)

The build brief flagged one condition to STOP on: if a wrong referral cannot be told from a
legitimate cross-zone referral mechanically, report the tradeoff rather than build a false-precision
check. The finding after proving it: **the two are indistinguishable at the moment of sending** —
both read "that lives in zone X's zone, ask X", and whether X's claim covers the target is a
natural-language match, the prover's and sweep's judgment [INV-150]. They become distinguishable
from the exchange's OUTCOME: a legitimate referral is answered by the named zone (or carried onward
to a real third zone that answers) and reaches no cap; a wrong referral is met by a counter-referral
between the same two agents — the pointed-at zone's own act of referring it back, which is what
proves it does not own the target — and reaches INV-196's cap. That outcome is exactly the event
the two-crossing bound already observes, so INV-225 adds no new detection, only the naming. No STOP:
the distinction is mechanical (referral-answered-by-counter-referral vs referral-answered-by-
acceptance), and the checker claims nothing beyond it — it never judges the target-vs-claim match.
The overlap/uniqueness half of the audit finding is refused by the owner's word (zones may overlap,
no forced disjointness; promoter inbox deposit 2026-07-17), so no uniqueness or overlap check is
built.

## ⟨DECIDE⟩ touched

None. Neither surface touches an open decision.

## Findings

| # | Finding | Folded / rejected |
|---|---|---|
| — | none must-fix | — |

0 must-fix. Both surfaces derive cleanly from their named siblings; the reach change preserves every
existing reach verdict under the default config and is red-proven on a reclassifying fixture config;
the wrong-referral checker is red-proven on a wrong exchange and passes a correct and an onward one.
Full suite green.
