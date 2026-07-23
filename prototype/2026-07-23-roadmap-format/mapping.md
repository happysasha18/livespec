# Live-row mapping — ROADMAP conversion (for orchestrator review)

Source pinned to git 859dcfc (the last pre-conversion commit; the working ROADMAP.md is the applied new body since 6edcf32).
Override table (rowconv.py, orchestrator triage 2026-07-23, three rounds):
- FORCE_ARCHIVE 99 (stale in-work leader over a landed close, verbatim), 128 (leg closed in the same cell minutes later, verbatim), 445 (spec-format conversion shipped v4.0.0, cell corrected at the move with the delegation accounting line).
- STATUS_CELL_OVERRIDE 69 (git date 810af02 + named trigger), 55 / 129 / 131 (closed-family leaders with one riding leg → *deferred* with the named leg).
- General rule added: a live-kept row whose leader is closed-family maps to *deferred*, never *queued* (probed: zero rows beyond the override table on the pinned source).

| id | old status leader | new status | flag |
|---|---|---|---|
| 44 | deferred | *deferred* 2026-07-05 | clean |
| 48 | deferred | *deferred* 2026-07-05 | no-date in status (used wish date) |
| 49 | deferred | *deferred* 2026-07-05 | no-date in status (used wish date) |
| 54 | build legs LANDED 2026-07-07 ~08:33, session 23; field leg OPEN | *deferred* 2026-07-07 | clean |
| 55 | design LANDED 2026-07-07 ~10:51, session 23; machine leg stays [target] | *deferred* 2026-07-07 | OVERRIDE |
| 69 | deferred | *deferred* 2026-07-05 | OVERRIDE |
| 93 | pack-side half LANDED 2026-07-05 ~22:20, session 8; row WAITING | *deferred* 2026-07-05 | clean |
| 95 | queued 2026-07-05 evening (mis-dated 07-06 at intake | *queued* 2026-07-05 | clean |
| 96 | queued 2026-07-05 evening (mis-dated 07-06 at intake | *queued* 2026-07-05 | clean |
| 100 | pack-side LANDED 2026-07-05 23:39 (git), session 10; row WAITING on | *deferred* 2026-07-05 | clean |
| 108 | landed 2026-07-06 ~10:55, session 12 — repo side whole; ONE | *deferred* 2026-07-06 | clean |
| 117 | landed 2026-07-06 ~10:55, session 12 — repo side whole; ONE | *deferred* 2026-07-06 | clean |
| 118 | landed 2026-07-06 ~10:55, session 12 — repo side whole; ONE | *deferred* 2026-07-06 | clean |
| 119 | landed 2026-07-06 ~10:55, session 12 — repo side whole; ONE | *deferred* 2026-07-06 | clean |
| 129 | landed 2026-07-06 ~15:58, session 16 — repo side whole; ONE | *deferred* 2026-07-06 | OVERRIDE |
| 130 | queued 2026-07-06 ~13:32, session 13 (door: feature | *queued* 2026-07-06 | clean |
| 131 | landed 2026-07-06 ~14:18, session 15 — OPEN LEG (INV-26): the | *deferred* 2026-07-06 | OVERRIDE |
| 133 | queued 2026-07-06 ~15:58, session 16 (door: feature | *queued* 2026-07-06 | clean |
| 134 | build leg MET 2026-07-06 ~20:42, session 19; field legs OPEN | *deferred* 2026-07-06 | clean |
| 140 | build legs MET 2026-07-06 ~21:26, session 20; field leg OPEN; | *deferred* 2026-07-06 | clean |
| 141 | build leg MET 2026-07-06 ~20:49, session 19; field legs OPEN | *deferred* 2026-07-06 | clean |
| 143 | build legs MET 2026-07-06 ~21:44, session 20; field leg OPEN | *deferred* 2026-07-06 | clean |
| 144 | build legs MET 2026-07-06 ~21:44, session 20; field leg OPEN | *deferred* 2026-07-06 | clean |
| 148 | queued 2026-07-06 ~23:25, session 22 (kind: prose | *queued* 2026-07-06 | clean |
| 163 | queued 2026-07-07 ~08:19, session 23 (door: feature | *queued* 2026-07-05 | clean |
| 165 | build legs LANDED 2026-07-07 ~09:38, session 23; field leg OPEN | *deferred* 2026-07-07 | clean |
| 166 | queued 2026-07-07 ~09:38, session 23, PRIORITY: his out-of-turn word | *queued* 2026-07-07 | clean |
| 168 | build legs LANDED 2026-07-07 ~11:02, session 23; field leg OPEN | *deferred* 2026-07-07 | clean |
| 170 | queued | *queued* 2026-07-10 | clean |
| 171 | queued | *queued* 2026-07-08 | no-date in status (used wish date) |
| 190 | queued 2026-07-09 ~23:53 (door: feature | *queued* 2026-07-09 | clean |
| 191 | queued 2026-07-09 ~23:54 (door: feature | *queued* 2026-07-09 | clean |
| 192 | DEFERRED on his word 2026-07-09 ~23:54 | *deferred* 2026-07-09 | clean |
| 193 | queued 2026-07-09 ~23:54 (door: feature | *queued* 2026-07-09 | clean |
| 197 | queued 2026-07-10 ~01:00 (door: feature | *queued* 2026-07-10 | clean |
| 198 | queued 2026-07-10 ~01:00 (door: feature | *queued* 2026-07-10 | clean |
| 199 | queued 2026-07-10 ~01:00 (door: feature | *queued* 2026-07-10 | clean |
| 203 | queued 2026-07-10 ~01:00 (door: feature | *queued* 2026-07-10 | clean |
| 204 | queued 2026-07-10 ~01:00 (door: feature | *queued* 2026-07-10 | clean |
| 205 | queued 2026-07-10 ~01:00 (door: refactor | *queued* 2026-07-10 | clean |
| 206 | queued 2026-07-10 ~01:00 (door: feature | *queued* 2026-07-10 | clean |
| 207 | queued 2026-07-10 ~01:00 (door: feature | *queued* 2026-07-10 | clean |
| 208 | queued 2026-07-10 ~01:08, INTENDED TONIGHT (door: feature | *queued* 2026-07-10 | clean |
| 215 | queued 2026-07-10 ~10:08, POST-1.0 on his word (door: feature | *queued* 2026-07-10 | clean |
| 217 | queued 2026-07-10 ~10:24 on his explicit word (door: feature | *queued* 2026-07-10 | clean |
| 220 | queued 2026-07-10 ~10:44, PRIORITY: first after the onboarding landing (door: | *queued* 2026-07-10 | clean |
| 221 | queued 2026-07-10 ~10:44, SECOND after row 220 (door: feature | *queued* 2026-07-10 | clean |
| 229 | queued 2026-07-10 ~11:01, POST-1.0 on his word (door: feature | *queued* 2026-07-10 | clean |
| 230 | queued 2026-07-10 ~11:02 on his word, POST-1.0 (door: feature | *queued* 2026-07-10 | clean |
| 231 | queued 2026-07-10 ~11:30 on his word, POST-1.0 (door: feature | *queued* 2026-07-10 | clean |
| 234 | queued 2026-07-10 ~13:06 on his word, rides the law batch | *queued* 2026-07-10 | clean |
| 235 | first leg landed 2026-07-10 ~14:55 (1.0.4, INV-95/M-224 red-proven, three homes) | *deferred* 2026-07-10 | AMBIGUOUS (leader reads closed; open-leg tail kept it live) |
| 236 | queued 2026-07-10 ~13:49 on his word, rides the law batch | *queued* 2026-07-10 | clean |
| 238 | queued 2026-07-10 ~14:15 from the audit finding (door: feature | *queued* 2026-07-05 | clean |
| 241 | first leg landed 2026-07-10 ~17:34 (1.0.8): code shipped by the | *deferred* 2026-07-10 | AMBIGUOUS (leader reads closed; open-leg tail kept it live) |
| 243 | queued 2026-07-10 ~14:24, BLOCKED on the campaign's publish | *queued* 2026-07-10 | clean |
| 247 | build legs LANDED 2026-07-12 ~02:41, session 37; field leg OPEN | *deferred* 2026-07-12 | clean |
| 261 | queued 2026-07-12 ~02:41 from row 247's landing split, | *queued* 2026-07-12 | clean |
| 279 | queued 2026-07-12 s38, | *queued* 2026-07-12 | clean |
| 302 | QUEUED | *queued* 2026-07-13 | no-date in status (used wish date) |
| 307 | QUEUED | *queued* 2026-07-13 | no-date in status (used wish date) |
| 308 | QUEUED | *queued* 2026-07-13 | no-date in status (used wish date) |
| 309 | QUEUED | *queued* 2026-07-13 | no-date in status (used wish date) |
| 332 | idea — not a build until it earns one | *queued* 2026-07-15 | no-date in status (used wish date) |
| 381 | far | *far* 2026-07-17 | no-date in status (used wish date) |
| 385 | queued 2026-07-17 [target] | *queued* 2026-07-17 | clean |
| 386 | in flight 2026-07-18 | *in-work* 2026-07-18 | clean |
| 389 | LAW arm LANDED 2026-07-18; the real cross-machine read OPEN — | *deferred* 2026-07-18 | clean |
| 396 | TRANSPORT-SPLIT CORRECTION LANDED 2026-07-18; the conversation channel's real first use | *deferred* 2026-07-18 | clean |
| 398 | queued 2026-07-17 | *queued* 2026-07-17 | clean |
| 399 | queued 2026-07-17 | *queued* 2026-07-17 | clean |
| 400 | queued 2026-07-17 | *queued* 2026-07-17 | clean |
| 401 | queued 2026-07-17 | *queued* 2026-07-17 | clean |
| 404 | queued 2026-07-17 | *queued* 2026-07-17 | clean |
| 405 | tripwire-build LANDED 2026-07-18; firing DEFERRED — field-gated on the harness | *deferred* 2026-07-18 | clean |
| 410 | queued 2026-07-17 | *queued* 2026-07-17 | clean |
| 411 | queued 2026-07-17, FAR TIER | *far* 2026-07-17 | clean |
| 412 | in flight 2026-07-18 | *in-work* 2026-07-18 | clean |
| 420 | queued 2026-07-17 | *queued* 2026-07-17 | clean |
| 421 | queued 2026-07-18, OPEN DESIGN QUESTION | *queued* 2026-07-18 | clean |
| 424 | MACHINERY LANDED 2026-07-20 v2.9.0 | *deferred* 2026-07-20 | AMBIGUOUS (leader reads closed; open-leg tail kept it live) |
| 425 | queued 2026-07-19 | *queued* 2026-07-19 | clean |
| 426 | queued 2026-07-19 | *queued* 2026-07-19 | clean |
| 427 | OPEN DESIGN 2026-07-19 — capture only, owner-held for scope | *queued* 2026-07-19 | clean |
| 428 | CAPTURE ONLY 2026-07-19 — recommended next-pass class clause, lands on | *queued* 2026-07-19 | clean |
| 432 | queued 2026-07-20 (surfaced by the conduct-judge adversarial audit) | *queued* 2026-07-20 | clean |
| 435 | far 2026-07-20 (surfaced by the INV-243 adversarial audit) | *far* 2026-07-20 | clean |
| 436 | queued 2026-07-20 (Alexander named the class: the axes are typical | *queued* 2026-07-20 | clean |
| 437 | queued 2026-07-20 (Alexander: "always можно сделать ещё lookalike" | *queued* 2026-07-20 | clean |
| 440 | queued 2026-07-21 (Alexander named it as a standing classifier the | *queued* 2026-07-21 | clean |
| 446 | queued 2026-07-22 | *queued* 2026-07-22 | clean |
| 447 | queued 2026-07-22 | *queued* 2026-07-22 | clean |
| 448 | queued 2026-07-22 | *queued* 2026-07-22 | clean |
| 449 | queued 2026-07-22 | *queued* 2026-07-22 | clean |
| 450 | queued 2026-07-22 | *queued* 2026-07-22 | clean |
| 451 | queued 2026-07-22 | *queued* 2026-07-22 | clean |
| 452 | queued 2026-07-22 | *queued* 2026-07-22 | clean |
| 453 | queued 2026-07-22 | *queued* 2026-07-22 | clean |
| 454 | queued 2026-07-22 | *queued* 2026-07-22 | clean |
| 455 | queued 2026-07-22 | *queued* 2026-07-22 | clean |
| 456 | queued 2026-07-22 | *queued* 2026-07-22 | clean |
| 457 | queued 2026-07-22 | *queued* 2026-07-22 | clean |
| 458 | queued 2026-07-22 | *queued* 2026-07-22 | clean |
| 459 | queued 2026-07-22 | *queued* 2026-07-22 | clean |
| 460 | queued 2026-07-22 | *queued* 2026-07-22 | clean |
| 465 | queued 2026-07-23 | *queued* 2026-07-23 | clean |
| 466 | queued 2026-07-23 | *queued* 2026-07-23 | clean |
| 467 | queued 2026-07-23 | *queued* 2026-07-23 | clean |
| 469 | queued 2026-07-23 | *queued* 2026-07-23 | clean |
| 471 | queued 2026-07-23 | *queued* 2026-07-23 | clean |
| 472 | queued 2026-07-23 | *queued* 2026-07-23 | clean |
| 473 | queued 2026-07-23 | *queued* 2026-07-23 | clean |
| 474 | queued 2026-07-23 | *queued* 2026-07-23 | clean |
| 475 | queued 2026-07-23 | *queued* 2026-07-23 | clean |
| 479 | queued 2026-07-23 | *queued* 2026-07-23 | clean |
| 480 | in-work 2026-07-23 | *in-work* 2026-07-23 | clean |
| 481 | queued 2026-07-23 | *queued* 2026-07-23 | clean |

## Archived rows (228) — moved to rotated-ROADMAP-2026-07.md

ids: 47, 59, 64, 99, 107, 109, 110, 115, 128, 135, 136, 137, 138, 139, 145, 149, 150, 151, 152, 154, 155, 156, 157, 158, 159, 160, 161, 162, 188, 195, 209, 210, 211, 212, 213, 214, 216, 218, 219, 222, 223, 224, 225, 226, 227, 228, 232, 233, 237, 239, 240, 242, 244, 245, 246, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 303, 304, 305, 306, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 382, 383, 384, 387, 388, 390, 391, 392, 393, 394, 395, 397, 402, 403, 406, 407, 408, 409, 413, 414, 415, 416, 417, 418, 419, 422, 423, 429, 430, 431, 433, 434, 438, 439, 441, 442, 443, 444, 445, 461, 462, 463, 464, 468, 470, 476, 477, 478

All verbatim except row 445 (status cell corrected at the move, delegation line carried). Rows 99, 128, 445 archived by override.

## Safe-default rows kept live

235, 241, 424 — structured open-leg tail (424 REMAINS the his-gate; 235/241 a pending `; open leg:`); mapped *deferred*.

## No-date rows

- resolved by override: row 69 (*deferred* 2026-07-05, git 810af02).
- date taken from the wish cell (status had none): [48, 49, 171, 302, 307, 308, 309, 332, 381]

