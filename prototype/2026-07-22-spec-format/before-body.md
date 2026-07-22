#### Intake: classifying and shaping a wish

**Several open questions arrive on one decision page.** They arrive together instead of one at a time in chat.
- The page opens in its own window; the rest of the work carries on while it waits [INV-4].
- Each question is a card — the recommended answer marked, with room to write a different one.
- Once the page comes back answered, the pipeline files it in the project's decision archive — the directory `docs/decisions/`, one name for this surface everywhere the pack refers to it — and folds every answer into its queue row the same session. An answer left unread is a decision lost.
- The person's word settles it; the click only records a first pick: an option picked and then taken back in plain speech is withdrawn, logged as answered-then-withdrawn, and asked again later in plainer terms. A pick made without understanding settles nothing that needs the person's considered word [INV-9].
- A withdrawn decision converges: after two withdrawals the recommended option is taken as a surfaced `[default]`. An answered question closes forever [INV-59], but a withdrawal re-asks in plainer terms with no cap of its own [INV-9], so a genuine taste call could loop unbounded. The bound is two: on the second withdrawal of the same decision the session takes the recommended option and surfaces it as a `[default]` in the landing report, silence stays consent from there and it is never re-asked [INV-31] — the same convergence an answered question already has [INV-59], now given to the withdrawal path. A later real change of mind rides the ordinary channel as a new wish, never a reopening of the closed decision. [INV-130]
- How the page works — the filename, the ordering, the round-trip — is written down once, in the communicator skill's rule 10 [INV-13].

[E-22]

**A decision card asks in consequences; the mechanism trails.** A decision card opens with what each option changes for the person: what it gives them, or what problem it removes, in the product's own words. The mechanism follows only where it aids the choice. Each option is labelled by its consequence, never by its implementation. A card that cannot be answered without understanding the mechanism is a defect of the card [INV-28 kin]. [INV-32]

**A wish is classified by size, priority, and work-kind.** Size uses one four-word vocabulary everywhere: bug, small, surface, large. The queue's class column uses the same four words and no second size scale. The door is a separate axis — where the wish enters the pipeline. Size is a separate question.

Priority is normal unless the row states otherwise, with two marks:
- **Critical** — the shipped product is broken for its user: an unusable surface, lost data, or a violated safety gate.
- **Quick win** — low effort, immediate value, no design decision inside.

When the classifier cannot call a size, a priority, or a work-kind [T-16], it asks the human at intake and does not guess. Until the human answers, the wish carries normal priority; its kind is the host's recorded default, or none; a kind not yet named scales nothing down [INV-22]. The open question stays in the row while the lane keeps moving [INV-4]. [INV-12]

**A large wish negotiates scope, never time.** The walk does not ask how long a wish will take, and does not accept an estimate in hours or days as an input. When a wish is larger than its worth, the walk answers in scope terms and proposes one of two moves:
- **cut the scope** — fewer surfaces in, plainer defaults on what stays;
- **split into stages** — each stage lands through the full pipeline on its own (the large size decomposes this way [INV-12]).

The proposal proceeds on the recommended option; the lane does not park on it [INV-4]. Every cut appears in the same batched report as every taken default [INV-18], and is never silent [INV-5].

**A proven artifact settles a fork before the human hears it.** Before surfacing a design choice, a session checks whether an existing proven artifact — the architecture, the spec, the invariants — already determines the answer. When it does, the session derives the requirement and says it back with the section cited as its ground, offering no fork. A fork reaches the human only for what the artifacts leave genuinely open: a taste call, or a real trade-off with no artifact-grounded winner. This is the read-the-doc twin of ask-never-guess [INV-4] — that rule forbids inventing an answer, this one forbids offering a choice the documents have already made. It sharpens the pre-ask scan's decide-or-verify gate [INV-4, INV-81] for design forks specifically. Its home is the base rulebook beside ask-never-guess; row 259's entry impact-analysis station cites it as the verdict of its three-source read. [INV-121]

A cut surface returned later is a new wish. A scope cut changes scope only, never order: it is not a quick-win mark, and only priority moves the lane [T-11].

No cut touches the delta's mandatory sentences — the fences [T-14], a kept surface's facets [INV-18], the non-goals, and the success measure [INV-20, INV-21]. Scope adjusts richness. [T-15]

**One wish is one user story; a row closes only whole.** A wish carrying several user stories — several distinct things a person will do and see — is split at intake, each story its own row through the full pipeline.

This differs from a stage split: a stage slices one story's depth [T-15], while separate stories are never fused into one row. Sub-behaviours of one story — its hover face, its phone face, a backpointer — are that story's acceptance, folded into that same row.

The classifier asks the human at intake whether a wish is one story or two, and does not guess [INV-12]. A split loses nothing: every row it produces cites the one spoken wish it came from [INV-1]. [T-17]

**A multi-leg row enumerates per-leg acceptance.** Where a row still carries several legs — a legacy fusion or a harvested batch — its Done-when enumerates per-leg acceptance, and the row does not close with an unmet leg. Half-done is a status, never a landing. The resume file's LIVE-STATE supersession does not compress an unfinished leg out of existence: a leg still open at compaction is restated in full [M-2]. [INV-26]

