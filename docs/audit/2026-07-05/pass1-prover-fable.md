# Prover record — FULL whole-spec review (preventive audit pass 1, Fable run)

Date: 2026-07-05 · Doc: SPEC.md v0.8.1 · Mode: FULL (MINOR gate for 0.5.0)
State audited: working tree at VERSION 0.2.4 (NEXT_STEPS names commit 07b6fea, 4 ahead of origin).
Cross-links in view: ARCHITECTURE.md v0.1, TEST_MATRIX.md v0.1, JOURNAL.md (2026-07-05 entries).
Run independence: this pass was produced WITHOUT reading the parallel Opus outputs under docs/audit/.
Fold status column: to be filled by the senior at the fold step (per build-pipeline step 2).

TRIAGE: PROCEED — a product spec with explicit entities, states, transitions, invariants and a Formal
index; the shipped-system claims are backed by ARCHITECTURE.md node pins written from commands run
2026-07-05, so findings are not conditional.

## Opening assessment

The spec states a method package: wishes enter a queue, walk a proven pipeline, machines hold the bounds,
the human is interrupted only for genuinely-theirs decisions. Strongest parts: the shipped-vs-target
honesty (S-0) is applied consistently — every [target] names its owning queue row; and the settings
ladder (E-13/E-16, new in v0.8) is unusually well composed — the session scope that is deliberately
never a file, inheritance narrowest-out, and the ignored-ALOUD rule for stale profile lines all close
holes most specs of this kind leave open. Two things need attention: the core lane invariant "execution
is serial" is contradicted by the pack's own blessed practice of parallel Sonnet workers (F1), and the
spec's session-level rules (write-ownership, the edit fence) don't say how they project onto workers a
session spawns — reachable today, this very audit run reached it (F2). Overall: needs one more small
iteration — fold F1 and settle F5's wording before the row-52 flip; no structural rework. Ready to gate
0.5.0 once F1 is folded.

## Phase 1 — the model

Entities and relationships:
- Wish: born spoken (E-2), becomes exactly one queue row (E-3); grows the spec (E-4).
- Queue row: one per wish; class {bug, small, surface, large} + priority {normal, critical, quick-win};
  never deleted, only closed with a named exit.
- Spec / Architecture doc / Matrix: the three derived layers; every spec fact owned by one architecture
  node (E-14), every fact ≥1 matrix row at a pinned level (E-15).
- Machines: guardrails (E-6, first slice live), snapshot (E-7, target), surface registry (E-10, target),
  matrix (E-5).
- Settings: package defaults (E-12) ⊃ personal profile ⊃ host profile (E-8) ⊃ session word (E-13);
  loader = thin bootstrap home (E-16).
- Package repo surfaces: inbox (E-11), attic (E-9), prover records, NEXT_STEPS/JOURNAL (M-2/M-3).

States of a wish:
1. arrived (row exists) — exits to classified (T-1..).
2. classified → spec-delta → validated → queued → in-work → landed (T-1..T-7, report closes it).
3. in-work — may exit to parked (bug preempts, T-9); parked resumes as the immediate next landing.
4. Terminal-but-kept: declined / deferred (named revisit trigger) / superseded (points to absorber) (T-8).

Actors: the human (ACT-1: taste, gates, wording, contract), the senior agent (ACT-2: judgment), tiered
workers (ACT-3: mechanical, checkpointed; router still target), outsider sessions (inbox-only, INV-10).

### What I assumed
- "Execution is serial" (INV-2) I read as governing the lane end-to-end, because the sentence says so —
  F1 tests that reading against the journal.
- The playbook repo I treated as NOT one of the three host projects when weighing E-16's "outside any
  project repo" (F5 asks for the sentence to say this itself).
- The pack's own repo I treated as exempt from E-6's offer-first hook rule (hooks self-installed on the
  flagship are the dogfood instance, M-4) — the spec implies but does not state this; benign.

## Phase 2 — structural issues

