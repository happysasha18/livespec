---
name: live-spec-base
description: The live-spec pack's shared rulebook and default settings, stated ONCE — the rules every pack skill works by (ask-never-guess, plain words with trailing anchors, one name per surface, one home per fact, checkpoint discipline, the concurrent-edit fence, freshness checks) plus the settings ladder of four nested scopes (package defaults → personal profile → host profile → the session's live word). Load it whenever a pack skill (spec-author, product-prover, build-pipeline, communicator, publish) is in use, when resolving how the pack should behave for a given human or host (language, proactivity, prover cadence), or when two skills seem to state one rule differently — this file is the normative home; the working skills only reference and elaborate. NOT for sessions outside the pack's work, and never a place to write host- or person-specific values (those live in profiles).
metadata:
  version: 0.1.23
---

# live-spec-base — one rulebook, six skills

The pack's shared working rules live HERE, once. A working skill (spec-author, product-prover,
build-pipeline, communicator, publish) opens by naming this base and the version it was written against, references
these rules, and elaborates only its own domain — communicator teaches HOW to speak plainly; THAT we speak
plainly is this file's sentence. A second full statement of a shared rule inside a working skill is drift —
a defect to fold at the next milestone, not a convenience (SPEC INV-13). Used standalone, outside the pack,
a working skill still stands: its pointer here reads as plain advice.

## The shared rules

1. **Ask, never guess.** A gap only the human can fill — a threshold, a policy, a taste call — is asked or
   marked `⟨DECIDE⟩` with a one-line question and a recommended pick. Never invent intent; and never ask
   what you can decide or verify yourself — a pending question rides in its row while the lane keeps moving
   on the recommendation (SPEC INV-4, INV-5, INV-12).

2. **Plain words carry the meaning; the code trails, quietly.** Every human-facing sentence stands on its
   own in the product's language; internal handles (INV-x, row numbers, worker names, model names, coined feature names or metaphors the reader never chose to learn) never do
   the talking. One convention, two faces: in **chat**, the anchor may trail the sentence in parentheses —
   "no remote copy exists (INV-8)"; in **documents**, anchors sit at line ends in square brackets — `[INV-8]`.
   Never open a line with a code. And when chat runs in one language while the docs run in another, a term
   or metaphor coined in the docs language is never loan-translated into chat — **no calques**: say what
   actually happens in natural chat-language words; the original term may trail in parentheses like any
   anchor (Alexander 2026-07-05 — a calque reads as machine-speak and degrades the product).

3. **One surface = one name, everywhere.** The moment one thing answers to two names, every cross-check
   silently loses the seam between them. The vocabulary comes from the host's SPEC.

4. **One canonical home per fact.** Everything else that mentions the fact is a pointer, and pointers are
   kept live — a doc superseded or moved gets every inbound reference repointed the same session. Two
   documents claiming authority over one fact is undefined behaviour when they disagree.

5. **Mechanical work goes to a junior; judgment stays senior.** If the steps can be written precisely
   (known edit strings, a known command, fan-out fact-gathering), a cheaper worker runs them — the cheapest
   tier that can (one-shot → haiku; multi-step mechanical → sonnet; judgment/design → senior). The junior
   pastes RAW output (command + exit code + failing lines) as it works; raw output is evidence, the
   junior's prose is only a lead, and the senior spot-checks by re-running.

6. **Every long or delegated piece of work keeps a persistent checkpoint.** A file on disk (host home:
   `.live-spec/checkpoints/`, gitignored — never a system temp dir) holding done / in-progress / next,
   updated AS the work runs — so a cut-off RESUMES from disk instead of restarting. Red at a pause is never
   committed; the failing test name + hypothesis becomes the top NEXT_STEPS item — the checkpoint IS the
   red test.

