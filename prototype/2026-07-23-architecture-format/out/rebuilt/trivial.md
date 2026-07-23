### [node: test-author]

**responsibility** — the test method's one home: derives TEST_MATRIX.md from the proven spec through the proven architecture and writes the tests — the level ladder, real-artifact assertions, red-first proof, the pinned skip-set, traceability as a standing test (row 163)

**owns** — E-27, INV-77, INV-78, INV-79, INV-80, INV-100, INV-102, INV-155, INV-157, INV-158, INV-160, INV-162, INV-204

**pins** — `skills/test-author/SKILL.md:1` (name + description), the level-ladder table and the two step sections in the same file; `templates/headless_harness.py:1` (the canonical hardened + muted harness template; shell-first resolution + launch frame probe; the cleanup-notice emitter at each reap); `guardrails/cleanup_notice.py:1` (the shared cleanup-notice shape, INV-204); `guardrails/check-cleanup-notice.sh:1` (the notice gate, INV-204)

**notes** — and the canonical browser test harness the pack ships once as a template, which a consumer adopts by updating and layers its own methods on (row 327, INV-157/158); the harness's process-group reap says what it ended through the shared cleanup-notice shape (row 417, INV-204)

### [node: design-reviewer]

**responsibility** — the design-review pass

**owns** — INV-141 (ROADMAP row 310), INV-142, INV-154, INV-156 (ROADMAP row 323; this node holds the class because it reached the one-class reading from the record-sibling seam it already owns (design review → record), the class declared once here and cited by product-prover and build-pipeline without restatement), INV-165, INV-169

**pins** — `skills/design-reviewer/SKILL.md:1` (frontmatter + when it fires), the similarity-lens, confidence-read, echo-channel, and record-discipline sections in the same file

### [node: publish]

**responsibility** — the publish-quality gate: per-kind publication checklist (its one home) + the target-plugin seam; runs before the human's gate, never instead (row 98)

**owns** — E-20, INV-44, INV-96, INV-119, INV-181, INV-228

**pins** — `skills/publish/SKILL.md:1` (frontmatter + when it fires), the kind-checklist table and target-plugin sections in the same file, the release-note shape with its optional offers section (INV-228: the release-note shape carries an optional offers section phrased as choices, and the publish walk records the offer-or-none decision, consuming the touchpoint-frame classification), `guardrails/check-release-note.py:1` (the release-note offer report-shape check, report-only, rides the suite not the push chain, INV-228), the mirror sync `scripts/sync-mirrors.sh:1` (banner · release history · attribution · language scan)

### [node: package-docs]

**responsibility** — live-spec's own host instance (dogfood): spec, queue, journal, resume file, version, records, dev-machine skill sync, its own problem ledger

**owns** — S-0, M-3, M-4, D-1, D-2, D-4, D-6, D-7, E-23

**pins** — `PRODUCT_SPEC.md:1`, `ROADMAP.md:15` (queue table), `JOURNAL.md:1`, `VERSION:1`, `scripts/sync-skills.sh:1` (E-23), `.live-spec/PROBLEMS.md:1` (E-24's dogfood instance; anchor owned by templates)

### [node: templates]

**responsibility** — the document shapes a host copies at bootstrap; the matrix's coverage checklist

**owns** — E-3, E-5, INV-6, B-1, E-24, INV-48, E-26

**pins** — `templates/TEST_MATRIX.template.md:43` (coverage validation), `templates/ROADMAP.template.md:1`, `templates/PRODUCT_SPEC.template.md:61` (index), `templates/PROBLEMS.template.md:1` (E-24 — the ledger's shape)

### [node: feedback-collector]

**responsibility** — the outbound feedback arm, the pack's third arrow: on a rare genuinely-strong reaction it offers, with the human's positive consent, to draft a distilled non-public upstream note to the pack's authors and deposit it in the gitignored `outbox/`, never sending — delivery the human's own step; off by default (the `feedback-upstream` flag); distinct from feedback-intake (the inverse arrow) and from the measurement family (ROADMAP row 321)

**owns** — E-30, T-21, INV-161, INV-179

**pins** — `skills/feedback-collector/SKILL.md:1` (frontmatter + when it fires), the offer / upstream-note / outbox sections in the same file

### [node: feedback-intake]

**responsibility** — the intake half of the exchange: receives anything handed back through three channels, routes each item to the home its law owns, keeps the feedback ledger's shape, echoes every arrival (row 47)

**owns** — E-28, T-20, INV-68

**pins** — `skills/feedback-intake/SKILL.md:1` (frontmatter + when it fires), the routing table and ledger-shape sections in the same file

### [node: onboarding-card]

**responsibility** — the settings card: a build-time renderer parsing the base's package-defaults table + the profile files into the card page per the frozen norm; shown at founding/adoption end and on the standing "what can I customize?" question (F-onboarding)

**owns** — INV-87, INV-88

**pins** — `scripts/onboarding-card.py:1` (renders the card), `docs/norms/onboarding-card-2026-07-10.html` (the frozen norm), trigger wiring: `adopt/ADOPT.md` (setup-end line) + `skills/communicator/SKILL.md` (standing-question line) — wiring pins, ownership stays here

### [node: snapshot] [target]

**responsibility** — saved baseline of the last accepted run; declared-scope diff (ROADMAP row 55)

**owns** — E-7, A-6

**pins** — — (spec'd; code still ahead)

### [node: design-sync]

**responsibility** — optional machine, [target: machine; wiring live] — declared components of a landing synced to the team's design project, human-gated (ROADMAP row 93; the machine's first real run remains)

**owns** — E-18

**pins** — wiring: `skills/live-spec-base/SKILL.md` (defaults table, `design-sync` row), `skills/communicator/SKILL.md` (rule 5 channel line), `skills/build-pipeline/SKILL.md` (step 9 sync line); machine: —

### [node: skill-evals]

**responsibility** — behaviour tests for the pack's own skills: per working skill one scenario, red proven bare, re-run at milestones (row 94)

**owns** — E-19

**pins** — `evals/README.md:1` (the method + honest boundary), `evals/` (one file per working skill), `tests/test_traceability.py` (`test_skill_evals_present`, self-closing over skills/)