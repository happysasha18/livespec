# build-pipeline

**Ship a change by the method — spec → prove → architecture → prove architecture → matrix → test → code → verify → commit & show. A [Claude Code](https://claude.com/claude-code) skill.**

It's the spine that runs the whole arc. You ask for a feature; build-pipeline walks it through writing the spec, proving it, deriving the tests, writing the code, verifying by deed, and committing — in that order, every time. It's the orchestrator for a pair of sibling skills: **[spec-author](https://github.com/happysasha18/spec-author)** writes the spec, **[product-prover](https://github.com/happysasha18/product-prover)** reviews it, and build-pipeline sequences them through to shipped code.

---

## The order it won't break

> spec → prove → architecture → prove architecture → matrix → test → code → verify → commit & show. A bug shortcuts to bug → matrix → test → code.

Never code first and back-fill a spec to match. The point of the order is that each step catches what the next one would otherwise build on top of: the prover only finds a cross-section hole when the whole spec is in front of it; the tests are derived from the matrix, which sits upstream of the code; "done" means you ran it and watched it work.

Tiny reversible edits skip the ceremony — but they still ship a test.

**Where your change enters:**
- **Bug** → matrix → test → code (no spec change unless the spec stated the wrong fact)
- **Removal** → dated tombstone in spec, retire the matrix rows, doc sweep, then code
- **Refactor** → straight to code, but run the full suite and audit the matrix
- **Docs only** → rendered re-read and one consistency grep

---

## The steps

1. **Spec** — invoke `spec-author`: entities, states, transitions, actors, invariants, and the cross-section composition between surfaces. Real gaps are marked `⟨DECIDE⟩` and asked, never guessed.
2. **Prove** — invoke `product-prover` on the *whole* spec each pass, including the parts the delta left untouched. Fold every defect by the book. A surface absent or unlinked at prove-time is invisible to the prover. Two modes: a full pass or a focused cross-link pass for a single new surface. Findings persist to a dated file so the next review starts from the last one's open rows.
3. **Architecture** — write or update `ARCHITECTURE.md` from the proven spec: named nodes, one responsibility each, every spec fact owned by exactly one node, named seams; in a live codebase every node pins to its owning `file:line` — this is where the spec is reconciled with shipped reality (cite `file:line` from a command you ran, fix the spec to the truth).
4. **Prove the architecture** — `product-prover` with the architecture lens, whenever the doc changed: every fact owned, no node without spec backing, every seam named.
5. **Test spec** — DERIVE the matrix from the proven spec through the proven architecture: rows organized node × fact, one row per invariant / state / transition, each pinned to a test level; derivation closes with a coverage-validation checklist actually walked.
6. **Test** — write tests that assert the **real shipped artifact** (render it, produce the file, call the function), watch them fail first, never edit a test just to pass.
7. **Code** — implement until green; delegate well-scoped mechanical work to a worker with a checkpoint file, keep the hard parts on the senior model, verify the result by deed.
8. **Verify by deed** — run it, see it, *then* call it done. Run the whole suite before any push.
9. **Commit & show** — commit green, bump the version, ship the docs in the same session, show the real render, push only after it's reviewed.

---

## Gates worth remembering

- **Before a minor (0.x.0) bump:** the 3-pass preventive audit — prove the whole spec + audit the matrix + check surface composition.
- **Order is law:** `spec → prove → architecture → prove architecture → matrix → test → code`; `bug → matrix → test → code`.
- **Delegation:** if you can write it as precise steps, it's a worker's job — decided *before* the first tool call; long work writes its progress to a persistent checkpoint, so a cut-off resumes from where it stopped.
- **Traceability gate:** `test_traceability.py` runs every commit — spec-to-test drift is caught on the commit that causes it, continuously, so it never waits for the next minor bump.

---

## What's inside

No code, no dependencies — build-pipeline is a single `SKILL.md`: a structured set of instructions Claude follows. Drop it in and ask. Works anywhere Claude Code runs.

---

## Usage

Drop the folder into `~/.claude/skills/build-pipeline/` (alongside [spec-author](https://github.com/happysasha18/spec-author) and [product-prover](https://github.com/happysasha18/product-prover)) and just ask:

> *"build this properly"* · *"do it by the method"* · *"spec and ship X"* · *"new surface for Y"*

---

## License

[MIT](LICENSE) © Alexander Abramovich.
