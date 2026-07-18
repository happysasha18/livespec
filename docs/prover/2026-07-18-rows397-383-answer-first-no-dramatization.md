# Prover record — 2026-07-18 — rows 397 + 383 (two chat/register machines)

Mode: CROSS-LINK. Two small deltas add to existing surfaces of the chat/register family. The whole spec
was proven FULL at the 2026-07-17 MINOR gate and re-checked at the batch-4 push (2026-07-18 ~04:17), with
no structural change since — this pass proves the two new surfaces against the named existing surfaces they
seam to. Single senior seat, no worker dispatch [INV-103].

Footprint: both cross-cutting in reach (they touch a shared chat/register law family) yet small in size —
each adds one Formal-index invariant, one owning-node entry, one matrix row, and one test file. The door is
feature for 397 (a new mechanical surface, the answer-first arm) and feature for 383 (a new pack law with a
carried clause). Work-kind: infra for 397 (a hook tool), skill/prose for 383 (a law statement plus a
delegation-guidance clause). The full pipeline ran on both.

## Surfaces under change

- **INV-220** (ROADMAP 397) — the answer-first arm. A Stop-hook notice `hooks/answer-first-scan.py`
  reddening a chat reply over a length floor whose opening block is a wall with no short lead. Owning node:
  guardrails (the chat-judge family, beside INV-202 the net-meter and INV-203 the register judge). New pin
  `hooks/answer-first-scan.py:1`. Installed byte-identical to `~/.claude/hooks/`, wired into the settings.json
  Stop chain under the net-meter, and classified in `guardrails/judge-hooks.json` (gate v).
- **INV-221** (ROADMAP 383) — no dramatization, in either direction. Grading the size of a change is the
  reader's act, both poles one bias. Owning node: build-pipeline (beside the sibling language law INV-166).
  New pin `skills/build-pipeline/references/delegation-protocol.md:1` (the worker-brief register-laws clause).

## Why 383 builds no redundant machine (the coverage check, done first)

