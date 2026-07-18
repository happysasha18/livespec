# Adoption and the resource-expectation model — design (2026-07-18)

Alexander asked, late on 2026-07-18, for a deep movement: a newcomer arrives at live-spec in one of two
states — a brand-new project, or a codebase that already works — and the experience must let everything
install and get picked up with no unpleasant surprises, in particular no "I am on the $20 plan and it
spent every token in three minutes" and no "I am on the $200 plan and it crammed everything into one
context." What kinds of expectation are there, how do we model them, which questions do we ask and which
do we derive, and which flows need work.

This design is grounded in four clean-context investigations run the same night, each reading the shipped
machinery: the adoption flows, the cost/tier/parallelism model, the settings ladder and its axes, and the
ask-versus-derive split. Every claim below traces to a file the investigation read.

## The two root findings

The night's work converged on two distinct gaps, each with a single root.

**The install-to-running gap.** The wiring of hooks and gates lives inside the full adoption walk, where
the agent itself runs `install-pack-hooks.sh`, the scaffold and ratchet installers, and the rest — so a
person who runs the whole walk ends up fully set up without touching a script, which is exactly what
happened for the pack's own author. The gap is the SHORT path: after `install.sh` or `/plugin install`
alone, the person has the skills loaded and nothing else — no gates, no chat-quality hooks, no clock or
chat-law hooks, no pre-push, no `guardrails.config.json`, no daily update check, no `.live-spec/` records.
The README's install section lists none of the wiring the walk performs, and the plugin route is worse:
`plugin.json` declares no hooks, so `/plugin install` wires none of the chat nets at all. A newcomer who
follows the short README reasonably believes "I installed it, I am set up," while the enforcement half is
un-wired — a stranger's quick setup silently falls short of what the full walk (and the author's own agent)
did. The fix is to make the short path and the plugin wire what the walk wires, so the two paths converge.

**The missing plan-and-cost axis.** The pack has no notion of which Claude plan a person is on — no
subscription tier, no dollar or token ceiling, no rate awareness, anywhere. The cost model is one
qualitative knob, `budget.pressure` with values full, lean, and tight, defaulting to full, and it is an
explicit non-goal to attach any number to it. So out of the box the pack assumes a person can afford full
rigor everywhere: the full suite at every landing, a full prover pass before every minor release, up to
three worker agents running at once, a fresh-context adversarial pass on every high-stakes landing, and a
whole-project re-prove every ten landings — none of it capped or metered, by design. A cost-sensitive
person who says nothing gets all of it. The same absence, from the other side, starves a person with
headroom: the parallelism cap is a fixed feel-number of three that does not scale, and opening lanes is a
discipline the agent has to remember rather than a mechanism, so a person on the largest plan gets work
run one item after another — the behaviour Alexander himself hit once and filed.

Everything below elaborates these two and proposes the flows that close them.

## The two entry scenarios today

**A brand-new project.** The README tells the newcomer to install the skills and copy the templates from
`templates/` into the project root. That is the whole scripted path, and it yields skill files plus
placeholder documents and nothing else — no gates, no hooks, no version-control gate, no founding records.
The real founding conversation (personal-versus-reusable, the project kind, the footprint layers and proof
rungs, the economy rung, the agent card) lives in the adoption walk's orient step and only happens if the
agent runs it; a person who merely copies templates never meets it. So the new-project experience is the
thinnest and the most misleading: it looks complete and enforces nothing.

**An existing codebase.** The adoption walk (`adopt/ADOPT.md`, six phases) is thorough and mostly sound: a
version-control gate and baseline commit first for reversibility, an optional cruft sweep, an orient step
that reads every existing document before writing, a code-and-surface inventory, a reverse-spec that turns
existing docs into the canonical set with every re-engineered claim marked unverified until reconciled,
attic-over-deletion with a human's word, then architecture, matrix, and the gate installers. The walk is
strong. Its weaknesses are at the edges: the gate installers auto-wire only some of the gates and merely
print the rest as manual steps, so a person can believe the gate is wired when it silently is not; the
ratchet installer recognises only a spec named `PRODUCT_SPEC.md` and exits with an error on a host that
adopted under `SPEC.md`, never reading the host profile's spec-file line; the seeded config ships
placeholder paths that red or, worse, silently disarm a check until filled; two different documents point
pre-push at two different homes; and the entire walk is unenforced agent judgment, so a skipped phase or a
hollow reconciliation has nothing mechanical to catch it.

A precise surprise inventory, each anchored to a file, is preserved in the night's investigation notes;
the load-bearing ones are folded into the flow list below.

## The expectation model — the axes and where they live

The settings ladder resolves four nested scopes, narrowest-out: the session's live word beats the host
profile beats the personal profile beats the package default. It captures, today, language, proactivity
mode, trust, prover cadence, worker tiering, the lane cap, the economy rung, and a handful of
project-shape settings. Three things are wrong for a newcomer.

First, the plan-and-cost axis does not exist — there is no home even to record it, and the one place plan
economics leak into the system is a prose note in the personal profile. This is the single highest-value
addition, because the pack's own worker-routing rule ("route to the cheapest sufficient tier") silently
assumes the whole tier ladder is reachable by the account, which on a small plan it is not.

Second, two expectations a newcomer reaches for as single dials are fragmented across several settings.
"Let it run on its own" is really the proactivity mode plus the trust level. "Prefer fast over thorough"
is really the economy rung plus the prover cadence. A newcomer has to find and set two or three keys to
express one intent.

Third, the new-versus-existing distinction is a process branch that leaves nothing behind — the pack knows
at founding time whether it is greenfield or brownfield, then discards the fact rather than storing it as a
host axis.

