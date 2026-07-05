# PASS 2 — TEST MATRIX audit (0.5.0 preventive-maintenance gate)

**Auditor:** Opus worker · **Date:** 2026-07-05 · **HEAD audited:** `15369ba1f892d76d10734e18b2e0dcff2bf15595`
**Scope:** `TEST_MATRIX.md` against `SPEC.md` (Formal index, 70 anchors) and `ARCHITECTURE.md` (12 nodes).
**Independent of** the other passes of the day (not read).

---

## 0. Suite result (baseline)

```
$ python3 -m pytest tests/ -q
...................................                                       [100%]
35 passed in 7.01s
```

35 green — baseline confirmed. `tests/test_traceability.py` (13 checks across 6 classes) + `tests/test_guardrails.py`
mechanize the *completeness* half of this audit. What they mechanize, and therefore what I did NOT re-do by hand:

- **coverage completeness** — `test_matrix_covers_every_anchor` (index ⇄ matrix bidirectional), `test_architecture_owns_every_anchor_once`, `test_matrix_blocks_match_architecture_nodes`.
- **shape** — `test_matrix_rows_have_level_and_negative_side` (every row: level ∈ {string,DOM-text,browser-computed,pixel}, contains the word "never", status ∈ vocabulary, no duplicate ids).
- **BUILT rows name a real `def test_…`** — `test_matrix_built_rows_name_real_tests` (name existence only).
- **inventory shipped-non-empty**, **coverage-checklist boxes all `[x]`** (`guardrails/check-matrix-coverage.sh`).

**My job = the part they do NOT mechanize:** is each row's LEVEL *adequate* and the text-product adaptation *honest*;
does each named test actually ASSERT the row's fact against the shipped artifact (not merely exist); is each NEVER
side actually asserted or only stated; and is the coverage checklist honest item-by-item.

---

## 1. Anchor ownership — 3.a  ✅ PASS

Re-derived independently (script output, checkpoint):

```
INDEX anchors expanded: 70
anchors in >1 matrix row: {}
index anchors with NO row: []
matrix anchors not in index: []
total distinct anchors owned: 70
```

- All 70 Formal-index anchors (S-0; E-1..16; T-1..11; INV-1..15; B-1; A-0..9; ACT-1..3; M-1..7; C-1; D-1..5) are owned by **exactly one** matrix row. No orphan, no stale, **no contradictory double-ownership.**
- The one range that is *split* — `T-1..T-7` — is split cleanly and consistently with the architecture: `T-1..T-6` → build-pipeline row `M-017`, `T-7` → communicator row `M-030`. No overlap, no gap. Correct.

---

## 2. Level adequacy & honest adaptation — 3.b  ⚠ mostly PASS, two should-fixes

Every row is level `string`. The header's adaptation (prover record F6) — a text/skills product ships no browser
surface, so the "rendered level" is a `string` assertion **against the shipped file on disk** — is **honest and correct**:
I found no rendered/visual/interactive surface anywhere in the pack, so checklist item 4 ("≥ browser-computed") is
genuinely vacuous. Structural facts get BUILT string tests; behavioral facts (a discipline that holds *over time*)
are TODO with a named future owner. That framing is sound.

**Where the adaptation is used to defer a fact that is testable NOW:**

- **[should-fix S2] `M-002` (E-13, settings ladder), `TEST_MATRIX.md:69`** — deferred to "milestone audit (M-1) + guardrails row 3", i.e. a hand audit. But E-13's structural core is fully documented in the shipped file: `skills/live-spec-base/SKILL.md:91-96` literally states *"session beats host beats personal beats package default (SPEC E-13)"* with the four-scope table. A one-line string test (`assert "session beats host beats personal beats package default" in base_skill`) is available today. Deferring a testable structural fact to a manual audit is exactly the "adaptation used to dodge" pattern the header warns against — even if the *behavioral* half (resolution actually happening) stays TODO.

- **[should-fix S3] `M-001` (E-12), `TEST_MATRIX.md:68`** — the fact is *"the base skill states every shared rule once; never a working skill restating a shared rule normatively."* Its owning test `test_skills_inherit_base_pin` asserts only that each working skill's body **contains the string `live-spec-base`** (an inherit pin). That is adjacent evidence, not the stated fact: it does not check the base states each rule once, nor that a working skill does *not* restate a rule normatively. The row over-claims what its test proves.

All other TODO-with-process-owner rows (M-004 INV-9 trust-by-human, M-008/009 ACT-1/2, M-013 E-4, M-014 C-1, M-016 E-2, M-030 T-7) are genuinely behavioral disciplines with no available string proxy — honest TODOs, correctly owner-named.

---

## 3. Row → test spot-check (≥10) — 3.c

`test_matrix_built_rows_name_real_tests` already proves every BUILT row names an existing `def`, so I checked the
harder question: **does the test's assertion match the row's fact?**

