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
- Read related active ADRs and relevant implementation/specification evidence. Track every non-ADR project document used to frame, explore, or record the replacement as a source document, including specifications, plans, RFCs, design notes, issues, proposals, and project READMEs.
- Use the template from the `adr-create` skill in `assets/adr.md` when writing the replacement. Read it before writing, replace every `{placeholder}`, and omit no required section.

## Workflow

1. Analyze the new context, the invalidated assumptions, the replacement alternatives, migration, compatibility, rollback, and consequences. Discuss unresolved trade-offs with the user as in a new architectural decision.
2. Allocate a new `NNNN-short-title.md` and matching `ADR-NNNN` ID using one above the highest existing number. Never reuse, rename, or renumber the old ADR.
3. While the replacement is unresolved, create the new ADR as `draft`; leave an old accepted ADR active. Normalize the replacement ADR's deliberation sources to a concise problem statement and link to the draft, without copying status or presenting the draft outcome as governing. If the old ADR is accepted, current-state documents continue to show its result and link until the replacement is accepted. If the old ADR is deprecated, do not restore its retired result. If one document both describes the current state and explores the replacement, preserve any still-governing old result and ADR link while replacing the new decision analysis with a concise problem statement and link to the draft. A draft must not silently disable an accepted decision.
4. Once the user explicitly accepts the replacement, update both records in one change:
   - new ADR: `status: accepted`; add the old ADR's relative link to `supersedes`;
   - old ADR: `status: superseded`; set `superseded-by` to the new ADR's relative link;
   - add an explanatory link to the old ADR, plus independent migration evidence that is not a source document, in the new ADR's `## Links` section;
   - do not add a link to or mention of the new ADR in the old ADR's body. Its `superseded-by` frontmatter field is the sole permitted reference to an ADR with a higher number or later date.
5. Update every source document for the replacement ADR and every applicable current-state document that cites the old governing decision. Keep only a concise problem/current-result statement and point it to the replacement ADR by stable ID. Preserve historical references where the document intentionally describes the old state. Do not link any of these source documents from the replacement ADR.
6. Do not edit generated or read-only source documents. Locate and update their maintaining source instead. If a necessary source-side change is semantically ambiguous or outside the writable workspace, ask the user and report the supersession change set as incomplete until it is resolved.
7. State explicitly that supersession is total. Do not mark the old ADR `superseded` while any design still depends on an unrecorded surviving part of it.
8. Refresh the bounded ADR catalog region in `docs/adrs/README.md`, creating it when absent. Include every ADR, sorted by number, with stable ID, title, status, date, and replacement link. Preserve prose outside the region.
9. Validate that the new ADR ID matches its H1, filename, and frontmatter number; lifecycle metadata resolves and agrees; neither ADR body refers to an ADR with a higher number or later date; the replacement ADR does not link its source documents; applicable source documents point to the replacement; the catalog matches the metadata; and no intermediate state leaves two contradictory accepted ADRs.

Use the canonical status vocabulary: `draft`, `accepted`, `rejected`, `withdrawn`, `deprecated`, `superseded`. `superseded` always requires a real replacement ADR. If an accepted decision merely stops applying and has no replacement, use `deprecated` via `adr-transition`.

Do not alter the old ADR's original context, decision, or consequences except for lifecycle metadata and an unnumbered supersession note. Do not add a `## Links` entry or body text that identifies a replacement with a higher number or later date.
