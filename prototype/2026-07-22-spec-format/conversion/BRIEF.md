# Conversion brief — one unit of PRODUCT_SPEC.md into the requirements genre

This brief instructs one converter working on one assigned unit (a `##` section or a run of `###`/`####` blocks) of `PRODUCT_SPEC.md`. The assignment message names the unit, its exact source line range, and the output directory under `prototype/2026-07-22-spec-format/conversion/`.

## Read first (locate your own anchors)

1. `docs/spec-format.md` — the genre definition: six laws, the criterion form, the comprehension gate.
2. The worked example: `prototype/2026-07-22-spec-format/conversion/bounds/section.md`, `mapping.md`, `GAPS.md`, `NUMBERS.md`. Your four output files follow these shapes exactly.
3. Your assigned source lines in `PRODUCT_SPEC.md`, and — for every code your unit cites — that code's row in the Formal index (the `## Reference` section, line 2027 onward).

## Produce four files in your output directory

- **section.md** — preamble (what the unit covers, the code-legend paragraph, the carried-terms sentence), glossary additions (only nouns the carried list below misses), then the requirements. Each requirement: Context (2–4 short sentences), User Story (one sentence), Acceptance Criteria in named cases (a bold case line, then 2–6 numbered criteria; numbering runs continuously through the requirement). Keywords *when*, *while*, *if*, *then*, *shall* in lowercase italics. Code anchors trail at line end.
- **mapping.md** — three parts, per the bounds example: (1) every cited code → its requirement home; (2) whether the code's Formal-index row was consumed; (3) every behavioural claim of the source prose → the criterion that now carries it. State the mechanical zero-drop check result: cited-set minus present-set must be empty.
- **GAPS.md** — every place the source states a behaviour but leaves the judge, the measure, the default, or the definition unanswered. Each hole gets a `[GAP: ...]` line under its criterion in section.md and a numbered entry here (Where / Hole / What it blocks). Inventing the missing answer is forbidden; the gap line is the correct output.
- **NUMBERS.md** — measured bytes (UTF-8): source body, consumed index rows, output total and its parts, the two ratios (whole-basis and prose-to-prose), and a short honest reading of what the ratio does and does not mean. Measure with a command; estimates are banned.

## Hard rules

- **Zero drop.** Every code the source cites appears in section.md. Every behavioural fact — in the prose or present only in the code's Formal-index row — lands in a criterion. History (dates, provenance, who asked when) is dropped by law 6; it lives in the journal already.
- **No invention.** A hole in the source becomes a `[GAP]` line. Nothing is filled in from imagination.
- **Requirement numbers are local to your unit** (R1..Rn). Units are renumbered mechanically at assembly.
- **Language.** Native plain technical English; short SVO sentences. The contrast frame that names a thing by denying its neighbour («X — not Y», "X, а не B") is banned; state what a thing is in its own sentence. Adjectives grading a result's importance are banned. No all-capital words outside code anchors.
- **Self-run the lints until green** before reporting done:
  ```
  python3 guardrails/check-vocabulary.py <dir>/section.md
  python3 guardrails/check-weak-words.py <dir>/section.md
  python3 guardrails/check-requirement-shape.py <dir>/section.md
  python3 guardrails/check-no-history.py <dir>/section.md
  python3 guardrails/check-one-name.py <dir>/section.md
  ```
- **Write only inside your output directory.** The source spec, other units' directories, and everything else in the repository are read-only to you.

## Terms already defined (carry, never redefine)

Intake glossary: request, inbox, pipeline, spec, architecture, invariant, guardrail, suite, host, pack, session, journal, attic, backlog item, queue, movement, delivery, delivery report, footprint, project layers, settings ladder, personal profile, profile, resume file, migration chapter, ratchet manifest.

Founding section: pack, host, founding, adoption, catch-up, version-control gate, scaffold, personal profile, settings ladder, settings card, project kind, project layers, proof kinds, design principle, engine, instance, content contract, attic, migration chapter, installer, freshness check, update check, ratchet manifest, agent card, founding-question set.

Agents-together section: agent, capability, zone, card scan, published contract, generation stamp, cadence, staleness bound, grant, named reference, description field, earned message, ground, referral, need-by, transport, harness, stranger, monitor, status report, adversarial read, expensive decision.

Bounds section: net, push gate, prover record, net-liveness meter, test matrix, feature-coverage trace, register judge, conduct judge, action trace, seat, touchpoint, far tier, waiting board, decision-set record, snapshot, design-sync, skill eval, surface registry, pen, remote seat, stranger-wish monitor, capture echo.

A noun on these lists is used with its existing meaning and gets no new entry. A new noun your unit needs gets a one-sentence entry in your glossary additions. If two units independently coin the same noun, the pooled-glossary assembly deduplicates; prefer a carried term where one fits.

## Report back (final message = data)

Return: unit name; requirement / case / criterion counts; cited-code count and the zero-drop verdict; lint results (five lines); GAP count with one-line titles; the two ratios from NUMBERS.md; anything that blocked you.
