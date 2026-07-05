# With-skill run — build-pipeline scenario (2026-07-06, model = sonnet worker, arm = with-skill)

Read `skills/build-pipeline/SKILL.md` in full first, then answered strictly by it.

Verbatim output:

---

1. **Step zero, before any tool call: name the door aloud, and echo the capture back.** Door = **bug**
   (existing surface — `--export` — silently produces a wrong artifact; no new surface or state is being
   introduced). Work-kind = **product** (`mytool` is the CLI the end user runs directly; the CSV is the
   artifact they receive — not internal tooling). Priority = high (silent data loss beats a loud crash);
   size = small, localized to write-paths. Capture echo, said back to whoever reported it: *"Heard —
   `mytool --export` writes a silently-empty CSV when the target directory is missing. Door: bug.
   Work-kind: product. Entering at bug → matrix → test → code."*

2. **Before taking the bug, grep `JOURNAL.md` for this area's name and check the dates.** If a second
   bug in this same export/write-path area has landed within the last ~30 days, this bug re-doors to
   **feature**: the area is missing an invariant, not missing a patch, and I restart at the full pipeline
   (spec it, re-prove, then fix under it). Assume for now the grep comes back clean and this stays a bug.

3. **Cite the existing architecture node** — a bug or small change doesn't rewrite `ARCHITECTURE.md`, it
   just cites the node that already owns the export/write path (its `file:line` pin), and skips straight
   to the matrix.

4. **Name the class before writing anything down (base rule 14): "a CLI flag that takes an output-file
   path writes without first ensuring its parent directory exists, so it silently produces an empty file
   instead of either creating the directory or failing with a clear error."** Grep the source tree for
   every other write-path with the same shape — every `--*-file` / `--output*` / `--log` / `--export`-style
   flag, every raw `open(`/`Path(...).write_*` call. The reported CSV bug is one sample of this class; the
   fix, the matrix rows, and the tests all have to cover every sibling found here, not just `--export`.

5. **Check `SPEC.md`** for whatever clause already governs `--export` / output-file behavior. If the fix
   corrects a fact SPEC.md already states, the spec sentence gets corrected in this same change. If
   neither "creates missing directories" nor "errors on a missing directory" is specified anywhere for
   this flag or its siblings, that is a genuine `⟨DECIDE⟩` — a real product decision, not something to
   guess.

6. **Where that decision is genuinely open, ask it once, batched with the class findings — and don't let
   it park the lane (SPEC INV-4/INV-5).** One question: *"Found N siblings with the identical
   missing-directory bug: [list]. Should `mytool` auto-create the missing output directory before
   writing, or fail fast with a clear, named error before writing anything? Whichever is chosen applies
   to `--export` and to all N siblings."* State the recommended default (fail-loud — it never leaves a
   corrupt/empty artifact behind, and it's the safer default for a data-export tool) and proceed on that
   default now; the human's actual answer, whenever it lands, is a one-line change to apply, not a reason
   to stall the fix.

7. **Update `SPEC.md`** with the corrected/added sentence for `--export` and every sibling flag from step
   4, under the chosen (or defaulted) contract — so the fix traces to a spec clause, not a silent
   micro-decision (this is what the Bounds guardrail checks for).

8. **Derive `TEST_MATRIX.md` rows** — one row per affected write-path × "target directory missing," each
   row stating both sides: what it DOES now (creates the dir and writes the real CSV, or fails with the
   named error and writes nothing) and what it must NEVER do (never leave a zero-byte file behind, never
   exit 0 while silently producing a wrong artifact). Pin the test level: this is CLI output, so the level
   is function/CLI-level — run the real tool, assert the real file on disk, never a source-string match.

9. **Write the failing tests first (red-on-bug).** For `--export` and every sibling from step 4, drive
   the real CLI (or the real function it calls) against a target whose parent directory is absent, and
   assert the corrected behavior from step 6/7. Run the suite and confirm these new tests fail against
   today's code, for the expected reason (empty file / wrong exit code) — proving they actually exercise
   the bug before any fix lands.

10. **Fix the code.** In the node cited in step 3, make the write path ensure the parent directory exists
    (or raise the specified error) before ever opening the file for write — and apply the identical change
    to every sibling call-site found in step 4, in the same change, not as a follow-up.

11. **Run the new tests to green, then the whole suite.** Green means zero failures and only the expected,
    pinned skip list — an unexpected skip doesn't count as a pass.

12. **Run the project's guardrails check** (completeness, tests-present, bounds, conflicts — the pre-push
    hook set) before considering this anywhere near done. Bounds specifically confirms the new behavior
    traces to the SPEC sentence from step 7; tests-present confirms `tests/` was touched.

13. **Verify by deed on the real artifact.** Actually run `mytool --export out/report.csv` in a real shell
    with `out/` absent and look at the real result myself — the directory now exists with a real non-empty
    CSV in it, or a clear real error message and no file written, matching whichever contract was chosen.
    Don't call it fixed off the test suite alone.

14. **Commit.** Bump PATCH (bug fix, no new surface). Update the CHANGELOG in user language with the real
    before/after example from step 13; write the WHY in `JOURNAL.md` (silent empty-file bug, the class it
    turned out to include, the chosen dir-creation-vs-fail-loud contract) — commit locally, unasked, since
    it's green with no regression.

15. **Report to the project owner in plain language, before any push:** what was broken, what the class
    search actually found (the N sibling flags), which contract was applied (the recommended default,
    flagged as still awaiting their explicit word if they haven't answered yet), the files touched (SPEC,
    matrix, tests, source, CHANGELOG, JOURNAL), and the real verified output from step 13. Push only after
    they've reviewed it.

---
