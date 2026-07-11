# PENDING DRAFT — row 242 (prose-only; NO new invariant; INV-113/M-251 stay FREE), drafted 2026-07-12 by an Opus drafter, NOT yet applied
# Next session: this is a PROSE row. The paragraph below is a PLAIN CANDIDATE for the clean-writer road,
# not a mechanical paste. See the applier note — the final text is clean-authored (INV-84) and lint-passed (INV-83) before it lands.
# versions: read live values, +0.0.1 on landing; INV-103 delegation-accounting line rides the landed ROADMAP status cell.

I have everything needed. Row 242 is draftable as a single README prose insertion. It does NOT hit the STOP rule (not a surface, not a bundle, not blocked). It mints NO new invariant and NO matrix row — its Done-when is prose-quality only ("the paragraph stands, clean-authored, lint-clean; the critique block reads as claim → critique → stance, no dangling admission"), with no red-proof clause, so no code is consumed. INV-113 / M-251 remain FREE for the next law-shaped row.

---

# DELTA — Row 242 — DRAFTABLE (prose-only, no code)

**What the row asks:** one paragraph in the README why-section's critique block that states the method's own position on the feel boundary — a spec owns what can be written and tested; feel belongs to the owner's eye; the method's answer to taste is routing, and it never dresses taste up as a test; the feel gate, the visitor walk, and the named-taste-defaults list exist to bring the right call to the owner's eye at the right moment; the portfolio critique stays cited as the case that taught it.

**One home.** README.md, the "Why live-spec, when BMAD… exist" section, appended to the critique block that today ends at the sharpest-critique paragraph (the photo-portfolio paragraph). No canonical block (single home). No new test file (prose-only; the register lint INV-83 already gates any shown artifact, and INV-84 gates the authoring).

**Governing laws it rides (already live, not re-stated):** INV-84 (human-facing prose is drafted by a clean writer from a plain brief) and INV-83 (the register lint blocks any shown artifact carrying a leaked term). Kin: rows 117/118's taste-defaults family (the feel gate / visitor walk / named-defaults list this paragraph points at).

## 242.a — README PROSE INSERT (README.md) — append one new paragraph after the critique block's last paragraph

**old_string** (exact, unique — the tail of the sharpest-critique paragraph, then the blank line and the "## Known issues" heading):
```
These lenses have since run on the pack's own features and on real incoming wishes.

## Known issues
```

**new_string** (inserts one paragraph between the critique block and the Known-issues heading; the paragraph text below is a PLAIN CANDIDATE — see the applier note):
```
These lenses have since run on the pack's own features and on real incoming wishes.

This critique taught a boundary the method now states as its own position. A spec owns what can be written down and tested. Feel belongs to the owner's eye, and a judgment like "eighty-percent-finished everywhere" formalizes badly. So the method answers taste by routing. It brings the right call to the owner's eye at the right moment, and it never dresses taste up as a test: the feel gate, the visitor walk, and the list of named taste defaults are the routes that carry a taste call to the eye that owns it. The photo-portfolio critique stays cited here as the case that taught this.

## Known issues
```

## 242.b — APPLIER NOTE: this paragraph is clean-authored, not pasted (INV-84 + INV-83)

- The README is durable human-facing prose, so INV-84 binds: the final paragraph is drafted by a **fresh writer session with the pack NOT loaded**, from a plain brief carrying (i) the facts (the stance in "What the row asks" above), (ii) the reader (a developer weighing live-spec against BMAD/Kiro/spec-kit), and (iii) the register laws. The candidate text in 242.a is a faithful plain-English draft for that brief; the applier does not paste it blindly — it either confirms the candidate passes the clean bar or replaces it with the clean writer's return.
- Before landing, run `scripts/spec-style-lint.py` (and the pre-show register lint `scripts/preshow-register-lint.py`) over the changed README section; land only lint-clean. This satisfies the Done-when's "lint-clean".
- Register guard I already held while drafting the candidate: no coined metaphors; short SVO sentences; NO "X — not Y" / "X, not Y" contrast frame — the one prohibition is its own plain clause ("it never dresses taste up as a test"), matching the profile's global scissors ban.
- Structure check for the Done-when: after insertion the block reads claim (the portfolio reported unfinished-everywhere) → critique (where the method wasn't looking) → answer (shipped lenses) → **stance** (this new paragraph). No dangling admission remains.

## 242.c — NO index row, NO matrix row, NO architecture edit

Prose-only application of INV-84/INV-83. Nothing is added to the spec's Formal index or TEST_MATRIX. INV-113 and M-251 are NOT consumed by this row and stay free for the next law-shaped row.

## 242.d — APPLIER VERSION REMINDER

- Only README.md changes. No skill body, no spec clause, no base rulebook — so the seven working-skill `` `live-spec-base` (vX.Y.Z) `` header pins do NOT move.
- `VERSION` (pack) — +0.0.1 over the live value at apply time (do not hardcode; read and increment). A README-only prose landing is a patch step.
- INV-103 delegation-accounting line: this lands 2026-07-12, so the landed ROADMAP row's status cell carries its one-line accounting (drafted by an Opus drafter, prose finalized by a clean writer, applied mechanically).

## 242.e — ANCHOR-COLLISION CHECK

Rows 233, 239, and 240 (applied before this draft) touch PRODUCT_SPEC.md, TEST_MATRIX.md, ARCHITECTURE.md, skills/communicator, skills/build-pipeline, and MIGRATION.md. **None of them touch README.md.** The 242.a anchor (`These lenses have since run on the pack's own features and on real incoming wishes.` → `## Known issues`) is therefore collision-free and stable. No flag.

---

## Self-verify

- STOP rule checked: not a surface (one README paragraph), not a bundle (one stance), not blocked (no pending human word — the row was queued on his 2026-07-10 ~14:24 word, the stance is stated, not asked). Draftable.
- No code consumed: Done-when is prose-quality only, no red-proof; INV-113/M-251 verified absent from the tree and left free.
- Candidate prose holds the register laws: no scissors frame, no coined metaphor, short SVO; the prohibition is a standalone clause.
- Single home; anchor quoted from the live README (line 103 tail → line 105 heading), collision-free against rows 233/239/240.

---

APPLIED + CLOSED at landing 2026-07-12 (row242-worker.md; the clean writer's paragraph landed).

242.c's "no matrix row" note was superseded by gate h (`check_tests_present.py`, INV-97): the
push-gate rejected a README-only diff with no tests/ change regardless of whether the row minted an
invariant. Resolved by the orchestrator's call (option a) — M-250 minted at landing, riding
INV-84/INV-83, no new invariant. See row242-worker.md's STOP-and-resolution account.
