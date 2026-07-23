# Register rewrite — live-spec-base (SKILL.md)

Register-only pass over `skills/live-spec-base/SKILL.md` (the pack rulebook: 34 numbered rules +
settings ladder). Rule numbers, INV/anchor codes, and frontmatter trigger semantics all preserved.
README.md was in the write set but read clean (three lines, no register issue); left untouched.

## Counts

- Contrast-by-denial (scissors) fixed: **22** (one further scissors could not be fixed — see pins).
- Metaphor / inflation / inverted-syntax fixed: **5 clusters** (monument-to-breaking; look-alike "is
  born"; "taken on trust never"; "the births are a closed set of two"; "the next phrase walked through
  untouched").
- Register-lint findings fixed: **1** — `en-full-rigor` at the `budget.pressure` default cell
  ("full — full rigor everywhere" → "full — every check runs at full strength").
- Cold-read rounds: **2** (initial stranger read + one confirming read; both by fresh zero-context
  subagents).

## Verification

- `scripts/preshow-register-lint.py skills/live-spec-base/SKILL.md` → **OK / exit 0**.
- Full scissors sweep (incl. cross-line) → only remaining hits are the two pinned/lawful cases below.
- `tests/test_traceability.py` → all base-touching assertions pass (207 passed across the base-touching
  files after the rule-32 restore). Repo has 4 pre-existing failures unrelated to this change
  (`test_craft_ladder`, `test_build_pipeline_bug_entry_drives_the_hunt` → build-pipeline;
  `test_skill_evals_present`, `test_real_repo_lists_complete` → the in-flight `text-audit` skill).
  None read base content I changed. Also pre-existing at full-suite level: test_config_health (2),
  test_made_with_attribution (2), test_readme_stance (2) — none read base.

## Pinned strings

### Changed then RESTORED (a pin the register fix could not keep)

- **Pinning file:** `tests/test_release_tier_rule.py` line 29 —
  `assert "stays a stated rule rather than a blocking check" in base`
- **OLD (restored, final state):** `...so it **stays a stated rule rather than a blocking check**, the
  same standing as a design-review finding that never blocks a lane [INV-141].`
- **NEW (attempted, then reverted):** `...so it **stays a stated rule the session holds**, the same
  standing as a design-review finding that never blocks a lane [INV-141].`
- **Why reverted:** the test pins the exact scissors phrase, so the register law's own guard test
  requires this contrast-by-denial wording to exist verbatim in the base. It cannot be fixed without
  editing `tests/`, which is out of the write set. The confirming cold read judged this line NON-blocking
  (the denial carries a positive anchor, "stays a stated rule"). Left as pinned.

### Reworded around a pin, pinned fragment kept verbatim

These sentences were reworded for register while keeping the exact pinned substring intact (verified
present in the final file):

- rule 14 — kept `escalate to the human when the class boundary needs his read`
  (pin: `tests/test_class_hunt.py`; `tests/test_traceability.py`). Reworded tail `rather than a guess`
  → `; the agent never guesses the boundary`.
- rule 29 — kept `re-tested by derivability every time it is touched`
  (pin: `tests/test_traceability.py`). Reworded tail `, not only when it is first written`
  → `, at its first writing and at every touch after`.
- rule 24 — kept `declared layers` (pin: `tests/test_traceability.py`) while replacing
  `instead of assuming code` → `never assuming a code layer`.
- rule 5 — kept `a worker's green is a lead the lead ACCEPTS by re-checking` (pin) while fixing the
  inverted tail `taken on trust never` → `; the lead never takes it on trust`.
- rule 31 — kept `named as a wrong referral` and the `check-*.py` script names while removing
  `rather than absorbed by the two-crossing cap`.

## Sentences LEFT UNCHANGED because rewriting risked meaning or a pin

1. **Rule 17 heading** — `Irreversible means gone, not merely public.` Pinned by regex
   (`^17\. \*\*Irreversible means gone, not merely public`) in `tests/test_traceability.py` and asserted
   in `test_spec_states_regression_fences`. Also lawful as a clarifying-scope contrast. Left verbatim.
2. **Rule 32** — `stays a stated rule rather than a blocking check` (see pins above). Left verbatim.
3. **Rule-of-thinking worked-failure example (lines 32–37)** — the initial cold read flagged the concrete
   "guard / register laws / probe" incident as opaque to a total outsider. Left as an internal domain
   example: it is a PACK-INTERNAL rulebook ("Reserve it for the pack's own work"), the register defect in
   it ("monument to breaking") was already removed, and its moral ("If the answer to a class is a list,
   the design is wrong") lands. Grounding "register laws"/"probe" for an outside stranger would bloat an
   internal doc — out of register scope.

## Cold-read findings addressed

- Initial cold read returned two BLOCKING items. Stop 11 (the internal worked-failure example) is the
  deliberate non-change above. Stop 26 (rule 7, line 100) was a contrast-by-denial buried in a run-on —
  `a convergence point the pen reconciles at integration, never an edge that serializes the lanes
  themselves` — and was fixed to `The shared living doc is a convergence point the pen reconciles at
  integration, so sharing it never forces the lanes to run one after another; co-location alone never
  pulls two rows into one lane`, split into two sentences.
- The remaining cold-read stops were pack-internal vocabulary (host, row, lane, pen, card, arm, tier)
  used before definition — legitimate for an internal rulebook, out of scope for a register pass.
- Confirming cold read: clean on both axes (no blocking sentence, no contrast-by-denial left without a
  positive statement); both flagged spots (line 100, line 439) read clean.
