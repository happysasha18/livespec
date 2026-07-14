---
name: live-spec-base
description: The live-spec pack's shared rulebook and default settings, stated ONCE — the rules every pack skill works by (ask-never-guess, plain words with trailing anchors, one name per surface, one home per fact, checkpoint discipline, the concurrent-edit fence, freshness checks, and more — twenty-six rules in the body) plus the settings ladder of four nested scopes (package defaults → personal profile → host profile → the session's live word). Load it whenever a pack skill (spec-author, product-prover, build-pipeline, test-author, communicator, feedback-intake, publish) is in use, when resolving how the pack should behave for a given human or host (language, proactivity, prover cadence), or when two skills seem to state one rule differently — this file is the normative home; the working skills only reference and elaborate. NOT for sessions outside the pack's work, and never a place to write host- or person-specific values (those live in profiles).
metadata:
  version: 1.0.11
---

# live-spec-base — one rulebook, seven working skills

The pack's shared working rules live HERE, once. A working skill (spec-author, product-prover,
build-pipeline, test-author, communicator, feedback-intake, publish) opens by naming this base and the version it was written against, references
these rules, and elaborates only its own domain — communicator teaches HOW to speak plainly; THAT we speak
plainly is this file's sentence. A second full statement of a shared rule inside a working skill is drift —
a defect to fold at the next milestone rather than a convenience (SPEC INV-13). Used standalone, outside the pack,
a working skill still stands: its pointer here reads as plain advice.

## The shared rules

1. **Ask, never guess.** A gap only the human can fill — a threshold, a policy, a taste call — is asked or
   marked `⟨DECIDE⟩` with a one-line question and a recommended pick. Never invent intent; and never ask
   what you can decide or verify yourself — a pending question rides in its row while the lane keeps moving
   on the recommendation (SPEC INV-4, INV-5, INV-12). And before offering the human a fork, check whether
   a proven artifact already settles it: when the architecture, the spec, or the invariants already
   determine the answer, DERIVE the requirement and say it back with the section cited as its ground,
   offering no fork; a fork reaches the human only for what the artifacts leave genuinely open — a taste
   call, or a real trade-off with no artifact-grounded winner. This is the read-the-doc twin of
   ask-never-guess: that half forbids inventing an answer, this half forbids offering a choice the
   documents have already made (SPEC INV-121).

2. **Plain words carry the meaning; the code trails, quietly.** Every human-facing sentence stands on its
   own in the product's language; internal handles (INV-x, row numbers, worker names, model names, coined feature names or metaphors the reader never chose to learn) never do
   the talking. One convention, two faces: in **chat**, the anchor may trail the sentence in parentheses —
   "no remote copy exists (INV-8)"; in **documents**, anchors sit at line ends in square brackets — `[INV-8]`.
   Never open a line with a code. And when chat runs in one language while the docs run in another, a term
   or metaphor coined in the docs language is never loan-translated into chat — **no calques**: say what
   actually happens in natural chat-language words; the original term may trail in parentheses like any
   anchor (2026-07-05 — a calque reads as machine-speak and degrades the product).

3. **One surface = one name, everywhere.** The moment one thing answers to two names, every cross-check
   silently loses the seam between them. The vocabulary comes from the host's SPEC.

4. **One canonical home per fact.** Everything else that mentions the fact is a pointer, and pointers are
   kept live — a doc superseded or moved gets every inbound reference repointed the same session. Two
   documents claiming authority over one fact is undefined behaviour when they disagree.

5. **The lead orchestrates; each unit routes to the cheapest tier that passes its brief (SPEC INV-69).**
   The lead — the orchestrator seat, whatever tier holds it — orchestrates, briefs, and accepts the work;
   it does not do the grunt itself. Every unit of work is routed on its own merits, PER UNIT: the trigger
   is judgment against mechanical, and the tier is PROPOSED for that unit — a one-shot with no decision to
   haiku, multi-step mechanical work to sonnet, anything carrying judgment or design to the senior, and a
   judgment step is never routed down. Size is a weak hint only, never the decider. The worker pastes RAW
   output (command + exit code + failing lines) as it works; raw output is evidence, the worker's prose is
   only a lead, and a worker's green is a lead the lead ACCEPTS by re-checking it, taken on trust never. A
   large or high-stakes landing earns an independent fresh-context checker beyond that re-check (SPEC
   INV-46). Every override of a proposed tier and every failed-acceptance escalation is logged, proposed
   tier → chosen tier → why (SPEC INV-69).

