# test-author

**Turns a proven spec into a test suite that would have caught the bug. A [Claude Code](https://claude.com/claude-code) skill, part of the [live-spec pack](https://github.com/happysasha18/live-spec).**

You give it a spec that a reviewer has already checked and an architecture that a reviewer has already checked. It builds TEST_MATRIX.md — a grid that lists every fact the spec promises and pins how each fact will be tested. Then it writes the tests, one owning test per grid row, and each test inspects the real thing the user receives.

A **spec** is the document that states what the product must do. An **architecture** is the document that states how the code is arranged to do it. "Proven" means a reviewer walked the document and signed off. The [product-prover](https://github.com/happysasha18/live-spec/tree/main/skills/product-prover) skill does that review.

This skill ships inside the live-spec pack. Install the pack to get it. Used on its own, this README reads as plain advice about writing tests.

---

## The problem it fixes

Green tests can lie. A test suite can pass in full while the shipped page shows the wrong thing to the user. This happens when a fact is checked at the wrong **level** — the depth at which a test looks. A test that only reads the source text can confirm the code SAYS the right word while the rendered screen shows the wrong one.

The method here was built on a real project. Two bugs a user could see shipped past about 660 passing tests. The tests read source strings for facts that were really about what appears on screen. The rebuild that followed produced the level ladder and the rules this skill carries.

---

## The level ladder

Every fact in the matrix is pinned to one of four levels. The level is the most important choice in the row.

| Level | What it proves | What it stays blind to |
|---|---|---|
| string | the source or output text contains the value | everything the user actually sees |
| DOM-text | the rendered document says the value | position, visibility, color, interaction |
| browser-computed | real layout, style, and behaviour in a real browser engine | subjective look and feel |
| pixel | the rendered look matches a frozen approved picture | nothing, but it is fragile, so it is held in reserve |

The pinning rules are fixed. A fact about visibility, layout, color, or interaction is pinned at browser-computed or higher. A fact about content is pinned at DOM-text. A fact about wiring or configuration may sit at string. When the level is unclear, ask what the user would see broken, then pick the level that can see the same thing.

The ladder stops below the real device. Touch physics, scroll snapping, and background tab throttling live past what a desktop headless browser can reach. A fact that lives there gets a real-device row: a matrix row the suite can never turn green, owed instead to the human's own hands on a real phone before the product ships.

---

## What else it enforces

- **Assert the real shipped artifact.** Render the page, produce the file, or call the function, then inspect the output. A source-string match on a screen fact only reveals a matrix defect.
- **Red first.** A new test runs against the state before the change, or against the bug, and it fails there before the code makes it pass. The failing run is recorded. A test born green proves nothing.
- **Never edit a test to make a change pass.** A failing test means the change or the matrix cell is wrong. Fix the cell first, then let the test follow the corrected cell.
- **Pin the skip-set.** A **skip** is a test the runner declines to run, for example when a browser is missing. Green means zero failures AND the skip list matches the exact set you expected. An unexpected skip is a failure in a quieter color.
- **Traceability is a standing test.** A test in the suite fails when a matrix row cites a test that is missing, when an id is duplicated, or when a spec fact has no row. Drift is caught at every commit.

An **invariant** is a fact that must hold in every state of the product. Each invariant owns its own test.

---

## What's inside

No code and nothing to build. The skill is a single `SKILL.md`, a set of instructions Claude follows, plus a matrix template. It works anywhere Claude Code runs.

---

## Install

Clone the pack and place its skill folders where Claude Code reads them.

```
git clone https://github.com/happysasha18/live-spec
cp -r live-spec/skills/* ~/.claude/skills/
```

The `test-author` folder now sits at `~/.claude/skills/test-author/`.

---

## Usage

Most of the time you do not call this skill by name. The pack's `build-pipeline` skill calls it at its matrix step and its test step (steps 5 and 6). Call it directly when you want just that work:

> *"derive the test matrix"* · *"pin test levels"* · *"why did green tests miss this bug?"* · *"rebuild the suite by the method"*

---

## When to use it, and when not

Use it once you have a spec and an architecture that a reviewer has checked. Use it when a passing suite let a visible bug through, and you need to find which facts were pinned too shallow.

Do not use it on a project with no reviewed spec or matrix. "Write tests for X" on its own is not enough here — that request goes to `build-pipeline` first, because the spec and architecture come before the tests. Do not use it to review a document; that is `product-prover`'s job. This skill covers facts with tests. The prover finds holes in what a document claims.

---

## One scenario

A spec says a warning banner turns red when a track clips. A writer files the fact at string level, and the test checks that the word `red` appears in the template. The test passes. The banner ships gray, because a later stylesheet rule overrode the color, and no user ever sees a red banner.

Run through this skill, the same fact gets pinned at browser-computed. The test opens the page in a real browser engine, triggers a clip, and reads the banner's computed color. On the broken build the test fails, in red, before the fix. The reader can trace the row straight back to the spec line it guards.

---

## License

[MIT](LICENSE) © Alexander Abramovich. The level ladder and the bug protocol were proven on [track-coach](https://github.com/happysasha18/track-coach) (MIT) during its July 2026 test overhaul, and are paraphrased here with thanks.
