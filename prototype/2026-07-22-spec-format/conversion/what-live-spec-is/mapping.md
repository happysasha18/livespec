# MAPPING — codes, consumed index rows, and atomic-claim coverage

This file proves the rewrite of the document header and `## What live-spec is` dropped nothing. Part 1 maps every code the source range cites to its new home. Part 2 states which codes carried a consumed Formal-index row. Part 3 maps every behavioural claim of the source to the criterion that now carries it.

This unit is the document's opening, so its `section.md` becomes the assembled document's own preamble. Zero codes are dropped: all 8 cited codes appear in `section.md` (verified mechanically — the cited-set of the source range minus the present-set is empty, and the reverse difference is empty too).

**Carried by assembly, not converted.** The source's first line, `# live-spec — Product Spec (v3.6.0, 2026-07-21)`, pairs the document title with its version and date. The version-and-date pair is assembly metadata — it belongs to the release the assembled document ships as, not to any requirement — so it is carried by the assembly step onto the reconstructed title line rather than converted to a criterion here, and the no-history law keeps the date out of the body. `section.md` keeps only the bare title `# live-spec — Product Spec`.

## Part 1 — every cited code → its new home

| Code | New home | Index row consumed? |
|---|---|:--:|
| S-0 | R1 | yes |
| E-6 | R1 | yes |
| E-7 | R1 | yes |
| E-10 | R1 | yes |
| E-18 | R1 | yes |
| A-6 | R1 | yes |
| E-12 | R2 | yes |
| E-1 | R3 | yes |

## Part 2 — consumed Formal-index rows

The range cites 8 distinct codes, and **all 8 carry a Formal-index row**. Each row's meaning now lives at the home named in Part 1; no consumed index row is left without a home.

**Codes owned by this range** (their Formal-index home is `header` or `What live-spec is`) are the ones this rewrite fully converts: S-0, E-1.

**Pure cross-references** — a rule owned by another section that this opening names rather than restates — are preserved as trailing anchors: E-6, E-7, E-10, E-18 (the planned machines, home `Machines`), A-6 (the adoption baseline, home `Adoption step 6`), and E-12 (the base skill, home `One rulebook`). The full behaviour of each stays defined in its home section.

**Cross-section glossary note.** The nouns this opening uses that other sections own — request, pipeline, spec, test matrix, queue, journal, inbox, host, surface registry, feedback ledger, snapshot, design-sync, skill eval — are defined in their home glossaries, not repeated here. This unit's `## Glossary additions` block adds only the three nouns it introduces: base skill, working skill, and target tag.

## Part 3 — atomic-claim coverage

Every behavioural claim of the source range, in source order, mapped to the criterion that now carries it.

| # | Source claim | Criterion |
|---|---|---|
| 1 | The spec separates what is built and working today from what is only planned, marking each feature and its parts at the granularity the target tag binds to. | R1.1 |
| 2 | A planned item carries a `[target]` tag on a line of its own; the tag never appears on the section around it. | R1.2 |
| 3 | The suite ties each `[target]` to the open roadmap row that builds it and goes red if that row ships with the tag on, if the tag vanishes, or if the tag was never named. | R1.3 |
| 4 | The planned items are the host-facing guardrail checks and the surface registry, the snapshot machinery used by the adoption baseline, and the design-sync machine. | R1.4 |
| 5 | A person submits any request of any size at any moment; live-spec breaks it into small pieces processed one at a time, each running the same proven pipeline to a tested delivery, leaving the person free to think about other things. | R1–R3 Context (the covering loop; its normative home is the build-loop section, cited without a code here) |
| 6 | Machines enforce the process at every step; every claim earns a test and nothing ships until it passes. | Preamble covering paragraph + R2.1 (the roles that run the enforced pipeline) |
| 7 | The roles behind the pipeline are an analyst (spec), an architect (edge cases and dead ends before code), a design reviewer (same-kind things behave alike), a tester (works out and writes the tests), and a project manager (runs the process and reports back). | R2.1 |
| 8 | These roles are the working skills, and the pipeline brings the person in for the decisions that are theirs. | R2.2 |
| 9 | One base skill holds the shared rulebook and the default settings the working skills run by. | R2.3 |
| 10 | A project can adopt live-spec at the start or partway through, adoption bringing the document templates, a midstream procedure, and the guardrails the project installs; the project that adopts it is the host. | R3.1, R3.2 |
| 11 | The host owns its own spec, matrix, queue, journal, surface registry, inbox, feedback ledger, and a `.live-spec/` folder holding its profile, checkpoints, and skill versions. | R3.3, R3.4 |

### Coverage result

11 behavioural claims mapped, covering all 3 requirements. The covering loop (claim 5) is the document's introductory framing; its normative home and its state codes live in the build-loop section, a different unit, so the source states it here without a code and it is carried as Context rather than converted to a coded criterion in this opening. History carried by the source — the version-and-date header pair — is handled by assembly and kept out of the body by the no-history law. No behavioural `shall`-claim of the source range is left uncovered, and this opening opens no source hole (see `GAPS.md`).
