# With-skill run — build-pipeline scenario (2026-07-06 push-gate re-run, model = sonnet worker, arm = with-skill, build-pipeline 0.2.19)

Read skills/build-pipeline/SKILL.md (+ base) first; 2 tool uses.

Verbatim output:

---

Here is the exact sequence I'd follow, in order, per `build-pipeline` (citing `live-spec-base` rules where they drive a step):

**0. Classify before touching anything.**
State the intake line out loud: size = small, priority = (ask if not given, otherwise treat as normal), **door = bug** (this is existing behavior misbehaving, not a new surface), **work-kind = product** (a real user hit this directly through the CLI's own interface — the tripwire is "a user faces it," which a CLI flag does just as much as a screen). This determines the bug shortcut applies: `bug → matrix → test → code`, entering by citing the existing architecture node rather than rewriting it.

**1. Check for recurrence before treating it as a one-off.**
Grep `JOURNAL.md` for "export," "out/", "mkdir," "directory," and any prior write-path incidents, and check the dates. If a second incident in this area has landed in the last ~30 days, this re-doors to a full feature entry (spec the missing invariant, re-prove, then fix under it) instead of a quick patch. If it's the first hit, continue as a bug.

**2. Reproduce it myself before assuming anything about the cause.**
Run `mytool --export out/report.csv` in a scratch directory with no `out/` present, and look at the actual resulting file — confirm it exists and is empty, and check the exit code. This is the primary-source evidence (rule 13); the bug report is a lead, not proof, until I've seen it myself.

**3. Read `SPEC.md`'s export clause.**
Find what the tool currently *promises* about `--export` and about missing destination directories. Two possibilities: the spec is silent on this case (a genuine gap), or it already implies behavior the code violates. Either way, note the exact clause.

**4. Read `ARCHITECTURE.md` to find the owning node for the export/write path**, and get its `file:line` pin from an actual grep/read — not from memory or the doc's own prose. This is the node the bug shortcut cites; no architecture rewrite needed unless the root cause reveals a missing node.

**5. Read the actual source at that pin to find the root cause.**
Almost certainly: the code opens the destination file for writing (or the CSV writer's underlying file handle) without checking/creating the parent directory, and either the OS error is swallowed or an empty file gets created before the failure surfaces. Pin the exact line.

**6. Name the class and sweep for siblings (rule 14 — a defect is a sample of its class).**
The pattern isn't "export is broken," it's "any CLI flag that writes to a user-given output path doesn't validate/create its parent directory and can silently leave a truncated/empty artifact on failure." Grep the whole repo for every other file-output flag (log file, config dump, cache path, any other `--output`/`--export`/`--save`-style flag) and check each one against the same failure mode. This determines how many matrix rows and tests I need, not just one.

**7. Decide the correct behavior — this is the one real judgment call.**
Whether missing dirs should be auto-created or should hard-fail with a clear error is a policy choice the spec doesn't currently make. Per rule 1, this becomes an `⟨DECIDE⟩` with a recommendation rather than a guess: recommend auto-creating missing parent directories (matches common CLI convention, avoids silent data loss) with a clear error and **no file left behind** if creation itself fails. I proceed on the recommendation and carry the open question into the landing report rather than blocking on it (rule 1/INV-4/5) — the human's gate is the review, not a mid-work stall.

**8. Update the SPEC sentence in the same change.**
Add/amend the export clause: what it does now (creates the missing directory before writing) and its never-side, the actual regression fence — it must never leave an empty or partial output file when the write can't complete. This is the "if the fixed fact also lives in SPEC prose, update it in the same change" instruction.

**9. Enter the matrix.**
Add row(s) to `TEST_MATRIX.md` under the owning node: both sides of the fact (creates missing dir + writes full content / never leaves empty or partial file on failure), pinned to a level that actually executes the tool and inspects the real output file — not a source-string check. Add matching rows for every sibling flag found in step 6 that shares the class.

**10. Write the tests first, and watch them fail (red-on-bug).**
A test that runs the real binary/entry point against a target path whose parent doesn't exist, then asserts on the real file: either it now exists with real rows, or the command exited non-zero and left nothing on disk. Confirm this test fails against the current code before changing anything — that's the proof it reproduces the reported defect. Add the equivalent test for each sibling flag from the sweep.

**11. Implement the fix — for the whole class, not just `--export`.**
Add the directory-creation/clear-error path at the shared write helper if one exists (better: fix once at the shared point); otherwise apply the same fix at each sibling call site found in step 6, so one instance reported means the whole class gets closed, not just the reported one.

**12. Run the new tests to green, then the full suite, then the guardrails.**
Whole suite, zero failures, skip-set matches the pinned expected list. Guardrails (tests-present, bounds-to-spec, conflicts) run before this is considered done, since this is what gates a push.

**13. Verify by deed, manually, one more time.**
Actually run `mytool --export out/report.csv` (and the sibling flags) against a fresh missing directory myself and read the real resulting file — not just trust the test suite.

**14. Update the user-facing docs in the same session.**
`CHANGELOG.md`: one plain-language entry with a concrete example ("exporting to a directory that doesn't exist now creates it, instead of writing an empty file"), no internal names. `JOURNAL.md`: the dated root cause, which sibling call sites were swept and fixed, and the recommendation made in step 7 — so a future recurrence-check (step 1's grep) has something to find.

**15. Commit locally** once green with no regression, version bump (PATCH by default).

**16. Show the human before any push.**
Report in plain words: what was actually wrong, what changed (the spec sentence, the fix, which sibling flags were also fixed), the one open taste call made (auto-create vs. hard-fail) named as a tweakable default rather than asked-and-blocked-on, and the before/after real command output as evidence. Push only after that review.

That is the point at which I'd consider it done — not when the new test goes green, but after the class-sweep siblings are also fixed, the spec/changelog/journal are updated, and the human has seen the real before/after run.
