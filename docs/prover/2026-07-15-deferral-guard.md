# Prover record — the deferral-marker mechanical net + delivery arm (INV-152 / base rule 29)

Prover: product-prover (unscoped, current lens set; references live-spec-base v1.0.17).
Date: 2026-07-15. Mode: adversarial whole-delta review of an uncommitted change.
Scope: the change described below, read against PRODUCT_SPEC.md, the base rulebook, TEST_MATRIX.md, the
guardrail scripts, the chat-law hook, and the conftest surface change. Nothing committed at review time.

## Verdict

**HOLDS-WITH-FIXES.** The design is sound and the mechanical arm is a genuine gain over discipline-only.
The suite is green (750/750), no anchor code was dropped in the build-pipeline offload (85 codes present on
both sides), and the spec clause and its formal-index row are mutually consistent. But the net has real
defects: it owes a TEST_MATRIX row by the pack's own precedent, its per-physical-line scan both **blocks
legitimate commits** and **lets genuine bare parks slip through** on hard-wrapped bullets (the dominant
NEXT_STEPS format), and it has no CI or suite backstop on the repo's own files. None break the suite; all
are fixable without redesign.

## Findings by severity

- Defects: 6
- Recommendations: 2

Ranked below, defects first.

---

### F1 — The per-physical-line scan fails OPEN: a genuine bare park slips through when signal or reason wraps

> `for n, raw in enumerate(f, 1): ... if scan_line(line):` — check-deferral-marker.py, scan_file

The gate reads one physical line at a time. Two real leaks follow, both reproduced against a fixture:

- **Wrapped signal → false PASS.** A park whose signal phrase straddles the line break is missed entirely,
  because a signal like `reserved for his` / `held for his` needs both words on one physical line.
  Repro: `the decision is held for\n  his word on the layout.` → exit 0 (not flagged). A genuine park
  reaches the tree uncaught.
- **Reason-elsewhere-on-line → false PASS.** `REASON_RE.search(line)` scans the whole line, so a reason
  word about a *different* item silences a bare park sharing the line. Repro:
  `the crop is a taste call (already done); but the export path is still his.` → exit 0. The parked item
  (`export path is still his`) names no reason of its own; the incidental `taste` about the crop passes it.

This is the worst class because the net's whole job is to CATCH bare parks, and it fails open. tlvphotos's
NEXT_STEPS.md carries 76 continuation lines, so hard-wrapping is the norm, not the exception, for exactly
the files this gate scans.

Rework `scan_file` to fold each logical bullet into one string (join a bullet line with its indented
continuation lines before `scan_line`), then scan the joined unit. Scope the reason check to the parked
item's own clause rather than the whole joined line if the reason-bleed matters after folding.

`defect · missing-scenario (state-space)`

---

### F2 — The same per-line scan fails CLOSED: a legitimate reasoned park on a wrapped bullet is red-flagged

> `window = line[max(0, start - 9):start]` and the per-line `scan_line` — check-deferral-marker.py

When the reason sits on the continuation line of a hard-wrapped bullet, the signal line names no reason and
is flagged. Repro: `the threshold is still his to correct;\n  it is a taste call about brightness.` → the
first line is flagged, exit 1, though the bullet plainly names its reason one line down. The gate blocks a
correct commit. It fails safe (a human sees the red and can act), but on the dominant wrapped-bullet format
it will fire spuriously and train the human to `--no-verify`, which then also disarms the fence gate that
shares the same hook.

Same root cause and same fix as F1 — fold logical bullets before scanning. Listing F1 and F2 separately
because they are opposite failure directions (open vs closed) of one mechanism.

`defect · missing-scenario (state-space)`

---

### F3 — The matrix owes a row for the new net and the delivery arm; M-297 was not updated

> `test_deferral_clause_stands + test_lives_in_the_base_rulebook + test_base_description_counts_the_rule + test_inv152_index_and_ownership` — TEST_MATRIX.md, M-297 (the INV-152 row), unchanged by this delta

The change adds a whole guardrail script (`check-deferral-marker.py`), its test
(`test_deferral_marker.py`), and a hook-delivery test (`test_output_carries_the_deferral_law`). None appear
anywhere in TEST_MATRIX.md (`grep -c` returns 0), and M-297's test column still names only the four
string-clause tests. The spec clause and index row now assert **"enforcement two arms"** including the
mechanical net, but the matrix row that owns INV-152 describes discipline only — the traceability from
INV-152 to its mechanical enforcement is absent.

