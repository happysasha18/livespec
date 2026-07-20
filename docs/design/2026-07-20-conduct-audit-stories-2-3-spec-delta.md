# SPEC-DELTA — the conduct-audit movement (draft, for the orchestrator to apply under the pen)

> **STATUS 2026-07-20.** Section A1 (INV-241, the conduct judge) LANDED — but the shipped INV-241
> carries five prover folds not reflected in the A1 draft below (hedge-class repoint reverted, a
> built-in env-overridable default strictness, a forward-looking late verdict, a distinct verdict
> slot, and INV-237 dropped from the law body leaving four members). Read the SHIPPED spec (PRODUCT_SPEC.md
> INV-241) as truth, not A1. **What remains to build: A2 (INV-242, the landing-refreshed-map gate) and
> A3 (INV-243, the config-health skill-copy arm)** — both deterministic, no model call. Note A3's home
> was corrected from "Composing across axes" to the machines section (guardrails node), beside the
> config-health perms arm INV-216. Note A2's open detail: the push-gate letters a–z are exhausted, so
> it rides the suite or folds into an existing gate rather than taking a new letter.

Source: `docs/design/2026-07-19-reminder-dependent-capability-audit.md`.
Target spec: `~/live-spec/PRODUCT_SPEC.md`.
New codes minted: **INV-241** (conduct judge), **INV-242** (landing-commit refreshed NEXT_STEPS), **INV-243** (config-health skill-copy arm).
This file DRAFTS only. No repo file was touched.

Three buckets from the design doc land here: bucket 1 as a model judge (INV-241), bucket 2 as two
deterministic gates (INV-242, INV-243), bucket 3 stays deferred (stated as a non-goal in section C).

---

## (A) Scenario prose to insert

### A1 — Conduct judge (INV-241) — insert into `### The machines that hold the bounds  [not a scenario]` (the section that homes INV-203 and INV-238), as a new bold-headline entry beside the register judge

> - **The register judge reads what the seat SAID; a conduct judge reads what the seat DID.** The register
>   judge holds a class a fixed word-list cannot, by handing a turn's text to a model that reads meaning
>   [INV-203]. The same failure has a twin the text never shows: the orchestration laws are about the
>   seat's ACTS during the turn — whether it dispatched a long authored artifact or a deep read to a
>   worker, whether it routed each unit of work to the cheapest sufficient tier, whether it kept pulling
>   unblocked work or idled, whether it ran the deep audit by default — and no text arm can see an act.
>   The conduct judge generalizes the register judge from the turn's output text to the turn's **action
>   trace**: the ordered record of which tools the seat called during the turn, read from the `tool_use`
>   events in the transcript, not from the reply's words. A model reads that trace against the standing
>   orchestration laws and reds a violation after the fact, exactly as the register judge reds a register
>   violation in the turn's text. It is the net INV-150 demands for the orchestration laws that until now
>   named none — the members reminded twice or more become mechanically watched rather than reminded
>   [base rule 23, INV-108]. It reuses the register judge's own machinery: `hooks/register_judge_core.py`
>   supplies the judge frame, the one model call, the hallucination guard, and the stand-down-on-its-own-breakage
>   contract [INV-203], and this feature adds only the trace-reading arm around that core. The mechanism
>   runs async in the register judge's two-arm shape, because a meaning-judge is too slow to block a turn:
>   a Stop arm collects the verdict in the background when the seat finishes a turn, and a
>   UserPromptSubmit arm surfaces the collected verdict at the human's next message, the correction
>   arriving one turn later since a finished turn cannot be recalled [INV-203]. Its law body is the
>   orchestration members carrying a reminder-history of two or more — worker-routing [INV-69],
>   lean-orchestrator [INV-137], pull-unblocked-work-and-never-idle [INV-143], classify-the-subtask
>   [profile proactivity.classify-the-subtask-not-its-heading], and deep-independent-audit-by-default
>   [INV-237] — and the single-occurrence members stay reminders until they recur [base rule 23]. It
>   judges every turn's trace, one model call per turn: token cost is a non-reason on the current plan
>   [profile proactivity.quality-over-budget], so the cheap universal watch beats a sampling that misses
>   the offence. The per-person STRICTNESS — how hard a given host's judge reds a borderline act — is a
>   parameter the judge READS but does not own: its home is the future parameters registry [ROADMAP 427],
>   where the lean-orchestrator setting is already slated to live, so the judge is built to read a
>   strictness supplied from that one home and the two movements never compete for it. It stands down
>   silently on its own breakage — a missing binary, a timeout, a non-zero exit, or a trace it cannot read
>   leaves no verdict rather than a red, since a guard that reds when its own machinery breaks trains the
>   guarded to route around it [INV-203]. Its runs and fires are read by the net-meter [INV-202] rather
>   than trusted, and it retires by the owner's standing word when it stops firing [INV-203]. Because it
>   reads the transcript rather than a committed file and rests on a model call, it stays OUT of the
>   deterministic suite and push gate, opt-in per host and off by default, the same boundary the
>   document-surface register judge keeps [INV-203], so the suite and push gate stay deterministic.
>   `hooks/register_judge_core.py` (shared core), `hooks/conduct-judge.py` with its collect and report
>   arms (the trace-reading arm). [INV-241]

