# GAPS — source holes found during the rewrite

A gap is a place where the source states a behaviour but leaves a judge, a measure, a default, or a definition unanswered. This unit — the document header and `## What live-spec is` — opens **no such hole**, so `section.md` carries no `[GAP]` line.

This is the expected result for the document's opening. The passage is definitional: it introduces what live-spec is, names the roles behind the pipeline, and states what the host owns. Each place that could have hidden a hole is answered in the source:

- **The target-tag granularity** is stated, not left open: the tag binds to the line it sits on ("a `[target]` tag on a line of its own"), so a partly-built feature is marked at line granularity.
- **What the host owns** is enumerated in full — spec, matrix, queue, journal, surface registry, inbox, feedback ledger, and the `.live-spec/` folder with its profile, checkpoints, and skill versions — with no evaluative slot left unfilled.
- **The roles** are each named with the one thing they do, and their carrier — the working skills over one base skill — is named.
- **The covering loop** (any request → small pieces → one pipeline → tested delivery) is introductory framing whose measures and states live in the build-loop section; it opens no hole here because it makes no measurable claim this opening must pin.

No answer was invented to reach this result; the source simply states what it needs to at the granularity an opening owes.
