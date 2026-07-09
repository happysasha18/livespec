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

## Grounding / kin

- Kin to the departures board / feature-map-on-demand (communicator) — a SHOW surface, feature language.
- Must not become a wall of internal codes (INV-28): the card speaks in the human's words, codes trail.
- Ties to spec-format-by-project-type (the `project.kind` unit) and the settings ladder (live-spec-base).
