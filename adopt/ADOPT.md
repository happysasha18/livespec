# ADOPT — Mid-flight adoption procedure

How to attach ADLC to an existing codebase that has no spec yet. Follow these steps in order; each one has a clear done-state before moving to the next.

---

## Step 1 — Inventory the code

**Goal:** Know what exists before writing anything down.

1. List every user-facing output the project produces (HTML files, CLI output, API responses, rendered widgets, emails — anything a user receives).
2. List every surface (a panel, a page, a form, a chart) visible in those outputs.
3. List every significant data entity the code operates on (from filenames, class names, database tables, or config keys).
4. Record this inventory in `data/adopt_inventory.md` — one line per item, no analysis yet.

Done when: `data/adopt_inventory.md` exists and every output + surface + entity has a line.

---

## Step 2 — Reverse-spec from the code

**Goal:** Write what the system actually does, not what you wish it did.

1. For each entity from the inventory: what states can it be in? What transitions move it between states? Who (user, automated process, external system) triggers each transition?
2. For each surface: what state does it carry? What does it show in each of its possible states?
3. Write a draft `SPEC.md` using `spec-author` — prose-first, plain language, structured on the spine (Purpose / Entities / States & transitions / Actors / Invariants / Cross-section composition / Glossary).
4. Mark anything you can't determine from the code alone with `⟨DECIDE⟩` and a one-line question. Do not guess intent.

Done when: `SPEC.md` exists with all known sections filled and all unknowns marked `⟨DECIDE⟩`.

---

## Step 3 — Build the surface registry

**Goal:** Every surface is named once and pinned to a file:line.

1. For each surface in the spec, find the file and line where it is generated or rendered.
2. Record in `data/surface_registry.md`: surface name | owning file:line | test that asserts it exists.
3. A surface with no owning file:line is an inventory gap — investigate or mark `⟨DECIDE⟩`.

Done when: every surface in SPEC.md has a row in the registry with a real `file:line`.

---

## Step 4 — First artifact snapshot as diff baseline

**Goal:** A recorded snapshot of every output so future changes are visible as diffs, not surprises.

1. Run the project and capture every user-facing output (save HTML, screenshot, or record CLI output).
2. Store snapshots in `data/snapshots/YYYY-MM-DD/`.
3. Note the version or commit hash these snapshots belong to.

Done when: snapshots exist for all outputs from the inventory.

---

## Step 5 — Derive the test matrix from the spec

**Goal:** Every spec invariant, state, and transition has a matrix row with a test level assigned.

1. Use `templates/TEST_MATRIX.template.md` as the starting point.
2. For each invariant in SPEC.md: one row, test level assigned (string / DOM / browser / pixel). Visibility and layout facts get level >= browser-computed.
3. Mark all rows `TODO` — they will be filled in as tests are written.

Done when: `TEST_MATRIX.md` exists with a row per spec invariant, all marked TODO.

---

## Step 6 — Incremental from here

From this point, the project is on the standard pipeline. Every new wish enters at Step 0 (intake) and flows through `spec → prove → matrix → test → code → verify → commit`. The adopt procedure is complete.

**First recommended action after adoption:** run `product-prover` on the whole spec to find the gaps that the reverse-spec pass missed. Fold every must-fix before writing new tests.