6. **Every long or delegated piece of work keeps a persistent checkpoint.** A file on disk (host home:
   `.live-spec/checkpoints/`, gitignored and kept inside the repo tree) holding done / in-progress / next,
   updated AS the work runs — so a cut-off RESUMES from disk instead of restarting. A landing that ships a checkpoint's items flips that checkpoint to its closed state in the same landing, so a returning session never reopens finished work. A checkpoint whose items all live in git history is stale by definition and reads as a resume defect (SPEC INV-107). Red at a pause is never
   committed; the failing test name + hypothesis becomes the top NEXT_STEPS item — the checkpoint IS the
   red test. A checkpoint or handoff note that records a LIVE background worker also records the worker's
   id (pointing at the worker's own checkpoint file), its briefed write-set, and the three liveness checks a
   resuming session runs before touching those files or spawning a sibling — the write-set's file times, the
   worker's heartbeat (a fixed-interval touch on its own checkpoint file, ~60 s [default], stale past ~2 min
   [default]), and one message to its id — and it never frames the worker's output as finished while the
   worker may still run (SPEC INV-76). Before a memory wipe, prefer
   halting the workers or letting them finish, so the next session starts single-writer; and say plainly
   when a worker dies with a closed window or a sleeping machine. The human's leave-word fires this rule
   for everything open at once: every lane to its checkpoint, workers halted or landed, green committed,
   and one closing line only when the whole walk holds (SPEC INV-95; the communicator carries the walk).