F1 — The lane's core invariant says serial execution; the pack's own journal records blessed parallel execution

> "Intake is parallel, execution is serial — one landing at a time; a new wish waits its turn" — Throwing a wish, SPEC.md:59-60

The flagship's journal (2026-07-05 ~15:45 entry) records rows 3 and 51 executed by two Sonnet workers
in parallel and both landed, with the senior on judgment — praised, not flagged. A reader building a host
on this spec must either forbid what the method's own authors do, or violate the invariant; and
`test_roadmap_single_in_work` (matrix M-022) makes two simultaneous in-work rows a red suite, so the
session either mis-marked the queue or ran red.

Refine INV-2 to say what practice already is: the LANE (spec-delta, validation, integration, the landing
ceremony) is serial; bounded delegated execution may overlap when the rows touch disjoint files and the
edit fence [INV-11] is armed; landings still close one at a time. Record the refinement as the
INV-5-visible decision it is.

`must-fix · internal-conflict (consistency)`

F2 — Session-level rules never say how they project onto the workers a session spawns (class finding, two instances)

> "Only a session you assigned to live-spec itself writes this repo" — Package repo, SPEC.md:293
> "Before writing to a repo — and again before every commit — the agent re-checks `git status` + HEAD" — Package repo, SPEC.md:309-310

Instance 1 (INV-10): a worker spawned by an assigned session writes the repo today — this very audit run
does it — yet the write-ownership test ("the human asked ME, in this conversation") is worded for
sessions, so a worker passes or fails it only by interpretation; an outsider session could claim the same
interpretation for ITS workers. Instance 2 (INV-11): four same-session workers writing sibling files each
see a tree with changes they did not make — the fence as written says STOP, and only inbox/ files are
named benign, so a literal worker either halts mid-audit or learns to ignore the fence.

Add one sentence to each: a worker inherits its spawning session's write-ownership NARROWED to the files
its brief names, never wider; and same-session sibling-worker files declared in the briefs join inbox/
as the fence's expected benign case.

`should-clarify · boundary-issue (composition)`

F3 — Two different name-collision laws in one pack, and the attic's law doesn't survive a second collision (class finding)

> "on a basename collision the source dir prefixes the name" — Adoption step 4, SPEC.md:114
> "name taken → append `-2`, `-3`, …" — Package repo (inbox), SPEC.md:301

The attic prefix rule resolves one collision shape only: the same path superseded twice (adopt moves
`src/config.md`, a later rework supersedes the regenerated `src/config.md`) yields the SAME prefixed name,
and an overwrite would silently lose the first attic copy — the exact loss INV-7 exists to prevent. The
inbox already carries the general law (numeric suffix); the pack thus states the same class of rule two
different ways.

Extend the inbox suffix law to attic collisions ("prefix, then `-2`, `-3` if still taken") and state the
collision law once, in the base skill, referenced by both surfaces.

`should-clarify · missing-scenario (state-space)`

## Phase 3 — property analysis

F4 — The mechanical push gate checks a today-dated record; the rule it enforces demands a record for the pushed STATE

> "a today-dated prover record exists" — Machines (guardrails), SPEC.md:272
> "No re-check record for the pushed state ⇒ the push should not have happened" — Rhythm (M-6), SPEC.md:343-344

Two pushes in one day: the morning push leaves a record; the spec changes at noon; the evening push passes
the hook on the morning record with no re-check — the operator sees a green gate and a violated M-6, and
nothing red anywhere. The spec itself promises honesty about mechanical reach (M-4), so the gap belongs in
the text or in the hook.

Tighten the hook: the record must be newer than the last commit touching SPEC.md (one `git log -1` +
mtime compare in `guardrails/pre-push`), or have E-6's sentence say aloud that same-day repeat pushes ride
the earlier record and the human gate covers the residue.

`should-clarify · unenforceable-promise (discharge)`

F5 — "Outside any project repo" will read as contradicted by the very landing that implements it

