# With-skill run — build-pipeline scenario (2026-07-10 rerun, model = sonnet worker, arm = with-skill, build-pipeline 0.2.44)

Read skills/build-pipeline/SKILL.md directly (Read tool, not the Skill tool); 1 tool use.

Verbatim output:

---

Here is the plan, worked strictly by `build-pipeline/SKILL.md`.

**Step zero — name the door aloud (before any tool call).**
1. Read `JOURNAL.md`, grepping for "export" (or the CLI's output-writing area) to check the ~30-day recurring-bug window, and read `PRODUCT_SPEC.md`'s existing clause(s) for `--export` / file-output behavior.
2. Apply the tripwires: is this "behaviour no spec clause backs" (⇒ FEATURE) or a violation of an existing, already-specced surface (⇒ BUG)? Since `--export` is an existing, shipped surface and the complaint is that its promised output silently degrades to data loss, this is a **bug** against an existing surface — unless the JOURNAL grep shows a second export-area bug inside 30 days, in which case it **re-doors to feature** (the area is missing an invariant → full pipeline from step 1: spec the invariant, re-prove, then fix under it). Assume for this walk the grep comes back clean, so it stays a bug.
3. State the intake line aloud and let the human hear the capture echo: size (single-surface, one-file-class fix) · priority (silent data loss, high) · **door: bug** · **work-kind: infra** (a CLI tool) · map: "changes feature `--export`" (cites the spec's export section/anchor).
4. Confirm one-story: this is one story ("export fails safely instead of writing empty output"); no mockup-first condition applies (no visual surface).

**Bug shortcut — `bug → matrix → test → code`, citing the existing architecture node.**
5. Open `ARCHITECTURE.md`, find the node that owns the export/output-writing fact (infra kind: "one node owns the tool, pinned to its entry point"), and cite its `file:line` pin — no architecture rewrite, just cite it.
6. If `PRODUCT_SPEC.md` already carries a sentence describing `--export`'s output contract, update that sentence in the same change to state the corrected contract (e.g., "fails loudly with no partial file" or "creates the target directory," whichever is decided in step 9 below) — spec updates ride with the fix, not after.
7. **Class sweep (base rule 14):** name the pattern — "a file-writing code path silently proceeds when its parent directory is missing" — then grep the whole CLI source for every other output-writing path (other export formats, log files, report/dump flags, config writers) and fix every sibling in this same change, not just `--export .csv`.

**Matrix (step 5, infra form).**
8. With `test-author`, add rows to `TEST_MATRIX.md` under the cited node: function-level rows ("run the tool, assert real output") for (a) the positive case — valid `out/` produces a real non-empty CSV — and (b) the never-side/regression fence — given a missing output directory, the tool must NEVER silently produce an empty file; it must either create the directory or exit non-zero with a clear stderr message. Do the same for every sibling path found in step 7. Each row pins its test level and states both the DOES and NEVER side.

**Test (step 6).**
9. With `test-author`, write tests in `tests/` that run the real `mytool` binary against a fixture where `out/` doesn't exist, then inspect the real filesystem/stderr/exit code — not a source-string check. Watch the new test **fail first** (red-on-bug, reproducing the reported silent-empty-file behavior) before touching source. Add the matching sibling tests from step 7.

**Code (step 7).**
10. Decide the correct behavior once (a judgment call, kept on the senior, not guessed): either auto-create the missing directory or fail with a clear error and no file written — pick the sensible default and treat it as an `[default]`-tagged tradeoff to be **told** at landing, never asked/confirmed. Implement the fix and its siblings; if the edit is mechanical and well-scoped (validate/create-or-error, applied across the sibling paths), delegate to a Sonnet-tier worker with a self-contained brief (exact files, exact spec/matrix anchors, exact checks) while keeping the design decision itself on the senior.

**Verify by deed (step 8).**
11. Run `mytool --export out/report.csv` for real against a missing `out/`, eyes on the actual result (directory created / error shown, no more silent empty file), for the original case and every sibling. Since code, spec, matrix, and test files are all in the diff, run the **whole suite** (reach-map law). Green = zero failures and the skip-set matches the pinned list exactly; anything unexpected is a failure.

**Commit & show (step 9).**
12. Commit once green with no regression. Update `CHANGELOG.md` in user-outcome language with one concrete example ("`mytool --export out/report.csv` now [creates `out/` / reports a clear error] instead of silently writing an empty file"). Diary the WHY in `JOURNAL.md`, naming the area ("export") so a future recurring check can grep it. Bump the version (PATCH). Push (remote already exists on this tree), re-walking the README against the pushed truth first. The landing report tells the `[default]` behavior choice from step 10 in plain words, with the example, unasked. Show the human the real terminal output of the fixed run.
