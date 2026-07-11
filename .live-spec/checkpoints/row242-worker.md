# Row 242 worker checkpoint — README feels-boundary stance paragraph

Briefed: 2026-07-12, applier role, mechanical landing from pending-draft-row242.md. Orchestrator's call:
insert the clean writer's paragraph (row242-clean-paragraph.md), using the draft's 242.a anchor; the
draft's own candidate paragraph is superseded, not used.

## Write-set
- .live-spec/checkpoints/row242-worker.md (this file)
- README.md (1 edit: one paragraph inserted after the critique block's last paragraph, before "## Known issues")
- VERSION (1.0.27 -> 1.0.28)
- .claude-plugin/plugin.json ("1.0.27" -> "1.0.28")
- ROADMAP.md (row 242 status cell -> landed, prose-only, delegation line)
- docs/prover/2026-07-12-row242-readme-stance.md (NEW, short form)
- .live-spec/checkpoints/pending-draft-row242.md (append APPLIED+CLOSED line)

## Anchor confirmed present before editing (2026-07-12)
- README.md: "These lenses have since run on the pack's own features and on real incoming wishes.\n\n## Known issues"
  present verbatim, unique (grep -c on the paragraph tail = 1), at line 103 tail -> line 105 heading.
  No collision with rows 233/239/240 (none touch README.md, per the draft's own 242.e check, reconfirmed).

## Live version values read (2026-07-12)
- VERSION (pack): live 1.0.27 -> 1.0.28.
- .claude-plugin/plugin.json: live "1.0.27" -> "1.0.28" (lockstep with VERSION, per house pattern).
- No skill-header version moves: README-only prose landing per the draft's 242.d — no spec clause, no
  skill body, no base rulebook touched, so the seven working-skill `live-spec-base` pins do not move.

## Lints (run on the changed README.md)
- `python3 scripts/spec-style-lint.py README.md` -> 0 errors, 12 warnings, all on pre-existing lines
  (28, 71, 73, 75, 77, 87, 93x2, 99x2, 101, 113) — none on the new paragraph. Advisory severity, exit 0.
- `python3 scripts/preshow-register-lint.py README.md` -> "OK (preshow-register): no coined metaphor,
  calque, or transliterated pack term found." Exit 0.
- Both pass; nothing to fix.

## Suite
- Before any edit: not re-baselined separately (draft's own self-verify already confirmed the pre-delta
  tree state; row 240's landing left it at 409 passed).
- After README edit + version bumps: `python3 -m pytest tests/` -> 409 passed in 36.16s, 0 failed.
- After the ROADMAP.md status-cell edit: `python3 -m pytest tests/` -> 409 passed in 36.52s, 0 failed
  (test_delegation_line.py's forward-scan confirms the new landed cell carries "delegation").

## Deviations from the draft
- Used the clean writer's paragraph (row242-clean-paragraph.md) instead of the draft's own 242.a
  candidate text, per the orchestrator's explicit call relayed in this session's brief. Both hold the
  same stance and register laws (no scissors frame, no coined metaphor, short SVO); wording differs
  (e.g. "three routes carry this work: the feel pass at verify..." vs the draft's candidate list). No
  other deviation — anchor, insertion point, and version/ROADMAP/prover mechanics followed the draft.

## Status

Steps 1-9 DONE, 2026-07-12. Green tail: `409 passed in 36.52s` (final re-run after the ROADMAP edit).
Both lints clean. README-only prose landing, no code minted, INV-113/M-251 left free. Committed
locally as 56dc672.

STOPPED at step 10 (push), 2026-07-12 — a gate the applier brief did not name.

- `git push origin main` was rejected by this repo's own pre-push hook, gate h ("the four host checks,
  this repo attached as its own first host, SPEC INV-97"), specifically `check_tests_present.py`
  (scaffold/guardrails/, wired via guardrails.config.json's `user_facing_globs`, which lists
  `README.md`): "FAIL (tests-present): user-facing file(s) changed with no change under tests/:
  README.md" — the diff touches a registered user-facing surface (README.md) and touches nothing
  under tests/, so the check reds regardless of whether the row mints an invariant or matrix row.
  All other gates in the same run passed (prover-record freshness, full suite 378 green inside the
  hook's own scoped run, matrix coverage, pin drift, skill loadability, prototype fence, surface
  completeness, anchor traces, conflict scan).
- This directly conflicts with the draft's own 242.c ("Nothing is added to the spec's Formal index or
  TEST_MATRIX... no matrix row") and the brief's framing of row 242 as prose-only, no code minted. The
  guardrail's own suggested fix is generic ("add or update a test under tests/ for this change (or
  record the exemption where your matrix expects it)") — this repo has no wired exemption/waiver path
  for this specific check (checked scripts/gate_common.py's waiver mechanism: it only serves the
  register-lint gate, not check_tests_present.py; guardrails.config.json's own "waivers": {} is empty
  and check_tests_present.py never reads it).
- Deciding whether to (a) add a minimal content-presence test under tests/ asserting the new paragraph
  is present in README.md — which would mean this row is no longer test-free, contradicting the
  draft's and brief's "no matrix row" framing, even though it need not mint a new INV/M code — or
  (b) adjust guardrails.config.json / add a wired exemption path, or (c) something else, is a design
  call outside an applier's mandate. Per the brief's own STOP rule ("lint failure you cannot fix
  mechanically, or any ambiguity: STOP, record, report, commit nothing"), halting here rather than
  picking one. No precedent found either way: no README-only commit has landed since gate h went live
  at 1.0.8 (commit 3c98294) to show how this was handled before.
- Working tree / repo state: commit 56dc672 exists on local main, NOT pushed. No further edits made
  after the push rejection. Nothing force-pushed, no gate bypassed, no --no-verify used.

## Continuation, 2026-07-12 — the orchestrator's call: option (a), the test pin

The orchestrator resolved the STOP: gate h stands as correctly firing; the landing gets its own test
pin — a user-facing prose claim is pinned by a string test, the method's own standing pattern (same as
every other row's homes).

- **New test:** `tests/test_readme_stance.py`, style modeled on `tests/test_no_silent_drop.py`
  (whitespace-collapsed needle matching). Two tests: `test_stance_paragraph_present` (three needles —
  "A spec owns what a project can write down and test.", "The method answers taste by routing", "The
  photo-portfolio project stays cited here as the case that taught the boundary.") and
  `test_stance_paragraph_before_known_issues` (position check: the stance text's index is less than
  "## Known issues"'s index in the raw file). Docstring names M-250, INV-84/INV-83, row 242, and the
  gate-h origin.
- **RED proof (mechanical):** `git checkout HEAD~1 -- README.md` (restores the pre-242 README, i.e.
  before commit 56dc672) then `python3 -m pytest tests/test_readme_stance.py -v` -> both tests FAILED
  ("stance paragraph not found" / AssertionError on the -1 index). `git checkout HEAD -- README.md`
  (restores the landed paragraph) then re-run -> `2 passed in 0.01s`. Both legs confirmed by the actual
  pytest output, not inferred.
- **TEST_MATRIX.md:** M-250 added. First placement (right after M-249, under the "attach" architecture
  node) failed `tests/test_traceability.py::TestMatrix::test_matrix_rows_sit_under_their_owning_node`
  ("M-250 sits under 'attach' but cites only ['INV-83', 'INV-84'] (owned elsewhere)") — INV-84 is owned
  by base-rulebook and INV-83 by communicator per ARCHITECTURE.md's owns-lists, neither by attach.
  Moved the row to sit under the "communicator" node block (right after M-247, which cites INV-109 —
  also a communicator-owned invariant), since communicator's owns-list includes INV-83. Re-run: green.
- **Full suite after the move:** `python3 -m pytest tests/` -> `411 passed in 35.73s`, 0 failed. (The
  brief predicted 410; actual is 411 — 409 baseline + the 2 new tests in test_readme_stance.py. Read as
  the brief's estimate being one test light, not a defect; the suite is fully green either way.)
- **Docs updated:** this checkpoint (this section); docs/prover/2026-07-12-row242-readme-stance.md
  (one-line gate-h note appended); ROADMAP.md row 242's status cell (delegation line extended with the
  gate-h block + M-250 resolution, "no code minted" corrected to "no invariant minted" since M-250 now
  exists, suite count 409 -> 411 throughout); pending-draft-row242.md (one line: 242.c's "no matrix
  row" note superseded by gate h, M-250 minted at landing).

## Status (final)

DONE, 2026-07-12. Green tail: `411 passed in 35.73s`. Both lints still clean (unaffected by the test
file). RED-then-green mechanically proven for M-250. TEST_MATRIX.md, ROADMAP.md, the prover record, and
pending-draft-row242.md all carry the gate-h resolution. Amend-and-push are the next steps outside this
checkpoint's own write-set (the orchestrator's steps 6-8).