> "the personal profile lives on the human's machine outside any project repo" — Who decides what (E-16), SPEC.md:210-211

Row 52's reviewed migration map gives the profile a git home INSIDE the playbook repo (private, personal)
with a symlink — the flip is the next landing, and its reviewer diffs the landing against this sentence
and finds them in conflict unless "project repo" already excludes a private personal repo. That reading is
plausible but nowhere stated.

Before the flip, reword to what is meant: "outside any HOST or pack repo; a private repo owned by the
human may serve as the profile's git home." One sentence, folds with the flip landing.

`should-clarify · internal-conflict (consistency)`

F6 — Bootstrap still gates version control SECOND, after the reversibility lesson moved adoption's gate FIRST

> "Copy the templates (SPEC, ARCHITECTURE, TEST_MATRIX, ROADMAP, JOURNAL, NEXT_STEPS) → version-control gate → the first wish" — Bootstrap, SPEC.md:86-87
> "the version-control gate [A-5] is performed FIRST — before anything is touched or moved — so the whole run is reversible" — Adoption, SPEC.md:93-94

A bootstrapped project copies six files into an unversioned directory; if the run dies between copy and
gate, the half-copied set has no baseline to diff or roll back against — precisely the argument A-0 used
to reorder adoption after the tlvphoto pilot. The two flows state opposite orders for the same gate with
the rationale written beside only one of them.

Reorder B-1: gate → copy templates → first wish; one line here and in the bootstrap section of the
templates/ADOPT text if it restates the order.

`should-clarify · internal-conflict (consistency)`

F7 — Nothing keeps the loader thin after the flip

> "The machine-global instruction file … shrinks to a thin loader: the pointer that loads the profile, plus ONLY the bootstrap lines" — Who decides what (E-16), SPEC.md:200-202

M-065's owning test is the one-shot flip landing (diff-proven fork map); the day after, any session may
append "just one line" to the loader — the exact accretion that bloated CLAUDE.md in the first place —
and no milestone item or matrix row goes red. The human finds out when the loader is fat again.

Add a standing item to M-1's milestone list (and a matrix row): every loader line passes the
must-hold-before-pack-loads test, count stated in the audit report; anything else is a fold into profile
or pack.

`worth-considering · missing-rule (invariant)`

F8 — A wish absorbed into another silently dies if the absorber is declined

> "superseded (absorbed by another wish; the row points to the absorbing one)" — Throwing a wish (T-8), SPEC.md:69-70

You wish X; X is superseded into Y; months later you decline Y knowing only Y's framing — X's row still
points at a dead absorber, no rule re-opens or re-asks it, and INV-1's "no wish is ever lost" holds on
paper (the row exists) while the wish is operationally gone without your "no" ever touching X.

One sentence on the decline exit: declining a wish lists its absorbed rows in the decline report, each
either declined-by-name or returned to the queue.

`worth-considering · undefined-path (transitions)`

F9 — Derivation headers pin the spec version they were born from, with no rule for when they re-pin

> "Derived from the proven SPEC v0.7.1 through the proven ARCHITECTURE.md v0.1" — TEST_MATRIX.md:3 (sibling: ARCHITECTURE.md:3 "Written from the proven SPEC v0.7")

Both documents now carry v0.8 anchors (E-16, M-065) under headers naming v0.7.x — a reader auditing
"decided under which spec" trusts the header and reads one version too early. The README's drifting pin
was fixed this morning as a class; these two are the surviving deliberate written-against pins, but no
rule says when they refresh.

Add to M-1: at each milestone the matrix and architecture headers re-pin to the spec version then proven
(one line each, part of the index re-check step).

`worth-considering · hard-to-operate (ops-ux)`

### Coverage tables

