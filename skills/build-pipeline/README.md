# build-pipeline

**Ship a change by the method — spec → prove → reconcile → matrix → test → code → verify → commit. A [Claude Code](https://claude.com/claude-code) skill.**

It's the spine that runs the whole arc. You ask for a feature; build-pipeline walks it through writing the spec, proving it, deriving the tests, writing the code, verifying by deed, and committing — in that order, every time. It's the orchestrator for a pair of sibling skills: **[spec-author](https://github.com/happysasha18/spec-author)** writes the spec, **[product-prover](https://github.com/happysasha18/product-prover)** reviews it, and build-pipeline sequences them through to shipped code.

---

## The order it won't break

> spec → prove → reconcile → matrix → test → code → verify → commit. A bug shortcuts to bug → matrix → test → code.

Never code first and back-fill a spec to match. The point of the order is that each step catches what the next one would otherwise build on top of: the prover only finds a cross-section hole when the whole spec is in front of it; the tests come from the matrix, not the code; "done" means you ran it and watched it work.

Tiny reversible edits skip the ceremony — but they still ship a test.

**Where your change enters:**
- **Bug** → matrix → test → code (no spec change unless the spec stated the wrong fact)
- **Removal** → dated tombstone in spec, retire the matrix rows, doc sweep, then code
- **Refactor** → straight to code, but run the full suite and audit the matrix
- **Docs only** → rendered re-read and one consistency grep

---

## The steps

1. **Spec** — invoke `spec-author`: entities, states, transitions, actors, invariants, and the cross-section composition between surfaces. Real gaps are marked `⟨DECIDE⟩` and asked, never guessed.
2. **Prove** — invoke `product-prover` on the *whole* spec, not the delta. Fold every must-fix by the book. A surface absent or unlinked at prove-time is invisible to the prover. Two modes: a full pass or a focused cross-link pass for a single new surface. Findings persist to a dated file so the next review starts from the last one's open rows.
3. **Reconcile with reality** — verify the spec's claims about how the code actually behaves (cite `file:line` from a command you ran), and fix the spec to the shipped truth before deriving tests.
4. **Matrix** — derive the test matrix from the proven spec: one row per invariant / state / transition.
5. **Test** — write tests that assert the **real shipped artifact** (render it, produce the file, call the function), watch them fail first, never edit a test just to pass.
6. **Code** — implement until green; delegate well-scoped mechanical work to a worker with a checkpoint file, keep the hard parts on the senior model, verify the result by deed.
7. **Verify by deed** — run it, see it, *then* call it done. Run the whole suite before any push.
8. **Commit & show** — commit green, bump the version, ship the docs in the same session, show the real render, push only after it's reviewed.

---

## Gates worth remembering

- **Before a minor (0.x.0) bump:** the 3-pass preventive audit — prove the whole spec + audit the matrix + check surface composition.
- **Order is law:** `spec → prove → reconcile → matrix → test → code`; `bug → matrix → test → code`.
- **Delegation:** if you can write it as precise steps, it's a worker's job — decided *before* the first tool call; long work writes its progress to a persistent checkpoint so a cut-off resumes instead of restarting.
- **Traceability gate:** `test_traceability.py` runs every commit — spec-to-test drift is caught on the commit that causes it, not at the next minor bump.

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
