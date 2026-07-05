# Pass 3 — Surface-composition audit (0.5.0 gate)

**Audited state.** `~/live-spec` @ `15369ba1f892d76d10734e18b2e0dcff2bf15595` (branch `main`, clean tree).
Object: `SPEC.md` v0.8.1 (441 lines). Canonical axis list from `spec-author/SKILL.md` v0.1.3 (lines 111–112):
**view · mode (quick/full, read/edit) · tier · viewport size · persistence/reopen · concurrency**, plus
SPEC's own added axis **document provenance** (native × re-engineered) [C-1].

This is the surface-composition pass: enumerate every stateful surface, confirm one-surface-one-name, then
compose each against the applicable axes AND against the surfaces it touches, and report every reachable
combination no SPEC sentence covers.

`viewport size` has no user-facing meaning for this product (a methodology package, no rendered UI grid);
it is marked N/A throughout rather than forced. The two axes that carry the weight here are **mode**
(writer-session vs read-only outsider), **persistence/reopen** (memory wipe, session death, fresh clone,
older stored values) and **concurrency** (two parallel sessions) — and INV-11 / C-1 make concurrency a
DECLARED axis, so composing against it is in-scope, not optional.

---

## 1. Surface inventory

One-surface-one-name holds across the doc; the naming column notes the few places worth watching.

| # | Surface | Name(s) in SPEC | Axes that apply | Covered / Hole |
|---|---|---|---|---|
| 1 | Wish | wish [E-2] | mode, persistence | states T-1..T-11 + parked; lifecycle closed. OK |
| 2 | Queue | queue / ROADMAP.md [E-3] | mode, concurrency, persistence | intake serial/parallel [INV-2], exits [T-8]; **host-concurrency hole H3** |
| 3 | Spec | spec / SPEC.md [E-4] | persistence, provenance | current-vs-target [S-0]; native/re-engineered [C-1]. OK |
| 4 | Settings ladder | settings ladder / four nested scopes [E-13] | mode, tier, persistence, concurrency | resolution stated; **tier hole H2, concurrency hole H1** |
| 5 | Personal profile | personal profile `~/.claude/live-spec/profile.md` [E-16] | persistence, concurrency | **H1 (outside any repo → no fence, fresh-clone loss)** |
| 6 | Host profile | host profile `.live-spec/profile.md` [E-8] | persistence, concurrency, provenance | **H1 (tracked-ness unstated), N2 (creation moment)** |
| 7 | `.live-spec/` folder | `.live-spec/` [E-1] | persistence, concurrency | adopt/=tracked [A-8], checkpoints=gitignored [ACT-3]; profile.md unstated (H1) |
| 8 | Inbox | inbox / inbox/ [E-11] | mode, concurrency, persistence | parallel-safe by design; **harvest atomicity N1** |
| 9 | Attic | attic / attic/ [E-9] | persistence, concurrency | collision→prefix; layout D-1 open; **same-dir collision N6** |
| 10 | Guardrails / hooks | guardrails [E-6] | mode (offered/imposed), persistence | offered only where git; OK (N: post-install git removal) |
| 11 | Snapshot [target] | snapshot [E-7] | persistence, mode | declared-scope asymmetry good; **version-N-1 baseline N5** |
| 12 | Surface registry | surface registry [E-10] | persistence, concurrency | self-closing; OK |
| 13 | Installed skill copy | installed set [A-7, M-7] · mirrors [D-4] | persistence (freshness), concurrency | **dev-machine installed-vs-repo freshness H4** |
| 14 | Base skill | base skill / `live-spec-base` [E-12] | persistence | **H5: E-12 says D-4 "still open"; D-4 is decided** |
| 15 | Architecture doc | ARCHITECTURE.md [E-14] | persistence, provenance | re-prove on structure change; OK |
| 16 | Matrix | TEST_MATRIX.md [E-5, E-15] | persistence | derived; coverage-validated; OK |
| 17 | NEXT_STEPS / JOURNAL | [M-2, M-3] | persistence/reopen | resume-file rule; **gitignore + safety-net not in SPEC N4** |
| 18 | Checkpoints | `.live-spec/checkpoints/` [ACT-3] | persistence, concurrency | not /tmp (survives reboot); **path uniqueness N3** |
| 19 | Worker tiers | tiered workers [ACT-3] | tier, mode | D-2 open (flagged); **session-scope inheritance H2** |
| 20 | Session mode | writer vs read-only outsider [INV-10] | mode, concurrency | crisp test; fence INV-11; OK |

