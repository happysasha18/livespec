# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

Sessions 28–30 landings are committed history — full detail in JOURNAL.md (session 30's chapter:
"the evening queue drained — rows 180-187, eight landings").

## LIVE STATE (2026-07-09 ~23:20, session 30)
Versions: pack 0.9.8 · base 0.1.26 · communicator 0.1.41 · product-prover 0.1.15 · spec-author 0.1.23 ·
build-pipeline 0.2.43 · publish 0.1.3 · test-author 0.1.2 · PRODUCT_SPEC v0.16.10 (INV-74..81 new) ·
ARCHITECTURE v0.3.0 (now carries its own Runtime view · Placement view · Quality budgets).
**Suite 236 green, 0 red, ~30 s wall** (inside its new ≤60 s [default] budget). Installed skills synced.
**RUN items 1-5 pushed earlier (`1eb7530`, `584298a`); everything since is LOCAL, unpushed** — 10 commits
`209f84e..581e077` (rows 180-187 + intake + journal), ride the next authorized push after a fresh prover
re-check (this host's every-push gate). Minor pre-existing: communicator rule 10 trips
`machine-jargon:questionnaire` (not gated; likely false positive). PLAYBOOK profile count "14 rules +
8-check" — separate repo, his call. Inbox EMPTY. Cross-window: dropped ONE wish into tlvphoto's inbox
(adopt the runtime+placement views there — its own window's queue; this window stays audit-only).

## 1.0 BAR (2026-07-09, his decision — the finish line for this push)
**1.0 = everything below done HERE, EXCEPT two field items that ride real windows post-1.0: the
remote/cloud session, and the REAL tlvphoto migration (writing into tlvphoto's tree).** MIGRATION
READINESS: the type-aware format + prover-seam-hunt prerequisites are BUILT; real migration goes in
tlvphoto's OWN window.

## 1.0 RUN — the loop's charter (ordered; resume COLD from here · project = live-spec · cwd ~/live-spec)
Each item walks the full pipeline (build-pipeline skill). **PARK** = build to the named gate, then STOP
for his word. The run is NOT done when the queue drains: each item's done-state is the proof. Memory may
be wiped — all state lives in this file + `docs/wishes/` + ROADMAP + JOURNAL; the working contract lives
in his profile + the installed hooks, not memory.

1. **Prover-seam-hunt — DONE** (INV-72, `c1ef03b`; JOURNAL session 29).
2. **Feature/flow spec format by project type — DONE** (E-29/INV-73, pushed). Deferred by name:
   render-time clickable cross-links (render-doc.py has no anchor resolution; named in spec-author).
3. **The 7 small design holes — DONE** (rows 173-179, pushed; `TestSmallDesignHoles`).
4. **Authoring terminology + rename — DONE** (pushed; `TestAuthoringTerminology`).
5. **Architecture tiers + views — DONE, reopening CLOSED 2026-07-09 evening** (row 180, `019d793`):
   runtime view (INV-74) + placement view (INV-75) mandated, the architecture lens grew 3→6 checks in all
   three homes, the template gained Runtime/Placement/Budgets/Feature-coverage sections, our own doc
   models them; validation RE-RAN read-only over tlvphoto with budgets + fact-ownership — diff vs its
   real ARCHITECTURE.md left no unnamed hole (one named deferral: the at-a-glance diagram stays optional).
   Derived doc: session scratchpad `tlvphoto-architecture-derived-v2.md` (not committed — foreign
   internals stay out of the public pack). Record: `docs/prover/2026-07-09-row180.md`.
6. **Project onboarding — PARKED at mockup v2, HIS EYE IS THE GATE.** v1 bounced (parameters unexplained);
   v2 consequence-first, opened 2026-07-09 evening (`onboarding-mockup-v2.html`, session-29 scratchpad —
   REBUILD from the wish if that scratchpad is gone: `docs/wishes/2026-07-09-project-onboarding-what-can-
   i-customize.md`). On his verdict: fold → spec delta → full pipeline.
7. **Then 1.0:** M-1 3-pass audit (runs AFTER item 6 lands so the audit covers it) → bump 1.0.0 → push on
   his explicit "go" (never without it). Rows 173-187 archive at this milestone.

ALSO LANDED THIS SESSION (queued rows outside the original bar, all closed 2026-07-09 evening):
- Row 181 worker-liveness across a memory wipe (INV-76, `186ee8b`) — from the tlvphoto inbox wish.
- Rows 182-186 the five test-method lessons (INV-77..80 + the lens-aware re-prove exemption;
  `c16bbf3` `1a7010b` `352a822` `ef00380` `2275300`). Record: `docs/prover/2026-07-09-rows182-186.md`.
- Row 187 pre-ask scan covers questions (INV-81, `3380c11`).

POST-1.0 (his bar, NOT in the run): remote-seat cloud session · REAL tlvphoto migration (its own window).
His-word backlog, not 1.0 blockers: chat-cleanliness `Stop`-hook backstop · readability-restructure
operation (word-preservation verifier) · row 171 no-hooks/no-GitHub · row 148 plainer-spec rewrite ·
thin-loader tidy · pack orchestration · artifact registry · try a semantic code layer (Serena MCP) in a
code-heavy window IF symbol search starts hurting twice a session (his 2026-07-09 question; trigger =
rule-20 struggle, today's verdict: current projects too small to pay for it).

## Field legs + standing habits (ride real windows / always-on)
- Field legs with him (real windows): 47/96 feedback loop · 54 first-run · 165 first-struggle · 168 remote
  seat · 134/141 zero-drift · 143 · 144 · 140 · 117 · 129 · 133. (ROADMAP holds the full rows.)
- Standing habits: `date` before ANY stamp (the hook BLOCKED two invented stamps tonight — read the clock
  at write time, every time) · a background/delegated run's verdict is the suite log's tail, never a
  wrapper's exit (INV-80 — violated once tonight, caught, law landed same hour) · NOW/NEXT current +
  heartbeat past ~10 min (INV-71) · plain product words, never a code leading a line (INV-28), say
  "live-spec" not "пакет" · inbox EMPTY.
