# live-spec — Product Spec

This document is the living statement of what live-spec is right now. Each section describes one scenario — what the reader does and what the reader sees — and the body below is a list of requirements. Edit history lives in `JOURNAL.md`; this spec states what is true today.

live-spec takes any request a person submits, of any size and at any moment, breaks it into story-sized pieces — one user story to a piece — and processes them one at a time. Each piece runs the same pipeline, each stage checked by its own gate before the next, reaches a delivery, and ships tested, so the person is free to keep thinking about other things. A machine enforces the process at every step, every claim earns a test, and nothing ships until that test passes.

Bracket codes like `[E-1]` and `[E-12]` point to the rule's home in the project spec; a reader can ignore them, a maintainer follows them. The letter before the number names the kind: `E-` an entity (a numbered part of the product), `A-` an adoption step, and `S-` a header rule. A `[target]` marker on a line of its own marks a feature that is planned rather than built. The keywords *when*, *if*, *then*, and *shall* are set in italics and carry their standard requirements meaning: *shall* states a duty, *when* opens a situation, *if* and *then* open a condition and its result.

Terms already defined in the intake glossary and the founding section — request, pipeline, spec, test matrix, suite, queue, delivery, journal, inbox, host, pack, session, profile, adoption, guardrail, surface registry, feedback ledger, snapshot, design-sync, skill eval — carry their meanings unchanged. The block below adds only the new nouns this section needs.

## Glossary additions

- **user story** — one requirement told as a short sentence naming who wants what and for which benefit; the unit a request is split into.
- **base skill** — the pack skill that holds the shared rulebook and the default settings, stated once for every working skill to point at.
- **working skill** — one of the pack's domain skills, each carrying one role of the pipeline: spec-author, product-prover, design-reviewer, build-pipeline, test-author, communicator, publish, feedback-intake, and feedback-collector.
- **target tag** — the marker `[target]` a spec line carries on a line of its own to mark a feature that is planned rather than built.
- **checkpoints** — the saved points a piece of work reaches and can resume from, written under `.live-spec/`.

---

## Requirement 1: The spec keeps what is built apart from what is planned

**Context:** The spec states what is built and working today apart from what is only planned, and it keeps a reader from mistaking one for the other. A planned feature carries the target tag on a line of its own, and the tag never spreads to the section around it. The suite ties each target tag to the queue row that builds it — a row still open, awaiting its landing — so the marker is enforced rather than trusted.

**User Story:** As a reader of the spec, I want a planned feature marked by a target tag the suite enforces, so that I never mistake a promised surface for a working one.

### Acceptance Criteria

**Case: built and planned are marked apart**

1. The spec *shall* state what is built and working today apart from what is only planned, marking each scenario and its named promised parts apart, so a scenario that holds built parts beside planned ones states a status for the scenario and for every named promised part. [S-0]
2. The system *shall* carry the target tag on a line of its own and *shall* keep it off the section around it. [S-0]

**Case: the suite ties each tag to its building row**

3. The system *shall* tie each target tag to the queue row that builds it, that row still open and awaiting its landing, and *shall* red the suite *if* that row ships with the tag still on, *if* the tag vanishes, or *if* the tag was never named. [S-0]
4. The system *shall* mark as planned the host-facing guardrail checks and the surface registry, the snapshot machinery that records a project's state at adoption as its baseline, and the design-sync machine. [E-6, E-10, E-7, A-6, E-18]

---

## Requirement 2: The pipeline runs as a set of roles carried by the working skills

**Context:** Behind the pipeline is a full set of roles. An analyst writes the spec, an architect stress-tests the design and finds the edge cases and dead ends before any code is written, a design reviewer judges the design and checks that same-kind things behave alike, a tester works out the tests and writes them, and a project manager runs the process and reports back to the person. The design reviewer proposes the groupings of same-kind things the spec never declared and checks behaviour parity inside each group. These roles are the working skills, and one base skill holds the shared rulebook and the default settings the other skills work by.

**User Story:** As a person relying on the pipeline, I want each request run by a full set of roles carried by named working skills over one base rulebook, so that every request meets an analyst, an architect, a reviewer, a tester, and a manager rather than a single undifferentiated pass.

### Acceptance Criteria

**Case: the roles are the working skills**

1. The system *shall* run each request through a set of roles — an analyst who writes the spec, an architect who finds the edge cases and dead ends before any code, a design reviewer who checks that same-kind things behave alike by proposing the groupings the spec never declared and checking behaviour parity inside each group, a tester who works out and writes the tests, and a project manager who runs the process and reports back. [E-12]
2. The system *shall* carry those roles as the working skills, bringing the person in where an answer needs a fact no artifact holds — a taste, a policy, or an act irreversible outside git. [E-12, INV-17]
3. The system *shall* hold the shared rulebook and the default settings the working skills run by in one base skill. [E-12]

---

## Requirement 3: A project adopts live-spec and the host owns its own state

**Context:** A project can adopt live-spec at the start or partway through work already under way. Adoption brings the document templates, a procedure for joining midstream, and the guardrails the project installs, and the project that adopts it is the host. The host owns everything about its own work rather than sharing one set across several projects.

**User Story:** As a project taking on live-spec, I want to adopt it at any point and own all my own state, so that my spec, queue, journal, and settings live with me rather than in a shared pool.

### Acceptance Criteria

**Case: a project adopts and becomes the host**

1. The system *shall* let a project adopt live-spec at the start or partway through work already under way, bringing the document templates, a procedure for joining midstream, and the guardrails already built for it: the repo's own pre-push checks and the opt-in commit fence (the check that blocks a commit when the repository moved under the session since its last read). The host-facing guardrail checks stay a separate, planned family. [E-1]
2. The system *shall* name the project that adopts live-spec the host. [E-1]

**Case: the host owns its own state**

3. The host *shall* own its own spec, test matrix, queue, journal, surface registry, inbox, and feedback ledger. [E-1]
   [GAP: the source lists the surface registry as planned and also states the host owns it today, with no reconciling clause.]
4. The host *shall* keep a `.live-spec/` folder holding its profile, its checkpoints, and the versions of the skills it runs. [E-1]