**Naming check (one surface = one name):** clean. `queue`↔`ROADMAP.md`, `snapshot`, `surface registry`,
`inbox`, `attic`, `base skill`↔`live-spec-base` are each single-named. Two "profile" surfaces exist but are
always qualified personal vs host and scoped distinctly [E-8 vs E-16] — not a collision. No surface is
referenced-but-undefined. No second document claims to be the spec/matrix.

---

## 2. Findings

### should-fix

**H1 — Profile files' persistence + concurrency are unspecified; the concurrent-edit fence structurally
cannot cover them.** SPEC.md:308-314 (INV-11) scopes the fence to `git status` + HEAD — "live-spec AND any
host repo two sessions might share." But E-16 (SPEC.md:207-209) states the personal profile "lives on the
human's machine outside any project repo," and E-8 (SPEC.md:163-166, 386) never says whether
`.live-spec/profile.md` is git-tracked (contrast: adopt artifacts are explicitly "tracked in git" [A-8,
SPEC.md:102-104]; checkpoints explicitly "gitignored" [ACT-3, SPEC.md:216-218] — profile.md is the one
left unstated).
- *Reachable:* two of the same human's sessions in different projects (the intended three-windows workflow)
  each promote a session line into the ONE personal profile [INV-14, SPEC.md:192-194]; a promotion is a
  read-modify-append with no lock and no git fence → interleaved/lost line. Separately, a fresh clone or a
  new machine has no personal profile and (if untracked) no host profile → resolution silently falls back to
  package defaults with no notice.
- *Why it matters:* concurrency is a DECLARED axis [INV-11/C-1] and settings loss is exactly the
  "reopened it and it looked broken" seam the pass exists to catch; the settings ladder is the product's
  highest-state surface.
- *Owner:* E-8 + E-16 must state each profile file's tracked-ness, and INV-11 (or a new sentence beside it)
  must state what protects a write to a file OUTSIDE any git repo (the personal profile) — a lock, a
  read-before-write compare, or an explicit "single-writer, human-serialized" rule.

**H2 — Session-scope override does not compose with the tier/worker axis.** E-13 (SPEC.md:170-184) resolves
"session beats host beats personal beats package default," and INV-14 (SPEC.md:192-196) says the session
scope "lives only in your spoken word … the agent never writes it anywhere." ACT-3 (SPEC.md:216-220) spawns
workers that "read the resolved contract" — but a worker is a fresh context that can read only the profile
FILES, never the senior's unspoken-to-disk session word.
- *Reachable:* the human says "today answer me in English" (session override, never written); the senior
  spawns a haiku worker to draft a report; the worker resolves language from personal profile (Russian
  chat) → output violates the live session setting.
- *Why it matters:* the ladder's narrowest, most-authoritative scope is invisible to the tier below it — a
  cross-section hole between surface #4 and surface #19.
- *Owner:* E-13 / ACT-3 — state that a worker brief must carry the live session-scope settings forward (the
  senior injects them into the brief), since the worker cannot resolve them from files.

**H3 — A host has no collision-free wish intake, yet host concurrency is a declared axis.** E-1
(SPEC.md:25-27) lists a host as owning "spec, matrix, queue, journal, surface registry, and `.live-spec/`"
— no inbox. The inbox [E-11, SPEC.md:300-307] and the FIRST-act sweep [T-10] are specified only for the
package repo. But INV-11 (SPEC.md:314) explicitly extends concurrency "to any host repo two sessions might
share."
- *Reachable:* a team adopts the pack; two contributors' sessions each add a wish row to the host's
  ROADMAP.md at once → the fence stops the second write but there is no parallel-safe door (the inbox) to
  fall back to, so "spoken means it exists" [INV-1] cannot hold on a host the way it does for live-spec.
- *Owner:* E-1 / E-11 — state whether the inbox is a host-general surface (every host gets `inbox/`) or
  package-repo-only; if the latter, name what preserves INV-1 under host concurrency.