| # | Row | Owning test | Verdict |
|---|---|---|---|
| 1 | M-005 (INV-11 fence) | `test_armed_stale_head_blocks_commit`, `test_unarmed_fence_passes_silently` | ✅ STRONG — exercises the real hook; stale HEAD → rc 1 "COMMIT BLOCKED"; unarmed → rc 0. Asserts both sides. |
| 2 | M-022 (INV-2 one landing) | `test_roadmap_single_in_work` | ✅ STRONG — asserts `len(in_work) <= 1` on the shipped ROADMAP. Never-side real. |
| 3 | M-025 (INV-12 class vocab) | `test_roadmap_class_vocabulary` | ✅ STRONG — asserts every class cell matches the four-word regex; `bad == []`. |
| 4 | M-026 (E-14 architecture) | `test_architecture_owns_every_anchor_once`, `_no_orphan_nodes` | ✅ STRONG — missing/dupe/stale/orphan all `== []`. |
| 5 | M-027 (E-15 matrix derived) | `test_matrix_covers_every_anchor`, `_blocks_match_architecture_nodes` | ✅ STRONG — bidirectional. |
| 6 | M-033 (INV-6 DO+NEVER) | `test_matrix_rows_have_level_and_negative_side` | ✅ GOOD — every row must contain "never"; asserts the fence's presence. |
| 7 | M-015 (M-6 push gate) | `test_real_repo_passes`, `test_missing_record_fails` | ✅ STRONG — runs `check-prover-record.sh`; missing record → rc 1 "FAIL". |
| 8 | M-053 (M-3 dated) | `test_roadmap_header_dated` | ✅ GOOD — regex date on shipped ROADMAP + versioned SPEC header. |
| 9 | M-054 (M-4 own host) | `test_hooks_and_scripts_exist_and_executable` | ✅ GOOD — asserts shipped hooks exist + executable bit. |
| 10 | M-011 (M-2 breakpoint) | `test_next_steps_live_state` | ✅ GOOD — exactly one `## LIVE STATE`, dated → asserts "never stacked". |
| 11 | M-007 (INV-14 no silent override) | `test_host_profile_recorded_override` | ⚠ PROXY — asserts the profile *cites* INV-14/E-13/M-6, i.e. the rule is written down; does NOT assert "no silent divergence" behaviorally. |
| 12 | M-012 (M-7 version homes) | `test_version_homes` | ⚠ PROXY — asserts VERSION is semver + each skill has `version:` frontmatter (presence). Does NOT assert "never scattered" (no stray version strings elsewhere). |
| 13 | M-039..M-047 (A-0..A-9) | `test_adopt_phases_cite_spec` | ⚠ PROXY — asserts ADOPT.md *cites* the A-codes; behavior "= next adopt run" per the row (honestly flagged). |
| 14 | M-048/M-050 (E-11/INV-10) | `test_inbox_states_write_rule` | ⚠ PROXY — asserts inbox README documents the write rule + filename format; does not enforce that outsiders never write. |
| 15 | M-055..M-059 (D-1..D-5) | `test_spec_decide_markers_match_open` | ✅ GOOD — a silently-resolved D would drop from Open decisions → test fails; asserts "never silently resolved". |

**Read:** the *behavioral-gate* tests (fence, roadmap, guardrails, traceability, next-steps, decide-markers) are strong,
genuinely two-sided assertions against shipped artifacts. The *documentation-citation* tests (host profile, inbox,
adopt, version homes) are one-sided PROXIES — they prove the rule/codes are written in the shipped file, not that the
behavior holds. For facts whose content *is* "the document states X" this is a true match; for behavioral disciplines
(INV-14, INV-10) it is a documentary fence only. The matrix is honest that these are string-level, so this is a **note**,
not a defect — except S3 above where the proxy is mislabeled as the fact itself.

---

## 4. NEVER-side actually asserted — 3.d

Every row carries a "never" clause in its text (mechanized). For **BUILT** rows I checked the never-side is *asserted*,
not only *stated*:

- **Genuinely asserted:** M-005 (stale HEAD blocked), M-011 (never stacked), M-015 (missing record fails), M-022 (≤1 in-work), M-025 (no out-of-vocab cell), M-033 (every row has never), M-055–059 (open decisions stay open), M-026/027 (no orphan/stale).
- **Stated but only documentarily fenced** (proxy, see §3): **M-007** (INV-14 "never a silent divergence"), **M-012** (M-7 "never scattered or absent" — presence tested, not absence-elsewhere), **M-050** (INV-10 "outsider never writes"). These rely on the rule being written down; no mechanical check would catch an actual violation. Inherent to a text product, but worth recording as a known limitation.
- **TODO rows** carry an un-asserted never-side by design (named debt) — correct per the header's "a TODO row is a named debt, never a silent one."

No BUILT row was found where the never-side is *falsely* claimed as mechanically enforced.

---

## 5. Coverage-validation checklist walk — 3.e  (5/5 boxes honest)