7. **The concurrent-edit fence, before every write and every commit.** Re-check `git status` + HEAD against
   what you last read; if HEAD moved or the tree holds changes you did not make — STOP, re-read, then
   proceed surgically or back off. A repo you were not assigned to is read-only (one exception: a new wish
   file in its inbox). Applies to ANY skill that writes shared files, not just adoption (SPEC INV-10, INV-11). And within ONE session up to three build lanes may roll without asking (SPEC T-18; a fourth only on the human's asked word): every write to a document the lanes share serializes under the single PEN, one lane at a time; a later train's code and tests live in its own isolated copy of the tree until the senior integrates them, so worktree isolation is the default when two lanes' write-sets overlap and a shared file one lane holds open is never written by another (SPEC INV-105); a landing commit carries exactly one row's delta, its gate run on a tree clean of any other lane's unfinished work (SPEC INV-39). A background worker from a PRIOR context is a concurrent writer too: it survives a memory wipe, and the OS process list and the harness task list are never proof of death. Such a worker is a foreign writer until verified by the resume protocol's three checks — the write-set's file times watched over a short window, the worker's heartbeat on its own checkpoint file (a fixed-interval touch, stale past ~2 min [default]), and one message to its recorded id — and no second worker goes onto a shared tree until the first has confirmed halted by its own reply or been declared dead by all three checks; the same-session fence-benign courtesy never crosses a wipe (SPEC INV-76). Every session mints a stable identity at its start — the harness session id where the context carries one, else the start time joined with the worktree path and a nonce — and records it in its `.live-spec/` checkpoint, unchanged for the session's life; the parallel-lanes pen tie-break orders on this identity for a genuine concurrent claim with no git ancestry, so exactly one session backs off (SPEC INV-117).

8. **Freshness: versions are re-checked at every safe breakpoint.** Re-stat the installed skills, the pack,
   and the profiles; on any version change re-read the changed file before continuing, working only from
   that freshly read copy, and journal one line naming old → new (SPEC A-7, M-7).

9. **History lives in the JOURNAL; docs travel with the change.** The dated WHY of every movement goes to
   JOURNAL.md the same session; SPEC / NEXT_STEPS / ROADMAP prose states only current truth. A shipped
   change updates its README / CHANGELOG / SKILL.md before the session ends. **Entries and harvested
   records carry date AND time of day** — "yesterday evening you wrote X, so I did Y" is answerable later
   only if the record holds the moment, not just the day; a decision file keeps its answered-at stamp, a
   journal entry opens with when it happened (2026-07-05).

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
    and its output. Your memory, a worker's summary, a document's prose are LEADS rather than evidence —
    before attributing a decision to the human or calling a behaviour "by design", read the actual source
    line (rule 5's raw-output clause is this rule's delegation face). No source at hand ⇒ say "not sure",
    then check before asserting.

14. **A found defect is a sample of its CLASS — go find the class, sweep the look-alikes.** A bug, a stale
    name, a jargon string, a design inconsistency: before calling the fix done, name the pattern behind the
    instance abstractly (the KIND of mistake — a scope too narrow, a missing guard, an assumption that holds
    in one place and fails in the neighbour), then actively search the whole repo and every user-facing
    surface for that kind and fix all siblings in the same change. The search goes looking for the siblings
    not yet seen, past the one instance already reported; one instance reported means the whole class is
    owned, and the human never finds the second instance by eye. A confirmed bug carries three more moves
    before it closes: check the architecture (a structural cause updates ARCHITECTURE.md, since a cluster in
    one district reads as an architecture smell), check the spec (a spec silent on the broken behaviour is
    the real defect, fixed first so the prover can flag it, then the code lands under it), and escalate to
    the human when the class boundary needs his read rather than a guess — the full four-move law lives in
    build-pipeline's bug entry and the spec's bug scenario (SPEC INV-124). A rule superseded at a broad scope is the same class: its restatements at narrower scopes — a host's CLAUDE.md, a project's playbook copy, an installed skill — go stale the instant the broad rule changes, so the same change that supersedes the rule sweeps those copies, never leaving a narrower scope quoting the old rule. Each working skill applies this in its own domain: the
    pipeline sweeps code and surfaces on every bugfix, the prover sweeps the document with its class lens before writing a
    point finding.

15. **The door is named before any code.** Every request states its entry point — feature · bug ·
    refactor · docs-only · skip — in one intake line beside size and priority, BEFORE the first line of
    code. The same line names the **work-kind** — product · infra · skill · prose — what the request
    BUILDS: the door picks WHICH pipeline steps run, the kind picks the FORM each running step takes
    (the per-kind table's one home is build-pipeline), and at landing every door-granted step has
    applied or been stood down BY NAME in the report, so every skip is named and every kind touches the
    safety net (SPEC T-16, INV-22). Hard tripwires decide, never mood: a new user-visible surface · new persistent state · a new
    interaction on an existing surface · a spec [target] mark on the touched surface · behaviour no spec
    clause backs ⇒ FEATURE, however casually asked — and the tripwire verdict outranks a casual label
    (queue-cutting stays with the bug door alone). The door re-fires mid-work: the moment running work is
    about to create a surface or state its door doesn't grant — STOP, reclassify, continue by the right
    door. Casual asks are routed, never refused — and never hand-built past the pipeline because they
    sounded small. (SPEC T-12, INV-16)

16. **A prototype stays a sketch.** Exploring is legal, but a sketch lives fenced: its own
    `prototype/` home, a PROTOTYPE label in the form its kind can show (screen banner · `_prototype:
    true` field/header · first-line CLI banner · name/header marker), never wired into or linked from a
    prod surface, and shown to the human only under its label. A request to merely SEE or TRY may be
    sketched; a request to HAVE it in the product is a feature — unclear which ⇒ one plain question
    (rule 1). Promotion is not a merge: the feature enters at the spec step; the sketch is evidence, its
    code holds no rights. Opening a prototype home is a repo write that belongs to the assigned senior
    alone; a worker doesn't open one on their own, and an outsider's route is an inbox wish instead. (SPEC E-17, INV-17)
17. **Irreversible means gone, not merely public.** Truly irreversible actions — spending money,
   deleting data, sending to a person or an audience you cannot unsend from — always STOP for the
   human's word, whatever the proactivity mode. A push to your own repository is NOT irreversible (it
   reverts); it rides the mode and the project's own push gates. When unsure which side an action is
   on, treat it as irreversible and ask — the criterion is "can we get back to before, ourselves,
   losing nothing?" (2026-07-05: money yes, deletion yes, a push no).

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
   the METHOD rather than of the day — it goes to the pack's own queue (from a host window: one inbox file).
   A recurrence on an owned entry appends its date and changes nothing else; the landing that closes an
   OWNED entry's row flips it to SOLVED. (SPEC E-24, INV-23; born of tlvphoto's retried-never-owned
   noise, 2026-07-05.) **And a known, owned problem never blocks unrelated work (SPEC INV-56):** it is PARKED — the
   ledger line, the owning row, or an expected-red note holds it — and every
   unrelated lane keeps rolling; hand-fixing loops cap at the two-strikes law above, and a defect with
   a NAMED mechanical owner is serviced in BATCH — instances fixed silently where the fence catches
   them, one ledger append at the session's end, with no per-instance ceremony interrupting the
   work (born of a clock drift hand-ceremonied ten times in one night while its owner row sat open,
   2026-07-07). A real NEW bug still preempts; this governs only the known, owned problem.

