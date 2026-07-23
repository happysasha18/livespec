# Live-row mapping — ROADMAP conversion (for orchestrator review)

Source pinned to git 859dcfc. Rounds 1-6 as before; round 7 adds the three-cell sweep (wish + status + acceptance) — verdict table below.
Override tables (rowconv.py): FORCE_ARCHIVE 99, 128, 445 (445 cell corrected + delegation line); STATUS_CELL_OVERRIDE 69, 55, 129, 131; SWEEP_OVERRIDES 420 (archive — audit COMPLETE, the lone open-marker hit is prose); closed-family live leader → *deferred* rule.

## Round 7 sweep — verdict table

Every live row rules 1/2/4/5 touched: id · evidence phrase · verdict · flag.

| id | evidence | verdict | flag |
|---|---|---|---|
| 54 | acceptance said "stays in-work" on its field leg | acceptance reads "stays open" | rule 5 rewrite |
| 130 | acceptance MET ×2 + LANDED 2026-07-06 ~16:36 whole | ARCHIVE 2026-07-06 | rule 1 |
| 133 | LANDED (legs 1+3); OPEN LEG: first real post-law ask | *deferred* — trigger: the law forbids firing uninvited, so the first real post-law | rule 2 |
| 134 | build leg MET; install + field legs — OPEN | *deferred* — trigger: the ledger entry flips back to SOLVED citing this row | rule 2 |
| 140 | build legs MET; applied once for real — OPEN | *deferred* — trigger: applied once for real — a budget-named session names its cut | rule 2 |
| 141 | build leg MET; install + field evidence — OPEN | *deferred* — trigger: the field evidence (a following tlvphoto session with no lea | rule 2 |
| 190 | two legs LANDED; tlvphoto validation — OPEN | *deferred* — trigger: validated against the tlvphoto/engine case read-only | rule 2 |
| 261 | LANDED 2026-07-14 whole; field beat waits: Discussion write | *deferred* — trigger: the live Discussion WRITE round-trip (a real discussion brid | rule 2 |
| 279 | status: ADOPTED + LANDED 2026-07-12, suite 588 green | ARCHIVE 2026-07-12 | rule 1 |
| 420 | acceptance: audit-and-build is COMPLETE, four candidates LANDED | ARCHIVE 2026-07-18 | rule 1 (SWEEP_OVERRIDES: prose 'rides' hit) |
| 436 | smallest-first opening landed; still deferred: value-space step | *deferred* — trigger: the value-space forcing step for each axis's in-between memb | rule 2 |

Row 279 read (rule 6): the status cell records the adopt branch executed whole — sweep to zero offences, gate wired red-first, suite 588 green — satisfying the acceptance's `if adopt` arm; the conditional wording is pre-landing text. Verdict: archive, 2026-07-12.

Counts: archived by sweep 3 (130, 279, 420) · queued→deferred 4 (133, 190, 261, 436) · re-triggered deferred 3 (134, 140, 141 — fallback→inline) · ambiguous 0 · acceptance rewrites 1 (row 54).

## Live rows

| id | new status | flag |
|---|---|---|
| 44 | *deferred* 2026-07-05 — revisit trigger: own version bump | clean |
| 48 | *deferred* 2026-07-05 — revisit trigger: own version bump | clean |
| 49 | *deferred* 2026-07-05 — revisit trigger: own version bump | clean |
| 54 | *deferred* 2026-07-07 — revisit trigger: first real run rides the next real founding/adoption | clean |
| 55 | *deferred* 2026-07-07 — revisit trigger: the machine leg rides row 3's landing | OVERRIDE |
| 69 | *deferred* 2026-07-05 — revisit trigger: the next edit to the product-prover skill | OVERRIDE |
| 93 | *deferred* 2026-07-05 — revisit trigger: the machine's FIRST REAL SYNC on a visual host (track-coach/tlvpho... | clean |
| 95 | *queued* 2026-07-05 | clean |
| 96 | *queued* 2026-07-05 | clean |
| 100 | *deferred* 2026-07-05 — revisit trigger: the first foreign-host run | clean |
| 108 | *deferred* 2026-07-06 — revisit trigger: installed-copy sync rides Alexander's `! sh ~/live-spec/install.sh... | clean |
| 117 | *deferred* 2026-07-06 — revisit trigger: installed-copy sync rides Alexander's `! sh ~/live-spec/install.sh... | clean |
| 118 | *deferred* 2026-07-06 — revisit trigger: installed-copy sync rides Alexander's `! sh ~/live-spec/install.sh... | clean |
| 119 | *deferred* 2026-07-06 — revisit trigger: installed-copy sync rides Alexander's `! sh ~/live-spec/install.sh... | clean |
| 129 | *deferred* 2026-07-06 — revisit trigger: the first real adopted host carries a project.kind line by deed | OVERRIDE |
| 131 | *deferred* 2026-07-06 — revisit trigger: the next working session narrates unprompted, with no third ask | OVERRIDE |
| 133 | *deferred* 2026-07-06 — revisit trigger: the law forbids firing uninvited, so the first real post-law ask r... | round-7 sweep |
| 134 | *deferred* 2026-07-06 — revisit trigger: the ledger entry flips back to SOLVED citing this row | round-7 sweep |
| 140 | *deferred* 2026-07-06 — revisit trigger: applied once for real — a budget-named session names its cuts aloud | round-7 sweep |
| 141 | *deferred* 2026-07-06 — revisit trigger: the field evidence (a following tlvphoto session with no leading c... | round-7 sweep |
| 143 | *deferred* 2026-07-06 — revisit trigger: re-read the wish's record in the status notes | NEEDS-TRIGGER |
| 144 | *deferred* 2026-07-06 — revisit trigger: re-read the wish's record in the status notes | NEEDS-TRIGGER |
| 148 | *queued* 2026-07-06 | clean |
| 163 | *queued* 2026-07-05 | clean |
| 165 | *deferred* 2026-07-07 — revisit trigger: first real struggle run | clean |
| 166 | *queued* 2026-07-07 | clean |
| 168 | *deferred* 2026-07-07 — revisit trigger: the first real remote-seat session | clean |
| 170 | *queued* 2026-07-10 | clean |
| 171 | *queued* 2026-07-08 | clean |
| 190 | *deferred* 2026-07-09 — revisit trigger: validated against the tlvphoto/engine case read-only | round-7 sweep |
| 191 | *queued* 2026-07-09 | clean |
| 192 | *deferred* 2026-07-09 — revisit trigger: the next prover-method landing, OR the first real spec where a sce... | clean |
| 193 | *queued* 2026-07-09 | clean |
| 197 | *queued* 2026-07-10 | clean |
| 198 | *queued* 2026-07-10 | clean |
| 199 | *queued* 2026-07-10 | clean |
| 203 | *queued* 2026-07-10 | clean |
| 204 | *queued* 2026-07-10 | clean |
| 205 | *queued* 2026-07-10 | clean |
| 206 | *queued* 2026-07-10 | clean |
| 207 | *queued* 2026-07-10 | clean |
| 208 | *queued* 2026-07-10 | clean |
| 215 | *queued* 2026-07-10 | clean |
| 217 | *queued* 2026-07-10 | clean |
| 220 | *queued* 2026-07-10 | clean |
| 221 | *queued* 2026-07-10 | clean |
| 229 | *queued* 2026-07-10 | clean |
| 230 | *queued* 2026-07-10 | clean |
| 231 | *queued* 2026-07-10 | clean |
| 234 | *queued* 2026-07-10 | clean |
| 235 | *deferred* 2026-07-10 — revisit trigger: the first real "I'm leaving" reaching the safe stop with the closi... | AMBIGUOUS (open-leg tail) |
| 236 | *queued* 2026-07-10 | clean |
| 238 | *queued* 2026-07-05 | clean |
| 241 | *deferred* 2026-07-10 — revisit trigger: one real EXTERNAL host attaches (track-coach's catch-up is the nat... | AMBIGUOUS (open-leg tail) |
| 243 | *queued* 2026-07-10 | clean |
| 247 | *deferred* 2026-07-12 — revisit trigger: Done-when (c) "one real remote deposit landed" stays open, closabl... | clean |
| 261 | *deferred* 2026-07-12 — revisit trigger: the live Discussion WRITE round-trip (a real discussion bridged en... | round-7 sweep |
| 302 | *queued* 2026-07-13 | clean |
| 307 | *queued* 2026-07-13 | clean |
| 308 | *queued* 2026-07-13 | clean |
| 309 | *queued* 2026-07-13 | clean |
| 332 | *queued* 2026-07-15 | clean |
| 381 | *far* 2026-07-17 | clean |
| 396 | *deferred* 2026-07-18 — revisit trigger: field-gated on the harness shipping a listener [INV-231, row 405] | clean |
| 389 | *deferred* 2026-07-18 — revisit trigger: field-gated, tied to rows 385/247 | clean |
| 386 | *in-work* 2026-07-18 | clean |
| 385 | *queued* 2026-07-17 | clean |
| 398 | *queued* 2026-07-17 | clean |
| 399 | *queued* 2026-07-17 | clean |
| 400 | *queued* 2026-07-17 | clean |
| 401 | *queued* 2026-07-17 | clean |
| 404 | *queued* 2026-07-17 | clean |
| 405 | *deferred* 2026-07-18 — revisit trigger: the harness shipping a listener | clean |
| 411 | *far* 2026-07-17 | clean |
| 410 | *queued* 2026-07-17 | clean |
| 412 | *in-work* 2026-07-18 | clean |
| 421 | *queued* 2026-07-18 | clean |
| 424 | *deferred* 2026-07-20 — revisit trigger: the back-describe of every registered code to the quality bar | AMBIGUOUS (open-leg tail) |
| 425 | *queued* 2026-07-19 | clean |
| 426 | *queued* 2026-07-19 | clean |
| 427 | *queued* 2026-07-19 | clean |
| 428 | *queued* 2026-07-19 | clean |
| 432 | *queued* 2026-07-20 | clean |
| 435 | *far* 2026-07-20 | clean |
| 436 | *deferred* 2026-07-20 — revisit trigger: the value-space forcing step for each axis's in-between member, th... | round-7 sweep |
| 437 | *queued* 2026-07-20 | clean |
| 440 | *queued* 2026-07-21 | clean |
| 446 | *queued* 2026-07-22 | clean |
| 447 | *queued* 2026-07-22 | clean |
| 448 | *queued* 2026-07-22 | clean |
| 449 | *queued* 2026-07-22 | clean |
| 450 | *queued* 2026-07-22 | clean |
| 451 | *queued* 2026-07-22 | clean |
| 452 | *queued* 2026-07-22 | clean |
| 453 | *queued* 2026-07-22 | clean |
| 454 | *queued* 2026-07-22 | clean |
| 455 | *queued* 2026-07-22 | clean |
| 456 | *queued* 2026-07-22 | clean |
| 457 | *queued* 2026-07-22 | clean |
| 458 | *queued* 2026-07-22 | clean |
| 459 | *queued* 2026-07-22 | clean |
| 460 | *queued* 2026-07-22 | clean |
| 465 | *queued* 2026-07-23 | clean |
| 466 | *queued* 2026-07-23 | clean |
| 467 | *queued* 2026-07-23 | clean |
| 469 | *queued* 2026-07-23 | clean |
| 471 | *queued* 2026-07-23 | clean |
| 472 | *queued* 2026-07-23 | clean |
| 473 | *queued* 2026-07-23 | clean |
| 474 | *queued* 2026-07-23 | clean |
| 475 | *queued* 2026-07-23 | clean |
| 479 | *queued* 2026-07-23 | clean |
| 480 | *in-work* 2026-07-23 | clean |
| 481 | *queued* 2026-07-23 | clean |

## Archived rows (231) — rotated-ROADMAP-2026-07.md

ids: 47, 59, 64, 99, 107, 109, 110, 115, 128, 130, 135, 136, 137, 138, 139, 145, 149, 150, 151, 152, 154, 155, 156, 157, 158, 159, 160, 161, 162, 188, 195, 209, 210, 211, 212, 213, 214, 216, 218, 219, 222, 223, 224, 225, 226, 227, 228, 232, 233, 237, 239, 240, 242, 244, 245, 246, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 303, 304, 305, 306, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 334, 335, 333, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 391, 394, 395, 393, 392, 390, 387, 388, 383, 384, 382, 397, 402, 403, 406, 407, 408, 409, 413, 414, 415, 416, 417, 418, 419, 420, 422, 423, 429, 430, 431, 433, 434, 438, 439, 441, 442, 443, 444, 445, 461, 462, 463, 464, 468, 470, 476, 477, 478

All verbatim except row 445 (corrected cell + delegation line). By override: 99, 128, 445; by round-7 sweep: 130, 279, 420.

## Trigger extraction (deferred rows: 33)

- inline (extracted): 27 · override: 4 (55, 69, 129, 131) · NEEDS-TRIGGER fallback: 2 (143, 144)

## No-date / wish-date rows

- row 69 resolved by override (git 810af02).
- date from the wish cell: [48, 49, 171, 302, 307, 308, 309, 332, 381]

