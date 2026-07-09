# Guardrails — the pipeline's mechanical teeth

Four checks wired to a git pre-push hook (and run as part of the test suite). A change that fails any of them is RED and cannot be pushed. Each project instantiates these checks for its own surfaces; the pipeline requires the check exists and is green.

Generic code is the next movement — lifted from track-coach's working instance and made project-agnostic. What follows is the authoritative description of what each check does.

---

## 1. Completeness

A surface registry plus a render-scan test that fails if any user-facing surface is empty OR is rendered but not in the registry. No partial or stripped artifact can ship or be shown.

The DOM (or the rendered file) is the source of truth; a hand-maintained list carries no authority. The test scans the actual rendered output and compares against the registry — so a new surface going unregistered is immediately RED, and a registered surface going missing is immediately RED.

Self-closing: you cannot drift past it by forgetting to update a list. The registry is the list; the test compares the list against reality every run.

---

## 2. Tests-present

A diff that touches a user-facing module must also touch `tests/`. A change with no test delta is RED.

This is the mechanical enforcement of "tests travel with every change." It does not check whether the test is good — that is the matrix and the prover's job. It checks whether a test exists at all. A one-line change to a rendered output with no test change fails this check; the developer must either add a test or explicitly justify the exemption in the matrix (SKIP with a reason).

---

## 3. Behaviour traces to spec

Every user-facing behaviour must trace to a SPEC clause. A behaviour with no spec backing — a silent default, an auto-mute, a sort order, a colour — is RED.

This is what catches freelancing mechanically: you cannot ship an unasked, unrecorded behaviour because the test will look for its spec clause and find nothing. The spec clause does not have to be detailed; it must exist. A one-line spec entry ("stems play in full-mix order by default — CR-5") is enough. Silence is not.

Implementation note: each user-facing module carries a `spec_refs` annotation (or equivalent per-project convention) naming the SPEC clause(s) it implements. The guardrail test checks that every annotation resolves to a real clause in PRODUCT_SPEC.md, and that every clause reachable from the rendered surface is annotated.

---

## 4. Conflicts

Catches structural inconsistencies that accumulate over time:
- Duplicate invariant IDs (two `INV-18` entries)
- A spec invariant with no matrix row
- A `⟨DECIDE⟩` marker that is still live in PRODUCT_SPEC.md but marked RESOLVED in the prover findings
- A surface named two ways in the same document (e.g. "stem lanes" and "#stemlanes" as if separate)
- An id in TEST_MATRIX.md that references a test file or function that does not exist

These are the inconsistencies that make a prover's findings unreliable and a matrix audit meaningless. Catching them mechanically means drift is caught every commit instead of once per MINOR audit.

---

## Honest boundary

Guardrails catch **structural** defects: empty surface, missing test, untraced behaviour, partial artifact, id/naming conflict. They do NOT catch a subtle semantic bug (is the number right? is the recommendation correct?). That still needs `product-prover` and a human's eyes. Enforce structure mechanically; reason about meaning with the prover.