20. **Search for a skill before reinventing (SPEC INV-65).** At a project's setup (founding, or
   adoption's orient, beside the founding questions) scan the installed skills and the catalogs you
   can reach for ones matching the project's kind and its crafts; propose the fit list with a
   recommendation — the human's word picks. At a struggle — a ledger entry's second occurrence, a
   taste artifact rejected twice, any returning failure family — the next attempt waits one search:
   an existing skill or checklist may already own the failure class; the find is adopted or rejected
   by name, recorded where the struggle lives. Borrowing practice: invoke a found skill as it ships;
   paraphrase folded lessons and credit the source by name; verbatim text only under its license,
   notice kept.

21. **Human-facing prose is drafted by a clean writer (SPEC INV-84).** When a human will read the
   text, prepare a plain brief that states the facts, names the intended reader, and lists the
   register laws, then hand it to a fresh writer session that has no package rules loaded. Let the
   writer produce the prose; review the returned draft against the brief and land it, and do not
   write the prose yourself. Apply this to new text and to any page you are already editing. The
   unit is the section your edit touches; redraft a whole page only on the human's word. Text you
   type live in chat stays your own words under the register laws; the road binds the durable prose
   a human returns to. Leave settled text alone until a human rejects a specific page or your edit
   opens that page.

22. **Every process converges on its goal (SPEC INV-98).** Name the goal up front as an artifact
   the work can be held against — a frozen norm, an exemplar bank, a failing test, a written
   acceptance. A paraphrase cannot serve as the goal. Measure every iteration against the goal
   itself; a proxy never replaces the goal, and measuring against a proxy is where a look-alike
   is born. The distance only shrinks, and a reached level locks by a mechanism — a norm template,
   a conformance test, a lint floor that only grows, a cap that only ratchets down; attention
   alone holds nothing across sessions. A deliberately divergent stretch — exploration, a labelled
   prototype (rule 16) — is legal only when named and bounded by its convergence point. The
   principle's chapter lives in the private playbook repo's PLAYBOOK.md; the pack's own first
   teeth are the norm-conformance rows and the convergence-lock tests (rows 216/217). (The
   owner's word, 2026-07-10: convergence covers every process and every kind of artifact — there
   is a goal, and we walk toward it, always.)

23. **A behavioural rule that breaks mid-turn twice earns a live channel (SPEC INV-108).** A standing
   behavioural rule keeps its normative home in a once-read file — the loader, a profile, a skill's
   text. When the rule breaks mid-turn a second time despite that home, it earns a live channel that
   same moment: an every-prompt hook line that reminds at the decision point, or a mechanical
   after-the-fact check that turns the suite red. Record the pick where the rule lives. The once-read
   homes stay the normative homes; the live channel only carries the rule to the moment it is needed.
   Prose in a once-read file loses to mid-turn momentum, and attention alone holds nothing across
   sessions. This rule is the convergence principle's hand for behaviour (rule 22), kin of rule 19's
   second-occurrence law. The worked proof: the routing rule lived in once-read files since June and
   broke mid-turn until the every-prompt hook line and the mechanical after-the-fact check landed
   (rows 253/254, 2026-07-12), the same cure that killed invented clock stamps. The 1.1.0 audit's
   once-read walk is this law's first sweep.

