# Onboarding design — ask little, default well, reveal the rest (2026-07-18)

Alexander's steer, 2026-07-18 night: there are many settings axes, but a newcomer must not be made to
decide them all at once. Tell them briefly what exists, set safe defaults, and let the rest be tuned
later. This document designs onboarding around that principle, for both entry states (a new project and an
existing codebase). It builds on the same night's four investigations of the adoption flows, the
cost/tier/parallelism model, the settings ladder, and the ask-versus-derive split.

## The principle, stated once

Onboarding asks only the facts that cannot be derived from the tree and that change behaviour
immediately. Everything else is given a safe default. The full set of axes is then shown as a map the
person can read and change at any time, never as a questionnaire they must complete. Any axis that matters
only later is surfaced later, at the moment it becomes relevant, with the context that makes the choice
obvious. The measure of good onboarding here is how little the person has to decide before the pack is
working well for them.

## The four moves of onboarding

**One — wire the machinery silently.** Whatever the entry, installation wires everything the full
adoption walk wires: the skills, the chat-quality and clock hooks, the scaffold and ratchet gates,
pre-push in one agreed home, a real seeded config, and the `.live-spec/` records. "Installed" has to mean
"running." This asks the person nothing; it removes the gap where the short install path and the plugin
today leave a stranger with skills and no enforcement.

**Two — detect the entry state, then confirm.** Whether the tree is a new project or an existing codebase
is visible in the tree; the pack detects it and confirms in one line rather than asking. An existing
codebase runs the full walk (inventory, reverse-spec); a new project scaffolds the templates. The person
does not choose a "mode."

**Three — ask the few must-asks, each as one simple choice with a safe default.** Only three, and each is
a single user-facing intent, not a raw setting:

- *What is this project?* — the project kind, proposed from the inventory and confirmed or corrected, never
  asked cold.
- *How should I balance cost against thoroughness?* — one choice among a few named presets, defaulting to
  the careful end. This is the user-facing proxy for the plan-and-cost concern: the person expresses intent
  ("keep it cheap" versus "spend for full rigor") and never has to name their Claude plan or a token
  number. The preset sets the economy rung, the parallel-lane appetite, and the worker tier together.
- *How much should I do on my own before checking with you?* — one choice among a few autonomy presets,
  defaulting to a balanced middle. The preset sets the proactivity mode and the trust level together.

Everything else is derived (language, test runner, framework, remote, spec-file name) or defaulted.

**Four — show the assumptions and the tunable map.** Onboarding closes by showing the settings card: what
was assumed, and every axis with its current value, each one changeable at any time by saying so or through
a settings view. The person leaves knowing the axes exist and having decided nothing beyond the three
choices above.

## The welcome and the user journey

The first contact sets the tone, so it earns real design rather than a form. The arc, from the person's
side:

1. **A warm hello that says what the pack is for, in one breath.** Plain, human, no vocabulary: something
   like — "Hi. I help you build software where the spec leads: we write down what the thing should do,
   check it holds together, then build and test against it, so nothing ships on a guess. Let me get set up
   on your project." The person learns what they are getting in two sentences.

2. **A short, honest ask, framed as "just these few, the rest as we go."** The pack names that it needs
   only a couple of things now and will handle the rest in context — "To start I need two or three things
   from you; everything else I'll either read from your project or sort out with you when it comes up." Then
   the three light choices (what this project is, cost-against-thoroughness, autonomy), each with its safe
   default already selected so the person can accept with a word.

3. **A visible "here's what I assumed, change any of it anytime."** The settings card, shown as a friendly
   summary, so the person sees the whole surface without having to touch it. This is where the many axes are
   named briefly and left tunable, honouring the principle.

4. **A first real action, offered not imposed.** For a new project, "want to start with the first spec?";
   for an existing codebase, "I've written a spec from your code — want me to review it for holes?" The
   person ends onboarding standing at a useful next step, not at a blank screen.

The journey's shape is: hello and what-I-do, then a light ask with defaults, then a shown map, then a first
action — with the promise, kept throughout, that anything unasked will be raised when it matters and never
dumped upfront. Every step is skippable by a person in a hurry (accept the defaults, go), and legible to a
person who wants to look.

