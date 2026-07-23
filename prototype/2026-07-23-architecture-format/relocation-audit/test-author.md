# owns-field relocation audit — [node: test-author]

Source: `prototype/2026-07-23-architecture-format/out/ARCHITECTURE.converted.md`, line 173.

The **owns** field for this node carries only bare spec-anchor codes, with no
attached prose:

> **owns** — E-27, INV-77, INV-78, INV-79, INV-80, INV-100, INV-102, INV-155, INV-157, INV-158, INV-160, INV-162, INV-204

There are no parentheticals or clauses attached to any anchor (contrast the
`spec-author` node at line 45, whose owns field is heavily annotated). So there
are no fragments to classify.

| fragment (quoted; shorten with … past 40 words) | anchor | class | evidence |
| --- | --- | --- | --- |
| (none — owns field carries bare codes only) | — | — | — |

## pins provenance

The **pins** field (line 175) — pin labels carrying a date, a session number,
or a landed-row provenance note:

- `templates/headless_harness.py:1` — carries landed-row notes: "shipped with row 327", "shell-first resolution + launch frame probe, row 364", "the cleanup-notice emitter at each reap, row 417".

Pins with only an invariant-code note (no date / session / row) — not counted:

- `guardrails/cleanup_notice.py:1` (the shared cleanup-notice shape, INV-204)
- `guardrails/check-cleanup-notice.sh:1` (the notice gate, INV-204)
- `skills/test-author/SKILL.md:1` (name + description) — no provenance note.