The register judge (INV-203, landed this movement) reads the graded-size class on BOTH machine-readable
surfaces: the chat surface (a Stop arm) and the document surface (the pre-show register lint's ceiling). Its
personal overlay carries the empty-intensifier law (LAW 2), whose text is "any adjective grading how
important a result is", a class covering both poles in any language. The literal overlay `scissors-personal.json`
carries the plus-pole patterns (`в корне`, `меняет дело`, `переворачивает`) and the minus-pole patterns
(`катастрофа`, `провал`, `полностью сломан`). So the two machine-readable surfaces already hold the class.

Verified both poles fire on the live personal overlay this run (the installed `scissors-scan.py` reading the
real `~/.claude/hooks/scissors-personal.json`):

| Pole | Sample | Fired |
|---|---|---|
| plus | «Это в корне меняет дело и полностью переворачивает подход к задаче.» | yes |
| minus | «Это катастрофа, подход полностью сломан.» | yes |

The genuinely-remaining part is therefore not a machine but two prose facts: (1) the pack-level LAW — the
profile holds the personal value, and every host writing under the pack inherits the general law; (2) the
one surface the judge does not read — a worker's own report and its agent-to-agent messages — reached by the
worker brief carrying the law beside no-scissors. Both are prose, not a gate, because chat and inter-agent
text are emitted before any gate can read them (the same boundary the answer-first arm names). 383 states the
law and carries the clause; it adds no redundant judge.

## Cross-link seams checked

| Seam | Both sides present + named the same? | Verdict |
|---|---|---|
| INV-220 ↔ INV-203 (the register judge's async-report shape it borrows) | yes — INV-220 cites the one-turn floor, INV-203 unchanged | clean: a chat reply is already emitted, so both flag the previous reply and let the correction follow one message later; neither is a pre-push gate |
| INV-220 ↔ INV-173 (canonical hooks home + universal/personal split + setup-walk install) | yes — INV-220 ships as a universal pack hook in hooks/, installed by `install-pack-hooks.sh` | clean: the arm carries no personal data (a structural proxy), so it ships universal like scissors-scan.py; the personal answer-first LAW stays in the profile |
| INV-220 ↔ INV-175 / INV-180 (config-health parity: installed copy = source) | yes — the installed copy is byte-identical, config-health green | clean: the whole-hooks-dir diff covers the new file automatically |
| INV-220 ↔ INV-211 (gate v: every hook under hooks/ classified in judge-hooks.json) | yes — `answer-first-scan` added to the wired map, gate v green | clean: the self-widening honesty check would have redded an unclassified new hook |
| INV-220 ↔ INV-202 (the net-meter reads its runs and fires) | yes — wired under the meter wrapper in the Stop chain | clean: a silent net is read, not trusted; the arm emits decision:block, which the meter counts as a fire |
| INV-220 ↔ INV-70 (tunable defaults, told not asked) | yes — the length floor and lead thresholds are named tunable, not laws | clean |
| INV-221 ↔ INV-203 (the judge holds the class on chat + document) | yes — INV-221 names the judge as the class-holder on the two machine-readable surfaces | clean: no redundant machine; the judge stands as-is |
| INV-221 ↔ INV-173 (the worker brief carries it beside no-scissors) | yes — the delegation-protocol clause names both laws and the surface | clean: the worker's own output is the surface the judge never reads; the brief is where the law reaches it |
| INV-221 ↔ INV-183 (agent-to-agent messages bound too) | yes — INV-221 binds every text including agent-to-agent messages | clean: the worker-brief clause and INV-183's two-channel law agree — a message a worker writes obeys the register laws |
| INV-221 ↔ base rule 30 (a stated law with no machine is a wish) | yes — the law escalates from a twice-written habit to a stated law | clean: the class already has its machine (the judge); the escalation is the pack-level statement plus the worker-brief prose |

## Red-first proofs

- **397**: with `hooks/answer-first-scan.py` moved aside, `tests/test_answer_first_arm.py` fails to import
  (`FileNotFoundError`) — the red. With the arm present the module is green (18 tests). The proxy was tuned
  against fixtures to the scissors overlay's own rigor: **eight** method-first walls all fire, **thirteen**
  lead-first replies and **three** short replies none falsely flagged (0/16 false positives), two of the
  lead-first fixtures over 900 characters to prove the discriminator is the opening SHAPE, not the length.
- **383**: at the pre-delta tree (HEAD c93e987) the SPEC carries no INV-221 and the delegation guidance
  names no no-dramatization law, so `tests/test_no_dramatization_law.py`'s law/clause assertions fail — the
  red. With the law and clause landed the module is green (8 tests), the judge mechanism reddening a
  graded-size sentence at both poles against canned model responses, and the live overlay confirmed above.

## Architecture lens

ARCHITECTURE.md changed (two owns-list entries + two pins). The lens checks pass: every new index anchor has
exactly one owning node (INV-220 → guardrails, INV-221 → build-pipeline; the anchor-uniqueness suite check is
green after removing two cross-node citations from the INV-221 descriptor that the anchor parser scraped as
false ownership), each new pin resolves to a real file within its length, and both seams above are walked.
This is a CROSS-LINK pass, not a milestone FULL pass, so the ARCHITECTURE Prover-record table is not appended.

## Open decisions touched

None. No ⟨DECIDE⟩ marker sits on either surface.

## Findings

Zero must-fix. One recommendation, folded in the same pass: the answer-first arm reads the FINAL reply
rather than the whole turn, unlike the register judge which reads every message since the last human turn.
This is deliberate and stated in the source and the invariant — a lead is owed by the reply the person
reads, not by the short inter-tool narration lines — so it is a scoped honest boundary rather than the
last-message defect the meter once caught in the scissors scan.
