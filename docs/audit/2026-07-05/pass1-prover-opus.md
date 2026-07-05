# Pass 1 — Product-Prover FULL review (Opus)

**Audit target.** `~/live-spec/SPEC.md` v0.8.1 (2026-07-05).
**Repo state.** git HEAD `15369ba1f892d76d10734e18b2e0dcff2bf15595` (task brief expected ~`07b6fea`; HEAD has moved on since the brief was written — findings are pinned to the v0.8.1 text as read at this HEAD).
**Cross-link context read:** `ARCHITECTURE.md` v0.1, `TEST_MATRIX.md` v0.1, `ROADMAP.md` (rows 3, 14, 30, 38, 50–56), `VERSION` (0.2.4).
**Mode.** FULL (required before the 0.5.0 MINOR gate). Reviewer: product-prover v0.1.3 method, all phases, all 8 stress families.
**Pass identity.** This is one of two independent Pass-1 runs; written without reading the sibling run.

---

## Opening assessment

This spec describes a discipline-as-a-package: a wish is spoken, becomes a durable queue row, walks a proven pipeline, and lands under mechanical gates, with the human interrupted only for genuine decisions. It is unusually mature for a self-authored spec — the anchor system is internally complete (every prose anchor has an index home and vice versa, verified by grep), the shipped-vs-target honesty rule (S-0) is actually honored, and the hard-won operational rules (the concurrent-edit fence, the inbox intake door, attic-never-delete) read like they were paid for in real incidents.

The two biggest things working: the **anchor/index discipline is airtight** — I could not find a single orphaned or homeless anchor — and the **write-ownership + fence model** for a shared public repo is genuinely well thought through. The two things that most need attention: the **serial-execution invariant (INV-2, "one landing at a time") does not compose with the two-parallel-sessions reality the same spec describes** — serialization is asserted globally but only enforced at commit time, per-session; and several **multi-step handoffs are described as single acts** (the inbox harvest, the push-gate fold, the adoption sequence containing a `[target]` step) where a crash or a parallel actor mid-step leaves an observable inconsistency.

Overall confidence: **needs one more iteration before the 0.5.0 gate** — not rework. The structural model is sound; the gaps are concentrated at concurrency seams and multi-step atomicity, which is exactly where a dogfooding flagship that already had "one evening of two parallel sessions" will get bitten. Roughly a half-day of spec surgery closes the must-fix set.

---

## Phase 1 — The model

### 1a. Entities and relationships

- **Package (live-spec)** — the attachable thing: a base skill + four working skills + templates + adoption procedure + guardrails. Versioned by the `VERSION` file (0.2.4). [E-12]
- **Host** — the project the package attaches to; owns its SPEC/ARCHITECTURE/MATRIX/ROADMAP/JOURNAL, a surface registry, and a `.live-spec/` folder. One package → many hosts; live-spec is its own host (dogfood). [E-1, M-4]
- **Wish** — one request in plain words, any size, any moment. Becomes exactly one queue row. [E-2]
- **Queue row (ROADMAP.md)** — the durable home of a wish: words · class · status · acceptance. Never deleted, only closed with a named exit. [E-3, INV-1]
- **Spec / Architecture / Matrix** — the three derived documents; matrix rows are `node × fact`. [E-4, E-14, E-15]
- **Inbox file** — one new committed file per wish born outside a live-spec session; harvested into a queue row. [E-11]
- **Profile (personal / host)** — the human's working contract, resolved through a four-scope ladder. [E-8, E-13, E-16]
- **Snapshot `[target]`** / **surface registry** / **guardrails** — the machines that hold the bounds. [E-6, E-7, E-10]
- **Attic** — append-only archive of superseded host files. [E-9]

### 1b. States and transitions