24. **The process stations are kind-abstract; a project declares its concrete layers and proofs (SPEC
   INV-135).** The entry impact read, the footprint categories, and the test ladder are stations the pack
   states once, and the stations are kind-abstract: each project kind fills them with its own concrete
   layers and its own concrete proof kinds. The three footprints generalize past code — a
   presentation-only change touches what the audience meets and nothing behind it, a single-module change
   stays inside one owned layer, a cross-cutting change moves a shared law or several layers at once — but
   the LAYERS themselves are the project's own: a codebase splits frontend, backend, and store; a photo
   site content, rendering engine, and deployment; a promotion campaign message, channels, and assets; a
   music project arrangement, stems, and mix. The proofs follow the same shape, each kind naming the
   rungs its test ladder really has: a codebase proves with unit tests and rendered or pixel checks, a
   photo site with a byte-diff of the baked output and the owner's eye-walk, a promotion campaign with a
   register lint and the owner's review. So each project kind, recorded at founding as `project.kind`
   (SPEC INV-36) in the host profile, declares its concrete layers and its concrete proof kinds there —
   one `project.layers` line and one `project.proofs` line. A profile that records a kind with neither is
   incomplete, flagged at adoption the way an unbacked surface is; the per-kind fill is then the
   project's own ratchet — the footprint check and the test-level check read the project's declared
   categories rather than a hardcoded code list. ARCHITECTURE.md carries the per-kind
   footprint-and-proof table, and spec-author and test-author read the declared layers and proofs
   instead of assuming code. The one method fits every window this way — one abstract station, each
   kind's own concrete fill — rather than a code method worn awkwardly by a photo site.

25. **The orchestrator reads to decide, not to discover (SPEC INV-137).** The lead's context holds only
   what orchestration needs — the human's words, the decisions taken, the distilled results workers hand
   back, and the few anchors the lead must cite. Reading a file to UNDERSTAND or DESIGN, past a glance, is
   itself work, so it routes like any work (rule 5): the lead dispatches it to a reader — a search-and-locate
   pass or a read-and-distill brief — and reads the distillation the worker returns, not the raw file bodies.
   A glance is bounded: one small file, or a handful of targeted lines whose result IS the deliverable (a
   version string, one clause to quote). Past the glance, dispatch. The duty binds the reads done to DISCOVER or UNDERSTAND, where a distillation is the right return. A read to VERIFY a claim or settle a decision stays with the lead: checking the real artifact and re-reading a primary source are the lead's own hands (rules 11, 13), and a dispatched verification returns the raw evidence the lead re-checks (rule 5). The leanness is load-bearing — a lead
   that fills its own context with source it could have had distilled loses the room to hold the whole arc,
   and its judgment degrades as the context bloats. Workers locate their own anchors from the brief, so the
   lead never reads a file merely to hand a worker its anchors (rule 5, SPEC INV-69). The brief's own read of
   the files it will change (SPEC INV-53) composes with this rule rather than fighting it: that read is
   dispatched to the reader whose distillation returns the per-file lines the brief records, or, for a small
   edit, is a decide-read the lead makes directly and keeps bounded. And the discipline is made visible rather
   than trusted to memory: the landing report's delegation accounting names the reads dispatched beside the
   work delegated (SPEC INV-103, INV-137), so a session that slid into reading-to-discover shows it.

26. **A project kind also declares design principles the verify pass runs (SPEC INV-136, INV-139).** Beside
   the concrete layers and proof kinds a project kind carries (rule 24, SPEC INV-135), a kind names a set of
   checkable design principles — the frontend kind's interactive-overlap rule and its legibility floor among
   them — homed in the per-kind design-principles table in ARCHITECTURE.md. The verify feel pass reads the
   declared principles and runs each in the medium's own form, a principle no suite can green being the
   human's own eye-walk. This rule is the base home the design-principles invariants own; their full
   statement and per-kind starter sets live in ARCHITECTURE.md.


## When NOT to load this

Reserve it for the pack's own work — a session outside the pack uses a general style guide instead; and
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
| session | the human's live word, held only in the conversation itself | RIGHT NOW, one conversation |

