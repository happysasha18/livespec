# Bare run — build-pipeline scenario (2026-07-05, Sonnet worker, tool uses: 0)

Honest-boundary note (evals/README.md): this "bare" run is loader-fed — it even cites "per this
project's own discipline". Its reds are therefore the SKILL's marginal value, its greens partly the
loader's.

Verbatim output:

---
Here is the ordered plan, as text only — no tools invoked.

1. **Reproduce first.** Run `mytool --export out/report.csv` against a fresh temp dir with no `out/` present, confirm it exits 0 and writes an empty (or missing-then-created-empty) file. Note the exact exit code and any stderr/stdout — this becomes the baseline "before" behavior.

2. **Find the root cause in source.** Grep the source tree for the export/write path (`--export`, csv writer, `open(`, file-write helpers) to see exactly where the file handle is opened relative to where rows are generated. Likely cause: the output file is opened (truncating/creating) before the directory-existence check or before the data-generation step fails/short-circuits, so a broken write silently produces a 0-byte file instead of erroring.

3. **Check for the whole class, not just this instance.** Grep for every other place the tool writes to a user-supplied path (`--export`, `--log`, `--out`, any `--output-*` flag, config write, cache write). Per this project's own discipline, a directory-doesn't-exist bug in one write path is very likely present in all of them — the fix has to cover the class, not just CSV export.

4. **Read SPEC.md** to see if output/export behavior is already specified. Check whether there's an existing invariant about "export always produces a valid, non-empty artifact or fails loudly" or similar. If nothing covers this, this is a spec gap as much as a code bug.

5. **Decide the intended behavior** (this is the actual design decision, made now, before touching code):
   - Option A: auto-create missing parent directories (`os.makedirs(parents, exist_ok=True)`) before writing, so `--export out/report.csv` just works.
   - Option B: fail fast with a clear error ("directory 'out/' does not exist") and non-zero exit, no file written at all.
   Pick based on what SPEC.md's stated philosophy for this tool is (permissive/convenient vs. explicit/fail-loud). If SPEC.md doesn't say, this is the one point where I'd stop and ask rather than guess, since it's a user-visible behavior choice, not a pure bug fix.

6. **Update SPEC.md** to add/amend the export behavior as an explicit invariant covering all write-path flags found in step 3 (e.g., "any `--export`/`--output`-style flag either creates missing parent directories or fails with a clear non-zero-exit error; it never silently produces an empty output file").

7. **Update ARCHITECTURE.md** if the fix introduces or changes a shared code path (e.g., a single `ensure_output_path()` / `safe_open_for_write()` helper used by every export flag) — document that shared helper so future export flags are wired through it by construction, not by convention.

8. **Update TEST_MATRIX.md** to add rows for: missing directory + each affected export/output flag, both the "auto-create" or "clear error" outcome depending on the step-5 decision, and a row confirming no empty file is ever left behind on failure.

9. **Write the tests first** in `tests/` for the new TEST_MATRIX.md rows (one test per affected flag/class member found in step 3, not just CSV export). Run the suite to confirm these new tests fail (red) for the expected reason — this proves they actually exercise the bug.

10. **Fix the source** implementing the step-5 decision, applied to the shared helper/all affected call sites identified in step 3 — not a pointwise patch to just the CSV export function.

11. **Run the full test suite** (not just the new tests) to confirm green and no regressions elsewhere.

12. **Manually re-run the original repro command** (`mytool --export out/report.csv` with `out/` absent) to verify the actual end-to-end behavior matches what SPEC.md now says, and check there's no leftover empty file if the chosen behavior is "fail loudly."

13. **Update the project's journal/changelog** (if one exists, e.g. JOURNAL.md) with a short dated entry: what broke, why, what the fix and new invariant are.

14. **Stop and report** — state before/after behavior, files touched (SPEC.md, ARCHITECTURE.md if applicable, TEST_MATRIX.md, the specific test files, the specific source files), and do not commit/push unless separately asked.
---
