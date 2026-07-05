# With-skill run — build-pipeline scenario (2026-07-05, Sonnet worker, read the SKILL.md first)

Verbatim output:

---
1. **Name the door aloud, before any file touch:** door = **bug** (silent wrong output, no new surface/state) · work-kind = **product** (mytool is the CLI the end user runs; the CSV is the artifact they receive) · priority = high (silent data loss beats a stack trace) · size = small, localized. Enter the pipeline at **bug → matrix → test → code**, not step 1.

2. **Read `SPEC.md`** for the clause governing `--export` / output-file behavior. Check whether directory-creation-on-write is already specified anywhere. If it is, that's the sentence to correct. If it genuinely isn't specified anywhere (neither "creates missing dirs" nor "errors on missing dir"), that correct-behavior choice is a real `⟨DECIDE⟩` — don't guess it.

3. **Read `ARCHITECTURE.md`** to find the node that owns the export/write path and its `file:line` pin. Cite the existing node; do not rewrite the architecture doc for a bug of this size.

4. **Name the class (base rule 14)** before writing anything: "a CLI flag that takes an output-file path writes without ensuring the parent directory exists, producing a silent empty file instead of a clear error or a created directory." Grep the source tree for every other flag/call-site with the same shape (every `--*-file`/`--output`/`--log`/`--export`-style option, every raw `open(`/`Path(...).write_*` call) to find every sibling of this bug, not just `--export`.

5. **Ask the project owner the one real gap, batched with the class findings:** "Found N siblings with the same missing-directory bug: [list]. Intended contract: should mytool auto-create the missing output directory, or fail with a clear error naming the missing path? Whichever you pick applies to all N call sites." Proceed once answered (or on a stated default if they defer).

6. **Update `SPEC.md`**: add or correct the sentence describing the export/output-file contract per the owner's answer, for `--export` and every sibling flag found in step 4 — so the corrected behavior traces to a spec clause (satisfies the Bounds guardrail).

7. **Update `TEST_MATRIX.md`**: add one row per affected write-path × the "target directory missing" fact, at function-level ("run the tool, assert real output") — covering the whole class, not just `--export`. Run the coverage checklist (every fact ≥1 row, negative-side row present) for just the touched section.

8. **Write the failing tests first (red-on-bug)** in `tests/`: for `--export` and each sibling, call the real CLI/function with a target whose parent dir doesn't exist, then assert the corrected real behavior (dir created + real CSV content, or a clear non-zero exit with a real error message — per step 5's answer). Run them and confirm they fail against current code.

9. **Fix the source**: in the owning node from step 3, make the write path ensure the parent directory exists (or raise the specified clear error) before writing, and apply the identical fix to every sibling call-site from step 4 — same change, same commit.

10. **Run the new tests to green, then the whole suite.** Green means zero failures and only the expected skip list.

11. **Run the project's guardrails check** (pre-push hook set: completeness, tests-present, bounds, conflicts) — must be green before anything is considered done.

12. **Verify by deed**: actually run `mytool --export out/report.csv` in a real shell with `out/` absent, look at the real result myself (real dir + real non-empty CSV, or the real error text) — don't call it fixed off the test alone.

13. **Commit**: bump PATCH version; update README/CHANGELOG if export behavior is user-documented there; add a `JOURNAL.md` line stating the why (silent empty-file bug, class fix across N call-sites, owner's chosen contract). Commit locally, unasked (green + no regression).

14. **Report to the project owner in plain language**, before any push: what was broken, what the class turned out to include, what changed (SPEC sentence, matrix rows, tests, code — file paths named), and the real verified output from step 12. Push/deposit only after they've reviewed it.
---