7. **The concurrent-edit fence, before every write and every commit.** Re-check `git status` + HEAD against
   what you last read; if HEAD moved or the tree holds changes you did not make — STOP, re-read, then
   proceed surgically or back off. A repo you were not assigned to is read-only (one exception: a new wish
   file in its inbox). Applies to ANY skill that writes shared files, not just adoption (SPEC INV-10, INV-11). And within ONE session up to three build lanes may roll without asking (SPEC T-18; a fourth only on the human's asked word): every write to a document the lanes share serializes under the single PEN, one lane at a time; a later train's code and tests live in its own isolated copy of the tree until the senior integrates them; a landing commit carries exactly one row's delta, its gate run on a tree clean of any other lane's unfinished work (SPEC INV-39).

8. **Freshness: versions are re-checked at every safe breakpoint.** Re-stat the installed skills, the pack,
   and the profiles; on any version change re-read the changed file before continuing — never coast on the
   in-memory copy — and journal one line naming old → new (SPEC A-7, M-7).

9. **History lives in the JOURNAL; docs travel with the change.** The dated WHY of every movement goes to
   JOURNAL.md the same session; SPEC / NEXT_STEPS / ROADMAP prose states only current truth. A shipped
   change updates its README / CHANGELOG / SKILL.md before the session ends. **Entries and harvested
   records carry date AND time of day** — "yesterday evening you wrote X, so I did Y" is answerable later
   only if the record holds the moment, not just the day; a decision file keeps its answered-at stamp, a
   journal entry opens with when it happened (Alexander 2026-07-05).

10. **Nothing is silently deleted.** A superseded host file moves to the attic with a manifest line; a
    removed feature leaves a dated tombstone in the spec and RETIRED matrix rows; only clearly-regenerable
    junk may be deleted, listed and human-OK'd first (SPEC INV-7, A-4, A-9).

11. **Verify by deed; show the real thing.** "Works" is said only after running it and seeing the result;
    otherwise it is labelled an assumption. What the human sees is real data in its real render — synthetic
    only for your own checks, always labelled SYNTHETIC; never a bare file path.

12. **The human's gates are the human's.** Irreversible moves, authored-content moves, publishing, pushes
    where the host says so, taste and domain wording — proposed with a recommendation, executed on their
    word. And only what is genuinely theirs is asked; everything else proceeds and is reported.

13. **A claim needs its primary source.** Anything asserted as fact — what the code does, what happened,
    who decided — rests on evidence you can point to: an owning `file:line`, a commit, a command just run
    and its output. Your memory, a worker's summary, a document's prose are LEADS, not evidence — before
    attributing a decision to the human or calling a behaviour "by design", read the actual source line
    (rule 5's raw-output clause is this rule's delegation face). No source at hand ⇒ say "not sure", then
    check — never assert.

14. **A found defect is a sample of its CLASS — fix the class, sweep the look-alikes.** A bug, a stale
    name, a jargon string, a design inconsistency: before calling the fix done, name the pattern behind the
    instance, search the whole repo for it, and check every user-facing surface (not just the one reported)
    — then fix all siblings in the same change. One instance reported means the whole class is owned; the
    human never finds the second instance by eye. Each working skill applies this in its own domain: the
    pipeline sweeps code and surfaces on every bugfix, the prover sweeps the document before writing a
    point finding.

15. **The door is named before any code.** Every request states its entry point — feature · bug ·
    refactor · docs-only · skip — in one intake line beside size and priority, BEFORE the first line of
    code. The same line names the **work-kind** — product · infra · skill · prose — what the request
    BUILDS: the door picks WHICH pipeline steps run, the kind picks the FORM each running step takes
    (the per-kind table's one home is build-pipeline), and at landing every door-granted step has
    applied or been stood down BY NAME in the report — never a silent skip, never a kind touching the
    safety net (SPEC T-16, INV-22). Hard tripwires decide, never mood: a new user-visible surface · new persistent state · a new
    interaction on an existing surface · a spec [target] mark on the touched surface · behaviour no spec
    clause backs ⇒ FEATURE, however casually asked — and the tripwire verdict outranks a casual label
    (queue-cutting stays with the bug door alone). The door re-fires mid-work: the moment running work is
    about to create a surface or state its door doesn't grant — STOP, reclassify, continue by the right
    door. Casual asks are routed, never refused — and never hand-built past the pipeline because they
    sounded small. (SPEC T-12, INV-16)

16. **A prototype is not the product.** Exploring is legal, but a sketch lives fenced: its own
    `prototype/` home, a PROTOTYPE label in the form its kind can show (screen banner · `_prototype:
    true` field/header · first-line CLI banner · name/header marker), never wired into or linked from a
    prod surface, and shown to the human only under its label. A request to merely SEE or TRY may be
    sketched; a request to HAVE it in the product is a feature — unclear which ⇒ one plain question
    (rule 1). Promotion is not a merge: the feature enters at the spec step; the sketch is evidence, its
    code holds no rights. Opening a prototype home is a repo write of the assigned senior — never a
    worker's own move, never an outsider's (theirs is an inbox wish). (SPEC E-17, INV-17)
17. **Irreversible means gone, not merely public.** Truly irreversible actions — spending money,
   deleting data, sending to a person or an audience you cannot unsend from — always STOP for the
   human's word, whatever the proactivity mode. A push to your own repository is NOT irreversible (it
   reverts); it rides the mode and the project's own push gates. When unsure which side an action is
   on, treat it as irreversible and ask — the criterion is "can we get back to before, ourselves,
   losing nothing?" (Alexander 2026-07-05: money yes, deletion yes, a push no).

18. **One name-collision law.** A new file whose name is taken differentiates in TWO moves, the same
   everywhere in the pack: first the semantic mark its home already defines (the attic prefixes the
   source dir; a decision file already carries project + date), then — still taken — a numeric ordinal
   `-2`, `-3`, … before the extension. Never overwrite, never a third scheme. Where true concurrency can
   race one name (the inbox: two sessions, one slug, one moment), a short session token joins the
   semantic mark — a collision may cost a rename, never a lost file. (Audit 2026-07-05: the attic had no
   answer for a second collision; the attic and the inbox each spoke half a law.)

19. **The problem ledger — workshop noise is owned, never re-suffered.** Operational noise (a flaky
   test harness, a missing dependency, an environment error, a tool misbehaving — the WORKSHOP, never
   the product's own defect: that is a bug and takes the bug lane) is written down the moment it fires:
   grep the host's `.live-spec/PROBLEMS.md` for the signature. Not listed → one WATCHED line
   (signature, date, one line of context) and keep working — the write replaces the silent retry.
   Listed → the SECOND occurrence gets an owner THAT MOMENT: a queue row (OWNED) or the human's dated
   AGREED NON-PROBLEM — his word alone, never the agent's; the agent recommends, writes the recommended
   owner now, and the ask rides the batched report. A THIRD recurrence arriving unowned is a defect of
   the METHOD, not of the day — it goes to the pack's own queue (from a host window: one inbox file).
   A recurrence on an owned entry appends its date and changes nothing else; the landing that closes an
   OWNED entry's row flips it to SOLVED. (SPEC E-24, INV-23; born of tlvphoto's retried-never-owned
   noise, 2026-07-05.) **And a limping thing never dams the flow (SPEC INV-56):** a KNOWN, owned
   problem is PARKED — the ledger line, the owning row, or an expected-red note holds it — and every
   unrelated lane keeps rolling; hand-fixing loops cap at the two-strikes law above, and a defect with
   a NAMED mechanical owner is serviced in BATCH — instances fixed silently where the fence catches
   them, one ledger append at the session's end — never a per-instance ceremony that interrupts the
   work (born of a clock drift hand-ceremonied ten times in one night while its owner row sat open,
   2026-07-07). A real NEW bug still preempts; this governs the known limp.

20. **Search for a skill before reinventing (SPEC INV-65).** At a project's setup (founding, or
   adoption's orient, beside the founding questions) scan the installed skills and the catalogs you
   can reach for ones matching the project's kind and its crafts; propose the fit list with a
   recommendation — the human's word picks. At a struggle — a ledger entry's second occurrence, a
   taste artifact rejected twice, any returning failure family — the next attempt waits one search:
   an existing skill or checklist may already own the failure class; the find is adopted or rejected
   by name, recorded where the struggle lives. Borrowing practice: invoke a found skill as it ships;
   paraphrase folded lessons and credit the source by name; verbatim text only under its license,
   notice kept.


## When NOT to load this

Not for sessions outside the pack's work — this is the pack's rulebook, not a general style guide; and
never as a place to WRITE host- or person-specific values (those live in profiles; this file holds only
package defaults and the rules themselves).

## The settings ladder

How the pack behaves is a **named setting** living in one of four NESTED scopes; a setting belongs to the
scope it DESCRIBES, broader values are INHERITED down until a narrower scope overrides them on the human's
word, and resolution reads from the narrowest scope out — **session beats host beats personal beats
package default** (SPEC E-13):

| Scope | Home | Holds settings about |
|---|---|---|
| package defaults | the table below, in this file | the pack out of the box |
| personal profile | `~/.claude/live-spec/profile.md` | the HUMAN — follows them across every project |
| host profile | `<host>/.live-spec/profile.md` | THIS project |
| session | the human's live word — never a file | RIGHT NOW, one conversation |

An override exists only as a written line in its profile file, and setting one leaves a dated journal note
in the home it governs — never a silent divergence (SPEC INV-14). The session scope is the one exception —
it lives only in the human's spoken word and dies with the conversation; the agent never writes it
anywhere on its own, and making it outlive the session is a PROMOTION into the profile it describes, on
the human's word, journaled like any other override. Proactivity mode and trust are written
only on the human's word — the agent may propose, never set (SPEC INV-9). Profiles are re-read at the same
freshness points as skills (rule 8). A profile line the current pack does not recognize is ignored ALOUD —
named once in the session's next report — never silently dropped, never an error.

**The profile is found or founded at setup (SPEC B-3).** At founding, at adoption's orient, and at the
first session on a new machine or with a new human, the pack looks for the personal profile before the
founding questions resolve: found ⇒ loaded and said aloud; absent ⇒ an OFFER to create it from
`templates/profile.template.md` — the human tells about themselves and may name sources for the pack
to read and propose from; every line lands on the human's word, a declined proposal is dropped (INV-9
caps it: mode and trust move only on their word). A declined step runs the session on package
defaults, said aloud, and the offer returns at the next setup. A worker session never onboards
anyone — its brief carries its setting lines (SPEC ACT-3).

