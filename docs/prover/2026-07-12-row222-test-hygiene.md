# Prover — row 222, tests clean up after themselves + the temp-home placement (2026-07-12, short form per INV-61)

Small delta (kind: skill, no new surface; architecture touch = anchor assignment INV-100 →
test-author) — the three-line short form.

- **Previous records:** 2026-07-11-row219-skill-kind-review clean (0 must-fix, the review table
  fully folded/rejected by name); no unfolded rows.
- **The delta in one line:** the hygiene law in two halves — every test removes what it creates
  (temp files, fixtures, processes, mutated shared state) and a suite run leaves the machine as it
  found it, a leak being a defect of the test; placement — test files are born in the system temp
  home or the gitignored state dir, user-visible folders are never a test's workspace, a headless
  browser's download directory is pointed at the temp home (the 42-files-in-Downloads incident,
  2026-07-10) — stated in the spec (INV-100, clause + index), test-author's writing rules, and the
  matrix template's checklist; the pack's own instantiation is mechanical: temp artifacts carry the
  livespec-test- prefix and a session-scoped before/after diff of the temp home (tests/conftest.py)
  fails the run on a surviving file, red-proven by a planted leak; the card tests' known leak swept
  (tracked temp helper + module teardown), zero suite-prefixed files left after a full run.
  Composition read: the red-first law untouched (the hygiene bullet sits beside it, neither weakens
  the other); INV-77's real-device boundary unrelated and whole; the guardrails' scratch-copy gate
  (gate B) runs the same conftest inside its copy — the diff scopes to the suite's own prefixes, so
  foreign temp traffic cannot false-positive it.
- **Verdict:** ready to ship — 0 must-fix, 0 should-clarify.
