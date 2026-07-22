# MAPPING — codes, consumed index rows, and atomic-claim coverage

This file proves the rewrite dropped nothing. Part 1 maps every code the source section cites to its new home. Part 2 states which of those codes carried a consumed Formal-index row. Part 3 maps every behavioural claim of the source to the criterion that now carries it.

## Part 1 — every cited code → its new home

`Rn` names Requirement n in `section.md`. A code in several requirements is anchored in each. `D-1` lives inside a `[GAP]` line, its home marked "(GAP)". Zero codes are dropped: all 96 cited codes appear in `section.md` (verified mechanically — cited-set minus present-set is empty).

| Code | New home | Index row consumed? |
|---|---|:--:|
| F-bootstrap | R2 | no (inline feature) |
| F-adoption | R10 | no (inline feature) |
| F-catchup | R13 | no (inline feature) |
| F-onboarding | R19 | no (inline feature) |
| F-pair | R20 | no (inline feature) |
| B-1 | R2 | yes |
| B-2 | R3, R5, R6 | yes |
| B-3 | R4 | yes |
| A-0 | R1 | yes |
| A-1 | R3, R5, R6, R10 | yes |
| A-2 | R10 | yes |
| A-3 | R10 | yes |
| A-4 | R11, R12 | yes |
| A-5 | R1, R10, R13, R15 | yes |
| A-6 | R10 | yes |
| A-7 | R10, R21 | yes |
| A-8 | R10, R13 | yes |
| A-9 | R12 | yes |
| A-10 | R7, R11 | yes |
| A-11 | R13 | yes |
| E-1 | R20 | yes |
| E-3 | R20 | yes |
| E-4 | R20 | yes |
| E-6 | R2 | yes |
| E-7 | R10 | yes |
| E-9 | R12 | yes |
| E-10 | R10 | yes |
| E-11 | R20 | yes |
| E-13 | R3, R4, R6, R19 | yes |
| E-14 | R10, R20 | yes |
| E-15 | R10 | yes |
| E-16 | R14, R21 | yes |
| E-17 | R11 | yes |
| E-20 | R20 | yes |
| E-21 | R21 | yes |
| E-23 | R21 | yes |
| E-25 | R10, R21 | yes |
| E-32 | R21 | yes |
| T-10 | R20 | yes |
| T-13 | R6 | yes |
| T-16 | R6 | yes |
| T-17 | R20 | yes |
| M-2 | R10 | yes |
| M-7 | R10, R13, R14, R21 | yes |
| INV-1 | R20 | yes |
| INV-4 | R3 | yes |
| INV-5 | R3 | yes |
| INV-7 | R12 | yes |
| INV-8 | R1 | yes |
| INV-9 | R4 | yes |
| INV-10 | R20 | yes |
| INV-11 | R20 | yes |
| INV-12 | R3 | yes |
| INV-16 | R11 | yes |
| INV-27 | R20 | yes |
| INV-28 | R21 | yes |
| INV-30 | R6, R8, R9 | yes |
| INV-31 | R19 | yes |
| INV-36 | R6, R7, R19 | yes |
| INV-37 | R6, R20 | yes |
| INV-39 | R16, R17 | yes |
| INV-56 | R20 | yes |
| INV-67 | R19 | yes |
| INV-72 | R8 | yes |
| INV-75 | R5 | yes |
| INV-77 | R8 | yes |
| INV-79 | R5, R20 | yes |
| INV-83 | R9, R19 | yes |
| INV-84 | R19 | yes |
| INV-85 | R5 | yes |
| INV-86 | R20 | yes |
| INV-87 | R19 | yes |
| INV-88 | R19 | yes |
| INV-89 | R13, R14 | yes |
| INV-90 | R14 | yes |
| INV-91 | R13, R21 | yes |
| INV-92 | R15 | yes |
| INV-107 | R16 | yes |
| INV-110 | R16, R18 | yes |
| INV-111 | R16, R17 | yes |
| INV-113 | R17 | yes |
| INV-114 | R16, R17 | yes |
| INV-119 | R20 | yes |
| INV-125 | R8 | yes |
| INV-126 | R8 | yes |
| INV-128 | R7 | yes |
| INV-134 | R7 | yes |
| INV-135 | R7, R8 | yes |
| INV-136 | R8 | yes |
| INV-139 | R9 | yes |
| INV-159 | R21 | yes |
| INV-163 | R7, R8, R9 | yes |
| INV-172 | R21 | yes |
| INV-177 | R21 | yes |
| INV-184 | R21 | yes |
| INV-227 | R13, R21 | yes |
| ACT-1 | R21 | yes |
| ACT-3 | R4 | yes |
| D-1 | R12 (GAP) | yes |
| D-7 | R20 | yes |

