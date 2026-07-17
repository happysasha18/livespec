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

## Corrections after adversarial review 2026-07-17

An adversarial review the same session read the landing and found six defects, two of them defeating the
row's own claim. Two claims in the record above were false and are corrected here: the landing said the
PLACE fix worked, and it said the judge was wired live. Neither held. The judge delivered no verdict at
all — `~/.claude/hooks/.judge/` held only `.err` files, zero verdicts — and the whole-turn read fetched
the wrong slice. Each defect was fixed on top with a red proof first.

1. **The chat judge delivered no verdict — a wait-on-non-child race destroyed every one.**
   `register-judge-collect.sh` backgrounded the judge, then ran `wait $!` in a sibling subshell; the
   judge was not that subshell's child, so wait returned at once, the still-empty `.part` was removed,
   and the judge finished writing into an unlinked inode. Red proof: `tests/test_register_judge_collect.py`
   drives the collect arm with a stubbed judge that sleeps then writes a verdict, and asserts the verdict
   file appears — it timed out against the old script (verdict destroyed), passes now. The report arm's
   read is covered too. Fix: one subshell owns both the write and the rename, wrapped in `nohup`. Source
   fixed and re-installed to `~/.claude/hooks/` (self-install granted); config-health stays green
   (source == installed).

2. **The whole-turn gather read the wrong slice.** `turn_text` walked back to the last `type=="user"`
   record as the turn boundary, but every tool result in a real transcript is a `type:"user"` record, so
   it read only the text after the final tool call — the last-message defect the row claimed to fix. Red
   proof: `test_turn_boundary_skips_tool_result_user_records` builds a transcript with an offending early
   message, a tool_use, a tool_result user record, and a clean final message, and asserts the offending
   text is gathered — it was excluded before, included now. Fix: skip user records whose content is a
   tool_result when finding the boundary.

3. **Quote validation was substring-only both directions.** A hallucinated offence quoting a trivial
   substring like "the" survived, and a real offence past the quote cap was dropped once the model
   truncated with an ellipsis. Red proof (both directions, canned responses):
   `test_trivially_short_quote_is_rejected` and `test_long_offence_recovered_when_model_truncates_over_the_cap`.
   Fix: a minimum meaningful-length floor drops trivially short quotes; the prompt asks for a bounded
   verbatim span; `matched_span` recovers the longest verbatim leading prefix so a genuine long offence
   is kept.

4. **INV-94 still commanded per-catch list growth**, against INV-83's retraction — "each caught phrase
   joins the register lint's pattern family" in both the prose home and the Formal index. Red proof:
   `test_inv94_no_longer_commands_per_catch_list_growth`. Fix: both homes now say the judge holds the
   class and a caught phrase informs the judge and the first pass, the list growing by nobody's duty;
   INV-94's subject (no line certifies its own sincerity) stays intact, traceability stays owned.

5. **A missing installed hook was a green skip**, so the judge could go dark with every gate green.
   `check-config-health.sh` skipped a sourced hook that had no installed copy. Red proof:
   `test_a_sourced_hook_missing_from_install_reds_as_drift`. Fix: a source hook with no installed copy is
   drift and reds; an installed-only overlay with no source stays silent
   (`test_an_installed_only_overlay_with_no_source_stays_silent`). Residual for row 420's gate audit: this
   arm proves the installed file exists and matches, not that settings.json still lists the
   Stop/UserPromptSubmit judge entries — that check is harder because settings.json is personal-layer.

6. **The owner's personal register bank shipped verbatim in a public test.** `tests/test_register_judge.py`
   reproduced the real personal scissors patterns. Fix: synthetic neutral stand-ins exercise the same
   matching path (`test_personal_overlay_patterns_are_exercised`), with no real personal phrase in the
   shipped test.
