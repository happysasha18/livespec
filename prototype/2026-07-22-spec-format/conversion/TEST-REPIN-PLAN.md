# Test re-pin plan — row 445 stage 3 preparation

This plan inventories every suite test that reads `PRODUCT_SPEC.md` content, classifies
each as a content-reader (pins specific wording, needs re-pinning once the document
converts) or a shape-reader (parses generic structure, governed by the stage-1 format
gates already planned in `delta/gates-plan.md`), and for every content-reader states
which of the nine conversion units' `mapping.md` covers its pinned code and sentence.
Read-only audit; no test was edited and the suite was not run.

Method: every `tests/*.py`, `evals/*.md`, and `guardrails/*` file that references
`PRODUCT_SPEC.md` was read in full (134 test files, 2 eval files, 9 guardrail scripts).
For each content-pinning test, the Formal-index code(s) it cites were looked up against
a table built from all nine units' mapping.md files (`code → unit`), then the pinned
sentence's actual presence was spot-checked in the target unit's `section.md` — a code
appearing in a unit's citation list is not proof the unit restates that code's specific
sentence, since a unit can cite a code purely as a cross-reference without repeating its
rule. Every finding below reflects a direct read of the source lines, not the lookup
table alone.

---

## UNMAPPED PINS — read this section first

### Finding 1: a whole essay is missing from the census's nine units

The nine conversion units cover the document's eight `##` sections outside `## Reference`
(body lines 1–1162 and 1440–2026). Two ranges carry real normative prose neither unit
has touched:

- **`## Starting and adopting a project`** (body lines 1163–1439) — a full top-level
  section, already known and named in `section_ranges` reasoning; no unit converts it.
- **`### Composing across axes`** (body lines 2031–2092), physically inside
  `## Reference` — this was NOT expected going in. The Reference section was assumed to
  be table rows only (the Formal index), but this subsection is a dense prose essay
  stating several cross-cutting laws in full. Some of its codes are dual-homed — the
  same rule is also stated properly inside a converted unit's body (confirmed for
  INV-132, INV-146, INV-208, INV-213, each with a real requirement in `bounds/section.md`
  quoted below). Others are **single-homed here only** — no converted unit's `section.md`
  restates them at all, confirmed by direct grep of all nine `section.md` files finding
  zero matches for the pinned sentence:

  | Code | Pinned sentence (test) | Test file |
  |---|---|---|
  | INV-127 | "Each scenario states how it is entered and how it exits." | `tests/test_scenario_entry_exit.py` |
  | INV-138 (the gated-behaviour/viewport-quantifier clause specifically — a different INV-138 sentence is properly covered, see below) | "A gated behaviour names every side of its gate... pending, arrived, and failed... every layout guarantee names its viewport quantifier" | `tests/test_edge_completeness.py` |
  | INV-126 | "Both directions of a paired state change get the same craft... same magnitude as the forward move" | `tests/test_paired_transition.py` |
  | INV-163 (the root discriminator sentence — member codes it cites ARE covered, see below) | "can the pack ship a single identical body..." | `tests/test_pack_to_host_split.py` |
  | INV-180 | "The pack's authored artifacts and their installed copies are one class..." | `tests/test_installed_copy_staleness_class.py` |
  | INV-244 | "A surface's composition axes are the set its project's kind owes" | `tests/test_composition_axes.py` |
  | INV-248 | "A declared composition axis that adds runtime code names whether its delivered artifact divides along that axis or ships whole" | `tests/test_delivery_separability.py` |

  **Recommendation:** treat `### Composing across axes` as a tenth conversion unit,
  scoped narrowly (lines 2031–2092), before re-pinning the seven tests above — they have
  nowhere to be re-pinned to today. This is a genuine hole in the stage-2 census, not a
  drop caused by any unit's own work.

### Finding 2: `code_to_unit.tsv` build gap (self-caught, fixed mid-task)