## Part 2 — consumed Formal-index rows

The section cites 100 code tokens resolving to 96 distinct codes. Of those, **95 carry a Formal-index row** and all 95 are consumed — each row's meaning now lives at the home named in Part 1. The 5 `F-*` feature codes are declared inline in the source (`[feature: F-bootstrap]`) and have no index row; they are preserved as feature anchors on the matching requirement title. No index row consumed by the section is left without a home.

Some cited codes are pure cross-references in the source (the section leans on a rule owned by another section rather than restating it): `INV-5`, `INV-31`, `E-7`, `E-23`, `INV-72`, `INV-77`, `INV-125`, `INV-126`, `INV-159`, `INV-163`, `D-1`, `D-7`. Each is preserved as a trailing anchor at the requirement that leans on it; its full behaviour stays defined in its own section, not re-converted here.

**Cross-section glossary note.** A handful of domain nouns the section uses are owned by other sections of the full document and are defined in their home glossary, not repeated here (per the reuse-by-reference rule): *feel pass*, *register lint*, *placement*, *surface registry*, *milestone*, *hooks*, *clean-writer road*, *snapshot machinery*, *dev-machine skill sync*, *economy setting*, *checkpoint discipline*. In a whole-document conversion these live once in the shared glossary; this pilot adds only the nouns this section introduces.

## Part 3 — atomic-claim coverage

Every behavioural claim of the source section, in source order, mapped to the criterion (or criteria) that now carries it. "R19.4" means Requirement 19, criterion 4.

### Bootstrap + the version-control gate

| # | Source claim | Criterion |
|---|---|---|
| 1 | The version-control gate runs first, in the same order adoption keeps. | R1.1 |
| 2 | Git must exist; initialize it if missing. | R1.2 |
| 3 | Settle a remote or decline it explicitly before creating anything. | R1.3 |
| 4 | A recommendation does not close the gate. | R1.4 |
| 5 | Never deliver into an unversioned host. | R1.5 |
| 6 | Copy the document templates and the suite scaffold into `tests/`. | R2.1 |
| 7 | The scaffold's green = document set exists, headers filled, coverage checklist present, one live-state block. | R2.4 |
| 8 | A leftover placeholder counts as red. | R2.5 |
| 9 | Green is a starting floor; delivery #1 ships its own first real test. | R2.6 |
| 10 | Offer hooks at bootstrap, never impose, plain words first. | R2.2 |
| 11 | The first request enters the queue and runs from intake. | R2.3 |

### Founding questions — personal vs reusable

| # | Source claim | Criterion |
|---|---|---|
| 12 | Ask the founding questions in the spec opening before the first request; do not infer. | R3.1 |
| 13 | Personal-tool-or-reusable-product is asked first. | R3.2 |
| 14 | A founding answer checks the personal profile first, else asks; says so aloud when seeded. | R3.4, R3.5 |
| 15 | Never derive the answer from example artifacts. | R3.6 |
| 16 | This question is stronger than proceed-on-default; it blocks the first request. | R3.3 |
| 17 | An inferred founding answer is the silent micro-decision at its most expensive. | R3.6 |
| 18 | Adoption owes the same question at orient. | R3.7 |

### Founding — learn who the human is

| # | Source claim | Criterion |
|---|---|---|
| 19 | Look for the personal profile first, at founding, orient, and a new machine/human. | R4.1 |
| 20 | If it exists, load it, name the file, read unrecognized lines aloud. | R4.2 |
| 21 | If absent, offer to create it from the template. | R4.3 |
| 22 | The human tells about themselves or names sources; propose lines. | R4.5 |
| 23 | Every line lands on the human's word; write told lines faithfully; accept/drop proposals one at a time; a dropped proposal stays dropped. | R4.4, R4.5 |
| 24 | The template marks every placeholder as a placeholder. | R4.6 |
| 25 | The human can decline the whole step; run on defaults, offer returns next setup. | R4.7 |
| 26 | Skip where nothing is left to do; a later session loads the profile. | R4.8 |
| 27 | A worker session never onboards; its brief carries the setting lines. | R4.9 |