### A2 — Landing-commit refreshed NEXT_STEPS gate (INV-242) — insert into the same `### The machines that hold the bounds` section, beside the config-health and push-gate deterministic entries

> - **A landing that ships a movement refreshes the forward map in the same breath.** The movement-end
>   report law says the seat refreshes NEXT_STEPS and reports after every big movement without being asked
>   [profile report.movement-end]; left as once-read prose it fired only on a reminder. Its checkable face
>   is a commit: a **landing** is a commit whose diff flips a ROADMAP.md row to a closed status
>   (done / shipped / landed) — the mechanical signature of a movement ending — and a landing whose diff
>   does not also touch NEXT_STEPS.md reds. This reads a checkable fact and owes no model call, so it is a
>   deterministic push-gate arm, wired where the config-health check and the commit fence already run
>   [INV-175], reading the pushed commit range and redding the push that carries a landing with a stale
>   forward map, naming the one fix (refresh NEXT_STEPS.md in the landing commit). A commit that closes no
>   row is not a landing and owes nothing, so a mid-movement work-in-progress commit never trips it —
>   only the row-closing flip that marks the movement's end does. `guardrails/check-landing-next-steps.py`,
>   riding the suite and the push gate. [INV-242]

### A3 — Config-health skill-copy arm (INV-243) — insert into `### Composing across axes  [not a scenario]`, immediately after the INV-175 config-health paragraph, as a short extension paragraph

> **The installed skill copy is the source skill, the same way the installed hook is the source hook.**
> The config-health check reds an installed hook missing from or drifted against its source in `hooks/`
> [INV-175]; a skill copy runs the identical risk: the pack authors a skill in `skills/<skill>` and the
> seat installs a working copy at `~/.claude/skills/<skill>`, and the two drift the moment an install is
> skipped, so an out-of-date installed skill silently runs an older behaviour than the pack ships — the
> self-install law left un-netted [profile trust.self-install]. Config-health gains a second arm beside
> the hook-diff arm: it diffs each installed skill copy against the pack's `skills/` source and reds an
> un-synced or drifted installed skill copy, naming the one fix (re-run the installer). It reads the whole
> skill source directory against the installed set rather than a fixed name list, so every skill the pack
> ships is covered the moment it lands, and a personal-layer skill with no pack source is left alone — the
> exact shape the hook arm already holds [INV-175]. A checkout with no installed skills by design (a CI
> runner) skips by name. `guardrails/check-config-health.sh` gains the skill-copy arm; it runs inside the
> suite and the push gate with the hook arm [INV-175]. [INV-243]

---

## (B) Formal-index rows to add (columns: `Anchor | One line | Description | Section`)

Insert after the INV-240 row. The `One line` column carries the dense technical summary in the house
style; the `Description` column carries the plain one-sentence human-clear form (the column added at
v3.0.0).

