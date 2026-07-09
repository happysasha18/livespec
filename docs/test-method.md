# The test method

This page explains, in plain words, how the live-spec pack builds a test suite from a proven spec.
It is the developer-facing companion to the normative method, which lives in
`skills/test-author/SKILL.md`; the binding clauses sit in the spec's "From the spec to the tests"
section (`PRODUCT_SPEC.md`). When this page and those homes differ, those homes win.

A "proven spec" is a `PRODUCT_SPEC.md` that passed a product-prover review. An "architecture node"
is one named part of the build in `ARCHITECTURE.md` (a pipeline stage, a module, a surface owner).

## Where the test matrix comes from

`TEST_MATRIX.md` is the spec projected into a checkable grid. It is derived from the proven spec
through the proven architecture; the spec stays the single source of truth, and the matrix stays a
projection of it. The derivation follows a fixed order (the full list lives in the skill):

- The matrix opens with an artifact inventory: every file the user receives, each owning at least
  one row that renders the real artifact. An artifact no test ever renders can ship broken while
  the suite stays green.
- Rows are grouped one block per architecture node, and every spec fact gets at least one row.
  A fact with a missing row is a derivation defect; it gets fixed in the matrix before any user
  could hit it as a bug.
- Every row states both sides: what the fact does, and what it must never do. The second side is
  the regression fence.
- The state space is named before the cells are filled: view states (mode, toggles) and data
  states (present, absent, empty) form the axes. A fact that must hold in every state is an
  invariant and owns its own test.
- The derivation closes by walking the coverage checklist that the template ships
  (`templates/TEST_MATRIX.template.md`), item by item.

The pack's own `TEST_MATRIX.md` is the worked example. It also shows an honest adaptation: the pack
ships text and skills with no browser surface, so its matrix records why its rows legally pin the
`string` level against shipped files on disk.

## The level ladder

Every matrix row pins a test level, and the level is the row's most important judgment. The ladder
has four rungs:

- `string` proves that source or output text contains something. It says nothing about what the
  user sees.
- `DOM-text` proves that the rendered document says something. It says nothing about position,
  visibility, color, or interaction.
- `browser-computed` proves real layout, style, and behaviour in a real browser engine.
- `pixel` proves the rendered look against a frozen, approved norm. It is brittle, so it is
  reserved for look-and-feel facts.

The pinning rule: any fact about visibility, layout, color, or interaction takes
`browser-computed` or higher. Content facts take `DOM-text`. Wiring and configuration facts may
take `string`. The method was born from a real failure: two user-visible bugs shipped past roughly
660 green tests because their facts were pinned at `string`, so the tests proved the code says the
right thing while the page showed the wrong one. When in doubt, ask what the user would see broken;
the pinned level must be able to see the same thing.

## Real-artifact assertions

A test asserts the real shipped artifact: render the page, produce the file, call the function,
then inspect that output. A source-string match on a rendered fact only proves the matrix pinned
the wrong level; the row still owes a real test.

## Red first

A new test must fail before the code lands. It runs against the pre-change state (or against the
live bug) and goes red; the red run is recorded; then the implementation makes it pass. A test born
green proves nothing about the change. The same discipline covers bugs: a bug first fixes the
matrix cell (or adds the missing invariant row), then gets a test proven red on the bug, then the
code. When a test goes red under a change, the matrix cell is corrected first and the test follows
the corrected cell; editing a test just to make a change pass is forbidden.

## The pinned skip-set

Green means two things at once: zero failures, and a skip list that exactly equals the expected,
pinned set. An unexpected skip (a missing browser, an absent fixture) is a failure wearing a
quieter color, and the gate treats it as one.

## Traceability as a standing test

Traceability runs inside the suite itself. A dedicated test fails on a matrix row that cites a
missing test, on a duplicate row id, on a spec fact with no row, and on stale references, so drift
between the spec, the matrix, and the tests is caught at every commit. The pack's own
`tests/test_traceability.py` is the worked example.

## Five field lessons

One real project week (tlvphoto, 2026-07) shipped five bug classes past green suites. Each landed
as a standing rule; the review that folded them is recorded in
`docs/prover/2026-07-09-rows182-186.md`.

**The suite names the real-device boundary** (INV-77). Touch physics, scroll snapping, and
background throttling live beyond a desktop headless browser's reach. A behaviour living there gets
a real-device walk row: a matrix row the suite can never turn green, owed to the human's own hands
on a named device class before ship. It prevents this failure: a momentum swipe on a real phone
flew through several works, and a backgrounded tab turned a 2.5-second failsafe into a black
screen, while every desktop run stayed green.

**A geometry fact is asserted relative, wide, and long** (INV-78). A centering or positioning fact
asserts relative geometry (the distance between the element's center and the viewport's center
stays within a tolerance), at two or more viewport sizes, and after several consecutive steps of
the interaction, so cumulative drift shows. It prevents this failure: centering was computed by an
absolute shift that differed from the screen size, every next image landed further off-center, and
a one-viewport one-step test passed forever.

**An engine extracted from a project tests on its own generic fixtures** (INV-79). When a generic
engine is carved out of a working project, its suite runs on engine-shaped fixtures with its own
ids and content model; the donor project's data may stay as an extra real-data suite. Every
donor-specific constant found at extraction becomes a named content-contract entry with a test that
the engine works without it. It prevents this failure: the donor's digits-only id pattern stayed in
the engine's validator and rejected the engine's own slug ids, while the donor-shaped suite stayed
green.

**The suite's own plumbing tells the truth about its verdict** (INV-80). Three legs of one class:

- A skip path executes even when never taken: the skip helper imports at module load, so a skip
  that cannot run goes red on every machine. A `skip()` name error once hid exactly there as a
  silent pass.
- An engine/instance shim owes a re-export completeness test that asserts every engine name the
  shim re-exports is present. A missing re-export once kept a whole suite silently red.
- The verdict of a background or delegated run is read from the suite log's own tail line
  ("N/N green"). A wrapper's exit 0 reports only that the wrapper finished; it says nothing about
  the tests. A foreground gate reading its own child process's exit code stays legal.

**The re-prove shortcut is aware of the prover's version** (the row-185 fold; it lives in
`adopt/ADOPT.md` and the product-prover skill). The prover grows new review lenses over time, so
"proven recently with no drift" only excuses a full re-prove when the same prover version produced
the last record; a prover that grew a lens since then re-arms the full pass, and every prover
record opens by naming the skill version that ran. It prevents this failure: a composition lens
landed after the week's specs were proven, the version boundary let their old green stand, and the
seam the new lens would have caught leaked through.