This breaks the pack's own precedent, which is uniform:
- INV-155 retry gate → M-301 names `test_no_retry_plugin`.
- INV-24 clock → M-106/M-110 (`check-future-times` run by deed) and M-132 gives the clock-hook script its
  own row (exists · executable · output carries the law) — the exact shape the new chat-law deferral line
  and guardrail owe.
- INV-120 → M-260 names `check-shipped-language.sh` and its tests.

Not suite-red (no test enumerates guardrail scripts against matrix rows, and `check-matrix-coverage.sh`
only checks the coverage-validation checkboxes), so it lands as a discipline gap the MINOR-bump matrix audit
would catch — but it is a gap: the change added a mechanical arm and left its owning matrix row untouched.

Update M-297 to name `test_deferral_marker.py` and the guardrail script, and add a hook-script row for the
chat-law deferral line modeled on M-132 (script exists · executable · output carries the law needles the
new `test_output_carries_the_deferral_law` already asserts).

`defect · missing-outcome-check (postcondition)`

---

### F4 — The net has no CI or suite backstop on the repo's own files; it is bypassable and weaker than its cited precedent

> `if [ -f "$REPO_ROOT/guardrails/check-deferral-marker.py" ]; then ... python3 ... || exit 1` — guardrails/pre-commit

`check-deferral-marker.py` is wired only into `pre-commit`. The CI mirror (`.github/workflows/gates.yml`,
M-154) mirrors the pre-**push** gates, not pre-commit, so the net never runs in CI. And
`test_deferral_marker.py` exercises only tempfile fixtures — nothing runs the gate against the repo's real
NEXT_STEPS.md or docs/decisions. Compare the precedent the change cites: the clock law has BOTH a suite test
on the real tree (M-106, `test_no_future_dated_stamps`) AND the pre-commit fence — a bare future stamp is
caught in CI regardless of the local hook. The deferral net has neither backstop.

Consequence: an author committing with `--no-verify`, or from a machine without the hook installed, lands a
bare park and CI stays green — while the spec, README, and rule 29 all now CLAIM mechanical enforcement
("reds a commit"). That is short of the pack's own bar (M-054: "never a claim of mechanical enforcement
beyond what is actually wired").

