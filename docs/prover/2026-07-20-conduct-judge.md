# Prover pass — INV-241, the conduct judge (CROSS-LINK)

Prover skill version: product-prover, live-spec-base v2.8.1 (per the skill's own version banner).
Mode: CROSS-LINK — the new surface (INV-241) proved against the named existing surfaces it composes
with (INV-203, INV-238, INV-150/INV-101, INV-202, INV-108/base rule 23, ROADMAP 427, and the net
targets INV-69/137/143/237/classify-the-subtask). Read-only on every other repo file.
Clean context: this seat did not author INV-241 [INV-237].

## Triage

PROCEED. INV-241 is a spec law for a stateful machine (a Stop/UserPromptSubmit two-arm judge reading
the transcript) with entities, transitions, and invariants — analyzable. The doc claims a system that
is spec'd-but-not-yet-built: `hooks/conduct-judge.py` does not exist on disk (only `register_judge_core.py`
and the register arms do), so every claim about the built machine is CONDITIONAL on the build matching
the spec. The seam findings below concern the SPEC's composition, which is what CROSS-LINK proves.

## Opening assessment

INV-241 generalizes the register judge (INV-203, a model reading the turn's TEXT) to a sibling that
reads the turn's ACTION TRACE — the `tool_use` events in the same transcript — and reds an
orchestration-law violation one turn late in the same async two-arm shape. The core reuse claim is
mechanically sound: `register-judge.py` already walks the transcript back to the last human message and
filters content blocks by type, so swapping the `text` filter for a `tool_use` filter sits on the exact
same machinery (`register_judge_core.py`'s judge frame, single model call, hallucination guard, and
stand-down contract all transfer). The scoping-to-twice-reminded-members is consistent with base rule 23
/ INV-108. But four seams do NOT hold as written, and they cluster around the two hardest joints: what a
late verdict about an ALREADY-COMMITTED act can ask, and whether a TRACE-only judge can hold the classes
its neighbours hand it. Verdict: SPEC HAS HOLES — four defects, all one-to-two-sentence folds, plus four
recommendations. None touches the register judge's own behaviour; the folds are additive.

## Findings

### D1 — INV-238 hands the conduct judge a class it cannot see: a hedge is words, this judge reads only acts

> "the class in any phrasing, judged against whether the act was actually derivable, is held by that bucket-1 conduct judge [INV-241], while this literal net catches only the frames it lists" — INV-238 declaration

INV-238 (hedge gate) defers its paraphrase class — "the class in any phrasing" of an offering-hedge — to
INV-241. But an offering-hedge is a REPLY-TEXT phenomenon ("just say the word", "let me know if you want
me to"): its evidence is the words the seat wrote. INV-241 is defined, four times over, to read "the
`tool_use` events in the transcript, NOT the reply's words." A trace-only judge cannot see a phrasing, so
it cannot hold "the class in any phrasing." The behavioural CORE of a hedge (the seat did not do a
derivable act, waiting for a cue) is partly trace-visible as an absent act, but the hedge's discriminator
— that the seat OFFERED instead of acted, and whether the pending call is a genuine human-only one —
lives in the text, exactly where this judge does not look. Consequence: a host turns on the conduct judge
believing paraphrased hedges are now caught semantically; they are not, and the gap INV-238 names as
covered stays open with no net actually on it.

Resolve the citation to a single coherent home. Either (a) widen INV-241's input to state it reads the
reply text alongside the trace for the text-evidenced behavioural classes — which breaks its clean
"trace, not words" identity and should be stated deliberately — or (b) repoint INV-238's deferral: the
conduct judge holds the ACT facet (a derivable act left undone, visible in the trace), and the
text-phrasing backstop belongs to a text-semantic judge (the register-judge family) or stays explicitly
unbuilt. Pick one and make both laws say the same thing.

`defect · internal-conflict (consistency)`

### D2 — the strictness the judge reads has no home until ROADMAP 427 ships, and no interim source is named

> "the judge is built to read a strictness supplied from that one home and the two movements never compete for it" — INV-241 declaration; ROADMAP 427 is "OPEN DESIGN — capture only, owner-held for scope"

INV-241 reads a per-person STRICTNESS parameter whose home is the future parameters registry,
ROADMAP 427. That row is OPEN, capture-only, owner-held — the registry is unbuilt, so at ship time there
is no home to read from. As written, INV-241 has a dangling dependency: "built to read a strictness
supplied from that one home" names only a source that does not exist yet. Its sibling INV-203 avoids this
exact trap by grounding its tunables in "the host's own tunable defaults [INV-70]" and the core's
`DEFAULT_MODEL` / `DEFAULT_TIMEOUT` env fallbacks — a concrete value present now. INV-241 names no such
interim default. Consequence: read literally, the conduct judge cannot ship before ROADMAP 427, blocking
a bucket-1 capability on an owner-held OPEN design row; read charitably, it ships on an unstated implicit
default and the spec is silent on what that default is.

Add one sentence: the judge runs at a built-in default strictness (an env-overridable constant in the
conduct arm, mirroring the core's `DEFAULT_MODEL`) until ROADMAP 427's registry becomes its home, at
which point the registry supersedes the constant. That unblocks ship now and keeps the single-home
promise for later.

`defect · missing-prerequisite (precondition)`

### D3 — a late verdict about a committed act has no defined ask; the register judge's "restate and send now" does not fit

> "the correction arriving one turn later since a finished turn cannot be recalled [INV-203]" — INV-241 declaration

The async shape is inherited honestly, but the register judge's late verdict yields a concrete corrective
ACT — its `block_reason` says "Restate each as a plain positive sentence ... and send the correction now",
and the restatement reaches the human. A conduct violation is an ACT that already happened and committed:
the seat authored the long artifact, spent the expensive tier, idled, or skipped the audit. One turn
later there is nothing to restate and, for a misroute, nothing to recover — the tokens are already spent.
The spec claims the judge reds "exactly as the register judge reds a register violation in the turn's
text", but the register judge's surfaced ask is register-specific and nonsensical when injected for a
conduct verdict. What the surfaced conduct verdict ASKS the seat to do is unstated — redo the act if
still cheap? note it and adjust the next turn? re-dispatch? Consequence: the report arm injects
"you misrouted last turn" into the next turn's context with no defined response, so the seat either wastes
tokens redoing committed work or silently absorbs the red, and the law's own correction promise is empty
for most of its members.

State the conduct report arm's ask in one sentence: the late verdict is a forward-looking behavioural
correction (adjust the next comparable act), with a redo only where the act is still cheaply reversible;
the conduct arm writes its own report text rather than reusing the register `block_reason` frame.

`defect · missing-outcome-check (postcondition)`

### D4 — two async judges, one per-session verdict slot that overwrites: the register and conduct verdicts clobber

> "async in the register judge's two-arm shape ... a Stop arm collects the verdict in the background ... a UserPromptSubmit arm surfaces the collected verdict" — INV-241 declaration; "One verdict slot per session: a second turn's judgment replaces an unread first" — `hooks/register-judge-collect.sh`

The register judge's collect arm writes ONE verdict file per session, `~/.claude/hooks/.judge/${SESSION}.json`,
and deliberately OVERWRITES it ("a second turn's judgment replaces an unread first"). INV-241 reuses this
two-arm shape with "its own collect and report arms", but the spec does not state its verdict slot is
disjoint from the register judge's. A naive copy of `register-judge-collect.sh` writes the same
`${SESSION}.json`, so whichever of the two judges finishes second clobbers the other's verdict for that
turn, and the report arm surfaces only one — the other is silently lost. Consequence: on a turn that both
a register offence and a conduct offence occur, the human sees one correction and never the other, at
random by which model call returns first; the loss is invisible because the overwrite is by design.

State that the conduct judge uses a distinct per-session verdict slot (e.g. `${SESSION}.conduct.json`)
and its report arm reads that slot, so the two judges' verdicts never share the register judge's
single overwritten file.

`defect · partial-success-risk (atomicity)`

### R1 — the net-meter can only read a net on the host's declared roster; INV-241 omits the registration its sibling states

> "Its runs and fires are read by the net-meter [INV-202] rather than trusted" — INV-241 declaration; "aggregates runs and fires against the host's declared roster" — INV-202

INV-202 meters a net only if it is on the host's DECLARED roster (a zero-run roster net reds by name; a
net absent from the roster writes no line and is invisible). INV-241 promises the net-meter reads its
runs and fires but names no roster registration and no `guardrails/judge-hooks.json` classification — the
very wiring its sibling INV-238 states explicitly ("classified in `guardrails/judge-hooks.json` [INV-211]
... covered by config-health parity [INV-175, INV-180]"). Without it the metering promise is
unenforceable and the installed copy is unguarded. This is sibling-parity: nothing stated is broken, but
the conduct judge should carry the same roster / judge-hooks.json / config-health wiring INV-238 carries.

Add the wiring sentence to INV-241: classified in `guardrails/judge-hooks.json` [INV-211], registered on
the host's net-meter roster [INV-202], covered by config-health parity [INV-175, INV-180].

`recommendation · now · boundary-issue (composition)`

### R2 — "judge every turn" spends a model call on chat-only turns with an empty trace; no skip floor is stated

> "It judges every turn's trace, one model call per turn" — INV-241 declaration

A turn with no `tool_use` blocks (a pure-chat reply) has an empty action trace — there is no act to
judge. The register judge guards the analogous case with a `MIN_CHARS` floor (skip a reply under 120
chars). INV-241 states no equivalent: "judge every turn" would spend a model call judging an empty trace,
which can only waste the call or invite a false red on absence. Token cost is a declared non-reason
[quality-over-budget], so this does not block, but the empty-trace case is a real skip-floor the sibling
has and INV-241's spec drops.

State that a turn whose trace holds no `tool_use` blocks is skipped (no verdict), the trace-side analogue
of the register judge's `MIN_CHARS` floor.

`recommendation · later · stuck-state (liveness)`

### R3 — the hallucination guard needs the trace rendered to quotable text, or its verbatim-span check has nothing to bite

> "reuses `hooks/register_judge_core.py`'s ... hallucination guard" — INV-241 declaration

The core's hallucination guard (`matched_span` / `parse_offences`) keeps only an offence whose quote is a
VERBATIM span of the input `text`. A `tool_use` trace is structured JSON, not prose; for the guard to
transfer, the conduct arm must serialize the trace into a quotable text blob (one line per call, e.g.
`Task(subagent_type=…, prompt=…)`) and hand THAT as `text`, so a hallucinated act-quote is dropped the
same way. This composes cleanly and is likely how it would be built, but the spec should name it so the
reused guard actually has text to match against.

State that the conduct arm renders the trace to a quotable text form before the core judge call, so the
verbatim-span hallucination guard bites on the trace the same way it bites on reply text.

`recommendation · later · unenforceable-promise (discharge)`

### R4 — INV-241 cites INV-150 as the demander, but INV-150 is scoped to the declared-laws home the orchestration laws do not sit in

> "It is the net INV-150 demands for the orchestration laws that until now named none" — INV-241 declaration

INV-150's net-per-law demand is textually scoped to DECLARED cross-cutting laws in the one declared-laws
home (INV-101), which names exactly three for this pack (register, clock stamps, no self-certification).
The orchestration laws (INV-69/137/143/237) are not in that home. The rule that actually promotes a
twice-reminded behavioural rule to a mechanical channel is base rule 23 / INV-108, which INV-241 also
cites correctly. The INV-150 citation is loose: its declared-laws STATION (INV-101) would expect the
netted law to appear in the home with a per-surface clause, which these orchestration laws do not have.
Nothing is broken — the one-net-per-property principle genuinely applies (see the quantifier note) — but
the citation should rest on INV-108 / base rule 23 as the demander and cite INV-150 only for the
one-net-per-property constraint.

Tighten INV-241's net-demand citation to base rule 23 / INV-108 (the recurrence→mechanism law), keeping
INV-150 as the reference for "no property owned by more than one net."

`recommendation · later · boundary-issue (composition)`

## Mandatory CROSS-LINK step — quantifier re-verify (SPEC INV-170)

Swept the composing surfaces for universals/enumerations the newcomer falsifies:

- INV-241's own claim "the orchestration laws that until now named **none**" — FALSIFIED by INV-237,
  which already names a net: the release gate checks for "a dated clean-context review record naming a
  seat other than the release's", and the newly-added-lens self-application. So INV-237 does NOT belong
  to the "named none" set, and adding INV-241 as INV-237's net creates a SECOND net on one property,
  which INV-150 forbids ("no property owned by more than one net at once"). This is a genuine seam
  tension folded into the finding below.
- INV-101 "the pack's **three** laws each name a mechanical gate" — NOT falsified; INV-241 is not a
  declared cross-cutting law, the home still names three.
- INV-150 "no property owned by more than one net at once" — the newcomer stresses it at INV-237 (above).
- INV-69/137/143/classify-the-subtask — verified to name no existing mechanical net (confirmed against
  their index rows and a guardrails/ scan); INV-241 legitimately becomes their first net, no conflict.

Verdict: HIT — the sweep found the INV-237 double-net, recorded as D5 below.

### D5 — INV-241 double-nets INV-237, which already carries a release-gate net; INV-150 forbids two nets on one property

> "law body = ... deep-independent-audit-by-default [INV-237]" — INV-241 declaration; "the release gate may require a dated clean-context review record ... the gate checks the record exists" — INV-237

INV-237 already names a mechanical-ish net (the release gate checking for a dated clean-context review
record). INV-241 puts INV-237 in its law body as a member it watches every turn. That is two nets on one
declared property — the release-time record-existence gate and the per-turn trace judge — which INV-150
explicitly forbids ("no property owned by more than one net at once and none dropped by any"). The two
plausibly partition INV-237 (release-time certification vs per-turn audit-by-default), but the spec does
not state the partition, so as written it is a bare double-net. Consequence: the declared-laws /
one-net-per-property invariant reads as violated at INV-237, and a later reader cannot tell whether the
release gate or the conduct judge owns an INV-237 violation.

State the partition in one sentence: INV-241 covers the per-turn audit-by-default FACET of INV-237 (did
this turn run the default deep audit, read from the trace), while the release gate covers the
release-certification facet — so INV-237's enforcement is partitioned across two moments, not
double-netted; or drop INV-237 from INV-241's law body and leave it to the release gate.

`defect · internal-conflict (consistency)`

## Seams that HOLD

- **The trace-reading arm sits on the register core.** `register-judge.py`'s `turn_text()` already walks
  the transcript back to the last non-tool_result human record and filters assistant content blocks by
  `type`; reading `tool_use` blocks instead of `text` blocks is the same walk on the same transcript.
  The judge frame, single model call, hallucination guard, and stand-down contract in
  `register_judge_core.py` are law-agnostic (the law body is handed in per surface), so the conduct arm
  genuinely adds only a trace-serializing reader. Mechanically sound (#1 in the hunt).
- **Async loop / atomicity, except the shared slot (D4).** The register judge's `stop_hook_active` guard
  and per-session atomic-rename already solve the re-trigger loop and the write/rename race; the conduct
  judge inherits both. The only new atomicity hole is the shared verdict slot (D4).
- **Twice-reminded scoping vs base rule 23 / INV-108.** INV-108 graduates a rule that breaks a second
  time to "an every-prompt reminder line ... or a mechanical after-the-fact check." The conduct judge is
  a mechanical after-the-fact check over the members with reminder-history ≥2, and single-occurrence
  members "stay reminders until they recur" — exactly base rule 23 / INV-108. Consistent (#4 in the hunt).
- **INV-202 metering shape** transfers (the wrapper is generic); the only gap is the missing roster
  registration (R1), not the meter itself.

## Closing

Top fixes before build: D1 (repoint INV-238's deferral / decide the conduct judge's input), D5 (partition
or drop INV-237), D2 (name the interim strictness default). All four defects are one-to-two-sentence
folds; none regresses the register judge or the hedge gate's existing behaviour.

Overall readiness: needs another iteration — fold D1–D5, then this surface is buildable.

## Fold tracker

| ID | Kind | One-line | Folded / rejected (+why) |
|----|------|----------|--------------------------|
| D1 | defect | INV-238 defers a text-hedge class to a trace-only judge | open |
| D2 | defect | strictness dangles on unbuilt ROADMAP 427, no interim default | open |
| D3 | defect | late verdict on a committed act has no defined ask | open |
| D4 | defect | conduct + register share one overwritten verdict slot | open |
| D5 | defect | INV-241 double-nets INV-237 vs INV-150's one-net rule | open |
| R1 | recommendation | net-meter roster / judge-hooks.json registration omitted | open |
| R2 | recommendation | no skip floor for a chat-only turn with an empty trace | open |
| R3 | recommendation | trace must render to quotable text for the hallucination guard | open |
| R4 | recommendation | net-demand cites INV-150; belongs to base rule 23 / INV-108 | open |

## Folds applied 2026-07-20 (orchestrator, under the pen)

- **D1 — folded by reverting scope.** The hedge paraphrase class is text, so a trace-only judge cannot hold it; the movement's repoint of INV-238's deferral to INV-241 was reverted to [INV-203]. INV-238's own pre-existing imprecision (its prose calls the paraphrase class held by "the bucket-1 conduct judge", which reads acts not words) is left untouched as out-of-delta and queued for a later text-semantic-judge refinement.
- **D2 — folded.** INV-241 now reads a built-in env-overridable default strictness until the parameters registry (ROADMAP 427) ships, grounding tunables the way INV-203 does; nothing dangles on the unbuilt registry.
- **D3 — folded.** The late verdict is stated as a forward-looking behavioural correction that names the missed act and asks a redo only where the act stays cheaply reversible.
- **D4 — folded.** The conduct collect arm writes its own verdict slot kept distinct from the register judge's per-session slot, so the two never overwrite each other (enforced in code).
- **D5 — folded by dropping INV-237.** The law body is scoped to worker-routing (INV-69), lean-orchestrator (INV-137), pull-unblocked-work (INV-143), and classify-the-subtask; deep-independent-audit keeps its own release-gate net (INV-237), so no double-net.
- **R2, R3 — folded into the spec** (empty-trace turn skipped; trace rendered to quotable text for the hallucination guard). **R4 — folded** (the net-demand now leads with base rule 23 / INV-108, INV-150 stated as satisfied not demanded). **R1 — carried to the code step** (judge-hooks.json registration + net-meter roster wired in the build).

Verdict after folds: SPEC HOLDS. The five defects are folded in PRODUCT_SPEC.md's INV-241 declaration and index row; the recommendations are folded or carried to the code step.

## Fresh-seat adversarial audit of the built code (2026-07-20)

A separate fresh seat drove the built hook against six crafted transcripts and read all four hook files, the tests, and the reused core. Verdict SHIP: the machinery is sound and safe (never crashes or false-reds when its own parts break; empty-trace skip and stand-down confirmed; genuinely off by default; all four conduct files classified library and unwired; M-426 cites only real tests; INV-241 single-owned). It confirmed each of the five folds landed in code (D2 env default, D4 distinct `.conduct.json` slot, D5 four-member law body with no INV-237, D3 forward-looking reason in code, D1 reverted). Two real gaps were folded before landing: the block-emit path and the forward-looking `conduct_reason` had no test (added `test_main_emits_the_conduct_block_end_to_end`, red-first proven by gutting the reason), and LAW 1/2's long-artifact discriminator had no size signal in the rendered trace (added an approximate content size to `_summarize`, covered by a test). The auditor's law-body-quality findings — the idle and classify members rest on partial trace evidence — were folded as an honesty note in the spec and the law body, net-metered and human-verified, with a follow-on queued (ROADMAP 431); the INV-238 paraphrase-class residual was queued (ROADMAP 432). Suite 1670 green.