States of a **Wish/queue row** (the one entity with a real lifecycle):
1. `arrived` — entered the minute the wish is spoken (or an inbox file is harvested); exits to `classified`.
2. `classified` — size (bug/small/surface/large) + priority (normal | critical | quick-win) assigned; exits to `queued`, or asks-at-intake if unclassifiable (carries `normal` meanwhile).
3. `queued` — waiting; exits to `in-work` when the lane frees (order bent by priority: critical heads even the bug line; a quick-win may bubble once).
4. `in-work` — the single active landing; exits to `landed`, or to `parked` if a bug preempts, or to an exit state (`declined`/`deferred`/`superseded`).
5. `parked` — a wish displaced by a bug; a checkpoint is written; resumes as "the immediate next landing." **(Exit condition contested — see F-3.)**
6. `landed` — green suite + guardrails + committed + row closed with acceptance met; triggers the report step.
7. exit states `declined` / `deferred` / `superseded` — terminal; the row stays in the table (but see F-5 on milestone compaction).

### 1c. Actors

- **Human (Alexander)** — taste, design, irreversible calls, push/publish gates, domain wording; sets mode/trust only by their own word. [ACT-1, INV-9]
- **Senior agent** — judgment: spec deltas, matrix levels, findings triage, this document. [ACT-2]
- **Workers (tiered) `[router: target]`** — mechanical execution, checkpointed. [ACT-3]
- **Outside session** — a session not assigned to live-spec; read-only on the repo except creating one inbox file. [INV-10, E-11]
- **The machines** — guardrails/snapshot/registry: automated gate actors, mostly `[target]`. [E-6, E-7, E-10]

### 1d. Composition / boundaries

Named nodes (from ARCHITECTURE.md): base-rulebook, spec-author, product-prover, build-pipeline, communicator, templates, attach, inbox, host-contract, package-docs, guardrails `[target]`, snapshot `[target]`. Every spec anchor is owned by exactly one node. Seams are named (spec→prove, prove→record, outside-wish→queue, ladder-resolution, checks→push).

### What I assumed

- I read **"one landing at a time" (INV-2) as intended globally** (across all sessions), not merely per-session — because the spec elsewhere treats the queue and serial execution as a single shared truth. If INV-2 is meant only per-session, that itself needs stating (F-1).
- I treated **`VERSION` (0.2.4, package) and the SPEC header (v0.8.1, document)** as two legitimate homes — package version vs document version — per M-3/M-7, not a contradiction.
- I treated the **snapshot, surface registry, guardrails host-checks, CI mirror, and model router as genuinely not-yet-built** (`[target]`), and did not raise findings about their internal mechanics as if they were shipped — only about how the spec's *shipped* flows depend on them.
- I read the **ARCHITECTURE/MATRIX "derived from SPEC v0.7 / v0.7.1" headers** as stale-but-not-wrong: the anchor set was kept in sync (E-16 is owned and has a matrix row) but the version-of-record citation wasn't bumped (F-11).

---

## Phase 2 — Structural issues in the model

**F-1 — "One landing at a time" is asserted globally but only enforced per-session; two parallel sessions break it.**

> "Intake is parallel, execution is serial — **one landing at a time**" — Section "Throwing a wish", INV-2 (SPEC.md:59)

The same spec describes two live-spec sessions running at once ("one evening of two parallel sessions taught us the rules", SPEC.md:290–291) and gives them a *commit-time* guard (the concurrent-edit fence, INV-11) plus "never push while another session is known to be live." But nothing serializes the **lane** itself: two assigned sessions can each pick a `queued` wish, each move it to `in-work`, and each work it — the fence only trips when the second one *commits* over a changed tree. So INV-2's "one landing at a time" is true within a session and false across the two sessions the spec explicitly supports. Concretely: the senior agent in session A lands wish 40 while session B lands wish 41; both touch ROADMAP.md and SPEC.md; B's commit fence forces a re-read, but two wishes were `in-work` simultaneously — the very thing INV-2 forbids — and their spec-deltas may conflict.

