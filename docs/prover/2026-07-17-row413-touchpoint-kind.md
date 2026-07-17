# Prover record — ROADMAP 413: every point of contact with the person has a kind

Date: 2026-07-17 · Doc version: v2.6.3 · Form: FULL (a new cross-cutting frame four rows hang off, plus
one new guardrail gate and its declaration manifest) · Mode: FULL prover walk of the new clause beside
the whole-spec composition, plus the architecture lens on the ARCHITECTURE.md edit.

## Footprint classification

Cross-cutting. The row states a new frame — every touchpoint has a kind, and the kind decides what may
be said there — that is the missing home for four already-queued rows (402, 403, 408, 409). It adds one
observability-class net beside the guardrails' existing gates (INV-202/203/204) and a small declaration
manifest the gate reads. No product-facing surface, no new persistent state at runtime, no new
architecture node: INV-205 lands on the existing guardrails node beside its net siblings. Full prover
walk, not the short form, because a new invariant is declared and it composes with four rows.

## What changed, and the law under it

- **INV-205 new** (`guardrails/touchpoints.json` + `guardrails/check-touchpoint-kind.py` +
  `guardrails/touchpoint-fixtures/`): each touchpoint declares its kind in the manifest — synchronous
  (the person present, the work waiting on him) or asynchronous (he reads on his own clock while the work
  rolls), plus whether the person opens the point himself. The afforded traffic derives from those two:
  an interruption on a synchronous point, a teaching line on a point the person opens himself, waiting
  traffic on every point. The gate reds a surface that speaks in a kind its touchpoint lacks.
- **The four instances declared.** 408 (the waiting list) and 409 (the parked feedback question) are
  asynchronous and person-opened — he opens the waiting list on request, and the parked question rides
  it. 402 (the release note offer) is asynchronous and person-opened — a changelog he reads when he opens
  the release notes himself, so an offer of next steps is afforded and an interruption is not. 403 (the
  far-tier surfacing) is asynchronous and agent-pushed — it rides the status report, so it may only wait.
  None of the four's kind was undecidable without building its own machine; each is grounded by its own
  row's text (408's "opens on request", 402's "human-audience, no-answer-needed", 403's "rides the status
  report"). 408 stays OPEN as its own build (`check-board.py`); this row only declares its kind.

## Architecture lens — the six checks on the ARCHITECTURE.md edit

1. **Every spec fact has an owning node.** INV-205's anchor lands on the guardrails node's owns-list,
   exactly one owner (traceability suite green). PASS.
2. **No node stands without spec backing.** No node added; the guardrails node's clause grows one entry
   backed by INV-205. PASS.
3. **Every seam names what crosses it.** No new seam. The gate reads the manifest and the declared
   surfaces at push time, a build-time file read internal to the guardrails node, not a cross-node
   runtime payload. PASS.
4. **Quality budgets with instrumentation homes.** No new budget; the gate is a boolean-presence check,
   read by the suite and the push gate. N/A.
5. **Runtime view walks every promised flow.** The gate rides the existing push-gate flow as gate p; it
   adds no new flow edge. PASS.
6. **Placement view.** The manifest and gate are build-time checks on the author's machine, the same
   placement as the sibling gates. PASS.

## Spec-lens findings

- **F1 (folded).** The frame keys on the person's own settings [ROADMAP 414], which are not derivable
  here. The clause states the frame for any person and marks the keyed settings as the person's own,
  riding his profile rather than the spec text (the settings-ladder scope, INV-101). Folded in the clause
  and the Formal-index row.
- **F2 (folded).** The teaching duty the row's word puts here — a capability the person has not met is
  introduced at a touchpoint whose kind affords it, so the product teaches itself through use — had to be
  named as a traffic kind the frame licenses, else "a teaching line on a point the person did not open"
  had no positive home. The clause names teaching as afforded on a point the person opens himself, and the
  gate's afforded-set derives it. Folded.
- **F3 (recommendation, folded).** INV-205's ownership could sit on the communicator node (it owns the
  human-facing surfaces the touchpoints render on) or the guardrails node (the manifest and gate live
  there, beside the net siblings INV-202/203/204). Chose guardrails for sibling-consistency with the
  other mechanical nets and because the shipped artifacts are the manifest and the gate. Recorded.
- **F4 (folded).** The gate must red a real violation, not look at nothing. It reads real file content —
  a surface's declared touchpoint and its traffic markers — against the real manifest, and the fixture
  corpus red-proves both forbidden combos (an interruption from an asynchronous point; a teaching line on
  an agent-pushed asynchronous point) while the three afforded mirrors pass. This is the committed-probe
  shape check-broad-kill already uses. Not a hollow gate. Folded (the fixtures ship).

## Verdict

HOLDS. Zero must-fix. The new clause composes with its neighbours: the frame names both kinds positively
and what each licenses, the machine reds a surface speaking in a kind its touchpoint lacks (red-proven on
the fixture corpus), and each of the four instance rows names its kind under the frame and passes quiet.
Open ⟨DECIDE⟩ touched by the change: none. The one open dependency (the person's own settings, ROADMAP
414) is named in the clause and left to his profile.
