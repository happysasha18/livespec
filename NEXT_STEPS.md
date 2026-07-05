# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md)

## LIVE STATE (2026-07-05 ~14:00, session 4)
PUBLIC: github.com/happysasha18/live-spec (repo + clone dir renamed, remote URL updated, fetch verified —
row 40 fully closed). **VERSION 0.2.1 on disk; ROW 50 LANDED, commit local, PUSH HELD for Alexander's
look.** The flagship now walks its own pipeline: ARCHITECTURE.md v0.1 (12 nodes, 69/69 spec anchors owned
exactly once, every pin from a command run) · TEST_MATRIX.md v0.1 (64 rows node × fact, DO+NEVER each;
text-product level adaptation recorded in its header) · `tests/test_traceability.py` (20 tests GREEN, zero
skips — the coverage walk mechanized; it went red on real defects before green). Prover record
`docs/prover/2026-07-05-architecture.md`: 8 findings — S-0's target-row promise was broken for snapshot +
model router (→ new rows 55–56), stale D-4/D-5 "page is out" claims (→ SPEC v0.7.1), undated queue header
(fixed); installer + decision page want spec sentences (→ row 57). The record doubles as the push-gate
re-check for this state. INV-15 binds from this landing on.
Standing: one window = one project; **live-spec = Fable only**.

## Forward queue (mirrors ROADMAP.md; priority marks live there)
1. **Alexander's look at the row-50 landing → push** (gate record already green for this state).
2. Rows 52+53 design (personal layer → profile with nested/inherited scopes; CLAUDE.md → thin loader) ·
   row 54 onboarding step · row 51 mirrors + sync command.
3. Row 57 (installer + decision page get spec sentences) · fold remaining 9 mined gaps (row 12), next:
   gap 3 "fix the class, sweep look-alikes" · prover debts rows 30, 38 (38 likely folds into row 52).
4. Guardrails scaffold (row 3 — scope now incl. INV-15 teeth + generalizing tests/test_traceability.py
   into the pre-push hook) · snapshot machinery (row 55) · CI-mirror (row 14).
5. Deferred tail: model router (56, after 52–54) · feedback skill (47) → measurement plugins (48) → A/B
   (49) · learn-from-others (44, own bump) · track-coach formal adopt · skill-creator eval (row 5).
