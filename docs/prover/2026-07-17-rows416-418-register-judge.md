# Prover record — rows 416 + 418, the register judge (2026-07-17)

One movement, two rows folded into one landing (the roadmap orders the fold): a register law that names
a CLASS is held by a model that reads meaning, and a list of literals holds nothing. Row 416 is the chat
surface, row 418 the document surface; the class is "a register law whose machine enumerates instances",
the two surfaces are its instances, and one mechanism serves both — the head rule applied to the head
rule's own repair.

Prior record checked: `docs/prover/2026-07-17-row391-net-meter.md` — no unfolded rows carried forward.

Full form (surface-sized delta touching a shipped gate: the pre-show register gate + the Stop-hook chat
scan). Lens: FULL cross-link on the changed surfaces + the six architecture checks.

## Spec cross-link (INV-83 restated, INV-203 new)

| # | finding | folded / rejected |
|---|---------|-------------------|
| 1 | INV-83 carried a growth DUTY ("the set grows by one per caught leak") that the pack's own head rule contradicts — a list is the wrong answer to a class. The duty was doctrine, shipped to every host. | folded — INV-83 rewritten: the set grows by nobody's duty, the doctrine retracted 2026-07-17; the register judge [INV-203] holds the residual class; the literal list stays the free first pass. |
| 2 | INV-83's tail deferred the chat gate to "queue row 203" as unbuilt. The judge builds exactly that gate. | folded — the tail now names the register judge's chat arm [INV-203] as the mechanical gate once queued; both surfaces rest on the judge. |
| 3 | A new mechanism (the judge) with no invariant is unbacked behaviour the prover flags. | folded — INV-203 authored, prose + Formal-index row, owned by the guardrails node. |
| 4 | INV-94 (self-certification) says caught phrases "join the register lint's pattern family as its own class" — a faint echo of the growth duty. | rejected as a blocker — INV-94 describes membership, not a standing per-leak growth command; it names no duty to grow a list forever. Left as-is; a sweep of its phrasing is not this row's delta. Noted for the next full audit. |
| 5 | The judge makes a live model call; a document-surface judge wired into the deterministic suite/push gate would make green non-deterministic. | folded — the document judge is opt-in (PRESHOW_REGISTER_JUDGE), off by default; the literal list carries the deterministic gate; INV-203 states this explicitly. |

## Architecture lens (six checks, guardrails node)

1. **Every spec fact owned by one node.** INV-203 → guardrails node owns-list (added), with pins to
   `hooks/register_judge_core.py`, `hooks/register-judge.py`, and the two arms. INV-83 stays
   communicator-owned; the stray `[INV-83]` anchor first written into the guardrails owns-column was
   caught by `test_architecture_owns_every_anchor_once` (dual ownership red) and removed — the
   traceability suite doing exactly its job. PASS after the fix.
2. **No node without spec backing.** The judge files are backed by INV-203; no speculative node. PASS.
3. **Every seam names what crosses it.** The judge dispatches text over stdin to `claude -p` and reads a
   strict-JSON verdict back; the collect arm writes the verdict to `~/.claude/hooks/.judge/<session>.json`,
   the report arm reads and deletes it. Named in INV-203 and the hook docstrings. PASS.
4. **Quality budgets + instrumentation home.** The judge's usefulness is a number the net-meter reads
   (runs/fires, INV-202), wired through `hook-meter.py` on this host; its watcher is the meter, its
   retirement the owner's word. PASS.
5. **Runtime view walks the flow.** Chat: Stop → collect (background judge) → verdict file →
   UserPromptSubmit report → the model sends the correction one turn later. Document: pre-show literal
   scan → opt-in judge ceiling → block or clean. Both walk end to end. PASS.
6. **Placement view.** The chat judge runs on the host machine (installed `~/.claude/hooks/`); the
   document judge runs in the host repo's suite/pre-show gate; the model call goes to the external
   `claude` binary. The mechanism source is `hooks/`, shipped by the pack, installed by the setup walk
   [INV-173]. PASS.

## Design review (scoped — surface add)

Same-kind grouping named: the two literal register nets (the Stop-hook scissors scan; the pre-show
register lint) are one kind — "a literal-pattern register net whose law names a class." Behaviour parity
after the delta: BOTH now keep their literal list as the free first pass AND gain the class-reading judge
above them (scissors scan → register-judge chat hook; preshow lint → the opt-in document judge). The two
were divergent before (only the document surface had a "ceiling" named, the clean-reader check; the chat
surface had none), and the landing makes them parallel — the judge is the shared ceiling. No open
divergence to carry to the human.

## Verdict

0 must-fix open. One recommendation parked (finding 4, INV-94 phrasing) for the next full audit, not a
blocker. The delta red-proved before green (register_judge_core.py absent → the judge test module fails
to collect; the spec still carried the growth doctrine → the retraction test red), then green.
