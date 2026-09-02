# ADR Suite

This package contains several agent skills for the full Architecture Decision Record lifecycle. Each skill writes or reads project ADRs under `docs/adrs/`.

## Skills

| Skill | Purpose | Typical phase |
| --- | --- | --- |
| `adr-create` | Explore alternatives with the user and create a draft or accepted ADR | Architecture/design |
| `adr-supersede` | Replace an active decision and maintain reciprocal links | Architecture change |
| `adr-transition` | Accept/reject/withdraw/deprecate an ADR using valid transitions | Decision governance |
| `adr-harvest` | Recover missing decisions from completed features or brownfield code | Post-implementation/baseline |
| `adr-review-spec` | Detect conflicts and missing ADRs in a planned feature | Specification and planning |
| `adr-audit` | Validate filenames, metadata, links, statuses, and repository health | CI/maintenance |

## Canonical convention

- Directory: `docs/adrs/`
- Catalog: `docs/adrs/README.md`
- Filename: `NNNN-short-title.md`, starting with `0001`
- Allocation: highest existing number plus one; gaps are never reused
- Stable identity: existing ADR files are never renumbered and normally never renamed
- Statuses: `draft`, `accepted`, `rejected`, `withdrawn`, `deprecated`, `superseded`

`docs/adrs/README.md` is the ADR catalog. It has one row for every ADR, sorted by number, with its number, title, status, date, and replacement link. Keep the catalog in a bounded machine-maintained region so surrounding human prose remains intact:

```markdown
<!-- adr-catalog:start -->
| Number | Title | Status | Date | Superseded by |
| --- | --- | --- | --- | --- |
| [0001-short-title](0001-short-title.md) | Example decision | accepted | 2026-09-03 | - |
<!-- adr-catalog:end -->
```

Create the file with this region when it is absent. Refresh the region whenever an ADR is created or its status, title, date, or replacement changes. The catalog is the discovery view; ADR frontmatter remains the authoritative record for a decision's full content and lifecycle links.

`cancelled` is deliberately not a canonical status because it hides three different events:

- an undecided proposal was abandoned: `withdrawn`;
- a proposal was considered and declined: `rejected`;
- an accepted decision ceased to govern without a direct replacement: `deprecated`.

If a new ADR directly replaces an old accepted decision, use `superseded` and reciprocal links.

## Status transitions

```mermaid
stateDiagram-v2
    [*] --> draft
    draft --> accepted
    draft --> rejected
    draft --> withdrawn
    accepted --> deprecated
    accepted --> superseded
    deprecated --> superseded
```

Rejected, withdrawn, and superseded ADRs remain as history. Reconsidering them creates a new linked ADR rather than reopening the old record.

## Recommended SDD integration

Skill descriptions enable relevant automatic discovery, especially for `adr-review-spec`, but project-level instructions provide the reliable governance gate. Add the following policy to the project's agent instructions (for example `AGENTS.md`) while leaving the framework's official commands and normal context-loading policy unchanged:

```markdown
## ADR governance

- Store ADRs in `docs/adrs/` and use `NNNN-short-title.md` filenames.
- Keep `docs/adrs/README.md` as the complete ADR catalog with each ADR's current status.
- When creating or reviewing a feature specification, architecture plan, or significant technical design, run `adr-review-spec` before finalizing it.
- If the review finds an unresolved architectural decision, use `adr-create` and link the resulting ADR from the specification or plan.
- If planned work contradicts an accepted ADR, do not silently proceed: conform the design or use `adr-supersede` with explicit approval.
- After a feature is implemented or its final documentation is updated, run `adr-harvest` to find decisions that escaped registration.
```

Suggested Spec Kit checkpoints:

1. After `/speckit.specify`: review boundaries, contracts, data/security constraints, and conflicts with accepted ADRs.
2. After `/speckit.plan`: review concrete technical commitments and create/supersede ADRs before implementation tasks are finalized.
3. After implementation/final docs: harvest only durable decisions that were actually adopted.
