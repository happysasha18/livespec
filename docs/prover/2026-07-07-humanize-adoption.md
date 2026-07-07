# Prover cross-link — SPEC humanize batch: "Attaching to a live project (adoption)" (2026-07-07, session 25)

Register rewrite of the largest scenario section (a numbered 7-step sequence + two bold blocks). Gates
green: 10/10 tested phrases re-matched section-scoped; bracket-code multiset identical to baseline (31
occurrences across A-0..A-10, the E-/M-/INV- codes, [default], [target]×2 — every count matched);
full suite 175 green. Clean on first splice. The numbered list 1–7 kept as a numbered list, so the
step codes A-1..A-7 stay in order and count.

## Facts carried (all KEPT)
- INTRO: adoption is a sequence, each phase completes first; version-control gate FIRST so the run is
  reversible [A-5]; codes name meanings not order (tlvphoto 2026-07-04); a [target] phase is recorded and
  skipped, deferral journaled [A-0].
- STEP 1 Orient: read every doc first, never assume a blank slate, owes the founding questions [B-2] [A-1].
- STEP 2 Inventory: code + surfaces (seed the surface registry [E-10]) + docs with owners (file:line) [A-2];
  working artifacts in `.live-spec/adopt/`, git-tracked, never in the host's own folders (pilot polluted
  `data/`) [A-8].
- STEP 3 Re-engineer: existing spec → SPEC.md sections (claims kept, marked unverified); file:line pins seed
  ARCHITECTURE.md [E-14]; tests → matrix rows under nodes [E-15]; roadmap/TODO → queue rows; reconcile an
  unverified claim at first touching landing, rest at first milestone [A-3]; per unbacked LIVE surface the
  human decides promote [INV-16] / quarantine [E-17] / attic [A-4], flagged at orient [A-10] — kept as a
  sub-list with the quarantine provenance note intact.
- STEP 4 Attic over deletion: superseded files → **attic (attic/)**, append-only manifest; collision law
  (source-dir prefix, then numeric ordinal `-2`,`-3`, base-skill rule 18) [E-9]; flat-vs-dated open [D-1]
  [A-4]; no adopt/rework run deletes a host file [INV-7]; cruft-sweep exception only through a gate, on the
  human's explicit OK, authored content never qualifies [A-9].
- STEP 5 Version-control gate (done FIRST): init git, `.gitignore`, pristine baseline commit, remote as a
  NAMED deliverable recorded in the journal, a recommendation does not close it (pilot local-only) [INV-8]
  [A-5].
- STEP 6 Baseline snapshot [target]: save current artifacts as the diff baseline [E-7] guards [A-6].
- STEP 7 Incremental: same wish lifecycle; record installed skill versions in `.live-spec/`; RE-READ a
  changed SKILL.md, never coast on stale, journal old→new; not event-only — re-stat at every breakpoint
  [M-2]; once a day ask the PUBLIC repo via the update check [E-25] [A-7].
- BLOCK install: `install.sh` copies skills to `~/.claude/skills/`, idempotent, an existing copy backed up
  with a timestamp before being overwritten, never deleted; backup beside the skills home not inside;
  installing and recording are two halves of one seam [E-21].
- BLOCK update-check: `scripts/check-pack-update.sh` runs once a day, throttled by a dated stamp; asks the
  public VERSION on main [M-7]; PROPOSES when newer (both versions, what-changed pointer, road); it never
  installs anything [ACT-1]; no-network reads as "check skipped" naming the address it tried; a machine
  ahead reads as up to date, proposes forward only, never a downgrade; E-23's outward twin; non-goals kept
  as a list; only face is the proposal line, facets N/A [INV-28]; success measure [default] [E-25].

## Wording changes worth naming (meaning intact)
- Numbered steps kept; the per-surface verdicts and the update-check non-goals pulled into sub-lists.
- Passive→active throughout ("the agent reads", "you reconcile", "the check PROPOSES").
- No new scissors; "Attic, not deletion" retitled "Attic over deletion" (positive), the rule text kept.

Verdict: **CLEAN.** Every fact and code carried; 10/10 tested phrases section-scoped; code multiset
identical; suite 175 green. No must-fix.
