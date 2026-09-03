---
name: adr-supersede
description: Replace an accepted or deprecated ADR with a new ADR and maintain bidirectional lifecycle links. Use when a prior architectural decision is being changed by a concrete replacement.
license: MIT
metadata:
  family: "adr-suite"
---

# Supersede an ADR

Replace a decision without rewriting history. The old ADR explains why the earlier choice existed; the new ADR explains why it is changing.

## Preconditions

- Resolve the exact old ADR by its stable ID (for example, `ADR-0001`) in `docs/adrs/` and read it fully.
- Normally only `accepted` or `deprecated` ADRs are superseded. If an abandoned `draft` has never governed the system, withdraw it and create a separate ADR instead.
- Verify that the new ADR will replace the whole decision. `superseded` cannot represent partial validity. If the old ADR bundled several independently surviving decisions, split their continuing state into new focused ADRs or define a scoped exception while keeping the old ADR accepted.
- Read related active ADRs and relevant implementation/specification evidence.

## Workflow

1. Analyze the new context, the invalidated assumptions, the replacement alternatives, migration, compatibility, rollback, and consequences. Discuss unresolved trade-offs with the user as in a new architectural decision.
2. Allocate a new `NNNN-short-title.md` and matching `ADR-NNNN` ID using one above the highest existing number. Never reuse, rename, or renumber the old ADR.
3. While the replacement is unresolved, create the new ADR as `draft`; leave the old ADR active. A draft must not silently disable an accepted decision.
4. Once the user explicitly accepts the replacement, update both records in one change:
   - new ADR: `status: accepted`; add the old ADR's relative link to `supersedes`;
   - old ADR: `status: superseded`; set `superseded-by` to the new ADR's relative link;
   - add reciprocal explanatory links that cite each ADR by stable ID, plus relevant migration evidence, in both `## Links` sections.
5. State explicitly that supersession is total. Do not mark the old ADR `superseded` while any design still depends on an unrecorded surviving part of it.
6. Refresh the bounded ADR catalog region in `docs/adrs/README.md`, creating it when absent. Include every ADR, sorted by number, with stable ID, title, status, date, and replacement link. Preserve prose outside the region.
7. Validate that the new ADR ID matches its H1, filename, and frontmatter number; both links resolve; metadata and prose agree; the catalog matches the metadata; and no intermediate state leaves two contradictory accepted ADRs.

Use the canonical status vocabulary: `draft`, `accepted`, `rejected`, `withdrawn`, `deprecated`, `superseded`. `superseded` always requires a real replacement ADR. If an accepted decision merely stops applying and has no replacement, use `deprecated` via `adr-transition`.

Do not alter the old ADR's original context, decision, or consequences except for lifecycle metadata, a prominent supersession note, and links.