### Founding — the engine/instance split

| # | Source claim | Criterion |
|---|---|---|
| 28 | When reusable lands on a content-carrying product, founding proposes the split, never imposes; the human decides; both outcomes recorded. | R5.1 |
| 29 | The proposal names two homes and what each owns (engine + instance). | R5.2 |
| 30 | Binary content placed per the placement prompt. | R5.3 |
| 31 | A donor-specific constant becomes a named content-contract entry with a works-without-it test. | R5.6 |
| 32 | A single-repo project is a complete outcome; a decline records `reuse.split-declined: <date>`. | R5.4 |
| 33 | Taking the split binds the pair-leadership rules from that moment. | R5.5 |
| 34 | The offer returns only when the product outgrows one home (a second instance, or content and mechanism can no longer share a file). | R5.7 (+ GAP) |
| 35 | Adoption owes the same proposal at orient. | R5.8 |

### Founding — project kind

| # | Source claim | Criterion |
|---|---|---|
| 36 | Founding asks the project kind; record it on a `project.kind` line. | R6.1 |
| 37 | Adoption asks the project kind again at orient. | R6.2 |
| 38 | Three intake verdicts stay separate: project kind, work type, placement. | R6.4 |
| 39 | Keep a recorded `work-kind.host-default`; the kind never silently overrides it. | R6.5 |
| 40 | The ask always belongs to the human; no personal-profile line states a host's kind. | R6.3 |
| 41 | Curate the kind vocabulary; a custom kind joins through the queue. | R6.6 |
| 42 | The line stays alive; update on the human's word and journal it at that moment. | R6.7 |

### Founding — concrete layers and proof kinds

| # | Source claim | Criterion |
|---|---|---|
| 43 | Founding records `project.layers` and `project.proofs` beside the kind. | R7.1 |
| 44 | The three footprints hold across kinds; the layers are the project's own. | R7.2 |
| 45 | A kind recorded with no layers and no proofs is incomplete, flagged at adoption. | R7.3 (+ GAP) |
| 46 | The footprint check and test-level rule read the declared categories. | R7.4 |
| 47 | The architecture carries the per-kind footprint-and-proof table; spec/test roles read the declared layers/proofs. | R7.5 |
| 48 | live-spec ships the shape and leaves the concrete assertion to its products. | R7.6 |

### Founding — design principles

| # | Source claim | Criterion |
|---|---|---|
| 49 | A visual-kind founding declares a `project.design-principles` line. | R8.1 |
| 50 | A visual kind recorded with none is flagged. | R8.2 |
| 51 | The verify pass reads and runs each principle in the medium's own form. | R8.3 |
| 52 | Suite-cannot-green principle → human's eye; suite-can → matrix row. | R8.4 |
| 53 | The frontend starter set gathers frontend guidance and adds the interactive-overlap rule. | R8.5 |
| 54 | Interactive controls from different layers hold separate clickable regions; non-interactive elements may overlap. | R8.6 |
| 55 | The prover reports the cross-surface overlap blind spot as a finding on the spec. | R8.7 |
| 56 | Per covering overlay, the product suite asserts every other interactive control is not rendered or not pressable. | R8.8 |

### Founding — the legibility floor

| # | Source claim | Criterion |
|---|---|---|
| 57 | The floor's numbers (4.5:1 normal, 3:1 large, ≥12 px body/caption; host may set its own). | R9.1 |
| 58 | The verify feel pass reads a surface's computed colours and sizes. | R9.2 |
| 59 | The pre-show legibility lint reads the declared colours and sizes. | R9.3 |
| 60 | A below-floor result blocks the showing until lifted. | R9.4 |
| 61 | The pack ships law + numbers + script; the product ships the assertion. | R9.5 |

### Adoption — the ordered phases

