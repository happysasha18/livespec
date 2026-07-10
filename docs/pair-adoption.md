# Adopting as a pair — an engine and its instance

Some projects hold two things at once. A generic mechanism does the work, and one concrete product
uses that mechanism to serve a real person today. A gallery engine hangs one photographer's photos.
A coaching engine reads one producer's tracks. This page is for the developer who wants to split
those two into separate repos and run each one under the pack. It explains the shape of the split
and points at the normative homes. The spec stays the law; this page reads it in plain order.

The generic mechanism is the **engine**. The concrete product that uses it is the **instance**.

## When the split applies, and who decides

The split applies only when a reusable product carries content of its own. A project that answers
personal, or answers reusable and stays one product, never reaches this question. When the reusable
answer lands on a product that already carries content, founding asks one more question: is the
generic mechanism worth its own home, apart from the content it serves right now?

The pack proposes the split. The human's word decides it. Both answers are recorded. Declining is a
full and normal outcome. When the human declines, the session records a one-line reuse note in the
host profile and raises the offer again only when the product outgrows one home, which happens when
a second instance appears or when the content and the mechanism start fighting for the same file.
Adoption owes the same proposal at its orient phase, beside the other founding questions. The
normative home for this clause is the founding-questions section of the spec, in PRODUCT_SPEC.md
under code INV-85.

## What each home owns after the split

The engine repo owns the mechanism. It is public by default, generic, and tested on its own generic
fixtures. It carries a **content contract** that names every place a concrete instance plugs in. The
engine owns the how.

The instance home owns the content. It holds the content itself, the corrections that content earns,
and the private fragments. The instance owns the what.

Heavy binaries follow the architecture placement guidance. An image archive, audio, video, or model
weights name their home in the placement view: object storage, or the machine's archive plus a named
backup. A git repository is the wrong home for large binaries, so a run that finds one there raises
it as a finding. The spec states what each home owns (PRODUCT_SPEC.md, INV-85); the architecture
method page states the placement rule (docs/architecture-method.md, heavy binaries).

## Running the pair day to day

Each repo of the pair is a full project under the pack. The engine repo and the instance home each
carry their own spec, queue, journal, inbox, and `.live-spec/` folder. No third document spans the
pair. The engine's spec states what the mechanism does for any instance, and it cites no instance's
content, since a spec that names these photos has stopped being generic. The instance's spec states
what this product is for its real user, in that user's own words.

One window serves one repo of the pair. When a window is unsure which repo it serves, it asks and
never guesses. A window is read-only on the pair's other half, save for one inbox file. The
instance's inbox is the human's front door, since the instance is the product they actually hold.

A lesson crosses between the two repos through the inbox door alone. The learning window files one
new inbox file into the other repo and journals the hand-off in its own tree. A lesson's travel
never writes a foreign repo. The normative home for pair leadership is the spec's pair clause
(PRODUCT_SPEC.md, INV-86).

A catch-up ask crosses the seam the same way. When the owner asks one window to bring the pair up
to the current pack and means both halves, that window runs the catch-up walk (MIGRATION.md) for
its own repo only, and files one inbox wish naming the other half's catch-up debt. The other
repo's own session executes its half. A pair half that carries no `.live-spec` records of its own
starts with the full adoption for that repo before any catch-up items.

## The worked walk — one wish crosses the seam

A user wish arrives at the instance window, for example a wish to let a visitor filter the gallery
by year. Intake places it on the instance's map and finds two parts: a generic part that any
instance could use, and this instance's own part. At the seam that is two wishes, split at intake.
Each new wish cites the one spoken wish.

The instance window is an outsider to the engine. It files the engine-shaped part as one engine inbox
wish. It parks its own half as a dated blocked-on-engine line, so its lane keeps moving.

The engine's session sweeps its inbox and lands the wish through the full pipeline on the engine's
own generic fixtures. A new plug-in point becomes a named content-contract entry with a
works-without-it test. The engine ships and versions on its own rhythm.

The instance then updates to that engine version, plugs its real content into the new entry, and
verifies on the real product. The instance's suite proves what the engine's generic suite by
construction cannot reach. The parked line un-parks and closes whole. The next instance inherits the
feature with no engine work, and both journals hold their half. The spec states this scenario
(PRODUCT_SPEC.md, F-pair).

## Migrating an existing single repo into a pair

A project that already holds an engine and its instance in one repo migrates in three moves.

First, run the ordinary adoption for each new home. The adoption run gives each repo its version
control baseline, its inventory, its re-engineered documents, its architecture and matrix, and its
attach record. The procedure is the same one every host uses (docs/adoption.md).

Second, carve the engine by the content-contract law. Every donor-specific constant found while
carving becomes a named content-contract entry with a works-without-it test. The engine keeps no
trace of the instance it grew from.

Third, rewrite only the documents the owner rejected or the split forces open. All new human-facing
text goes through a clean writer: prepare a plain brief that states the facts, names the reader, and
lists the register laws, then hand it to a fresh writer session with no pack rules loaded. The unit
is the section the edit touches. A blanket rewrite of settled prose is refused by law; a whole page
is redrafted only on the human's word. The clean-writer road covers every new page (base rule 21,
skills/live-spec-base/SKILL.md).

## Two decisions the owner keeps

Two choices stay open, and the owner makes each one.

The first choice is how to read the two queues. One option stitches a single wish-list view across
both queues. The other keeps two plain queues, each read on its own. The queues stay per-repo either
way. The recommended pick is two plain queues, held until real friction, such as flipping between two
windows to follow one wish's halves, earns a stitched view (PRODUCT_SPEC.md, D-6).

The second choice is how deep the instance's spec reaches into the engine. One option lets the
instance spec cite engine internals. The other lets it cite only the engine's contract-entry handles.
The recommended pick is contract-entry handles alone, since a handle is the engine's versioned public
promise, while an internal rots at the engine's next refactor (PRODUCT_SPEC.md, D-7).
