# Prover — row 242, the README feels-boundary stance (2026-07-12, short form per INV-61)

Small delta (kind: prose; architecture = no assignment — no invariant minted, no matrix row).

- **Previous records:** 2026-07-12-row240-layout-pass-vehicle clean (0 must-fix); no unfolded rows.
- **The delta in one line:** one paragraph appended to README.md's "Why live-spec, when BMAD…" critique
  block, after "These lenses have since run on the pack's own features and on real incoming wishes."
  and before "## Known issues" — the method states its own position on the feel boundary: a spec owns
  what can be written down and tested; feel belongs to the owner's eye; the method answers taste by
  routing, never dressing a taste call up as a test; the feel pass at verify, the visitor walk, and the
  list of named taste defaults are the routes; the photo-portfolio critique stays cited as the case that
  taught it. Prose-only under INV-84 (clean-writer authorship) and INV-83 (the pre-show register lint);
  mints no new invariant and no matrix row, so INV-113/M-251 stay free. Composition read: no clash with
  INV-109 (no-silent-drop — this paragraph adds, it removes nothing) or INV-83/84 (it satisfies them,
  not extends them); no architecture edit, no skill-header version move.
- **Text provenance:** the pending draft's own candidate paragraph (242.a) was superseded — the
  orchestrator's call directed the clean writer's paragraph (row242-clean-paragraph.md, authored in a
  fresh session with the pack not loaded) to land instead. Both texts hold the same stance and register
  laws; the clean writer's is the landed one.
- **Lint gate:** `scripts/spec-style-lint.py README.md` — 0 errors, 12 pre-existing warnings (none on
  the new paragraph's lines). `scripts/preshow-register-lint.py README.md` — OK, no coined metaphor,
  calque, or transliterated pack term found.
- **Verdict:** ready to ship — 0 must-fix, 0 should-clarify.
- **Gate h note:** the first push attempt was blocked by this repo's own `check_tests_present.py`
  (INV-97, this repo attached as its own first host) — README.md is a registered `user_facing_globs`
  entry, so the diff needed a tests/ change regardless of the row minting no invariant. Resolved by the
  orchestrator's call (option a): a new string test, M-250 (rides INV-84/INV-83, mints no new
  invariant), pins the landed paragraph — `tests/test_readme_stance.py`, red proven against the
  pre-delta README then green against the landed one.