| # | Source claim | Criterion |
|---|---|---|
| 62 | Orient reads every existing document before touching anything and answers the founding questions. | R10.1 |
| 63 | Inventory lists code, surfaces, and documents, each with its owner (surfaces to file:line). | R10.2 |
| 64 | Listing surfaces seeds the surface registry. | R10.3 |
| 65 | Adoption's working artifacts live git-tracked in `.live-spec/adopt/`, not scattered. | R10.4 |
| 66 | An existing spec becomes spec sections, claims marked unverified. | R10.5 |
| 67 | Inventory seeds architecture nodes; existing tests → matrix rows; roadmap/TODO → queue rows. | R10.6 |
| 68 | Reconcile every unverified claim at the first delivery that touches it, or by the first milestone. | R10.7 |
| 69 | The version-control gate runs first, before touching or moving anything. | R10.8 |
| 70 | Save a first baseline snapshot as found, git-tracked, as the diff baseline the snapshot machinery guards. | R10.9 |
| 71 | Incremental thereafter: same lifecycle; record installed skill versions at attach. | R10.10 |
| 72 | On a version change, re-read the changed skill and journal old→new. | R10.11 |
| 73 | Re-check at every safe breakpoint; ask the public repo once a day. | R10.12 |

### Adoption — the unbacked-surface verdict

| # | Source claim | Criterion |
|---|---|---|
| 74 | Flag every unbacked live surface at orient for the human's per-surface verdict. | R11.1 |
| 75 | Promote → enter at the spec step as a feature. | R11.2 |
| 76 | Quarantine → prototype home, label, dated provenance record; a production change. | R11.3 |
| 77 | Attic → archive it. | R11.4 |

### Adoption — attic over deletion

| # | Source claim | Criterion |
|---|---|---|
| 78 | A superseded file moves to the attic with a manifest line; nothing deleted. | R12.1 |
| 79 | The attic is append-only, one manifest line per file. | R12.2 |
| 80 | On a basename collision, prefix with source directory, then a numeric ordinal. | R12.3 |
| 81 | Flat-with-manifest vs dated subfolders stays an open decision. | R12.5 (GAP, D-1) |
| 82 | The cruft sweep lists counts/sizes and deletes only on the human's explicit OK. | R12.4 |
| 83 | Authored content never qualifies for the sweep; it always goes through the attic. | R12.5 |

### Catch-up — the sequence and its phases

| # | Source claim | Criterion |
|---|---|---|
| 84 | A release owing host actions ships a dated, versioned migration chapter; one owing nothing adds none and says so. | R13.1 |
| 85 | The work list is the ordered chain of chapters from the host's version forward, oldest first. | R13.2 |
| 86 | No readable version → start at the earliest chapter. | R13.3 |
| 87 | Four phases in fixed order: orient, plan, execute, verify. | R13.4 |
| 88 | Orient reads records, tree, pack version, and journal; the tree is the truth on disagreement. | R13.5 |
| 89 | The delta includes never-answered founding questions; orient reads `founding.set-version`. | R13.6 |
| 90 | The plan lives in `.live-spec/adopt/`, lists moves and conflicts; the owner's word precedes any move; a nothing-to-do walk ends. | R13.7 |
| 91 | Execute opens with a clean-tree baseline commit under the checkpoint discipline and resumes from the checkpoint. | R13.8 |
| 92 | Verify runs the host's gates including the suite, stays open until green, re-records the installed-set, lands one journal chapter. | R13.9 |
| 93 | Machine-level steps run once per machine; an already-done check skips them. | R13.10 |

### Catch-up — half-done safety and preserve-and-re-home

| # | Source claim | Criterion |
|---|---|---|
| 94 | Each step reads its precondition from the tree. | R14.1 |
| 95 | A step whose end state holds is skipped. | R14.2 |
| 96 | Both old and new form present → merge file by file. | R14.3 |
| 97 | Identical content on both sides → drop the old copy to the attic. | R14.4 |
| 98 | A differing profile is reconciled by the settings ladder. | R14.5 |
| 99 | A move up follows the promotion law and re-reads the shared file first. | R14.6 |
| 100 | Any other differing file rides the plan to the gate; never nest a directory in its replacement; never overwrite new with old. | R14.7 |
| 101 | Settled prose is rewritten only where rejected or unholdable; the plan carries each rewrite. | R14.8 |
| 102 | A host's own document names are kept, recorded as a host-profile line; the canonical name is read under it. | R14.9 |
| 103 | An outdated installed-set record retires to the attic; the record is read from disk; disk is authoritative. | R14.10 |
| 104 | Stray state files re-home (root checkpoint, closed checkpoint, look-alike directory). | R14.11 |