The model this suggests: add the plan-and-cost axis at personal scope, since it follows the human across
projects; offer newcomer-facing composite presets that set the fragmented keys together as one choice; and
consider persisting the greenfield/brownfield mode as a host axis.

## Ask versus derive at adoption

The pack's own rule is the yardstick: a fact that pins to an artifact — the codebase, the architecture,
the spec, an approved prototype — is derived and cited; a fact that pins only to the human's judgment (a
taste, a policy, an act irreversible outside git, a device-feel) is asked. Measured against it, adoption
today both over-asks and under-asks.

The facts that genuinely must be asked, each a named human-only fact: the project kind (a definition no
artifact holds); personal-versus-reusable (an intent about what the project is for); the plan and any cost
ceiling (a policy no file in the tree holds — the sharp missing one); the autonomy posture (how much the
seat may move without the human); the economy rung (their own time-and-money tolerance); and the
irreversible or outward acts already gated well today — creating a remote, deleting cruft, moving files to
the attic. The facts that should be derived: the project's language, test runner, framework, and
conventions from the inventory; the remote URL from the tree; the spec file name from what exists; the
design principles seeded from the per-kind starter table.

The over-asks to fix: the footprint layers and proof rungs are asked cold though a codebase largely shows
them, and the project kind is asked cold although the accepted posture is to infer-to-cheapen and let the
human's word decide — a reconciliation that lives in a wish note but never propagated into the walk. Both
should become propose-from-inventory, then confirm-or-correct. The under-asks to fix: the plan-and-cost
axis is assumed silently, and the autonomy posture defaults silently whenever the personal profile is
declined.

## The flows to change

The list below is ordered by how much it improves the newcomer's experience, with the version bite of each
and whether it is mine to build from the artifacts or a taste call that is Alexander's.

1. **Close the install-to-running gap with one honest installer path.** A single command (or a clearly
   sequenced short list in the README's install section) that, after copying skills, wires the chat hooks,
   installs the scaffold and ratchet gates, wires pre-push in one agreed home, and seeds a real config —
   or, where a step must stay manual, says so loudly at the end with the exact remaining commands. The
   plugin should carry its hooks so `/plugin install` is not a silent half-install. Kind: a real feature
   plus doc — MINOR. Mine to build once the one-home pre-push question is answered (a small policy fork
   below).

2. **Add the plan-and-cost axis and derive a starting posture from it.** A new personal-scope setting for
   the reachable tiers and any ceiling, asked once at adoption as a named policy question; from the
   answer, propose a starting economy rung and a lane appetite instead of defaulting everyone to full and
   three. The human's word stays final. Kind: a new invariant and setting — MINOR. The axis and the ask
   are mine; the exact plan-to-rung-and-lane defaults are a taste fork below.

3. **Make parallelism follow headroom, not memory.** A floor that proposes opening independent lanes up to
   the plan's appetite, so a large-plan person stops getting work run one item at a time. The spec holds
   that judging independence resists a purely mechanical gate, so this is propose-and-open, not force.
   Kind: MINOR. Mine to build as a proposal step; the appetite mapping rides the plan fork.

4. **Fix the adoption over-asks.** Propose the project kind, layers, and proofs from the inventory and ask
   the human only to confirm or correct; propagate the infer-to-confirm reconciliation into the walk.
   Kind: a correction to the walk — patch to MINOR depending on how the founding-questions data is shaped.
   Mine to build from the existing wish note.

5. **Repair the sharp installer edges.** Teach the ratchet installer to read the host profile's spec-file
   line rather than only recognising `PRODUCT_SPEC.md`; make a silent no-op of pre-push wiring impossible
   by ending every ambiguous case with a loud manual recipe and a verification line; ship a config whose
   default disarms nothing silently; unify the two pre-push homes. Kind: bug-fixes — patch. Mine to build.

6. **Bring the daily update check and the bundled skills under the flow.** Wire or schedule the update
   check so a host stops drifting silently behind the pack, and bring the bundled token-heavy skills (deep
   research and kin) under a budget signal or at least a warning. Kind: MINOR. The update-check wiring is
   mine; whether to meter the bundled skills touches the standing no-token-meter non-goal and is a fork.

## The open forks for Alexander

These do not pin to any artifact, so I will not guess them; each is waiting on your word.

- **The plan-to-posture defaults.** For each plan tier, what starting economy rung and lane appetite should
  the pack propose? This is your policy call about how cautious the out-of-the-box spend should be.

- **The numeric-ceiling question.** A real cost ceiling that trips would break the pack's standing non-goal
  of no token meter and no auto-downgrade. Do we keep that non-goal and stay with qualitative rungs plus a
  plan-derived starting posture, or do we admit a soft numeric ceiling for the cost-sensitive case? Your
  call, because it moves a stated principle.

- **The scope of the plan axis.** Personal scope fits a person who is the same across projects, but one
  machine can serve several clients on different plans. Does the plan live in the personal profile, or does
  it belong to the host when the host is a client's tree?

- **The one pre-push home.** The tracked `guardrails/pre-push` or the untracked `.git/hooks/pre-push`. The
  installer and the scaffold README currently disagree; picking one is a small policy call that unblocks
  the single-installer flow above.

## Status and next step

This design is the synthesis of the investigation; nothing here is built yet. The buildable parts (the
single installer path, the plan axis and its ask, the headroom parallelism proposal, the over-ask fixes,
the installer-edge repairs, the update-check wiring) are mine to land through the method once the four
forks above are answered. The forks are the morning's first decision. The safest independent piece to land
first, needing no fork, is the installer-edge repairs (item 5) and the over-ask fixes (item 4).
