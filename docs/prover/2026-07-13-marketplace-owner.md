# Prover record — marketplace owner placeholder replaced with the real owner

Date: 2026-07-13 · reviewer: orchestrator (senior, own context) · mode: feature-fit on a one-line
metadata fix (a voiced bug: the install-time owner read a scaffold placeholder).

## Scope of the change

- `.claude-plugin/marketplace.json`: `"owner": { "name": "Community" }` → `"owner": { "name":
  "Alexander Abramovich", "url": "https://github.com/happysasha18" }`. An install shows the source
  owner; the placeholder hid the author on every install.
- `scripts/shipped-language-allowlist.json`: `.claude-plugin/marketplace.json` (and `**/marketplace.json`)
  added to `authorship_globs`, the same carve-out that already spares `plugin.json`. The marketplace
  owner is a structured authorship field, parallel to the plugin owner, so the shipped-language gate
  reads its name as authorship rather than a requirement statement.

## Findings

| # | Finding | Severity | Disposition |
|---|---|---|---|
| 1 | Does the new owner value carry a name the shipped-language gate would flag? | blocking | RESOLVED — the field is an authorship field; added to `authorship_globs` beside `plugin.json`, matching the existing byline carve-out (INV-120). Gate reads 0 offences after. |
| 2 | Does widening `authorship_globs` open a hole that hides a real requirement-statement attribution? | should-clarify | CLEAR — the glob spares only `marketplace.json`, a fixed plugin-metadata file whose only name-bearing field is the owner; it carries no prose that could state a requirement. |
| 3 | Is the value factually correct? | must-fix if wrong | CLEAN — name matches the LICENSE byline (© Alexander Abramovich); the URL is the repo owner's GitHub profile (happysasha18). |

0 open must-fix. No new ⟨DECIDE⟩ opened. The same placeholder in the sibling `promoter` repo was routed to
its inbox (its own window owns that tree).