### Catch-up — proof and restore

| # | Source claim | Criterion |
|---|---|---|
| 105 | Record a pre-sequence inventory (fingerprint, anchor multiset, suite verdict). | R15.1 |
| 106 | Re-record the same inventory after execute and compare. | R15.2 |
| 107 | Every difference is accounted for by a plan item; the suite reads at least as green. | R15.3 |
| 108 | A difference outside the plan blocks verify until accepted or reverted. | R15.4 |
| 109 | The plan names the baseline commit and the one restore command. | R15.5 |
| 110 | The attic keeps every superseded file readable without a restore. | R15.6 |
| 111 | A docs-only sequence skips the facet sweep and opens the plan by the ordinary show rule. | R15.7 |

### Catch-up — the same-version layout vehicle

| # | Source claim | Criterion |
|---|---|---|
| 112 | A no-version-delta docs restructure routes to the host queue and runs one named vehicle. | R16.1 |
| 113 | Decisions checkpointed before any move; a clean pushed base gives a one-command restore. | R16.2 |
| 114 | Content proven by word-token and punctuation multiset checks. | R16.3 |
| 115 | The full suite reads green from the log's own line. | R16.4 |
| 116 | One journal chapter names what moved and why. | R16.5 |
| 117 | A branch-back closes through the merge gate (multiset as first part); a direct-main pass stands on its own suite. | R16.6 |
| 118 | A host cites the vehicle and never improvises a layout pass. | R16.7 |

### Catch-up — the merge gate

| # | Source claim | Criterion |
|---|---|---|
| 119 | The merge gate judges the delta in three parts (token identity + punctuation, green suite, delta-scoped prover). | R17.1 |
| 120 | It blocks on an unmatched token, red suite, new-side finding, or unnamed meaning change. | R17.2 |
| 121 | Pre-existing findings equal on both sides route to queue rows and do not block. | R17.3 |
| 122 | A deliberate redesign routes by the redesign law; its merge stands on suite + prover, no token demand. | R17.4 |
| 123 | A session that sharpens the spoken bar says the sharpened form back and marks it its own. | R17.5 |

### Catch-up — routing and non-goals

| # | Source claim | Criterion |
|---|---|---|
| 124 | Catch-up fires only when the recorded version is behind current. | R18.1 |
| 125 | A no-delta ask routes to the host's own queue row. | R18.2 |
| 126 | Catch-up does not fire on first adoption, a single-document edit, or a product restructure. | R18.3 |
| 127 | Non-goals: no automating script, no forced rename, no pack-side registry of catch-up states. | R18.4 |

### Meeting the settings — the card

| # | Source claim | Criterion |
|---|---|---|
| 128 | Render the card at founding's end and at orient's end once kind and economy have settled. | R19.1 |
| 129 | The card lists every setting: name, current value, one change-line; a default shown as told; asks nothing. | R19.2 |
| 130 | Each value is read from the settings ladder. | R19.3 |
| 131 | The card opens by the show rule and passes the pre-show register lint on copy and rendered values. | R19.4 |
| 132 | The standing question is answered by the same card re-rendered from current truth; no hand-kept copy answers. | R19.5 |
| 133 | Both derive from one source: the pack-defaults table joined with profiles and host lines; no second list. | R19.6 |
| 134 | Completeness both ways; a missing card-visible row and a sourceless card row are each a defect. | R19.7 |
| 135 | The fixed copy states rules; a personal value shows only as the reader's own, labelled theirs to change. | R19.8 |
| 136 | The fixed copy never presents one person's value as the product's prescription. | R19.9 |
| 137 | A build-time script renders the card and fails loudly on a malformed row. | R19.10 |
| 138 | A missing profile renders on defaults, says so, names the founding offer. | R19.11 |
| 139 | A new table row gets its card copy drafted on the clean-writer road before it first renders. | R19.12 |
| 140 | Facets: one column on a phone/narrow window, multi-column otherwise. | R19.13 |
| 141 | Facets: static HTML, keyboard-scrollable, no hover dependence. | R19.14 |
| 142 | Facets: empty state (missing profile), error state (malformed row, loud), blocked state (flagged text stops the showing). | R19.15 |
| 143 | Facets: read-only render, concurrent-safe; an open card shows its render-moment truth. | R19.16 |