```
| INV-241 | the conduct judge: the register judge [INV-203] generalized from a turn's output text to its action trace (the ordered `tool_use` events in the transcript, not the reply's words), a model reading the trace against the standing orchestration laws and redding an act-level violation after the fact; the net INV-150 demands for the orchestration laws that named none, watching the members reminded twice or more [base rule 23, INV-108]; reuses `hooks/register_judge_core.py`'s judge frame, single model call, hallucination guard, and stand-down-on-own-breakage [INV-203]; async two-arm shape — a Stop arm collects the verdict in the background, a UserPromptSubmit arm surfaces it at the human's next message, the correction one turn later since a finished turn cannot be recalled [INV-203]; law body = worker-routing [INV-69], lean-orchestrator [INV-137], pull-unblocked-work-and-never-idle [INV-143], classify-the-subtask [profile proactivity.classify-the-subtask-not-its-heading], deep-independent-audit-by-default [INV-237], the single-occurrence members staying reminders until they recur [base rule 23]; judges every turn's trace, one model call per turn, token cost a non-reason on the current plan [profile proactivity.quality-over-budget]; the per-person strictness is a parameter it READS but does not own, homed in the future parameters registry [ROADMAP 427] so the two movements never compete for one home; stands down silently on its own breakage (a missing binary, timeout, non-zero exit, or unreadable trace leaves no verdict rather than a red) [INV-203]; runs and fires read by the net-meter [INV-202], retiring by the owner's word when it stops firing [INV-203]; reads the transcript rather than a committed file and rests on a model call, so it stays out of the deterministic suite and push gate, opt-in per host and off by default [INV-203]; `hooks/register_judge_core.py` (shared core), `hooks/conduct-judge.py` with collect and report arms; the owner's word 2026-07-19, the reminder-dependent capability audit's bucket 1 | A model reads the turn's action trace — the ordered record of which tools the seat called, not the reply's words — against the standing orchestration laws and flags after the fact when the seat authored a long artifact itself instead of dispatching it, misrouted a unit of work, idled after a landing, or skipped the default deep audit, running async in the register judge's two-arm shape so the verdict arrives one turn later without blocking the turn. | Machines |
| INV-242 | the landing-refreshed-map gate: the movement-end report law [profile report.movement-end] given a checkable face — a landing is a commit whose diff flips a ROADMAP.md row to a closed status (done / shipped / landed), the mechanical signature of a movement ending, and a landing whose diff does not also touch NEXT_STEPS.md reds; a deterministic push-gate arm reading the pushed commit range, no model call, wired where config-health and the commit fence run [INV-175], naming the one fix (refresh NEXT_STEPS.md in the landing commit); a commit closing no row is not a landing and owes nothing, so a mid-movement WIP commit never trips it; `guardrails/check-landing-next-steps.py`, riding the suite and the push gate; the owner's word 2026-07-19, the reminder-dependent capability audit's bucket 2 | A push-gate check reds a landing commit — one whose diff closes a roadmap row by flipping its status to done, shipped, or landed — when that same commit does not also touch NEXT_STEPS.md, so the forward map is refreshed in the breath the movement lands rather than only on a reminder, while a mid-movement commit that closes no row is never forced to touch it. | Machines |
| INV-243 | the config-health skill-copy arm: the installed skill copy is the source skill, the self-install law [profile trust.self-install] given a net; config-health [INV-175] gains a second arm beside the hook-diff arm that diffs each installed skill copy at `~/.claude/skills/<skill>` against the pack's `skills/` source and reds an un-synced or drifted installed skill copy, naming the one fix (re-run the installer); it reads the whole skill source directory against the installed set rather than a fixed name list so every shipped skill is covered automatically and a personal-layer skill with no pack source is left alone [INV-175]; a CI checkout with no installed skills skips by name; `guardrails/check-config-health.sh` gains the arm, runs inside the suite and the push gate with the hook arm [INV-175]; the owner's word 2026-07-19, the reminder-dependent capability audit's bucket 2 | The config-health check gains an arm that diffs each installed skill copy against the pack's skills source and reds a missing or drifted installed skill, so a stale installed skill can no longer silently run an older behaviour than the pack ships, covering every shipped skill automatically and leaving a personal-layer skill with no pack source alone. | Composing across axes |
```