Add a suite test that runs `check-deferral-marker.py` against the repo's real NEXT_STEPS.md and
docs/decisions/*.md (asserting green on the swept tree, the shape of `test_gate_green_on_the_swept_tree` for
INV-120), so CI carries the net even where the local hook is skipped. Optionally also wire it into the
pre-push gate.

`defect · unenforceable-promise (discharge)`

---

### F5 — Base rule 29 calls both arms "mechanical"; the delivery arm is a reminder that cannot block

> "Two mechanical arms hold this rule the way INV-155's retry-plugin grep holds the green definition" — skills/live-spec-base/SKILL.md, rule 29

The spec clause carefully distinguishes "a mechanical net ... and a delivery arm." Rule 29 collapses that
into "Two **mechanical** arms." The second arm — the chat-law hook's deferral line — only prints a reminder;
it blocks nothing. The pack's own principle is that chat cannot be machine-gated, and INV-150's net taxonomy
separates a mechanical gate from a reminder-class delivery. Calling the reminder "mechanical" is a category
error and overclaims enforcement: a reader of rule 29 believes both arms hold the line mechanically, when
only the commit gate does. The INV-155 analogy compounds it — the retry-plugin grep is a single mechanical
gate, unlike the delivery arm being compared to it.

Reword rule 29 to match the spec clause: one mechanical arm (the commit gate) and one delivery arm (the
reminder at the marker/AskUserQuestion moment), and reserve the INV-155-grep analogy for the mechanical arm.

`defect · internal-conflict (consistency)`

---

### F6 — The negation window (9 chars) misses a negation set a few words before the signal

> `window = line[max(0, start - 9):start]; return bool(NEGATORS.search(window))` — check-deferral-marker.py, negated()

The negation guard only looks 9 characters back. A negated park with any filler between the negator and the
signal is wrongly flagged. Repro: `these items are not currently owner-reserved, ship them.` → flagged,
exit 1, though the line explicitly NEGATES the marker. Nine characters holds "not " + one short word at most;
"not currently", "never really", "is not yet" all overshoot it. This fails closed (a false block), so it is
less damaging than F1, but it is the same family of brittleness as F1/F2 and will bite on natural phrasing.

Widen the negation look-back to a token window (e.g. the 3–4 words preceding the signal, or a regex that
allows a small run of words between a negator and the signal) rather than a fixed character count. Note the
symmetric risk this trades against — too wide a window lets an incidental negator silence a real park (a
false pass) — so bound it to a couple of words and test both directions.

`defect · missing-prerequisite (precondition)`

---

### R1 — The heading skip does not cover fenced code or HTML comments

> `if line.lstrip().startswith("#"): continue` — check-deferral-marker.py, scan_file

Only lines whose lstrip starts with `#` are skipped as headings. A park phrase quoted inside a fenced code
block or an HTML comment in NEXT_STEPS.md would still be scanned and could flag. Low likelihood in practice,
but if the gate is meant to read only work items, track fenced-block state and skip inside it. Nothing here
blocks; a quality gain on offer.

`recommendation · later · boundary-issue (composition)`

---

### R2 — Default-target scan is NEXT_STEPS-only, so the decision-page arm depends entirely on the caller

> `default = os.path.join(os.getcwd(), "NEXT_STEPS.md")` — check-deferral-marker.py, main

Run with no arguments the gate scans only ./NEXT_STEPS.md; the docs/decisions/*.md coverage the README and
spec both advertise lives only in the pre-commit's explicit target list. That is fine as wired, but it means
a human running the script by hand to check a decision page gets no coverage unless they know to pass the
path. Consider globbing docs/decisions/*.md into the default set so the standalone tool matches its
advertised scope. Non-blocking.

`recommendation · later · boundary-issue (composition)`

---

## What held up well (checked, no finding)

- **Anchor ownership after the offload.** Every INV/M/T/E/ACT code present in the pre-delta
  build-pipeline SKILL.md is still present in the new surface (SKILL.md + references/*.md): 85 codes both
  sides, empty `comm -23`. No pointer dropped a code. The conftest `read_all` change correctly makes the
  content-presence tests read the whole skill surface, and the traceability suite is green.
- **The conftest read_all change does not inflate a size test.** The size/thinness checks
  (test_compaction_discipline and peers) read via `read()`/`read_flat` (SKILL.md alone, now 499 lines);
  only content-presence tests were repointed to `read_all`. read_all concatenates references, so it cannot
  mask a "content left the skill entirely" regression for an anchor that is still somewhere in the surface —
  the intended semantics (one skill = one home).
- **Spec clause ↔ formal-index row.** Internally consistent: both state the two arms, name the guardrail by
  path, and pin the delivery arm to INV-28. No claim in one that is absent from the other. (The only
  cross-document mismatch is F5, between rule 29 and the spec clause.)
- **Real-world false-positive rate is effectively zero on the sampled corpus.** The gate produced one
  finding on ~/tlvphotos/NEXT_STEPS.md (line 73, "that one flip is his to call" — a real bare park that
  names no reason, a true-ish positive) and clean exits on ~/.claude/skills/track-coach/NEXT_STEPS.md and
  ~/live-spec/NEXT_STEPS.md. The F1/F2/F4/F6 defects are latent on these exact files (no wrapped-reason or
  far-negation bullet happened to occur), not observed — but the 76 continuation lines in tlvphotos's file
  make them live risks the first time such a bullet is written.
- **Negation and quote guards hold for the common cases.** Prose "he gave his word" (bare "his word",
  excluded by design), a signal inside «guillemets» (narration), and a close-range "NOT owner-reserved" all
  pass untouched.
- **Suite:** `python3 -m pytest -q tests` → 750 passed.

## Top 3 to fix before this lands

1. F1/F2 — fold logical bullets before scanning, so the net stops failing open on wrapped signals/reasons
   and failing closed on wrapped reasons (the dominant NEXT_STEPS format).
2. F3 — update M-297 and add a hook-script matrix row, so INV-152's mechanical arms are traceable by the
   pack's own precedent.
3. F4 — add a suite/CI backstop that runs the gate against the real files, so the "reds a commit" claim is
   actually wired end-to-end.

## Properties the change should state explicitly

- The gate reads a NEXT_STEPS/decision file as a list of logical WORK ITEMS (bullet + its continuation
  lines), not as physical lines; a signal and its reason are evaluated within one item.
- Every mechanical arm of INV-152 has a TEST_MATRIX row naming its script and test.
- The deferral net runs in CI on the repo's own files, not only in the local pre-commit hook.

Overall readiness: needs another iteration — the enforcement mechanism is right in shape but leaks on the
real file format and is not yet traced or backstopped to the pack's standard.