The lookup table this audit built from the nine mapping.md files initially had **zero
rows for the `agents-together` unit** — its `mapping.md` numbers its parts `## 1.` / `## 2.`
/ `## 3.` rather than the `## Part 1` / `## Part 2` / `## Part 3` heading the other eight
units use, so the extraction script's pattern silently skipped it. Fixed during this
audit (77 codes added). Any code shown below as "covered by agents-together" was
confirmed by direct reading of that unit's `mapping.md`, not the (now-fixed) table alone.

### Softer check-me items (not proven drops — flagged for a second look)

| Test | Code | Concern |
|---|---|---|
| `tests/test_design_principles.py` | INV-136 | The pinned interactive-overlap sentence was not found restated in `build-loop-b-doors-spec-lanes` despite the code being cited there; may actually belong to the unconverted "Starting and adopting a project" founding-questions material. |
| `tests/test_release_tier_rule.py` | INV-217 | Maps to `rules-and-who-applies` R18, but R18 states a different rule (fresh-seat/no-self-certification) and only cites INV-217 in passing; the release-tier substance itself has no Part-3 claim in that unit. |
| `tests/test_restructure_merge_gate.py` | INV-114 | Delta-scoped merge-gate substance is covered, but the specific duty "says the sharpened form back and marks it as its own interpretation" was not found in either covering unit. |
| `tests/test_review_record_class.py` | INV-156 family | Behaviour is covered (`build-loop-b` R32), but the literal record-home paths `docs/design-review/` and `docs/audit/` do not reappear in any converted text (only `docs/prover/` survives, in an unrelated requirement). |
| `tests/test_skill_review.py` | INV-208 | Behaviour covered (`bounds` R22), but the literal strings `check-skill-review.sh` and `docs/skill-review` are absent from the converted unit's text. |
| `tests/test_traceability.py::TestPackUpdateCheck.test_spec_states_update_check` | E-25 | Pins update-check mechanics whose prose lives at lines 1313–1436 (the unconverted founding section), even though E-25 nominally resolves to `agents-together` for an unrelated mention (the session-start regeneration watcher). Treat this one method as out-of-scope, not the whole file. |

None of the six items above is a hard "dangerous" drop the way Finding 1's seven codes
are — each has partial or ambiguous coverage rather than zero coverage — but each is
worth a human glance before its test is re-pinned mechanically.

---

## Reconciliation against the census (NEXT_STEPS: "32 shape-readers (17 tests + 15 gates)
## must be rebuilt... ~99 content-reader tests")

**Found:** 134 test files under `tests/` read `PRODUCT_SPEC.md` (plus 2 `evals/*.md` files
that only name it inside a fictional scenario prompt — not real pins, excluded — and 9
`guardrails/*.py`/`*.sh` scripts that read it directly, all pure mechanism).

Per-file verdict tally from reading all 134 files in full:

| Verdict | Count | Meaning |
|---|---|---|
| CONTENT-READER | 79 | the file's assertions are substantially wording pins |
| MIXED | 40 | most of the file drives a gate/mechanism against fixtures, but it also carries one or more real sentence pins against `PRODUCT_SPEC.md` |
| SHAPE-READER | 12 | every assertion against `PRODUCT_SPEC.md` is structural (headings, table rows, byte counts, code/filename presence) — no wording is pinned |
| N/A | 3 | the file never actually reads the real root `PRODUCT_SPEC.md` (fixture-only, or a synthetic tool-call payload string) |

**Reconciliation:**

