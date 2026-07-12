# Skill-creator walk — the seven working skills + live-spec-base, 2026-07-12 (1.1.0 MINOR gate)

The walk runs the skill-creator craft lens over the eight repo skills, the catch-up sweep the milestone
gate names for skills landed before INV-99's per-landing walk (SPEC M-1, gate bullet: "walk the pack's
skills through skill-creator … format, frontmatter, and the description-triggering lens — the craft of
the skill file. Our evals already test behaviour; this checks the craft. Fold or reject each finding,
with a written reason, in a dated record."). It follows the form of the 2026-07-06 sweep (row 130): the
same craft bar — frontmatter correctness, description triggering quality (use + NOT-side), body structure
and scanability, size against the ~500-line ideal, live cross-references, cold-reader clarity — read over
the repo copies, findings judged and classified. Special weight went on the three bodies that changed
since 2026-07-06: build-pipeline (now 1.0.9, was 289 lines), product-prover (1.0.2), communicator (1.0.4,
was 249 lines). This walk WRITES only this record; nothing else edits, per the gate's read-only audit
discipline.

## Sizes (lines of SKILL.md)

feedback-intake 93 · publish 116 · test-author 164 · live-spec-base 272 · product-prover 395 ·
spec-author 454 · build-pipeline 466 · **communicator 679**.

Seven sit at or under the ~500-line ideal. communicator alone is well past it — it nearly tripled from
its 249 at the last sweep. build-pipeline (466) and spec-author (454) now sit just under the ceiling,
worth watching.

## Mechanical checks that passed for all eight

- **Frontmatter** clean everywhere: `name` matches the skill dir, a `description` is present, and
  `metadata.version` is set. build-pipeline uses a folded-scalar (`description: >`) block, valid YAML that
  resolves to one line.
- **The base pin is consistent:** all seven working skills open by naming `live-spec-base (v1.0.5)`, and
  the base's own frontmatter is 1.0.5 — the lockstep held through the recent law batch.
- **No stale references.** Every script the skills cite exists (`preshow-lint.py`,
  `preshow-register-lint.py`, `spec-style-lint.py`, `spec-redundancy-precheck.py`, `spec-judge.py`,
  `spec-done-gate.py`, `clock-hook.sh`), every referenced doc exists
  (`docs/prose-quality-gate-design.md`, `docs/spec-style.md`, `docs/spec-format-by-project-type.md`),
  and every template the pipeline/spec-author name is in `templates/`. spec-author's product-prover link
  and both skills' template pointers resolve to the pack repo — the 2026-07-06 fixes (#1, #5) still hold.
- **Description NOT-side** present and sharp on all eight (the 2026-07-06 folds for live-spec-base,
  product-prover, communicator all stand).

## Findings and their fates

| # | Skill | Finding | Severity | Fate |
|---|---|---|---|---|
| 1 | live-spec-base | The description says "twenty-one rules in the body", but the body now holds 23 numbered rules — rules 22 (convergence, INV-98) and 23 (live channel, INV-108) landed since 2026-07-06 and the self-count was never updated. A stale self-description; triggering is unaffected (the classifier keys on the semantic text, not the number), but the file misstates its own contents. | should-fix | OPEN — one-word edit ("twenty-one" → "twenty-three"); belongs with the doc-compaction leg of this same MINOR gate, not this read-only walk. |
| 2 | communicator | At 679 lines the body is well past skill-creator's ~500-line ideal (249 at the last sweep). The embedded "writing register" — 16 rules plus a 10-point verification checklist, lines 458–593 (~135 lines) — is a self-contained sub-system and the natural candidate for a `references/` file loaded on demand, skill-creator's own pattern for heavy material. | should-fix | OPEN, with care — the content is load-bearing and correct; the pre-report walk's step 1 ("re-read the rules above — open this file") assumes the register lives in this file, so any extraction must keep that walk pointed at it. A queue row, not a gate blocker. |
| 3 | build-pipeline, spec-author | Both sit just under the ceiling (466, 454) and both grew this cycle. No defect today; noted so the next additions extract rather than append. | note | Recorded; no action. |

## Verdicts (per skill)

- **live-spec-base** (272) — frontmatter clean, structure scannable, references live. One should-fix: the
  stale "twenty-one rules" self-count (finding #1).
- **spec-author** (454) — clean; strong description with NOT-side, the product-prover link live, dense but
  well-grouped under headers. Near the size ceiling (note #3).
- **product-prover** (395) — clean; the new restructure-merge-gate paragraph (1.0.2, line 169) reads
  coherently and cross-references INV-111/39/114 correctly. Phases and lenses intact.
- **build-pipeline** (466) — clean; heavily sectioned and scannable despite the growth to 1.0.9, tables and
  numbered steps carry it, cross-refs (playbook, templates) live. Near the ceiling (note #3).
- **communicator** (679) — content correct and well-grouped under six named areas with stable anchors;
  counts ("twenty-two rules", "Sixteen rules") accurate. One should-fix: size discipline (finding #2).
- **test-author** (164) — clean; frontmatter, NOT-side, ladder/tables all sound.
- **feedback-intake** (93) — clean; routing table clear, receipt discipline tight.
- **publish** (116) — clean; the kind checklist plus the before/after worked example (the 2026-07-06 fold
  #12) stand.

## Bottom line

Eight skills walked. **Zero must-fix.** Two should-fix — a stale rule-count in live-spec-base's
description (finding #1) and communicator's body over the size ideal (finding #2) — plus one size note
(#3). Both should-fixes are craft/bookkeeping, not correctness or triggering defects; neither blocks the
1.1.0 gate. Finding #1 rides the gate's doc-compaction leg; finding #2 is a queue row to land with care.
