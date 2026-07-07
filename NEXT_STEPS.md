# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

**LATEST (2026-07-07 20:56, session 25, /loop dynamic): SPEC humanize — ALL 18/18 scenario sections DONE,
SPEC.md now fully in the technical-writer register.** Every section rewritten via a fresh clean-context
agent and gated: tested phrases preserved section-scoped, bracket-code multiset identical to baseline, full
suite 175 green, a prover cross-link per section under `docs/prover/`. The last and biggest, **Throwing a
wish (595 lines)**, was done in 10 contiguous chunks each gated vs the WHOLE-section baseline (157 phrases /
165 code occurrences held throughout); a stale cross-ref inside it was fixed ('A prototype is not the
product' → 'A prototype stays a sketch'). 35 commits ahead of origin, none pushed. LESSONS logged: a
lowercase tested phrase must never be capitalized at a sentence start; a chunk splice's end-anchor must be
the NEXT bold-lead (both caught by the gate before any commit).
**NEXT in the movement (loop continues):** (1) SPEC template `templates/SPEC.template.md` — one small batch
(D1); (2) final whole-doc register-consistency sweep (touch up the earliest sections to the settled voice);
(3) ARCHITECTURE.md rewrite (his 19:07 scope; check its test-protection first); (4) whole-document prover
pass + 0.9.0 3-pass audit + stale-quote grep over untested prose (README/OVERVIEW/MIGRATION/docs); (5)
VERSION bump; (6) my full-certification push on his word. Push BLOCKED until (1)-(5) all green.
**SCOPE EXPANDED (his word 19:07): rewrite ALL the specs, not only SPEC.md — ARCHITECTURE.md too** (in
the same register; check what tests assert about ARCHITECTURE content before rewriting, its facts are
protected differently). After SPEC + ARCHITECTURE, confirm README/OVERVIEW/ROADMAP as candidates.
**PUSH GATE (his word 19:07, CHANGED): push ONLY when I certify the whole thing is 100% correct and
verified — my full go-ahead, no push-then-apology. Not per batch, not at a mechanical milestone alone;
my certification is the gate. Commit locally meanwhile.**
**GENERALIZE (his word 19:07): when this works end-to-end, hand him the exact command/prompt to run in
the OTHER projects (track-coach, tlvphoto) to do the same rewrite — the reusable migration sub-skill (D4).**
Runs on Opus (Fable pulled today). Register deployed==repo. Language: no coined mechanism-names in chat
OR docs — say "tested phrases"/"bracket codes" (his sharp word 18:47); durable fix rides row 170.
SAFE TO WIPE MEMORY here.

## LIVE STATE (2026-07-07 ~15:35, session 24 cont. — **SPEC-humanize BATCH 1 LANDED; register FROZEN
(V2); sweeping the rest via fresh-context spawns.** Batch 1 = section "What live-spec is" rewritten
(software house + conveyor + explicit prover edge-case stage) · `scripts/needle-extract.py` written (the
section-scoped safety gate) · voice honed into spec-author (`## How it reads`, new "confident product
person" bullet pointing at the opening as the exemplar). All gates green (needle · anchors E-12/E-1 ·
station-chain not duplicated · 8 skills load · 175 suite). **The winning register = confident product
PITCH (V2), NOT his flat promoter register — his promoter tone-card was tried and rejected for the spec.**
**REGISTER RE-DECIDED ~15:55: neutral native-English open-source technical-writer voice** (Fable-defined
on this window), NOT the V2 pitch as a universal rule. Full 14-rule register + 8-item verify checklist now
live in the communicator skill ("The writing register" section); spec-author points to it (one home). Key
refinement (his 15:57 word): natural/industry words are fine even when metaphor ("software house",
"conveyor", "pipeline"); what to kill is invented INTERNAL terms / my private interpretations ("axis",
"surface") — define them plainly at first use or replace. So the V2 opening STAYS (its metaphors are
natural); "Composing across axes" redone (Fable) with axis/surface defined in plain words. Sections done:
opening (V2) · Composing · Asking-what-the-product-does · pilot "When a bug cuts the line". ~15 sections
left. METHOD forward (his word): each section rewritten by a FRESH-CONTEXT agent given the register + the
section's exact test-checked phrases + hard constraints; the main head only orchestrates + runs the gates. Plan+fixes:
`docs/research/2026-07-07-spec-humanize-plan.md`; Fable record `docs/prover/2026-07-07-spec-humanize-plan.md`
(READY-WITH-FIXES, 5 MUST-FIX folded). Movement = ask #1 + row 148 Phase 3 + 0.9.0 compaction, ONE pass.
tlvphoto = its first EXTERNAL run, SEPARATE process on his command, NEVER this session. Earlier session
24 — **row 56 LANDED: the model router (SPEC INV-69), D-2 decided.** The rule: a piece of work's model tier is PROPOSED by its STEP and kind (judgment→senior,
never routed down · one-shot→haiku · multi-step mechanical→sonnet), not its size alone; the economy rung
moves the threshold; advisory — senior may override per wish, logged proposed→chosen→why. First routed
landing = this build itself (senior on spec/prove/arch/matrix; sonnet on version-bump+sync, ~10 min saved;
one override logged — spec prose kept on senior per INV-62). Prover CROSS-LINK docs/prover/2026-07-07-row56.md
(4 findings, all folded; must-fix = the [router target] tag sweep). M-175/`test_routing_rule` red→green.
**Pack 0.8.75, base 0.1.24, SPEC v0.15.61, suite 175 green.** Earlier session 24: row 169 (plugin
shopfront) + row 47 (feedback-intake, 8th skill) + row 12 (CLAUDE.md/PLAYBOOK mining) all closed.
PUBLIC: github.com/happysasha18/live-spec. **NOT yet pushed (rows 12 + 56 commits local, ahead of origin).**