The personal layer has ONE home — the profile; the machine-global instruction file (e.g. `~/.claude/CLAUDE.md`)
is a thin LOADER: the pointer that loads the profile plus only the bootstrap lines that must hold before
any pack file is read, and it is those bootstrap lines' one home — the profile never restates them (SPEC E-16).

### Package defaults

| Setting | Default | A profile may say |
|---|---|---|
| `language.docs` | English — docs, commits, code, artifacts | another docs language |
| `language.chat` | mirror the human's language | pin one (e.g. Russian) |
| `proactivity.mode` | ask-at-max — surface forks, wait on taste calls | max-proactive: proceed on recommendations, batch questions |
| `trust` | low — human word before outward moves | raised only by the human (INV-9) |
| `prover.cadence` | FULL pass before every MINOR bump; CROSS-LINK on every surface add | tighter (e.g. live-spec itself: before every push) or looser, recorded |
| `worker.tiering` | router proposes the cheapest sufficient tier; senior may override, logged | fixed tier per size class (SPEC D-2) |
| `checkpoints.home` | `<host>/.live-spec/checkpoints/`, gitignored | another host path |
| `work-kind.host-default` | none — each wish's kind is called at intake | a host with ONE usual kind names it as the intake default (SPEC T-16) |
| `project.kind` | none — asked at founding and at adoption's orient, always the human's answer, never profile-seeded or inferred (SPEC INV-36) | the host's own kind: book · backend service · static site · fullstack app · CLI · skill pack · a custom kind through the queue; seeds project-wide defaults, never overriding an explicit line; updated on the human's word the moment the project outgrows it, journaled |
| `design-sync` | off — a host with visual components may switch it on (recorded profile line, SPEC E-18, INV-14) | on: a landing's DECLARED components sync to the team's design project, every sync behind the human's publish gate (rule 17) |
| `budget.pressure` | full — full rigor everywhere; the economy ladder's rung (SPEC T-19, INV-40) | lean or tight, ONLY on the human's word (a session's word or a profile line; asked — or the default told — at a project's setup, founding or adoption, alongside `project.kind`; the agent proposes a rung when money/time pressure is named, never sets one); each rung's legal sheds and the never-bend list live in the SPEC's economy-ladder section — every taken shed is named in the landing report, and an explicit host line outlives any rung |

A profile file is plain markdown: one `setting: value` line per override, each with a trailing date and,
when it narrows the defaults, one line of WHY. Settings not listed above may be proposed as wishes — the
table grows through the queue like everything else.

> The pack, whole: **live-spec-base** holds the shared rules and defaults · **spec-author** writes the spec ·
> **product-prover** reviews it · **build-pipeline** ships the change · **test-author** derives the matrix and writes the tests · **communicator** makes the human
> exchange land · **feedback-intake** brings what comes back to its home · **publish** sees the work out the door, owing its kind's checklist.