---

## (C) Regression fences, non-goals, and the success measure

### Regression fences (existing promises that must stay true through this change)

- **The register judge keeps working unchanged [INV-203].** The conduct judge reuses
  `hooks/register_judge_core.py` (frame, model call, hallucination guard, stand-down contract) and adds
  only a trace-reading arm around it; the register judge's text-reading arms — the chat Stop/prompt-submit
  arms and the document-surface ceiling — are untouched.
- **The config-health hook arm keeps working [INV-175].** The existing hook-diff arm and the perms arm
  (`guardrails/check-config-health-perms.py`) keep running; the skill-copy arm is added beside them, not
  in place of them, and holds the same whole-directory-versus-installed-set shape [INV-175].
- **The commit fence and the deterministic push gate stay deterministic [INV-175, INV-11, INV-174].**
  The two new deterministic gates (INV-242, INV-243) join the suite and push gate as ordinary arms; the
  conduct judge (INV-241) stays OUT of the deterministic gate — transcript-and-model-based, opt-in, off
  by default — exactly as the document-surface register judge does [INV-203], so the suite and push gate
  keep the same deterministic guarantee.
- **INV-150 stays satisfied, and is further satisfied.** Every declared cross-cutting law names its net.
  The three new laws each name theirs (INV-241 the conduct-judge hook, INV-242
  `check-landing-next-steps.py`, INV-243 the config-health skill-copy arm). Beyond fencing, INV-241 is
  the net for the orchestration laws INV-69 / INV-137 / INV-143 / INV-237 that until now named no
  mechanical net — so this movement moves those laws from "reminder" to "watched" rather than leaving a
  declared-laws gap [INV-101, INV-150].
- **The hedge gate keeps working [INV-238].** The bucket-2 hedge gate holds the literal offering-hedge
  frames and already defers the paraphrase class to the conduct judge; its Stop-gate is untouched. (See
  the citation-reconciliation note in section D — INV-238's row points that deferral at [INV-203] and
  should now resolve to [INV-241].)

### Non-goals (deliberately left out this movement)

- **Bucket 3 stays passive.** The plan-time members — plan-time question sweep, how-to-ask, full-run
  classifier, loops-are-the-seat's-to-propose-and-arm, recap-unanswered, and working-narration — stay
  passive reminder lines or, at most, a later plan-time arm of the same conduct judge; no machinery is
  built for them here. Working-narration in particular cannot be blocked (the outgoing chat reply is
  unhookable), so a reminder is its working answer.
- **The conduct judge does not block a turn.** It reds after the fact, one turn later, like the register
  judge; it is not a pre-turn gate and cannot stop an act mid-turn.
- **The conduct judge does not own strictness.** It reads a per-person strictness supplied by the future
  parameters registry [ROADMAP 427]; setting or storing that value is that movement's, not this one's.
- **The conduct judge's law body is scoped to the twice-reminded members.** The design doc's full bucket-1
  list is broader (search-for-a-skill, problem-ledger-second-occurrence, human-prose-by-a-clean-writer,
  the parallel-worktrees decision, fix-the-class-and-sweep); those join the law body when they recur a
  second time [base rule 23], not now.
- **No new deterministic-gate dependency on a model.** The two deterministic gates read checkable facts
  only; neither calls a model.

### Success measures (one per new code)

- **INV-241:** a fixture suite of action-trace transcripts, each carrying one known orchestration
  violation (a long artifact authored inline instead of dispatched; a judgment subtask routed down or a
  one-shot kept on the senior; an idle after a landing; the default deep audit skipped) reds every
  violating trace and stays green on every clean trace, and the net-meter [INV-202] shows the judge
  firing on real violations over a review window rather than never.
- **INV-242:** the fixture suite reds a landing commit (a ROADMAP row flipped to a closed status) whose
  diff omits NEXT_STEPS.md, and stays green both on a landing that refreshed NEXT_STEPS.md and on a
  non-landing commit that closes no row.
- **INV-243:** config-health reds a missing or drifted installed skill copy and stays green when every
  installed skill matches the pack's `skills/` source.

