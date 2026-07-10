# Wish: a new project's human should discover what they can customize

**From:** Alexander, live-spec host session, 2026-07-09. Named as a 1.0-blocking wish.

## The wish, in plain words

When live-spec attaches to a project, the method already carries **many settings** — but a new
user has no way to see them or know they are theirs to set. Alexander's words: "у тебя тут очень
много настроек, например какой это проект, какие есть параметры (поищи в себе увидишь), так что
имеет смысл подумать как юзер узнает что он может кастомизировать."

So: build a small onboarding — something at project setup that SHOWS the human the choices that are
theirs, in plain language, so customization is discoverable rather than hidden inside the pack.

## The settings that already exist (the "поищи в себе" inventory — to verify & complete when building)

- **`project.kind`** — book · backend service · static site · fullstack app · CLI · skill pack · custom
  (always ASKED, never profile-read; no personal line can say what a host is — SPEC INV-36). Sets the
  spec unit, the acceptance style, and what the coverage check means (spec-format-by-project-type).
- **`budget.pressure`** — the economy rung: full · lean · tight (SPEC T-19). Told/asked at setup.
- **Personal profile** (`~/.claude/live-spec/profile.md`): language, proactivity mode, how-to-show-work,
  resume habits, prover cadence — the human's, reusable across their projects.
- **Host profile** (`.live-spec/profile.md`): host-only overrides on the ladder (SPEC E-13).
- **Skill fit list** (SPEC INV-65): which skills attach for this project's kind and crafts.
- Settings ladder: package defaults → personal profile → host profile → the session's live word
  (live-spec-base).

## What a fix might look like (for the build session to shape, not a spec here)

- At setup (founding / adoption orient), after the kind + rung are settled, SHOW the human a plain-word
  card: "here is what this project decided, and here is what you can change and how" — each setting by its
  plain name, its current value, and the one line that changes it. Silence stays consent (defaults told,
  not interrogated — INV-31); this is a SHOW, not a questionnaire.
- Possibly a standing "what can I customize?" answer the human can ask at any time (kin to the feature map
  on demand), rendered from the actual settings ladder, not a hand-kept list that drifts.
- One home for the setting catalog so the card and the on-demand answer read from the SAME source
  (one-fact-one-home), and the coverage stays honest as new settings are added.

## Field scan (2026-07-09 evening, researched on his ask — how the field does onboarding)

Surveyed: CLI init wizards (npm/cargo/create-next-app, eslint --init), the zero-config movement
(Prettier, Vite, Biome), IDE walkthroughs (VS Code), contextual tips (Figma/Linear), AI-agent packs
(Claude Code /init + CLAUDE.md, Cursor rules, Copilot instruction files, BMAD installer), and the
disclosure research (Nielsen Norman: linear tours of 8–12 steps cause drop-off; wizards are for 3–5
required, sequence-dependent, uninferable decisions only).

**The consensus, in one line: inspect first · ask one thing · tell one thing · write the rest to a
skimmable file · let the other settings introduce themselves at first relevance.** CLI tooling migrated
one-way from init questionnaires to defaults-plus-editable-file; AI tools converged on
inspect-then-confirm (the agent reads the repo and drafts; the human corrects a draft, which is
cheaper than answering questions). An upfront ask stays justified only for a fact that is uninferable
AND forks everything downstream — and even then it is phrased as a stated default to confirm, never a
blank menu.

**Applied to live-spec's onboarding (the recommended shape for the spec delta):**
1. At attach, INSPECT the project first; never ask what the tree already answers.
2. ONE confirm-or-correct question: project.kind, stated as an inference ("this looks like a static
   site — right?"). The kind law stays satisfied: the human's word still decides, the inference only
   cheapens the deciding.
3. budget.pressure is TOLD in one line with its escape ("full rigor; say 'work lean' when time is
   short"), never asked.
4. The settings card (mockup v2) shows ONCE after those two lines, and rebuilds on demand from the live
   settings ("what can I customize?"). The settings ladder's files stay the one readable home; the card
   is a projection, never a second truth.
5. The remaining settings surface CONTEXTUALLY, one line at first relevance: the push gate at the first
   push, design-sync at the first visual component, worker tiering at the first delegation. A tip whose
   trigger can never fire for a newcomer is a defect.
6. Never a multi-screen wizard; total forced interaction = one question + one told default.

**Anti-patterns to keep out (each observed in the field):** wizard fatigue / question forms · a settings
dump disguised as a summary (a card that itself needs onboarding) · asking what is inferable · defaults
so often wrong that the confirm becomes a read-everything · an unsafe re-run that clobbers hand edits ·
always-on rule bloat (everything loaded everywhere).

Key sources: code.claude.com/docs/en/commands (/init) · cursor.com/docs/rules ·
docs.github.com/copilot/customizing-copilot · code.visualstudio.com/api/ux-guidelines/walkthroughs ·
docs.bmad-method.org/how-to/install-bmad · uxpin.com/studio/blog/what-is-progressive-disclosure.

## Grounding / kin

- Kin to the departures board / feature-map-on-demand (communicator) — a SHOW surface, feature language.
- Must not become a wall of internal codes (INV-28): the card speaks in the human's words, codes trail.
- Ties to spec-format-by-project-type (the `project.kind` unit) and the settings ladder (live-spec-base).

## Addendum (2026-07-10, his word): the remote question joins the flow

Setup also settles WHERE accepted work is pushed (SPEC INV-82): the remote is discovered from the
tree (inspect-first); only a project with no remote gets one contextual question at the first push
moment — create one (GitHub · GitLab · whatever they name) or stay local. The card's settings list
shows the discovered remote like any other current value.

## Addendum — third mockup bounced (2026-07-10 ~00:50, his word)

Mockup v3 was shown at night; verdict: still reads as bad machine text ("мы опять в яме?" —
paraphrase: the same jargon pit again). Three exhibit lines from the mockup itself:

1. "How setup feels — almost no questions" — understandable but a bare claim, reads dubious.
2. "working at full rigor — say 'work lean' when time is short" — opaque: an internal economy
   setting translated literally instead of the consequence in the user's words.
3. "Everything else comes up naturally when it first matters:" — opaque: machine-flavoured
   restatement of the deferred-questions mechanism.

Consequences (the class fix, not the point fix):
- These three lines are the red-proof fixtures for the pre-show register lint (queue row 170):
  the lint MUST go red on all three before it counts as working; a failed pre-show check BLOCKS
  the showing.
- Authoring method changes: human-facing product text is drafted by a fresh writer session with
  the reader's brief only (new user, first contact; every line answers "what do I do and what
  happens"), then the lint, then a clean-context reader check. The pack-marinated session never
  drafts it.
- Mockup v4 goes through that road and is shown in the morning. The build stays parked until his
  "годится".

## Addendum — v4 verdict (2026-07-10 ~09:16, his morning word)

v4 ACCEPTED with one class fix, landed the same hour: the page hardcoded his personal setting values
(the Language row said "Our conversation in Russian"; the name row said "Alexander."; the
settings-ladder example leaned on Russian). His word: those are his own profile values; the page
states the RULE instead — conversation happens in whatever language the user writes (the agent
follows), written work is always in good English; the name is whatever the user introduces themselves
with. Three spots fixed by a clean writer, register lint green, page re-shown. The BUILD gate is now
OPEN on this accepted mockup (the mockup is the norm for look and feel).