An override exists only as a written line in its profile file, and setting one leaves a dated journal note
in the home it governs, keeping every divergence visible (SPEC INV-14). The session scope is the one exception —
it lives only in the human's spoken word and dies with the conversation; the agent never writes it
anywhere on its own, and making it outlive the session is a PROMOTION into the profile it describes, on
the human's word, journaled like any other override. Proactivity mode and trust are written
only on the human's word — the agent may propose, never set (SPEC INV-9). Profiles are re-read at the same
freshness points as skills (rule 8). A profile line the current pack does not recognize is ignored ALOUD —
named once in the session's next report as a visible, ordinary skip, never an error.

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

| Setting | Default | A profile may say | Card |
|---|---|---|---|
| `language.docs` | English — docs, commits, code, artifacts | another docs language | visible |
| `language.chat` | mirror the human's language | pin one (e.g. Russian) | visible |
| `proactivity.mode` | ask-at-max — surface forks, wait on taste calls | max-proactive: proceed on recommendations, batch questions | visible |
| `trust` | low — human word before outward moves | raised only by the human (INV-9) | internal |
| `prover.cadence` | FULL pass before every MINOR bump; CROSS-LINK on every surface add | tighter (e.g. live-spec itself: before every push) or looser, recorded | internal |
| `worker.tiering` | router proposes the cheapest sufficient tier; senior may override, logged | fixed tier per size class (SPEC D-2) | internal |
| `checkpoints.home` | `<host>/.live-spec/checkpoints/`, gitignored | another host path | internal |
| `spec.file` | `PRODUCT_SPEC.md` — the host's product spec file; every pack guide reads "PRODUCT_SPEC.md" as this file under its recorded name | a host that adopted under its own name keeps it, recorded as one host-profile line (e.g. `spec.file: SPEC.md`); a rename may be offered together with its pointer sweep, never forced (SPEC INV-90) | internal |
| `work-kind.host-default` | none — each wish's kind is called at intake | a host with ONE usual kind names it as the intake default (SPEC T-16) | internal |
| `project.kind` | none — asked at founding and at adoption's orient, always the human's answer, never profile-seeded or inferred (SPEC INV-36) | the host's own kind: book · backend service · static site · fullstack app · CLI · skill pack · a custom kind through the queue; seeds project-wide defaults, never overriding an explicit line; updated on the human's word the moment the project outgrows it, journaled | visible |
| `project.design-principles` | none for a kind with no visual surface; a visual kind (e.g. frontend / fullstack app) declares its set at founding, seeded from that kind's starter table in ARCHITECTURE.md's per-kind design-principles section (SPEC INV-136) | the project's own checkable design rules, one line, extended past the starter set through the queue; a visual kind recorded with none is flagged the way a kind recorded with no layers or proofs is (SPEC INV-135) | internal |
| `design-sync` | off — a host with visual components may switch it on (recorded profile line, SPEC E-18, INV-14) | on: a landing's DECLARED components sync to the team's design project, every sync behind the human's publish gate (rule 17) | internal |
| `budget.pressure` | full — full rigor everywhere; the economy ladder's rung (SPEC T-19, INV-40) | lean or tight, ONLY on the human's word (a session's word or a profile line; asked — or the default told — at a project's setup, founding or adoption, alongside `project.kind`; the agent proposes a rung when money/time pressure is named, never sets one); each rung's legal sheds and the never-bend list live in the SPEC's economy-ladder section — every taken shed is named in the landing report, and an explicit host line outlives any rung | visible |

The Card column says what the settings card renders: a `visible` row appears on the card; an `internal` row is workshop machinery the card leaves out, reaching the reader only as a recorded host-profile line in the card's project-rules part. The card's own law lives in the SPEC (INV-87).

A profile file is plain markdown: one `setting: value` line per override, each with a trailing date and,
when it narrows the defaults, one line of WHY. Settings not listed above may be proposed as wishes — the
table grows through the queue like everything else.

> The pack, whole: **live-spec-base** holds the shared rules and defaults · **spec-author** writes the spec ·
> **product-prover** reviews it · **build-pipeline** ships the change · **test-author** derives the matrix and writes the tests · **communicator** makes the human
> exchange land · **feedback-intake** brings what comes back to its home · **publish** sees the work out the door, owing its kind's checklist.