Add a sentence to INV-2 (or the two-sessions section) stating the scope of serialization and the lane token: either (a) INV-2 is **per-repo global**, enforced by a single lane claim — a session marks the one `in-work` row and a second assigned session must see it and wait or pick a non-conflicting bug; or (b) INV-2 is **per-session** and cross-session collisions are caught only by the fence — in which case say so and state that two `in-work` rows are legal. I prefer (a): make the `in-work` row itself the lane token (one row `in-work` per repo is already asserted by test `test_roadmap_single_in_work`), and require an assigned session to check for an existing `in-work` row before starting.

`must-fix · boundary-issue (composition)`

---

**F-2 — The adoption "sequence, each phase completes before the next" contains a `[target]` phase that cannot complete today.**

> "Adoption is a sequence; each phase completes before the next." — Section "Attaching to a live project", A-0 (SPEC.md:93) … "6. **Baseline snapshot [target]**" (SPEC.md:127)

Step 6 (baseline snapshot) depends on the snapshot machinery [E-7], which is `[target]` — not built. So on a real adoption today, phase 6 cannot complete, yet phase 7 ("Incremental thereafter") must follow it. The pilot (tlvphoto, 2026-07-04) evidently reached "incremental" without a snapshot, so the "each phase completes before the next" rule is already violated in practice and the spec doesn't say how. An operator adopting a second host reads a strict sequence, hits a step with no machinery, and has no stated instruction — skip? block? stub?

State the degraded-mode rule explicitly: "Until the snapshot machinery [E-7] ships (ROADMAP row 55), adoption **records** the current artifacts as the baseline manually and marks A-6 deferred in the run's journal; phase 7 proceeds." Add "phases marked `[target]` are recorded-and-skipped until their machine lands" to A-0.

`should-clarify · stuck-state (liveness)`

---

**F-3 — Parked-wish resume vs quick-win bubbling: two rules claim the "next landing" slot.**

> "the parked wish resumes as the immediate next landing" — Section "When a bug cuts the line", T-9 (SPEC.md:79–80)
> "when the lane frees, it may be taken ahead of larger queued wishes" — Section "Priority bends the lane order", T-11 (SPEC.md:55–56)

When a bug finishes and the lane frees, T-9 says the parked wish resumes as the *immediate* next landing, while T-11 says a queued quick-win *may bubble ahead* of larger queued wishes when the lane frees. If a quick-win is queued while a wish sits parked, which takes the freed lane — the resuming parked wish (T-9) or the bubbling quick-win (T-11)? The spec gives both the same slot. An operator watching the queue can't predict the next landing, and the anti-starvation reasoning ("after one bubbled landing the queue head goes next") assumes the parked wish is "the queue head," which isn't stated.

Add one precedence sentence: recommend **parked-wish resume outranks a quick-win bubble** — the parked wish already paid the context-switch cost and is mid-flight; a quick-win bubbles only against *fresh* `queued` wishes, never ahead of a resume. State it in T-9: "A parked wish resumes ahead of any queued wish, quick-win included."

`must-fix · undefined-path (transitions)`

---

## Phase 3 — Property analysis

**F-4 — The inbox harvest is a multi-step handoff described as one act; a crash or re-sweep can duplicate or drop a wish.**

> "harvests each file into a queue row … the harvest commit removes the file" — Section "The package repo", T-10 (SPEC.md:304–307)

Harvesting is at least two writes: add a ROADMAP row, and remove the inbox file. The spec says "the harvest commit removes the file" but never says the row-add and the file-removal are the **same** commit, nor whether N files harvest in one commit or N. If they are separate commits, a crash between them leaves either the file present with a row already added (next sweep re-harvests → duplicate row, violating "one wish = one row") or the row missing with the file gone (wish lost, violating INV-1 "no wish is ever lost"). The outside session that filed it sees its file vanish and has no way to tell which happened.

State harvest atomicity and idempotency: "Each harvest is ONE commit that both adds the ROADMAP row and removes the inbox file; if interrupted, the file remains and the next sweep re-harvests — the row-add must be idempotent (a file already represented by a row is removed, not re-added)." Add an acceptance handle: the row records the source inbox filename so a re-sweep can detect an existing row.

`must-fix · partial-success-risk (atomicity)`

---