**⚠ ALEXANDER'S TWO ASKS at the row-56 landing (2026-07-07 ~13:03) — read before resuming:**
1. **Human-first RE-LAYOUT of the whole SPEC** — the spec reads too much like "spec-language"; re-verstat it
   so a product person reads it plainly (scenarios lead, jargon trails). He calls this a *responsible* step,
   best done **from a fresh /clear session** (clean context — matches [[human-prose-polish-clean-context]]).
   Do NOT start it mid-loaded-session. This is the TOP next item — likely folds with / precedes the 0.9.0
   doc-compaction milestone. (Relation to row 148's genre whole-doc rewrite: overlapping but not identical —
   148 is content migration, this is readability re-layout; reconcile at the fresh session.)
2. **Reporting/orchestration persona = PROJECT MANAGER** — the one who runs the whole pipeline and reports
   to him wears the PM hat: plain product-outcome language, jargon only in parens. His step-zero echo read
   as spec-jargon and he didn't follow it. Adopt now in every report; may earn a pack line (craft-ladder /
   communicator persona). See memory [[plain-language-communication]] + [[report-as-project-manager]].
3. **⚠ DURABLE-GAP flagged by Alexander (2026-07-07 ~13:31) — carry into the new-rules migration.** The
   board copy fix (three coined titles + "краснит"/"вслепую" swept) was POINTWISE — a sketch FILE edited
   by hand. It survives a memory wipe (on disk) but is NOT a rule: nothing mechanically catches a coined
   doc-metaphor on a HUMAN-FACING page, and the PM persona lives only in a memory note so far. The durable
   fix (bake into the PACK, not one file): (a) name the PM reporting persona in communicator / craft-ladder;
   (b) a guard/check that a shown page carries no coined-metaphor titles — extend the plain-language law to
   rendered surfaces, not just chat. **Row 170 (harvested from the tlvphoto inbox this session) IS this
   feature's home**: a mechanical pre-show lint in communicator that catches banned constructs before a
   human sees them — the scissors ban first, the coined-metaphor titles folded in as a sibling pattern.
   Ride it on the SPEC re-layout / new-rules move. Class rule: [[never-patch-pointwise-domain-language]] —
   his exact worry.

This session ran on **Opus** by his word (Fable pulled from Claude Code today). His language laws live in
the profile (scissors ban · native-plain English · industry-vocabulary narration). Board:
prototype/work-board-sketch.html (update at every station change — his standing ask).

## Forward queue (mirrors ROADMAP.md)

1. **TOP — sweeping (batch 1 DONE):** next SPEC-humanize batches, each via a fresh-context spawn in the
   frozen V2 register. Order: small warm-ups ("Composing across axes", "Asking what the product does"),
   then the needled heavies (the wish walk, worker contract, milestone laws), governance last, template
   as one small batch, a final register-sweep pass to close. Per batch: capture needles → spawn rewrite →
   section-scoped needle re-match + anchor→sentence diff + full suite + prover cross-link → show → commit.
   This IS ask #1 + row 148 Phase 3 + 0.9.0 compaction as one movement. Row 56 is DONE.
   **Without-him rows available:** 96 tail (rows 48/49 re-scope against INV-21 — 47's part DONE; first real
   feedback loop rides a live host window).
2. **Rows waiting HIS word:** 166 board sketch round 2 (look + composition) · 148 Phase 3 go (genre
   whole-doc rewrite by docs/research/2026-07-07-genre-migration-plan.md — reconcile with ask #1).
3. Field legs riding real windows with him: 47/96 first real feedback loop · 54 first-run · 163
   first-use · 165 first-struggle-search · 168 first remote seat · 134+141 zero-drift · 143 · 144 ·
   140 · 117 · 129 · 133.
4. Standing habits: `date` before ANY stamp; narrate in feature language (no coined terms in chat);
   echo speaks door·kind·name·row·map; board updated at every station change; inbox EMPTY (scissors-scanner
   wish harvested to row 170, ~13:33).
