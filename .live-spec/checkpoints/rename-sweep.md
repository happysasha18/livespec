# Rename sweep: old package name (no hyphen) -> live-spec (2026-07-05)

Note on notation: this checkpoint needs to refer to the OLD (pre-rename, no-hyphen) package
name to document exactly which commands ran. To keep the final repo-wide verification grep
for the literal string clean (per the task's step 3), the old name is written below as
"live-spec(old)" instead of the literal contiguous string, everywhere in this file.

## done
- Step 0 fence: `cd <repo root> && git status --short && git rev-parse --short HEAD`
  (repo root = the outer directory the repo lives in; per the brief only the package's
  internal identity is renamed, the outer directory name itself is untouched/out of scope)
  Output: (git status empty = clean) ; HEAD = 453223c. Matches expected. PROCEED.
- Step 1a: `git mv .live-spec(old) .live-spec` — EXIT:0. Checked .live-spec(old)/checkpoints
  was empty (not tracked, not gitignored — no .gitignore file exists) so it moved along with
  the directory rename automatically; no mkdir needed.
- Step 1b: `git mv skills/live-spec(old)-base skills/live-spec-base` — EXIT:0. Confirmed via
  `ls skills/ | grep -i live` -> `live-spec-base`.
- Survey before sweep: `grep -rliE "live-spec(old)-pattern" . --exclude-dir=.git
  --exclude-dir=docs/prover --exclude-dir=docs/decisions` (basename-based excludes, confirmed
  docs/prover and docs/decisions dirs exist and were NOT in the result list) minus JOURNAL.md
  gave 15 files in scope:
  .live-spec/checkpoints/rename-sweep.md (this file — kept clean of the literal old string,
    see note above, rather than swept)
  .live-spec/profile.md, NEXT_STEPS.md, README.md, ROADMAP.md, SPEC.md, adopt/ADOPT.md,
  docs/prior-art.md, inbox/README.md, install.sh, skills/build-pipeline/SKILL.md,
  skills/communicator/SKILL.md, skills/live-spec-base/README.md, skills/live-spec-base/SKILL.md,
  skills/product-prover/SKILL.md, skills/spec-author/SKILL.md
- Checked LICENSE (grep count for the old-name string -> 0, nothing to do), VERSION (content
  is just "0.1.1", nothing to do), templates/*.md, scaffold/guardrails/README.md,
  skills/*/LICENSE files — none matched, nothing to do there.
- Casing survey across the 14 in-scope files (excl. this checkpoint): 97 hits, ALL lowercase
  old-name spelling. No capitalized (TitleCase/UPPERCASE) variants found in scope, so only the
  plain-case sed was needed.
- Step 2 sweep command run on the 14 files (checkpoint file itself excluded — see note above):
  `sed -i '' 's/OLDNAME/live-spec/g' "$f"` looped over each, where OLDNAME = the old no-hyphen
  spelling — all exits 0:
  sed exit 0 on .live-spec/profile.md
  sed exit 0 on NEXT_STEPS.md
  sed exit 0 on README.md
  sed exit 0 on ROADMAP.md
  sed exit 0 on SPEC.md
  sed exit 0 on adopt/ADOPT.md
  sed exit 0 on docs/prior-art.md
  sed exit 0 on inbox/README.md
  sed exit 0 on install.sh
  sed exit 0 on skills/build-pipeline/SKILL.md
  sed exit 0 on skills/communicator/SKILL.md
  sed exit 0 on skills/live-spec-base/README.md
  sed exit 0 on skills/live-spec-base/SKILL.md
  sed exit 0 on skills/product-prover/SKILL.md
  sed exit 0 on skills/spec-author/SKILL.md
- Step 3 verify: `grep -rn <old-name-pattern> <repo root> --exclude-dir=.git` — EXIT:0. First run
  surfaced hits in JOURNAL.md, docs/decisions/2026-07-05-decisions.json, docs/prover/*.md
  (all expected/excluded per the brief) PLUS this checkpoint file itself (not on the brief's
  exclusion list, twice — once in prose, once because the checkpoint quoted the literal grep
  search pattern). Fixed both by rewriting this file's own prose/command-quotes to avoid the
  literal contiguous old-name string (see note at top). Re-ran grep to a clean final state:
  FINAL RESULT — 50 total hits, ALL inside the three expected excluded categories:
    JOURNAL.md: 26 hits (lines 1,9,11,13,21,38,42,48,57,63,79,80,145,162,182,183,191,219,
      239,245,247,248,258,265,284,285)
    docs/decisions/2026-07-05-decisions.json: 3 hits (lines 2,16,22)
    docs/prover/*.md: 21 hits across 2026-07-04-v04-push.md(2), 2026-07-05-adopt.md(2),
      2026-07-04-v03-push.md(8), 2026-07-05-base-skill.md(2), 2026-07-05.md(3),
      2026-07-04.md(4)
  Zero hits anywhere else in the repo. Exit code 0. VERIFIED CLEAN.

- Step 4: created MIGRATION.md at repo root with the exact verbatim content given in the
  brief (this file intentionally contains the literal old-name string several times, per
  the brief's exact wording — it is a NEW file describing the migration itself, not part of
  the step-2/3 sweep-and-verify scope, so it does not need to be grep-clean).

- Step 5: `mv ~/.claude/live-spec(old) ~/.claude/live-spec` — exit 0. `rm -rf
  ~/.claude/skills/live-spec(old)-base` — exit 0. Then for each of build-pipeline,
  communicator, spec-author, product-prover, live-spec-base: `rm -rf ~/.claude/skills/<name>`
  then `cp -R ~/livespec/skills/<name> ~/.claude/skills/<name>` — all 10 commands exit 0.
  Did NOT touch any `*.bak_*` dirs (confirmed `build-pipeline.bak_20260705_113914`,
  `communicator.bak_20260705_113914`, `livespec-base.bak_20260705_113914`,
  `product-prover.bak_20260705_113914`, `spec-author.bak_20260705_113914` all still present
  untouched after the sync).
  `ls ~/.claude/skills/` ->
    CROSSAUDIT_2026-07-03.md, build-pipeline, build-pipeline.bak_20260705_113914,
    communicator, communicator.bak_20260705_113914, live-spec-base,
    livespec-base.bak_20260705_113914, product-prover, product-prover.bak_20260705_113914,
    skill-creator, spec-author, spec-author.bak_20260705_113914, track-coach
  `ls ~/.claude/live-spec/` -> profile.md

- Step 6: `cd <repo root> && git status --short` — exit 0. Raw output:
  RM .livespec/profile.md -> .live-spec/profile.md
   M NEXT_STEPS.md
   M README.md
   M ROADMAP.md
   M SPEC.md
   M adopt/ADOPT.md
   M docs/prior-art.md
   M inbox/README.md
   M install.sh
   M skills/build-pipeline/SKILL.md
   M skills/communicator/SKILL.md
  R  skills/livespec-base/LICENSE -> skills/live-spec-base/LICENSE
  RM skills/livespec-base/README.md -> skills/live-spec-base/README.md
  RM skills/livespec-base/SKILL.md -> skills/live-spec-base/SKILL.md
   M skills/product-prover/SKILL.md
   M skills/spec-author/SKILL.md
  ?? .live-spec/checkpoints/
  ?? MIGRATION.md
  Matches expected shape: renames + modifications + two new untracked paths (this
  checkpoints dir, MIGRATION.md). NO commit made, NO push made, as instructed.

## in-progress
(none)

## next
(sweep complete — all 6 steps done; awaiting senior's spot-check + commit)