---

## (D) Homes and citations used, and why

- **INV-203 (register judge)** — the pattern INV-241 generalizes: the judge frame, the async two-arm
  Stop/UserPromptSubmit shape, the shared core `register_judge_core.py`, the hallucination guard, the
  stand-down-on-own-breakage contract, the net-meter reading, the opt-in/off-by-default boundary that
  keeps the deterministic gate clean. Cited throughout A1 and the INV-241 row so the two judges share one
  mechanism rather than forking a second.
- **INV-150 + INV-101 (every declared law names its net / the declared-laws home)** — the reason the
  conduct judge exists as a law at all: it is the named net for the orchestration laws that had none, and
  each new law names its own net. Cited so the prover's declared-laws station finds a net per law.
- **INV-69, INV-137, INV-143, INV-237 + profile classify-the-subtask** — the five law-body members, each
  cited by its own anchor (classify-the-subtask by its profile home, having no INV). These are the laws
  the judge reads the trace against.
- **base rule 23 / INV-108 (a rule that breaks mid-turn twice earns a live channel)** — the discriminator
  from the design doc that sorts the twice-reminded members into the judge's body and leaves the
  single-occurrence members as reminders. Cited to justify the scoped law body.
- **INV-164 (a machine holds what attention drifts on) / profile quality-over-budget** — token cost as a
  non-reason, deriving fork-1 (judge every turn) rather than sampling.
- **INV-175 (config-health) + INV-11/INV-174 (commit fence)** — the home INV-243 extends (the skill-copy
  arm sits beside the hook arm and the perms arm) and where INV-242 wires (the deterministic push gate).
  Cited so the config-health law stays one home with a new arm, not a second machine.
- **profile report.movement-end / profile trust.self-install** — the once-read profile laws INV-242 and
  INV-243 give a machine to. Cited as the behavioural homes the gates enforce.
- **ROADMAP 427 (the parameters registry)** — a FORWARD pointer only: this row does not yet exist in the
  spec or the roadmap text I could read, so the citation names it as the future home of the strictness
  parameter, per design fork-2. The orchestrator should confirm ROADMAP 427 is the intended row id when
  applying (see ⟨DECIDE⟩ below).
- **INV-202 (net-meter), INV-238 (hedge gate)** — the net-meter reads the judge's fires; the hedge gate
  is the bucket-2 sibling that defers its paraphrase class to this judge.

### Citation to RECONCILE when applying (not a new decision, a dangling pointer)

INV-238's Formal-index row already reads "…a paraphrase slips through and the class in any phrasing is
held by the bucket-1 conduct-judge **[INV-203]**". That reference was a placeholder before the conduct
judge had its own anchor; now that it lands as **INV-241**, that pointer should be updated to **[INV-241]**
(or [INV-203, INV-241]) in INV-238's prose and its index row, so the hedge gate's deferral points at the
judge that actually holds the paraphrase class. Flag for the pen — a one-token edit, but a real dangling
citation if left.

### ⟨DECIDE⟩ left open

- **⟨DECIDE — the landing signature for INV-242.⟩** I defined "landing" checkably as *a commit whose diff
  flips a ROADMAP.md row to a closed status*, because that is the mechanical face of a movement ending and
  it never forces a NEXT_STEPS touch on a mid-movement WIP commit. The design doc's phrasing was "closes a
  row / ships a spec-or-code change" — the second disjunct (ANY commit that touches PRODUCT_SPEC.md, a
  skill body, guardrails, or hooks also counts as a landing owing a refresh) would fire far more often,
  including on intermediate spec edits. Recommendation: keep the row-closing signature only; the
  movement-end law is about movements, and a row-status flip is the checkable end of a movement. Needs the
  owner's or orchestrator's word if the broader spec-or-code signature is wanted instead.
- **⟨DECIDE — the ROADMAP 427 row id.⟩** The parameters registry / strictness home is cited as ROADMAP 427
  from the design doc, but no such row is present in the spec text yet. Confirm the row id (or the actual
  home) when applying, so the forward pointer resolves rather than dangles.
