# Wish: the architecture doc owes a runtime view and a placement view

**From:** Alexander, live-spec host session, 2026-07-09 evening. His verdict on the read-only tlvphoto
derivation (RUN item 5's validation artifact), paraphrased: the derived doc misses much of what
tlvphoto's own hand-grown LLD carries — the tiers (who does what, where the model runs, where the
rendering happens), and when the product spec promises flows, the architecture must show how it
realizes them. This REOPENS item 5: the per-kind node scaffold landed, and the method still describes
only part of what an architecture doc owes.

## What the method has today

The architecture step (build-pipeline step 3 + `templates/ARCHITECTURE.template.md`) asks for: named
nodes with one responsibility and `file:line` pins · seams with format owners · quality budgets with an
instrumentation home · the feature coverage table (unit → node + test) · the per-kind starting scaffold.
In the standards crosswalk (spec-author), this covers the arc42 building-block view (§5) and quality
scenarios (§10).

## The two missing views (arc42 §6 and §7 have no counterpart in the method)

1. **Runtime view — how each product-spec flow runs through the nodes.** The product spec's scenarios
   are flows (in tlvphoto: door → museum hang → walk → quiz → story). The architecture doc must show,
   per flow, the walk through the nodes: which node serves each step, what data crosses at each hop,
   and where the flow can fail. The feature coverage table names WHICH nodes implement a feature; the
   runtime view shows HOW. Evidence: the derived tlvphoto doc has nodes and seams and never traces one
   visitor flow through them.

2. **Placement view — what runs where, with its technology.** Every node states its tier: build-time on
   the author's machine · CDN static · client browser · edge worker · external service (the Anthropic
   API, Cloudflare KV) — plus the load-bearing technology choice where one exists (CLIP for embeddings,
   headless-Chrome for test rendering). His ask, paraphrased (2026-07-09): who does what, where the
   model runs, where the rendering happens. The derived
   doc holds this only as prose ("two halves split by a seam"); it needs a first-class column or table
   so the reader can answer "where does this run" for any node at a glance.

## A third finding: the validation run skipped the method's own mandatory parts

The derived doc carries no quality budgets (the method mandates numbers + an instrumentation home,
SPEC INV-41) and no spec-fact ownership table (tlvphoto has a product spec; the simulation never mapped
its facts to the derived nodes). So the validation proved the scaffold and under-exercised the method.
The reopened item re-runs the read-only derivation with the two new views AND the already-mandated
parts, then diffs the result against tlvphoto's real ARCHITECTURE.md as the bar: every section the real
LLD needed and the method did not produce is a named hole, closed or explicitly deferred.

## Boundaries

- tlvphoto stays untouched — the derivation is read-only, the artifact lives in scratch/docs here.
- The template grows sections, never a second document: runtime view and placement view live inside
  ARCHITECTURE.md, scaled by project.kind (a book has no placement view; it says so in one line).
- Prose register: the derived doc's voice went ornate ("the shape in one breath", "a hard seam") — the
  clean-agent + lint gate that guards PRODUCT_SPEC prose must guard ARCHITECTURE prose the same way.