**F-5 — "Rows are never deleted" directly conflicts with milestone compaction of the queue; the resolution exists only in a queue row, not in the spec.**

> "rows are never deleted — only closed with a named exit. No wish is ever lost." — Section "Throwing a wish", INV-1 (SPEC.md:37)
> "doc COMPACTION (pruning: redundancy removed from spec/matrix/queue/skills — nothing grows unboundedly)" — Section "The rhythm", M-1 (SPEC.md:325)

INV-1 and T-8 promise every row stays in the table forever; M-1's milestone compaction prunes "the queue." As written these openly conflict. The reconciliation ("closed rows MOVE to a dated archive, attic-style") lives only in **ROADMAP row 30** — a queued prover finding — not in the spec text. A reader of v0.8.1 alone sees a contradiction with no pointer to its resolution, and the 0.5.0 milestone will itself run M-1 compaction against a queue INV-1 says is immutable.

Fold row 30 into the spec now (it's a `small` and it gates a clean milestone): change INV-1/T-8 to "rows are never deleted — closed rows are **archived** (moved to a dated queue archive at milestones, never edited, never lost — the attic principle for the queue)" and have M-1 say "compaction ARCHIVES closed rows, never deletes them [INV-1]." This removes the contradiction and lets the 0.5.0 milestone run honestly.

`must-fix · direct-contradiction (contradiction)`

---

**F-6 — The push-gate fold can change the pushed spec after the prover reviewed it, so the record no longer matches the artifact — while the gate's own invariant demands a matching record.**

> "folds produced by the gate's own pass do NOT re-trigger the gate — they ship with the same record … No re-check record for the pushed state ⇒ the push should not have happened." — Section "The rhythm", M-6 (SPEC.md:342–344)

A push-gate prover pass finds a must-fix; you fold it (edit SPEC.md); the folds "ship with the same record." So the record describes the **pre-fold** spec, but the pushed artifact is the **post-fold** spec — the record does not match what shipped, yet the same paragraph asserts "no re-check record for the pushed state ⇒ the push should not have happened." The loop-avoidance is sensible, but the invariant as stated is self-violating for any push that folds a finding, and a large fold (a must-fix can rewrite a whole rule) could introduce a new hole the record never saw.

Bound the fold and make the record honest: "the push-gate record covers the reviewed spec PLUS an enumerated list of the folds applied from that pass; folds must be **local** (edit only the sections the finding named). A fold that changes a section the finding did not name re-triggers the gate." Add the fold list to the record template.

`should-clarify · internal-conflict (consistency)`

---

**F-7 — The inbox collision law "creating a fresh file cannot collide" is too strong under two simultaneous outsiders.**

> "name taken → append `-2`, `-3`, … a few plain lines, never an edit to an existing file — creating a fresh file cannot collide" — Section "The package repo", E-11 (SPEC.md:301–304)

The claim rests on each wish getting a unique NEW path. But two outside sessions filing wishes with the same date+source+slug at the same instant both compute the same next suffix: both see the base name taken (or both see it free), both write `...-2.md`, and the second `git push` collides on an identical path — a merge conflict on the inbox, which the outsider (read-only, unfamiliar with the repo) is least equipped to resolve. "Cannot collide" is true against *sequential* creation, not concurrent.

Weaken the claim and give the tie-break: "creating a fresh file cannot collide with an EXISTING file; two simultaneous same-slug creations are resolved by the human at push (rare), or the suffix includes a short random token / the session id to make concurrent names disjoint." I prefer the session-id/token suffix — it makes the "cannot collide" claim actually true.

`should-clarify · concurrency (concurrency and order)`

---

**F-8 — Tie-breaks are unspecified where the spec orders by "arrival."**

> "**critical** bugs head the waiting line (among themselves by arrival), the rest follow by arrival" — Section "When a bug cuts the line", T-9 (SPEC.md:80–82)

The lane order leans on "arrival" order in three places (T-9 bug ordering, T-11 quick-win bubbling, the general queue). Two wishes/bugs recorded in the same minute (plausible when a human dumps several at once, or when an inbox sweep harvests a batch) have no defined relative order. The resolution is currently the queue's row order, but that isn't stated, so two sessions (or the same session across a restart) could order a batch differently.

State the tie-break once, generally: "When arrival times tie, order is the ROADMAP row order (top-to-bottom); an inbox batch harvests in filename-sorted order." This is a one-liner in the classification paragraph, referenced by T-9 and T-11.

`worth-considering · ambiguity (ambiguity and ties)`

---

**F-9 — The "ignored ALOUD" rule for an unrecognized profile line silently degrades when the session has no next report.**

> "a profile line the current pack does not recognize … is ignored ALOUD — named once in the session's next report, never a silent drop" — Section "Who decides what", E-13 (SPEC.md:182–184)

The guarantee is "named in the session's next report." If the session ends (wipe, crash, or a run that produces no report before dying) after reading the profile but before reporting, the unrecognized line was silently dropped after all — exactly the outcome the rule forbids — and the human never learns their contract line was ignored. For a settings layer that governs trust and language, a silently-dropped line is a real drift.

Strengthen to a durable surface, not an ephemeral one: "an unrecognized profile line is logged to the host journal AND named in the next report; the journal note is the durable home so a session that dies before reporting still leaves the trace." This reuses the existing journal-note discipline (INV-14).

`should-clarify · observability (observability)`

---

**F-10 — S-0 "never claims shipped what isn't" is honored today but enforced only by hand; no gate catches a forgotten `[target]` tag.**

> "This spec never claims shipped what isn't — sections below marked [target] await their row. [S-0]" — header (SPEC.md:14)

I verified by grep that every `[target]` item (E-6, E-7, E-10, M-5, ACT-3, A-6) is owned by a real ROADMAP row (3, 14, 55, 56) — so S-0 holds right now. But matrix M-052 records this as a *hand* check at milestones ("caught by hand in prover F1 this pass"), not a test. The failure mode is asymmetric and easy: a feature ships, someone forgets to drop its `[target]` tag (spec now under-claims — benign), OR worse, a `[target]` tag is removed when the feature ISN'T actually wired (spec over-claims — the exact thing S-0 forbids), and no mechanical check fires. For the flagship whose whole pitch is "the machines hold the bounds," an honesty invariant held only by hand is a soft spot.

Add a traceability test (cheap, string-level, fits the existing `tests/test_traceability.py`): "every `[target]` token in SPEC.md maps to a ROADMAP row whose status is not `landed`; every anchor the architecture pins to a real `file:line` (non-empty pin) must NOT carry `[target]` in the spec." This mechanizes S-0. Record it as a matrix row now even if the test lands with row 55.

`should-clarify · hard-to-monitor (observability)`

---

**F-11 — The derived docs cite an older SPEC version than the one shipped; a reader can't tell if ARCHITECTURE/MATRIX are current.**

> "Written from the proven SPEC v0.7" — ARCHITECTURE.md:3 · "Derived from the proven SPEC v0.7.1" — TEST_MATRIX.md:3 (SPEC header is **v0.8.1**)

Between v0.7.1 and v0.8.1 the settings ladder was rewritten (four nested scopes) and E-16 was added (rows 52–53). The matrix DID keep pace on coverage (M-065 owns E-16; M-002 was updated) and the architecture DOES assign E-16 to host-contract — so the anchor set is in sync — but both headers still cite v0.7/v0.7.1 and were last *proven* against v0.7. Per the spec's own rule (E-14), adding E-16 to an existing node is an "assignment" that "triggers no re-prove," so not re-proving is arguably in-bounds — but the stale version citation makes that invisible: a reader can't distinguish "deliberately not re-proven (assignment only)" from "forgotten." The matrix also carries a count seam: its coverage line says "70/70" while ROADMAP row 50's landing note says "69/69."

Bump the derivation citations to the current SPEC version with a one-line provenance note: "ARCHITECTURE.md derived from SPEC v0.7, kept current through v0.8.1 by assignment (E-16, no re-prove per E-14); last full architecture-lens prove: v0.1 / 2026-07-05." Reconcile the 69 vs 70 anchor count in one place. (This is a cross-link/traceability finding, not a defect in the SPEC prose itself — but it gates the 0.5.0 milestone, which re-walks the matrix against the CURRENT spec.)

`should-clarify · hard-to-operate (ops-ux)`

---

**F-12 — Workers have no stated failure/escalation path: a cheap-tier worker that returns a wrong result has no defined route up.**

> "the cheapest sufficient tier does the job (haiku one-shot / sonnet multi-step / senior judgment), budget-aware" — Section "Who decides what", ACT-3 (SPEC.md:217–218)

The routing picks the *cheapest sufficient* tier, but "sufficient" is judged before the work; nothing says what happens when the cheap tier proves insufficient (a haiku one-shot returns a wrong or empty result). Is there re-route to a higher tier, a retry bound, a senior fallback? Without it, a mis-routed mechanical task can silently produce a bad artifact that the senior only catches on spot-check — or not at all. The router is `[target]` (row 56), so this can be captured there, but the *rule* (escalate on insufficiency) is a spec-level property that belongs stated, not buried in the future machine.

State the escalation property now: "A worker result that fails its checkpoint verification (raw output doesn't meet the acceptance the brief named) escalates one tier up, bounded (at most to senior); the escalation is logged in the checkpoint. A tier is 'sufficient' only if its output passes verification, judged after the run, not before." Land the mechanism with row 56.

`should-clarify · stuck-state (liveness)`

---

**F-13 — Bootstrap has a version-control gate; the pipeline that runs *after* it does not name a green-suite precondition for the very first landing.**

> "the first wish enters the queue → the pipeline runs from intake. [B-1]" — Section "Starting a new project", B-1 (SPEC.md:86–89)

A landing's definition (T-1..T-6) requires "green suite + guardrails." On a *brand-new* bootstrapped project there is no suite yet and no guardrails installed — so the first wish's landing can't satisfy the landed-definition as written, or it satisfies it vacuously (zero tests = green). The spec doesn't say which. Bootstrap sets up version control but not the initial empty-but-present test scaffold, so "green suite" is undefined for landing #1.

State the bootstrap postcondition: "Bootstrap copies the six templates AND a minimal test scaffold (an empty-but-runnable suite + the traceability walk); 'green suite' for the first landing means that scaffold runs clean. Guardrails are OFFERED at bootstrap the same way as at adoption [E-6]." One sentence in B-1.

`worth-considering · missing-prerequisite (precondition)`

---

### Coverage tables

CRUD is meaningful here for exactly one mutated persistent entity (the queue row); the rest of the product is authored documents. Rendering it for the queue row only:

| Entity | Create | Read | Update | Delete | Notes |
|---|---|---|---|---|---|
| Queue row (wish) | covered (spoken → row, or inbox harvest) | covered (queue is the durable home) | covered (status transitions) | **intentionally absent** — INV-1 says never delete; but see F-5 (compaction conflict) and F-4 (harvest atomicity) |

Invariants per state (Wish lifecycle):

| State | Invariants stated | Invariants missing |
|---|---|---|
| arrived | row exists the minute spoken (INV-1) | tie-break on same-minute arrivals (F-8) |
| queued | order = priority-bent arrival | precedence vs a resuming parked wish (F-3); global vs per-session lane (F-1) |
| in-work | exactly one at a time (INV-2) | holds only per-session; two-session composition (F-1) |
| parked | checkpoint written, nothing red committed; at most one parked | resume-vs-bubble precedence (F-3) |
| landed | green suite + guardrails + committed + row closed | "green suite" undefined for bootstrap landing #1 (F-13) |
| exit (declined/deferred/superseded) | row stays in the table | vs milestone compaction (F-5) |

Authorization per action (the one place authority is non-trivial — three writer classes on the shared repo):

| Action | Roles allowed | Enforceable? | Notes |
|---|---|---|---|
| Write spec/queue/journal/skills | assigned live-spec session only | partial | INV-10 rule + fence (INV-11); enforcement is the commit fence + human push discipline, not a hard ACL |
| Create inbox file | any outside session (one new committed file) | yes | the sole write exception; but concurrent same-slug collides (F-7) |
| Set mode/trust | human only | by convention | INV-9; "agent never raises its own level" is a discipline, unmonitored (no gate asserts the agent didn't) |
| Push | human-gated (live-spec: every push behind the fence + fresh prover record) | partial | M-6; fold-vs-record seam (F-6) |
| Land (move a wish to landed) | assigned session | **not serialized across sessions** | F-1 — the core gap |

---

## Phase 3.5 — Acknowledged gaps

The spec is honest about its open decisions; these are commentary, not discoveries.

**A-G1 — attic layout (flat+manifest vs dated subfolders).**
> "flat with a manifest and source-dir prefix on collision (current pick) vs dated subfolders" — Open decisions, D-1 (SPEC.md:355–356)
Consequence: on a large adopt run, a flat attic with hundreds of superseded files becomes hard to browse; the manifest is the only index. Revisit trigger ("next real adopt run") is named — fine. Recommend keeping the current pick but adding a size threshold ("switch to dated subfolders past N files") so the decision self-triggers.
`acknowledged · abstraction`

**A-G2 — tier-routing override (mechanical vs senior-override).**
> "router proposes, senior may override, override is logged" — Open decisions, D-2 (SPEC.md:357–358)
Interacts with F-12 (escalation on insufficiency). Recommend closing D-2 and F-12 together at row 56 — both are "who moves the tier and when."
`acknowledged · actors`

**A-G3 — snapshot retention (last-only vs last-N).**
> "last-only (current pick) vs last-N" — Open decisions, D-3 (SPEC.md:359–360)
Consequence: last-only means a diff dispute two landings back can't be reconstructed. Named trigger is fine. Recommend last-only until the first dispute, as written.
`acknowledged · state-space`

**A-G4 — personal profile lives outside any git repo (ROADMAP row 38).**
Not in SPEC's Open Decisions but flagged in the queue: the personal profile at `~/.claude/live-spec/profile.md` has no history/backup/fence, so a disk loss or two racing sessions silently loses the human's contract. This is the durability twin of F-9. Recommend folding row 38's fix (git home + symlink) before the profile becomes load-bearing for trust/mode.
`acknowledged · ops-ux`

No other explicit TBDs remain — D-4 and D-5 are recorded as decided.

---

## Phase 4 — Human and operational factors

**F-14 — Two version scales (package 0.2.4, SPEC document v0.8.1) with no stated relationship invite "which version are we on?" confusion.**

> `VERSION` = `0.2.4` (repo root) vs SPEC header `v0.8.1` — M-7 (SPEC.md:331–334) / M-3 (SPEC.md:329–330)

Both homes are legitimate per M-7 (package = VERSION file) and M-3 (documents dated-versioned), and I am NOT calling this a contradiction. But a human — or a future agent — reading "v0.8.1" in the spec and "0.2.4" in VERSION has no stated map between them, and the 0.5.0 gate is a *package* MINOR bump (0.2.4 → 0.5.0? or does the doc version drive it?). The relationship "the package VERSION is the released whole; each document carries its own independent doc-version" should be one sentence in M-3/M-7 so the milestone knows which number moves.

State the relationship: "The package `VERSION` and each document's version are independent scales; a MINOR package bump does not force a document re-version and vice versa. The 0.x.0 milestone gate is on the **package** VERSION." One sentence closes the ambiguity.

`should-clarify · cognitive-load (cognitive-load)`

**Observability of the [target] boundary** — covered in F-10; the honest `[target]` tagging is good practice, just unmechanized.

**Scale/performance budget** — the spec never states a ceiling for the queue (how many rows before ROADMAP.md is unwieldy) or the attic (files before the manifest is unbrowsable, A-G1). For a text product these are soft, but the milestone compaction (M-1) is the implicit answer for the queue. Worth one line naming the assumed ceiling ("the queue stays one-screen-scannable via milestone archival; past ~N open rows, compact early").

**Security/privacy** — genuinely light-touch and mostly out of scope (local docs + a public repo), EXCEPT the personal profile holding the human's working contract (A-G4/F-9). That one file is the privacy-sensitive surface and it currently lives unprotected outside git. Named, not a blind spot.

---

## Phase 5 — Closing summary

### Top 3 to fix before the 0.5.0 gate

1. **F-1** — make "one landing at a time" (INV-2) compose with two parallel sessions: one `in-work` row = the repo-global lane token, checked before a session starts a landing. The flagship dogfoods two sessions; this is the highest operational risk.
2. **F-5** — resolve the "rows never deleted" (INV-1) vs milestone-compaction contradiction *in the spec* (fold ROADMAP row 30). The 0.5.0 milestone will itself run the compaction the spec forbids.
3. **F-4** — state inbox-harvest atomicity + idempotency (one commit adds row & removes file; re-sweep is safe). Otherwise a crash mid-harvest duplicates or loses a wish, breaking INV-1.

### Properties to state explicitly (paste-ready)

- "At most one queue row is `in-work` per repo at any time, across all sessions; a session claims the lane by finding no existing `in-work` row before starting a landing." (closes F-1)
- "A parked wish resumes ahead of any queued wish, quick-win included; quick-wins bubble only against fresh queued wishes." (closes F-3)
- "Harvesting an inbox file is one atomic commit that adds the ROADMAP row and removes the file; the row records the source filename so a re-sweep never double-harvests." (closes F-4)
- "Closed queue rows are archived at milestones (dated queue archive, never edited, never deleted) — the attic principle for the queue." (closes F-5)
- "Every `[target]` token maps to a non-landed ROADMAP row; an anchor with a real architecture pin never carries `[target]`." (mechanizes S-0 / closes F-10)

### Open questions only the author can answer

- Is INV-2 ("one landing at a time") meant **globally** across sessions or **per-session**? The whole of F-1's fix hinges on this — it's a genuine design call, not something I can infer.
- Does the 0.5.0 MINOR gate move the **package** VERSION (0.2.4→0.5.0) or is it a document milestone? (F-14) — determines which number the milestone bumps.

### Overall readiness

**Needs one more iteration.** The structural model is sound and the anchor discipline is exemplary; the must-fix set (F-1, F-3, F-4, F-5) is four concentrated seam/atomicity fixes plus the two should-clarify traceability items that a MINOR gate touches directly (F-6, F-11). None require rework — they require precise spec sentences, most already scoped as queue rows (30, 52, 55, 56). Close the four must-fixes and the two gate-adjacent should-clarifies, then the spec is ready to gate 0.5.0.

---

## Summary table

| Severity | Count | Finding IDs |
|---|---|---|
| must-fix | 4 | F-1, F-3, F-4, F-5 |
| should-clarify | 7 | F-2, F-6, F-7, F-9, F-10, F-11, F-14 |
| worth-considering | 2 | F-8, F-13 |
| acknowledged (Phase 3.5) | 4 | A-G1, A-G2, A-G3, A-G4 |
| **Total hidden-gap findings** | **13** | F-1 … F-14 (F-12 = should-clarify on workers) |

*(F-12 is a should-clarify; the should-clarify count above is 7 with F-12 → 8. Corrected tally: must-fix 4, should-clarify 8, worth-considering 2, acknowledged 4.)*

**Verdict on the 0.5.0 MINOR gate:** **NOT YET — one iteration away.** Four must-fixes (F-1 lane composition, F-3 resume-vs-bubble, F-4 harvest atomicity, F-5 the INV-1/compaction contradiction) must land in the spec before the milestone, and two gate-adjacent should-clarifies (F-6 fold-vs-record, F-11 stale derivation citations) should land with them because the milestone re-walks the matrix against the current spec. The remaining should-clarifies and worth-considerings can ride as queue rows into 0.5.x. Most fixes are single sentences and several are already scoped as ROADMAP rows.