**H4 — On the pack DEVELOPER's own machine, the installed skill copy vs the repo copy has no freshness
rule.** A-7 (SPEC.md:129-135) and M-7 (SPEC.md:331-334) govern a HOST's recorded installed set; D-4
(SPEC.md:361-364) makes the pack repo the source and standalone repos read-only mirrors (sync = row 51).
None of these covers the seam that the skills load from `~/.claude/skills/<name>/` while they are edited in
the `~/live-spec` repo tree.
- *Reachable:* Alexander edits a skill in the repo; the running session (and any spawned worker) loads the
  older installed copy under `~/.claude/skills/` → work proceeds under a stale skill with no re-stat trigger
  (A-7's re-stat compares installed-set versions, not repo-vs-installed).
- *Owner:* M-7 / A-7 — state how (and when) the repo copy propagates to the installed copy for the pack's
  own development, and add that seam to the freshness check.

**H5 — E-12 states an open decision that the Open-decisions section marks decided (internal staleness).**
E-12 (SPEC.md:146) reads "(folder: `live-spec-base`; the pack-structure half of the question is still open
[D-4])," but D-4 (SPEC.md:361-364) records the pack-structure question **decided 2026-07-05**
(package-is-source) with the folder-name half also closed. The prose therefore advertises as open a
question its own index closes — a one-home/freshness drift a reader hits head-on.
- *Owner:* E-12 prose — drop "still open," point at D-4's decision (the spec must state today's truth, no
  stale open-question scar).

### note

- **N1 — Inbox harvest atomicity across session death.** T-10 (SPEC.md:304-307): sweep → add queue row →
  harvest commit removes the file. If the session dies between the row-add and the removal commit (or the
  reverse), the next sweep can double-harvest or (worse ordering) drop a wish. State the atomic unit or the
  idempotent re-sweep rule. [T-10]
- **N2 — Host profile creation moment unspecified.** Bootstrap [B-1, SPEC.md:86-89] copies six templates but
  never creates `.live-spec/profile.md`; resolution [E-13] relies on "absent scope ⇒ inherit," which is
  implied ("inherited … until a narrower one overrides") but never stated as an explicit rule for a MISSING
  scope file. [B-1/E-8/E-13]
- **N3 — Checkpoint path uniqueness under concurrent workers.** ACT-3 (SPEC.md:216-218) puts checkpoints in
  `.live-spec/checkpoints/` but does not require unique per-worker paths; two workers could collide. [ACT-3]
- **N4 — NEXT_STEPS persistence is thin in SPEC.** M-2 (SPEC.md:318-322) names NEXT_STEPS live-state but not
  its gitignore status or the "JOURNAL is the safety net" rule (both live in CLAUDE.md, not SPEC); a
  gitignored resume file is a persistence surface the spec should own. [M-2/M-3]
- **N5 — Snapshot version-N-1 × changed surface set.** E-7 [target] (SPEC.md:277-280) advances the baseline
  per declared surface, but says nothing about diffing an old baseline after the surface registry [E-10] or
  snapshot FORMAT changes — the persistence-version case the axis list calls out. Deferred with [target] but
  worth a sentence when E-7 lands. [E-7]
- **N6 — Attic same-dir basename collision.** E-9 (SPEC.md:113-116) disambiguates a collision by prefixing
  the source dir; two runs moving the same-named file from the SAME source dir are not disambiguated. Edge;
  relevant only once two writers touch one host attic. [E-9]

---

## 3. Verdict — readiness to gate 0.5.0

**No must-fix; 5 should-fix; 6 notes.** The doc is structurally sound for the surface-composition lens:
naming is clean (one surface = one name throughout), no surface is referenced-but-undefined, no rival
source-of-truth doc, and the two hardest axes for this product — mode (writer/read-only) and
persistence/reopen after a wipe — are genuinely composed (INV-10, INV-11, INV-14, E-13, E-16 do real work
here). The holes are all **single-sentence additions at a named home, not redesigns.**

The pass does not block 0.5.0, but two of the should-fix items sit on the exact axis this pass exists to
guard and should fold BEFORE the gate rather than becoming queue rows:
- **H1 (profile persistence + concurrency)** — the settings ladder is the product's highest-state surface,
  and the fence provably cannot reach the personal profile; leaving profile-file tracked-ness unstated is a
  live data-loss seam on Alexander's own multi-window workflow.
- **H3 (host wish-intake under concurrency)** — concurrency is a DECLARED host axis [INV-11], yet INV-1
  ("no wish is ever lost") has no host-side mechanism; the composition is incomplete, not merely thin.

H2, H4, H5 are safe to land as owned queue rows if the gate is time-boxed (H5 is a two-word prose fix and
should just be made). Recommendation: **fold H1 + H3 + H5, queue-row H2 + H4, record the six notes**, then
gate 0.5.0.

*(Pass 3 of 3; passes ran independently — this report is the surface-composition slice only.)*