CRUD per entity (the product's mutable records):

| Entity | Create | Read | Update | Delete | Notes |
|---|---|---|---|---|---|
| Queue row | covered (T-1, T-10) | covered (report, M-1 re-list) | covered (status, marks) | covered-as-never (INV-1) | closes, never deletes |
| Inbox file | covered (E-11) | covered (T-10 sweep) | forbidden (new-file-only) | covered (harvest commit; named non-attic case) | clean |
| Attic file | covered (A-4) | covered (manifest) | append-only | forbidden (INV-7) | second-collision gap → F3 |
| Profile line | covered (INV-14, on the human's word) | covered (ladder resolution) | covered (journaled override) | partial — removal of a line is presumably an override too, not stated | minor; rides F5's reword if touched |
| Snapshot baseline | [target] (A-6) | [target] | covered (advance at landed, declared-only) | open (D-3 retention) | honest target |

Invariants per state (wish): arrived/queued — INV-1, INV-12 stated; in-work — INV-2 (→F1), INV-4, INV-5
stated; parked — T-9 states the checkpoint + nothing-red; terminal exits — T-8 stated, absorber-death
missing (→F8). No state lacks an exit; no dead ends found.

Authorization per action: the actor table is crisp and stated (ACT-1/2/3, INV-9, INV-10); the one
enforcement gap is worker-inheritance (→F2). No separate table needed beyond that finding.

## Phase 3.5 — acknowledged gaps

D-1 (attic layout), D-2 (tier routing), D-3 (snapshot retention) — each carries a current pick and a
named revisit trigger; that is exactly the right shape, nothing to add now. D-3's trigger ("when a diff
dispute needs history") is the vaguest of the three — fine to leave until the snapshot machinery (row 55)
makes it concrete. D-4/D-5 record decided states with executing rows — checked against the queue, both
rows exist (51 closed, 52–54 live). `acknowledged · missing-rule (invariant)` for the set.

## Phase 4 — human and operational factors

- Observability is a strength: report shape (T-7), ignored-ALOUD profile lines, the M-1 re-listing of
  open gates and unharvested inbox files — the human can always see what waits on them.
- One operational ceiling left implicit: nothing states how large the queue may grow before M-1's
  re-listing and the audit passes stop being readable in one sitting (the queue is at ~58 rows today).
  A one-line budget ("queue re-listing groups by status once rows exceed N") would name it. Rides as a
  note, not a finding.
- Security/privacy: the personal profile is personal data; its git home (F5) should stay a PRIVATE repo —
  the spec should say the word "private" when F5's sentence is folded. Otherwise out of scope by nature
  of the product — a named skip.

## Phase 5 — closing summary

Top fixes before the 0.5.0 gate closes:
1. F1 — refine INV-2 to match blessed practice (serial lane, bounded parallel delegation, serial closes).
2. F5 — reword E-16's "outside any project repo" before the row-52 flip lands against it.
3. F2 — one sentence each on worker inheritance for INV-10 and the fence's benign set for INV-11.

Properties to paste into the spec:
- "The lane is serial; delegated execution may overlap only on disjoint files with the fence armed;
  landings close one at a time."
- "A worker inherits its session's write-ownership narrowed to the files its brief names."
- "Attic collisions resolve by prefix, then numeric suffix — the same law as the inbox."
- "Declining a wish lists its absorbed rows; each is declined by name or returned to the queue."

Open questions genuinely for the author: none — every finding above carries a recommended resolution.

Counts: 1 must-fix · 5 should-clarify · 3 worth-considering.
Readiness: needs one more small iteration — fold F1 (and F5 with the flip), then ready to gate 0.5.0.

| Finding | Severity | Folded / rejected |
|---|---|---|
| F1 serial-lane contradiction | must-fix | — |
| F2 worker projection of INV-10/11 | should-clarify | — |
| F3 attic collision law | should-clarify | — |
| F4 push-gate freshness | should-clarify | — |
| F5 profile git-home wording | should-clarify | — |
| F6 bootstrap gate order | should-clarify | — |
| F7 loader thinness fence | worth-considering | — |
| F8 absorbed-wish death | worth-considering | — |
| F9 header re-pin rule | worth-considering | — |