- **Shape side.** Census said 17. This audit's strict pure-shape count is 12
  (`test_collector_anonymization.py` [only its PRODUCT_SPEC.md touch], `test_convergence_locks.py`,
  `test_derived_doc_header_policy.py`, `test_formal_index.py`, `test_guardrails.py`,
  `test_judge_listed.py`, `test_listener_tripwire.py`, `test_mirror_release_history.py`
  [PRODUCT_SPEC.md touch only], `test_muted_launch_guardrail.py` [PRODUCT_SPEC.md touch
  only], `test_onboarding_card.py`, `test_read_grant.py`, `test_reap_owned_group.py`),
  plus 3 N/A files that arguably belong in the same "no re-pin needed" bucket
  (`test_conduct_judge.py`, `test_requirement_shape.py`, `test_scaffold_guardrails.py`) —
  15 together. The remaining gap against 17 is most likely the census's original
  quick-count folding in one or two of the 40 MIXED files on the shape side of a binary
  split; this audit did not find two further files with zero content-pin risk.
  On the gate side, the census's 15 lines up with `delta/gates-plan.md`'s Areas 1–6
  script list (`check-requirement-shape.py`, `check-vocabulary.py`, `check-one-name.py`,
  `check-weak-words.py`, `check-style.py`, `check-gap-lines.py`, `check-no-history.py`,
  `build-index.py`, `check-index-generated.py`, `check-delta-record.py`,
  `check-size-ratchet.py`, `comprehension-gate.py`, `gatelib.py`, `check-gate-reach.py` —
  14 named there, close enough to 15 to treat as already governed and not re-derived
  here, per the task's own framing.
- **Content side.** Census said ~99. This audit's CONTENT-READER-only count is 79
  (lower than 99); CONTENT-READER + MIXED (every file carrying at least one real
  wording pin, even alongside heavy gate-mechanism testing) is 119 (higher than 99).
  The true "needs re-pinning" count sits between these two readings depending on how
  strictly a MIXED file's thin content tail counts — the honest number is **a range of
  79–119, with 99 a reasonable midpoint**, not a number this audit can collapse to one
  integer without a policy call on MIXED files. Practically: every one of the 119
  should get a pass at re-pin time, since even a MIXED file's one or two content
  assertions will break on reword; the 79 pure ones need a fuller line-by-line rewrite.
- The 3 N/A files, and the two `evals/*.md` files, need no action at all — they never
  pin the real document's wording.

---

## Content-readers, grouped by covering conversion unit

Each row: test file — primary pinned code(s) — one-line coverage note. "Clean" means the
pinned sentence's substance was confirmed present in that unit's `section.md`/`mapping.md`
Part 3 by direct check (by this audit or by the batch that read the file). Files already
listed in the UNMAPPED PINS or check-me tables above are not repeated here except by
filename for completeness.

### what-live-spec-is (body lines 1–47)

Small unit; no content-reader test in the audited set resolved here as primary home
beyond cross-references already counted under other units.

### build-loop-a-intake (body lines 48–276)

| Test | Code(s) | Note |
|---|---|---|
| `test_derive_before_fork.py` | INV-121 | clean |
| `test_detached_work_visibility.py` | INV-35 | clean |
| `test_no_self_certification.py` | INV-94 | clean |
| `test_no_silent_drop.py` | INV-109 | clean |
| `test_leave_command.py` | INV-95 | clean |
| `test_report_estimates.py` | INV-93 | clean |
| `test_founding_layers_proofs.py`* | INV-135 | *actually OUT-OF-SCOPE — see below |
| `test_stranger_door.py`, `test_stranger_echo.py` | INV-146, INV-147, INV-27 | clean, dual-homed with `bounds` |
| `test_impact_analysis_entry.py` | INV-128 (+ INV-121 cross-ref) | clean |
| `test_register_judge.py` (partial) | INV-83, INV-94 | clean |

### build-loop-b-doors-spec-lanes (body lines 277–620)

| Test | Code(s) | Note |
|---|---|---|
| `test_design_reviewer.py` | INV-141, INV-142, INV-154 | clean |
| `test_docs_layout_vehicle.py`* | INV-111 | see build-loop-c below (dual home) |
| `test_entry_state_lens.py` | INV-167 | clean |
| `test_finding_kind.py` | INV-140 | clean |
| `test_footprint_note.py` | INV-134 | clean |
| `test_forward_binding_and_infra_class.py` | INV-159, INV-160 | clean |
| `test_full_pass_coverage_record.py` | INV-171 | clean |
| `test_gesture_overlay_parity.py` | INV-165 | clean |
| `test_impersonal_shipped_docs.py`* | INV-118 | dual home, see build-loop-c |
| `test_critical_preempt_bound.py` | INV-133 | clean |
| `test_cross_surface_policy.py` | INV-125 | clean |
| `test_crosslink_quantifier_reverify.py` | INV-170 | clean |
| `test_declared_laws.py` | INV-101, INV-150 | clean, but see NOTE below |
| `test_deferred_revisit_cadence.py` | INV-129 | clean, confirmed at body lines 603–609 |
| `test_delegation_line.py` | INV-103 | clean (paraphrase match) |
| `test_instance_enumeration_keying.py` | INV-226, INV-138 (enumeration-keying sentence, distinct from the gated-behaviour sentence in Finding 1), INV-41, INV-18 | clean |
| `test_lane_branch_road.py` | E-34, T-23, INV-198..201, INV-214, INV-105 | clean |
| `test_legibility_floor.py` | INV-139 | clean |
| `test_milestone_enumerates_design_review.py` | INV-141 | clean |
| `test_orchestrator_read_discipline.py` | INV-137 | clean |
| `test_pen_tiebreak_identity.py` | INV-117 | clean |
| `test_redoor_independence_rebuild.py` | INV-131, INV-49 | clean |
| `test_request_classifier.py` | INV-151, INV-153 (+ INV-150/189/191/104) | clean |
| `test_resume_rederive.py` | INV-247, INV-129 | clean |
| `test_scenario_entry_exit.py` | INV-127 | **UNMAPPED — see Finding 1** |
| `test_second_sibling_intake.py` | INV-169 | clean |
| `test_skill_kind_review.py` | INV-99 | clean |
| `test_spec_is_definition_of_correct.py` | INV-144 | clean |
| `test_traffic_transport.py` | INV-183 (+ INV-236 agents-together) | clean |
| `test_transition_payload_lens.py` | INV-168, INV-165, INV-167 | clean |
| `test_voiced_fix_tripwire.py` | INV-104 | clean, body line 313 |
| `test_founding_set_version.py`* | — | actually OUT-OF-SCOPE, see below |
| `test_seat_acts_by_default.py`* | INV-143 | actually `rules-and-who-applies`, see there |
| `test_withdrawal_convergence.py` | INV-130 (+ INV-59 wider) | clean |
| `test_composition_axes.py` | INV-244 | **UNMAPPED — see Finding 1** |
| `test_paired_transition.py` (partial: INV-138 viewport facet) | INV-138 | clean for this facet; INV-126 core is unmapped, see Finding 1 |
| `test_pack_to_host_split.py` (partial: member codes) | INV-125, INV-136, INV-139, INV-158, E-26, INV-159 | clean for member codes; INV-163 root sentence unmapped, see Finding 1 |
| `test_instance_engine_boundary.py`* | INV-119 | actually OUT-OF-SCOPE, see below |

### build-loop-c-prototype-tests-rhythm-publish (body lines 621–927)

| Test | Code(s) | Note |
|---|---|---|
| `test_architecture_proved_at_full_pass.py` | INV-116 | clean |
| `test_architecture_redesign_owes_rework.py` | INV-113 | clean |
| `test_catchup_discriminator.py` | INV-110 | clean |
| `test_checkpoint_closes.py` | INV-107 | clean |
| `test_ci_verdict.py` | INV-106 | clean |
| `test_class_hunt.py` | INV-124 | clean, primary home (also `when-something-breaks`) |
| `test_code_compaction_station.py` | INV-123, INV-122 | clean |
| `test_compaction_discipline.py` | INV-115, INV-164 | clean |
| `test_docs_layout_vehicle.py` | INV-111 | clean |
| `test_enumeration_reads_as_list.py` | INV-215 | clean |
| `test_flaky_test_is_a_defect.py` | INV-155 | clean |
| `test_impersonal_shipped_docs.py` | INV-118 | clean |
| `test_made_with_attribution.py` | INV-96 | clean |
| `test_mirror_assertion_ban.py` | INV-102 | clean |
| `test_mirror_release_history.py` (banner test only) | INV-181 | clean |
| `test_no_dramatization_law.py` | INV-221 (+ INV-203, INV-173) | clean |
| `test_suite_hygiene.py` | INV-100 | clean |
| `test_vacuous_pass.py` (thin) | INV-218 | clean |
| `test_harness_template.py` (2 methods) | INV-155, INV-157, INV-158 | clean |

### what-the-human-sends-back (body lines 928–1055)

| Test | Code(s) | Note |
|---|---|---|
| `test_feedback_collector.py` | E-30, T-21, INV-161 | clean |
| `test_behavioural_break_one_home.py` (one home) | INV-108 | clean |
| `test_deposit_description.py`, `test_description_field.py` (content class), `test_inbox_deposit_protocol.py` | INV-239, E-35, INV-249 | clean — confirmed directly against `agents-together` (see Finding 2 tsv gap); NOTE these actually belong to **agents-together**, not what-the-human-sends-back — corrected placement below |
| `test_collector_anonymization.py` (thin) | INV-179 | clean |

### when-something-breaks (body lines 1056–1162)

| Test | Code(s) | Note |
|---|---|---|
| `test_class_hunt.py` (dual) | INV-124 | clean, primary home |
| `test_flaky_test_is_a_defect.py` (dual) | INV-155 | clean |

### agents-together (body lines 1440–1616) — recall: missing from the tsv until fixed mid-audit

| Test | Code(s) | Note |
|---|---|---|
| `test_agent_channels.py` | E-31, INV-182/183/236/188-197/153/225/146/130 (24 codes) | clean — largest content file in the census, ~100+ pinned sentences, all confirmed present |
| `test_agent_card_gate.py` | INV-219, INV-184 | clean |
| `test_deposit_description.py` | INV-239, M-422 | clean |
| `test_description_field.py` (`TestDescriptionFieldTraceability` class only) | INV-239, E-35 | clean; rest of file is a shape-reader driving the real gate script |
| `test_inbox_deposit_protocol.py` | INV-249 (+ INV-247 cross-ref) | clean |
| `test_named_reference.py` (partial) | INV-240, T-24, E-35 | clean |
| `test_traffic_transport.py` (partial) | INV-236 | clean |

### rules-and-who-applies (body lines 1617–1842)

| Test | Code(s) | Note |
|---|---|---|
| `test_expensive_decision_read.py` | INV-235 | clean |
| `test_clean_context_review.py` | INV-237 | clean |
| `test_seat_acts_by_default.py` | INV-143 | clean, body line 1768 |
| `test_minor_gate_reconciliations.py` (partial: `test_d1`/`test_d2`) | INV-137, INV-53 | clean |
| `test_delegation_line.py` (dual) | INV-103 | clean |
| `test_orchestrator_read_discipline.py` (dual) | INV-137 | clean |

### bounds (body lines 1843–2026)

| Test | Code(s) | Note |
|---|---|---|
| `test_answer_first_arm.py` (thin) | INV-220 | clean |
| `test_authority_anchor.py` (thin) | INV-207 | clean |
| `test_board.py` (thin) | INV-206, INV-229 | clean |
| `test_broad_kill_guardrail.py` | INV-162 | clean |
| `test_canonical_state_dir.py` | INV-105 | clean |
| `test_ci_mirror.py` (thin) | INV-210 | clean |
| `test_cleanup_notice.py` (thin) | INV-204 | clean |
| `test_config_health.py` (thin) | INV-216 | clean |
| `test_convergence_rule.py` | INV-98 | clean |
| `test_doc_bound.py` (thin), `test_doc_rotation.py` (thin) | INV-234, INV-209 | clean |
| `test_every_gate_can_fail.py` (thin) | INV-212 | clean |
| `test_far_tier.py` | INV-222, INV-223 | clean, multiply covered |
| `test_four_checks_contract.py` | INV-97 | clean |
| `test_hedge_arm.py` (thin) | INV-238 | clean |
| `test_inbox_remote_arm.py` | INV-112 | clean |
| `test_installed_copy_staleness_class.py` | INV-180 | **UNMAPPED — see Finding 1** |
| `test_judge_listed.py` (thin) | INV-211 | clean |
| `test_lean_orchestrator_arm.py` (thin) | INV-246 | clean |
| `test_live_channel_law.py` | INV-108 | clean |
| `test_local_inbox_deposit.py` | INV-174 | clean |
| `test_muted_launch_guardrail.py` (thin) | INV-157 | clean |
| `test_net_meter.py` (thin) | INV-202 | clean |
| `test_node_fitness_test.py` | INV-122 | clean |
| `test_node_growth.py` (thin) | INV-233 | clean |
| `test_reap_owned_group.py` (thin), `test_read_grant.py` (thin) | INV-230, INV-232 | clean |
| `test_release_note.py` (thin) | INV-228 | clean |
| `test_retroactive_gate.py` | INV-176 | clean |
| `test_review_record_class.py` | INV-156, INV-140/141/145/46 | clean substance, path literals check-me (see above) |
| `test_runaway_child.py` (thin) | INV-213 | clean |
| `test_skill_review.py` | INV-208 | clean substance, path literals check-me (see above) |
| `test_touchpoint_kind.py` (thin) | INV-205 | clean |
| `test_update_watcher.py` (thin) | INV-177 | clean |
| `test_version_is_one_fact.py` (thin) | INV-178 | clean |
| `test_preshow_register_lint.py` (thin) | INV-83 | clean |

### Corrected placements (were listed under the wrong unit by first-pass code lookup, corrected by direct read)

- `test_deposit_description.py`, `test_description_field.py` (content class), `test_inbox_deposit_protocol.py`, `test_named_reference.py` (partial), `test_agent_card_gate.py`, `test_agent_channels.py`, `test_traffic_transport.py` (partial) → **agents-together**, not `what-the-human-sends-back` — corrected in the agents-together table above; listed once there.

### Out-of-scope (Starting and adopting a project, body lines 1163–1439) — expected gap, not dangerous

| Test | Code(s) |
|---|---|
| `test_founding_layers_proofs.py` | INV-135 (tsv lists a converted unit citing it, but only as cross-reference — the founding-declares-layers-and-proofs substance is unconverted) |
| `test_founding_set_version.py` | INV-227 |
| `test_instance_engine_boundary.py` | INV-119 |
| `test_design_principles.py` | INV-136 (see check-me above — may belong here) |
| `test_catchup_walk.py` (partial — most of this file drives MIGRATION.md, out of this rewrite's scope entirely) | A-11, INV-89/90/91/92, F-catchup |
| `test_traceability.py` (partial — 8 of ~140 codes) | A-0, A-1, A-2, A-4, A-5, A-9, E-21, INV-8 |

### Out-of-scope (## Reference / Composing across axes, body lines 2027–2350ish) — see Finding 1

`test_scenario_entry_exit.py` (INV-127), `test_composition_axes.py` (INV-244),
`test_delivery_separability.py` (INV-248), `test_installed_copy_staleness_class.py`
(INV-180), `test_pack_to_host_split.py` (INV-163 root sentence only),
`test_paired_transition.py` (INV-126 core law only), `test_edge_completeness.py`
(INV-138 gated-behaviour sentence only), plus `test_traceability.py`'s D-3/INV-244
instances and its one `TestPackUpdateCheck` method noted in the check-me table.

---

## Shape-readers (pure — no wording pinned, unaffected by the rewrite)

`test_collector_anonymization.py` (PRODUCT_SPEC.md touch only — its content pins target
`skills/feedback-collector/SKILL.md`), `test_convergence_locks.py`,
`test_derived_doc_header_policy.py` (never actually reads PRODUCT_SPEC.md — docstring
mention only), `test_formal_index.py`, `test_guardrails.py` (drives real guardrail
scripts against fixtures; its one register-lint touch on the real spec is a generic
structural sweep), `test_judge_listed.py` (PRODUCT_SPEC.md touch is code/filename
presence only), `test_listener_tripwire.py`, `test_mirror_release_history.py`
(PRODUCT_SPEC.md touch is code/filename presence only, aside from the one banner
content test moved to build-loop-c above), `test_muted_launch_guardrail.py`
(PRODUCT_SPEC.md touch is presence-only, aside from the one thin content line moved to
bounds above), `test_onboarding_card.py`, `test_read_grant.py`, `test_reap_owned_group.py`.

Also confirmed pure shape (mechanism/fixture-driven, thin or presence-only
PRODUCT_SPEC.md touches moved into their covering unit's table above rather than listed
twice): `test_doc_bound.py`, `test_doc_rotation.py`, `test_every_gate_can_fail.py`,
`test_answer_first_arm.py`, `test_authority_anchor.py`, `test_board.py`,
`test_ci_mirror.py`, `test_cleanup_notice.py`, `test_config_health.py`,
`test_hedge_arm.py`, `test_lean_orchestrator_arm.py`, `test_net_meter.py`,
`test_node_growth.py`, `test_release_note.py`, `test_touchpoint_kind.py`,
`test_update_watcher.py`, `test_vacuous_pass.py`, `test_version_is_one_fact.py`,
`test_preshow_register_lint.py`, `test_far_tier.py`'s gate-fixture classes,
`test_harness_template.py`'s bulk (drives `templates/headless_harness.py` source, not
PRODUCT_SPEC.md), `test_no_dramatization_law.py`'s judge-mechanism classes,
`test_lane_branch_road.py`'s git-deed classes, `test_stranger_door.py`'s monitor-script
classes, `test_traceability.py`'s index/matrix/version/coverage-parsing classes
(roughly a third of that file).

Already governed by the stage-1 format gates work per `delta/gates-plan.md` (Areas 1–6):
`check-requirement-shape.py` / `test_requirement_shape.py` (unarmed, fixture-only, not
yet reading the real document), `check-vocabulary.py`, `check-one-name.py`,
`check-weak-words.py`, `check-gap-lines.py`, `check-no-history.py`,
`check-index-generated.py`, `check-delta-record.py`, `check-size-ratchet.py` /
`test_size_ratchet.py`, `comprehension-gate.py`, `check-gate-reach.py`,
`build-index.py` / `test_build_index.py`, `test_vocabulary_check.py`,
`test_one_name_check.py`, `test_weak_words.py`, `test_no_history.py`,
`test_index_generated.py`, `test_style_lint_tiers.py`, `test_ratchet_kit.py`,
`test_delta_classifier.py` — none of these currently read the real `PRODUCT_SPEC.md`
(they drive the new, still-unarmed format gates against synthetic fixtures), so none
needs re-pinning; verify at arming time that they still don't, per the gates plan.

**Existing guardrail scripts that read `PRODUCT_SPEC.md` directly** (all confirmed pure
mechanism — byte bounds, freshness-by-git-commit, index-row presence, arming switches —
zero wording pinned): `check-description-field.py`, `check-doc-bound.py`,
`check-doc-rotation.py`, `check-freeze.sh`, `check-index-prose.py`,
`check-prover-record.sh`, `check-push-reach.sh`, `check-requirement-shape.py`,
`check-size-ratchet.py`. `check-pin-drift.sh` and `check-matrix-coverage.sh` do not read
`PRODUCT_SPEC.md` at all (they read other artifacts); their pytest wrapper
(`test_guardrails.py`) is already counted above.

## Not-applicable (never read the real root PRODUCT_SPEC.md)

- `tests/test_conduct_judge.py` — "PRODUCT_SPEC.md" appears only inside a synthetic
  tool-call payload string fed to a hook, never an actual file open.
- `tests/test_requirement_shape.py` — drives the new, unarmed format gate on fixtures.
- `tests/test_scaffold_guardrails.py` — reads a fixture copy under
  `tests/fixtures/scaffold_guardrails/`, never the real root file.
- `evals/build-pipeline.md`, `evals/spec-author.md` — name PRODUCT_SPEC.md only inside a
  fictional scenario prompt describing a different, imaginary repo.

---

## What to do with this at stage 3

1. Convert `### Composing across axes` (PRODUCT_SPEC.md lines 2031–2092) as an
   additional unit before or alongside assembly — it is the only home for the seven
   codes in Finding 1, and it is the reason the census undercounted the section coverage.
2. Re-pin the 119 CONTENT-READER + MIXED files from their covering unit's `mapping.md`
   (code → new text), following each unit's table above.
3. Resolve the six check-me items with a human or a second read before treating them as
   settled — none is proven dropped, but none is proven safe either.
4. Leave the 12 pure shape-readers and 3 N/A files alone; they need no re-pin action
   from this document (the shape side is `delta/gates-plan.md`'s job).
