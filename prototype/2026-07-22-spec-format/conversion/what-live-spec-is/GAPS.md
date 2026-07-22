# GAPS — source holes found during the rewrite

A gap is a place where the source states a behaviour but leaves a judge, a measure, a default, or a definition unanswered. This unit — the document header and `## What live-spec is` — carries one such hole, on the surface registry's status; the rest of the passage opens no hole.

The passage is mostly definitional: it introduces what live-spec is, names the roles behind the pipeline, and states what the host owns. Each other place that could have hidden a hole is answered in the source:

- **The target-tag granularity** is stated, not left open: the tag binds to the line it sits on ("a `[target]` tag on a line of its own"), so a partly-built feature is marked at line granularity.
- **What the host owns** is enumerated in full — spec, matrix, queue, journal, surface registry, inbox, feedback ledger, and the `.live-spec/` folder with its profile, checkpoints, and skill versions — with no evaluative slot left unfilled.
- **The roles** are each named with the one thing they do, and their carrier — the working skills over one base skill — is named.
- **The covering loop** (any request → small pieces → one pipeline → tested delivery) is introductory framing whose measures and states live in the build-loop section; it opens no hole here because it makes no measurable claim this opening must pin.
- **The guardrails a project installs on adoption** are named concretely — the repo's own pre-push checks and the opt-in commit fence — and the source keeps that pair distinct from the host-facing guardrail checks, which it names a separate, planned family; no hole here.

## Gap 1 — the surface registry's status contradicts itself

**Where:** Requirement 3, criterion 3 (`section.md`).

**Hole:** The source's own header list names "the host-facing guardrail checks and the surface registry" as planned, tied to `[E-6, E-10]`. The same source, one paragraph later, states the host owns its "surface registry" today, tied to `[E-1]`, alongside the spec, matrix, queue, journal, inbox, and feedback ledger it plainly already has. Nothing in this unit's source lines reconciles the two: no sentence says the registry exists in a lesser form now and ships in full later, the way the guardrails item does. The two statuses stand side by side, unresolved.

**What it blocks:** A reader (and a downstream prover) cannot tell whether a host's surface registry is a present duty or a future one. Criterion 3 keeps both statuses as the source states them and carries a `[GAP]` line rather than inventing a reconciling clause the source does not supply.