## Just-in-time reveal

The axes not asked upfront surface when they first matter, with context. The first time several
independent items could run at once, the pack says it can parallelise and names the current lane appetite,
so the person tunes parallelism at the moment it is meaningful. The first time a full prover pass is about
to cost real time, the pack names the cadence and its escape. A decision offered where its effect is
visible is a decision the person can actually make; the same decision offered on a setup screen is noise.

## Defaults that do not surprise

The default cost preset sits at the careful end, so a person who accepts the defaults and says nothing
never gets the current out-of-the-box behaviour of full rigor with three concurrent workers. A person with
headroom moves up in one word, or at the first just-in-time prompt. This inverts today's default, where
silence buys the most expensive posture — the exact source of the "$20 plan, gone in three minutes"
surprise.

## The composite presets (the dials the choices move)

The two preset choices are sugar over the real settings, so the ladder underneath is unchanged and an
expert can still set any single key directly.

- **Cost against thoroughness.** Careful: the tight economy rung, a single lane, the cheapest sufficient
  worker tier. Balanced: the lean rung, two lanes. Full: full rigor, three lanes. (Exact values are a fork
  for Alexander below.)
- **Autonomy.** Ask-often: ask-at-max proactivity, trust low. Balanced: proceed on a clear recommendation,
  trust low for outward moves. Run-solo: max-proactive, trust raised for reversible acts only, outward
  moves still gated.

The never-bend floor holds under every preset: the push gate runs at full rigor, the human's gates stand,
red-before-fix holds, the door law and tripwires hold. A cheaper preset buys less mid-work spend, never a
weaker landing.

## The two entry states, concretely

A **new project**: the pack detects a near-empty tree, scaffolds the templates, wires the machinery, asks
the three choices (the project kind proposed from whatever seed exists, or asked plainly if the tree says
nothing), and shows the card. First real action offered: writing the first spec.

An **existing codebase**: the pack detects real code, runs the full walk (the version-control baseline,
the inventory, the reverse-spec with every re-engineered claim marked unverified, the attic-over-deletion
with the person's word), wires the machinery, asks the three choices with the project kind and footprint
proposed from the inventory, and shows the card. First real action offered: a full prover pass over the
re-engineered spec.

## Open forks for Alexander

None of these pin to an artifact, so they wait on your word.

- **The preset values.** The exact economy rung, lane count, and tier for each cost preset, and the exact
  proactivity and trust for each autonomy preset.
- **The default preset.** Careful or balanced as the out-of-the-box choice when the person says nothing.
- **Whether to ask the cost preset at all, or infer it.** Asking one cost-intent question is the lightest
  honest option; inferring from observed behaviour is lighter still but guesses a policy fact. My
  recommendation is to ask the one question, since it pins to no artifact and shapes spend immediately.
- **How many presets.** Two or three per axis. Three reads as careful/balanced/full; two is even lighter.

## Open thread — speed against clarity (report in the morning)

Alexander named a tension to resolve deliberately: onboarding should be fast to get through, and at the
same time the person should genuinely understand what is about to happen and how the pack will work. These
pull against each other — a fast path hides the machinery, an understandable path explains it. The design
above leans fast (three light asks, defaults pre-selected, the rest revealed later), so the open question
is where clarity is owed anyway: what must the person understand before they accept the defaults, versus
what is safe to let them discover as it happens. Candidate answer to develop: the welcome's two sentences
carry the whole mental model (spec leads, then build and test against it), the card carries the "here is
what I assumed" transparency, and each just-in-time reveal carries a one-line "here is why I am asking now"
— so understanding is delivered in small, timed pieces rather than as an upfront lecture or not at all. This
needs its own pass and a worked example of the first five minutes from the person's side; report it in the
morning.

## Where this sits in the movement

This onboarding design is the user-facing half of the adoption-and-resource movement
(`2026-07-18-adoption-and-resource-model.md`). It lands as a MINOR, since it raises usability rather than
fixing a defect, and it must land with no regression to the existing walk — guarded by several
clean-context adversarial passes before it ships, per Alexander's standing instruction. The machinery
convergence (move one) and the installer-edge repairs are the safe first pieces; the presets and the
default-posture inversion wait on the forks above.