| Item (`TEST_MATRIX.md:193-197`) | Verdict |
|---|---|
| 1. Every anchor in ≥1 row — 70/70, mechanized | ✅ PASS — re-derived 70/70 independently. Count "70" is correct. (The parenthetical "rows 52–53" refers to ROADMAP rows for E-16, not matrix rows — mildly confusing, see N4.) |
| 2. Every node has ≥1 block + negative-side rows — 12/12 | ✅ PASS — 12 arch nodes ⇄ 12 matrix blocks (`test_matrix_blocks_match_architecture_nodes`); every row has a "never". |
| 3. Every inventory entry owns ≥1 rendered-level row — string vs shipped | ⚠ PASS with wording gap (N1) — the actual guarantee is *shipped-and-non-empty* via `test_artifact_inventory`; inventory entries are a separate table, not M-rows, so "owns ≥1 rendered-level row" over-states the mechanism. |
| 4. Every visibility/layout fact ≥ browser-computed — vacuous, no browser surface | ✅ PASS — honest; the pack ships docs + shell only. |
| 5. No row cites a stale anchor/node | ✅ PASS — `test_matrix_covers_every_anchor` fails on any stale ref; re-derived: none. |

---

## 6. Findings summary

| ID | Severity | Location | Finding | Proposed fix |
|---|---|---|---|---|
| S1 | should-fix | `TEST_MATRIX.md:3` vs `SPEC.md:1` | Provenance line pins "proven SPEC **v0.7.1**"; shipped SPEC is **v0.8.1**. Anchor set is still fully covered (mechanically re-proven), so risk is low, but the stale pin means a reader can't tell the matrix reflects current spec — violates "documents versioned like code / one home." | Update the derivation line to v0.8.1 (confirm no anchor delta — there is none) and bump the matrix's own `(v0.1 …)` header if re-derived. |
| S2 | should-fix | `TEST_MATRIX.md:69` (M-002, E-13) | Settings-ladder structural fact is deferred to a hand audit though it is documented at `skills/live-spec-base/SKILL.md:91-96` and string-testable today. | Add `test_settings_ladder_documented` asserting the base skill states the four-scope resolution order; keep the behavioral half TODO. Flip M-002 status to BUILT for the structural clause. |
| S3 | should-fix | `TEST_MATRIX.md:68` (M-001, E-12) | Owning test `test_skills_inherit_base_pin` asserts only the presence of the inherit pin, not the row's fact ("base states each rule once; no working skill restates normatively"). Row over-claims. | Either narrow the fact to "each working skill carries the base-inherit pin" (what is tested), or add a real check that no working skill restates a base rule normatively, and split the fact accordingly. |
| N1 | note | `TEST_MATRIX.md:195` | Checklist item 3 says each inventory entry "owns ≥1 rendered-level row"; the mechanism actually guarantees shipped-and-non-empty. Wording over-states. | Reword to "every inventory entry is asserted shipped-and-non-empty (`test_artifact_inventory`)". |
| N2 | note | rows M-007, M-012, M-050 | Never-side is a documentation proxy (rule written down), not a behavioral assertion — inherent to a text product, but a real limitation of the regression fence. | Record as a known limitation in the header; where cheap, strengthen (e.g. M-012 could assert no stray semver strings outside the named homes). |
| N3 | note | `VERSION` = `0.2.4` | The task states this audit gates **0.5.0**, but the shipped VERSION is 0.2.4 (next MINOR would be 0.3.0). Not a matrix defect — flag for Alexander so the target number is intentional. | Confirm the intended gate number before bumping. |
| N4 | note | `TEST_MATRIX.md:193` | "70/70 (E-16 added …, rows 52–53)" — "rows 52–53" are ROADMAP rows, ambiguous next to matrix-row language. | Clarify "(ROADMAP rows 52–53)". |

**Counts:** must-fix **0** · should-fix **3** · note **4**.

---

## 7. Verdict

**The matrix is READY to gate 0.5.0, conditional on the three should-fixes being folded (all are small, local edits).**

Rationale: the completeness backbone is not just asserted but mechanically re-proven every run — 70/70 anchors each
owned by exactly one row, no orphan/stale/contradictory ownership, every block matched to an architecture node, every
BUILT row naming a test that exists, the coverage checklist enforced by a git hook. The text-product level adaptation
is honestly reasoned and genuinely vacuous for the browser clause. The three should-fixes are quality/honesty gaps
(a stale version pin S1, one deferrable-but-testable fact S2, one over-claimed row S3), none of which breaks the
suite or hides an uncovered fact. No must-fix hole was found. S1 and S2 in particular should land before the 0.x.0
bump because the gate rule prizes exactly this: no fact testable-now left to a hand audit, and no document coasting
on a stale version. N3 (VERSION 0.2.4 vs the stated 0.5.0 target) is outside the matrix and needs Alexander's word.