### Running an engine and its instance as a pair

| # | Source claim | Criterion |
|---|---|---|
| 144 | Each repo is a full host with its own spec/queue/journal/`.live-spec/`; no third document spans the pair. | R20.1 |
| 145 | The engine's spec is generic and cites no instance content; the instance's spec is real-user and cites the engine only by handles. | R20.2 |
| 146 | A both-shaped request splits into one row in each queue, each citing the one spoken request. | R20.3 |
| 147 | Each repo has its own inbox; the instance's is the human's front intake point. | R20.4 |
| 148 | A lesson crosses only through the inbox under write-ownership, with a journalled hand-off and no foreign write beyond one file. | R20.5 |
| 149 | One window serves one repo, read-only on the other half save one inbox file; the concurrent-edit fence binds inside each. | R20.6 |
| 150 | The load-bearing crossing: file the engine part, park a dated blocked-on-engine debt line, keep the lane moving. | R20.7 |
| 151 | The debt line appears in every status report until the engine ships. | R20.8 |
| 152 | The engine sweeps its inbox, lands on generic fixtures, makes each plug-in a contract entry with a works-without-it test, ships on its own rhythm. | R20.9 |
| 153 | The instance updates, plugs real content, verifies on the real product, un-parks and closes whole. | R20.10 |
| 154 | The engine's spec cites only its own public commits and gives each mechanism a neutral name. | R20.11 |
| 155 | A locale label is noted as instance-supplied; the neutral term stays the one name. | R20.12 |
| 156 | The publish gate checks two leaks (private provenance hash, locale label as mechanism name). | R20.13 |
| — | Pair regression fences (a declined split runs as today; the three verdicts stay a closed three; the cross-seam channel reuses inbox/write-ownership/fence). | Carried by R20 context + R6.4, R20.6 anchors; stated as source regression fences, not re-converted. |
| — | Pair non-goals (no repo-layout mandate, no auto extraction, no cross-repo atomicity, no new sharing model). | Source non-goal statement; noted, not converted to a criterion. |

### How the skills arrive and how a machine learns a newer pack exists

| # | Source claim | Criterion |
|---|---|---|
| 157 | The installer copies every pack skill into the skills home. | R21.1 |
| 158 | It is idempotent: timestamped backup before overwrite; deletes nothing. | R21.2 |
| 159 | The backup lands in an attic folder beside the skills home, not inside it. | R21.3 |
| 160 | The installer writes to `.live-spec/` exactly what adoption's record clause writes. | R21.4 |
| 161 | The update check runs once a day, throttled by a dated stamp; asks the public VERSION on main; is the outward twin of the skill sync. | R21.5 |
| 162 | A newer remote → propose in chat (both versions, what changed, install road); installs nothing. | R21.6 |
| 163 | No network / unreadable → one honest skip line naming the address; stamp unwritten to retry; never blocks or guesses. | R21.7 |
| 164 | A machine ahead reads as up to date; never proposes a downgrade. | R21.8 |
| 165 | The check's only face is the proposal line, under the plain-language register. | R21.9 |
| 166 | It reads the ratchet manifest pins and names the stale vendored files, each with its re-install road. | R21.10 |
| 167 | A host with no manifest gets the plain version proposal. | R21.11 |
| 168 | The founding arm reads `founding.set-version` and names each never-answered founding question beside the vendored report. | R21.12 |
| 169 | No readable set-version → every question named as potentially owed. | R21.13 |
| 170 | A never-answered question is surfaced for the owner at catch-up; the pack answers none (forward-binding); the homes are recorded. | R21.14 |
| — | Update-check non-goals (no background daemon, no auto-install, no per-skill remote diff). | Source non-goal statement; noted, not converted to a criterion. |

### Coverage result

170 behavioural claims mapped. Three source non-goal/regression blocks (pair fences, pair non-goals, update-check non-goals) are recorded as source policy statements carried in context and anchors rather than converted to `shall` criteria — they state what the system does **not** do, which the format keeps as prose. No behavioural `shall`-claim of the source is left uncovered.
