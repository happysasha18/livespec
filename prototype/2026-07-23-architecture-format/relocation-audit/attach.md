# owns-field prose audit — node `attach`

The owns field carries one parenthetical, attached to anchor INV-227. It splits into three fragments.

| fragment (quoted) | anchor | class | evidence |
| --- | --- | --- | --- |
| "the founding-question set is versioned" | INV-227 | DUPLICATE | PRODUCT_SPEC.md:101 (glossary) — "**founding-question set** — the versioned set of questions founding asks a host. … a host records which version it answered." |
| "the update check's founding arm names each never-answered question" | INV-227 | DUPLICATE | PRODUCT_SPEC.md:4174 (R188.12) — "*when* the update check runs, its founding arm *shall* read the host's recorded `founding.set-version` against the current set and name each founding question the host has never answered, beside the vendored-file report. [INV-227]" |
| "the recorded `founding.set-version` profile line is carried by host-contract as wiring, ownership stays here beside E-25 and INV-177" | INV-227 | KEEP | Wiring note: another node (host-contract) carries the text, ownership stays at `attach`. Architecture-level ownership statement, not a spec rule. (The underlying fact — set version homed in host profile — is at PRODUCT_SPEC.md:4176, R188.14, but the fragment's content is the wiring/ownership assignment, which belongs in the architecture.) |

## pins-provenance list

The `attach` node's pins field carries ten pins; none of their labels carry a date, a session number, or a landed-row provenance note:

- `adopt/ADOPT.md:39` (VCS gate first)
- `:172` (unbacked-surface verdict)
- `:183` (attic)
- `:259` (attach record)
- `:80` (B-3 — who am I working with, first step of orient)
- `MIGRATION.md:1` (A-11 — the catch-up walk's operating guide)
- `install.sh:2` (E-21 — the installer itself)
- `scripts/check-pack-update.sh:1` (E-25 — the update check + the founding arm, INV-227)
- `scripts/founding-questions.json:1` (INV-227 — the versioned founding-question set)
- `adopt/install-ratchet.sh:1` (INV-172 — the ratchet kit installer)

Pins carrying provenance (date / session number / landed-row): none.
