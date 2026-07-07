# Prover cross-link — SPEC humanize batch: "The machines that hold the bounds" (2026-07-07, session 25)

Register rewrite of the machines section (a bulleted list of named machines + two bold-lead paragraphs).
Gates green: 14/14 tested phrases re-matched section-scoped; bracket-token multiset identical to baseline,
including the TWO inline status-label tokens kept in place on their bold leads
(`[target: the machine; the design is decided]` on the snapshot, `[target: the machine; the wiring is live]`
on Design-sync) and the four plain [target] tokens; the italic `*landed*` kept; full suite 175 green.
Clean on first splice.

## Facts carried (all KEPT)
- The matrix (TEST_MATRIX.md) [E-5]: ≥1 row/fact pinned to a level, node × spec fact [E-14, E-15], positive
  AND negative side, negative = regression fence [INV-6].
- The guardrails [E-6]: pre-push checks pulled into a sub-list (prover record, suite green scoped by reach
  [INV-45], anchor ownership, coverage box, prototype fence [E-17, INV-17], concurrent-edit fence); host set
  still [target]; hooks OFFERED never imposed, only with git, plain-words explanation (Alexander 2026-07-05).
- The snapshot [target: the machine; the design is decided] [E-7]: last-accepted artifact = baseline; home
  `.live-spec/snapshot/`, folder + manifest per surface; baseline advances only at *landed*, only for
  declared surfaces, undeclared surfaces keep the old baseline (declared-scope check [E-6] catches the
  unasked change); adoption saves first baseline [A-6]; git history is the archive [E-8]; too-heavy surface
  keeps hash, only the hash is diffed; D-3 decided, machine [target], row 3.
- Design-sync [target: the machine; the wiring is live] [E-18]: optional, syncs the components a landing
  DECLARED [E-7] to the design project (claude.ai/design); SUPPLEMENTS the in-session render; WIRED today,
  `design-sync` off-by-default [E-13], recorded profile line [INV-14]; machine still [target], row 93; every
  sync human-gated (PUBLISHES) [ACT-1]; pack never syncs, work-kind axis says so [T-16], other kinds stand
  down [INV-22].
- The skill evals [E-19]: skills tested at BEHAVIOUR; ≥1 recorded eval per skill (bare session errs, skill
  corrects, red-first, dated run); home `evals/`; re-run at milestones + behaviour-changing landings; a
  skill without its eval is a milestone-audit defect.
- The surface registry [target] [E-10]: per-host list, the PREFERRED form is executable, mismatch is a
  failing test both directions, `.md` fallback, completeness check RED on rendered-but-unregistered,
  self-closing.
- The gate is thorough by REACH, not by ritual [INV-45]: README-only push double-miss (795-test run, his
  word); check-set from a declared reach map off the diff's file list; three teeth pulled into a sub-list
  (EXPLICIT / CONSERVATIVE — an unmapped or new file means the FULL suite / SELF-TESTED); cheap gates never
  scope; Full rigor [INV-40] = every check the diff can reach, green.
- A gate that blocks speaks one language [INV-47]: typed failure line `{severity, code, message, fix}`;
  blocking/advisory declaration; rebuild validates before writing; home guardrails README; binds by deed.

## Wording changes worth naming (meaning intact)
- The guardrails checklist, the three teeth, kept/pulled into sub-lists; long sentences split.
- The status-label brackets and the italic `*landed*` preserved character-for-character.
- No new scissors introduced; the section title's "not by ritual" kept as-is.

Verdict: **CLEAN.** Every fact and token carried; 14/14 tested phrases section-scoped; token multiset
identical incl. the inline status labels; suite 175 green. No must-fix.
