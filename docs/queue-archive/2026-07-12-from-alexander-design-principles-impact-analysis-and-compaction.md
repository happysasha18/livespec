> Harvested into ROADMAP rows 259-260 (2026-07-12).

# Wish — design principles: impact analysis at every request's entry + periodic compaction

From: Alexander, live word in the live-spec window, 2026-07-12 ~02:04.

His word (paraphrase): every incoming request gets an entry analysis that reads the spec AND the
architecture AND the code together and decides how to solve it. A feature that changes only
presentation logic is one kind of work; a feature that changes backend modules is another; a
cross-cutting change is a third. These analyses always run at the entry of every request. And do
not forget periodic compaction of docs and code: finding the right abstractions so everything is
more testable, more reusable, and workable in parallel. Formulate the proper design principles.

Formulated principles (drafted at his ask, 2026-07-12 ~02:10, for the pipeline to refine):

1. Impact analysis stands at every request's entry. Every incoming request (feature, bug, wish)
   is first triaged against three sources at once: the spec (what behavior changes), the
   architecture (which modules own it), the code (what actually gets touched). The change's
   footprint is named aloud before any work starts.
2. The footprint decides the route. A presentation-only change takes the light road. A change
   inside one backend module goes through that module's interface and tests. A cross-cutting
   change (several modules, or a shared law) always opens the full pipeline. The process weight
   matches the footprint in both directions.
3. Module boundaries are kept so a typical request lands in one module. The sign of a right
   boundary: an edit inside the module leaves its neighbors untouched. Requests that repeatedly
   cut across several modules are the signal to move a boundary.
4. An abstraction proves itself by three questions. Can it be tested alone. Does a second place
   need it. Can two people work on it and its neighbor in parallel without queuing on shared
   files. Three yes answers make it right; two no answers make it premature or false.
5. Compaction is a scheduled station. Docs and code take periodic compaction passes: duplicates
   merge, dead weight is removed with every removal listed (INV-109 covers the listing),
   ripened abstractions are extracted. Triggers: the MINOR-version audit, and the second
   occurrence of the same problem.
6. A reached level locks. After each compaction pass the bar is pinned by a test or a lint so it
   cannot slide back (the convergence principle, rows 216-218).

ADDENDUM (his word 2026-07-12 ~02:06): tests are part of these principles — the set must state the
test architecture too (how tests follow the footprint layers, make abstractions provable, and keep
parallel work safe). He authorized a deep Opus thinking pass to draft the set as a proper
architect would; the draft lands at .live-spec/checkpoints/pending-design-principles-architect-draft.md
and feeds this wish's queue rows.

ADDENDUM 2 (his word 2026-07-12 ~02:08): the formulation duty sits with the agent — he names the
direction, the agent thinks through what affects what and reminds him of a dimension he forgot
(tests were the example). And modularity applies to the PROCESS itself, tuned by PROJECT TYPE:
programming is one project kind; a photo portfolio, a music project, a promotion campaign each
have their own layer decomposition, their own module analogues, and their own test analogues
(lints, text provers, eye-walks). The principle set must state how the entry analysis, the
footprint categories, and the test ladder specialize per project kind instead of assuming code.

Kin to check at sweep: the door/kind classification the pipeline already runs (this wish adds the
LAYER/footprint dimension read from spec+architecture+code together); rows 216-218 (convergence);
row 257 candidate (architecture rework owes document rework); ARCHITECTURE.md's module map.
