### [node: text-audit]

**responsibility** — the audit-and-fix loop for human-facing texts: run the mechanical register lints, then fresh zero-context cold reads, fixing each finding at its source until two consecutive reads come back clean

**owns** — INV-266, INV-267, INV-268 (text-audit is the skill that runs this loop)

**pins** — `skills/text-audit/SKILL.md:1` (frontmatter + when it fires), the mechanical-lint and cold-read-loop sections in the same file

**notes** — the tenth working skill, named in the pack's skill roster and the pipeline-roles glossary (its cold-read comprehension loop is the mechanical-lints-then-panel discipline the format-laws requirements state, homed here). the working-skill roster's text-audit member (the roster entity's home stays base-rulebook; this node bodies the skill without owning that anchor).