# The map — what lives where, and why (one page)

Written for the moment someone asks "where does X live?" or "why are there three repos?". No jargon;
every claim here is answerable in one line. (Normative rules live in SPEC.md and the skills — this page
only points.)

## Three homes on a machine, three different jobs

**1. The pack — `~/live-spec` (public, github.com/happysasha18/live-spec).**
The PRODUCT. A package any software project can attach to so that work runs by one discipline: you throw
wishes in passing, each one is classified before any code, specified, reviewed, tested, and lands with
automatic pre-push checks. Anyone on the internet can read and use this repo — so nothing personal is in
it.

**2. The personal layer — `~/.claude/playbook` (private).**
Everything about ONE person that must follow them across projects: the personal profile (chat language,
how proactive to be, "no calques", how to show work), working-principle notes, and the attic of
superseded personal files. It is a git repo so every rule keeps its date, its reason, and a one-command
rollback — but a private one, because it is personal.

**3. The starter note — `~/.claude/CLAUDE.md`.**
Not a storehouse — a twenty-line note the assistant reads first in every session. It says three things:
one window = one project (ask if unsure) · load the personal profile from the playbook · work by the
live-spec pack. The file physically sits inside the playbook repo (so it has history and a backup);
`~/.claude/CLAUDE.md` is a link pointing at it. It used to hold every rule; now each rule lives in its
real home and the note only points.

## Inside the pack: one rulebook, five working skills

- **live-spec-base** — the shared rulebook: rules that bind EVERY skill (ask-never-guess, plain words,
  no calques, one home per fact, the door before code, prototype ≠ product…) stated ONCE, plus default
  settings. When two skills seem to disagree, this file wins.
- **spec-author** — writes the spec. Owns the canonical checklists an author walks (the cross-view axes,
  the standard facets of a feature).
- **product-prover** — reviews the spec and the architecture like a formal-methods architect; runs the
  re-check that gates every push.
- **build-pipeline** — runs a change end to end: door → spec → prove → architecture → matrix → tests →
  code → verify → commit. The order is law.
- **communicator** — everything the human sees: plain-language reports, batched questions, decision
  pages, how a prototype may be shown.
- **publish** — the moment work leaves the machine: what a good publication owes per kind of artifact
  (a skill shows its commands, a tool shows real runs, a visual product shows fresh screenshots), and
  how a target (GitHub, a plugin directory, a design project) plugs its own steps into the walk.

Around them: `templates/` (the document shapes a project copies), `adopt/` (how to attach to an existing
project), `guardrails/` (the automatic pre-push checks), `inbox/` (how an outside session files a wish
without write access).

## The pack eats its own cooking

`~/live-spec` is also a PROJECT run by the method — so the repo carries its own SPEC.md (what the pack
promises), ROADMAP.md (the wish queue), ARCHITECTURE.md, TEST_MATRIX.md, tests/, JOURNAL.md (the why,
dated), NEXT_STEPS.md (cold-resume state), and docs/prover/ (every review record). These files are the
flagship INSTANCE of the method, not extra machinery.

## Where does a rule go? (the only table worth memorizing)

| The rule is about… | It lives in… |
|---|---|
| every project and every user of the pack | `live-spec-base` (one sentence of law), elaborated in the ONE working skill whose job it is |
| how to write specs / review / run changes / talk to the human | that working skill |
| one person, across all their projects | their profile in the private playbook |
| one project (host) | that project's `.live-spec/profile.md` |
| this minute only | said in the session; strongest word wins, never silently recorded |

One rule, one home. Everything else may point at the home, never restate it.

## Who reads what, in what order

A session starts → reads the starter note (3 lines of substance) → loads the personal profile (how to
work with this human) → loads the pack skills as work demands them → the project's own SPEC/ROADMAP say
what the product is and what's next. A cold session resumes from NEXT_STEPS.md alone.
