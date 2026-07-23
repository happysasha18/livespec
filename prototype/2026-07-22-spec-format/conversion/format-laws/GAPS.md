# GAPS — the source holes this section records

The format-mechanism source (the stage-1 delta and its gates plan) leaves one behaviour stated with its measure unset. It is carried as a `[GAP]` line under the criterion it touches, never filled by invention (INV-252).

## GAP 1 — the cold-reader panel's size and supplier (R5.3)

> [GAP: the number of cold readers that form one panel, and the actor that supplies them, are unstated.]

The comprehension gate reads a changed section with a panel of cold readers and passes it only after two consecutive zero-blocking reads (R5.3–R5.5). The source states the panel exists and how its verdict is read, but not how many readers make one panel, nor which actor supplies them. The gates plan resolves the mechanism without inventing a number — `guardrails/comprehension-gate.py` takes the read count from a configured value rather than hard-coding a panel size — so the hole is a stated configuration point, not a blocking one. Recorded here as the honest output for a real hole; a queue row owns closing it if a fixed panel size is ever decided.
