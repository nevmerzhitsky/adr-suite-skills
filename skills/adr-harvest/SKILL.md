---
name: adr-harvest
description: Discover significant architectural decisions embedded in completed feature documentation, code, tests, or migrations and register missing ADRs. Use after implementation or when documenting a brownfield system; do not use to record every implementation detail.
license: MIT
metadata:
  family: "adr-suite"
---

# Harvest missing ADRs

Recover decisions from completed work without fabricating the historical rationale.

## What qualifies

A candidate should have lasting consequences beyond one local implementation detail. Strong signals include cross-cutting constraints, public APIs or protocols, persistence/data ownership, security or privacy boundaries, deployment/runtime topology, major dependencies, compatibility commitments, costly migrations, or a deliberate trade-off that future maintainers might otherwise reverse accidentally.

## Workflow

1. Read the named feature/specification and the minimum supporting code, tests, schema/migrations, and active ADRs necessary to verify it. Treat final docs and observable implementation as evidence, not as proof of unstated rationale.
2. Extract atomic candidate decisions. Separate one decision from a bundle when it could be reversed independently.
3. Deduplicate against all ADRs, including rejected, deprecated, and superseded records. Identify existing records by stable ID. Existing history may explain the choice even when it is not active.
4. Present a candidate register before writing:

| Candidate | Architectural significance | Evidence | Existing ADR ID | Confidence | Proposed action |
| --- | --- | --- | --- | --- | --- |

5. Distinguish `recovered fact`, `inferred rationale`, and `unknown`. Ask the user about missing rationale, alternatives, decision date/owners, or whether candidates should be combined. Prefer a small selectable batch plus an open question.
6. After the user selects candidates, allocate new `NNNN-short-title.md` files and matching `ADR-NNNN` IDs in `docs/adrs/`, never reusing gaps.
7. Write a retrospective note in `## Context and problem statement`, cite repository evidence and related ADRs by stable ID under `## Links`, and analyze plausible alternatives. Clearly label rationale that remains inferred. When a review exposed an undocumented but established standard, record the competing pattern and the standard it confirms.
8. Use `accepted` only when the evidence establishes that the decision governs the current system and the user confirms the recovered record. Otherwise use `draft`. Never backdate with false precision; use the recording date and describe any approximate historical date in prose.
9. Refresh the bounded ADR catalog region in `docs/adrs/README.md`, creating it when absent. Include every ADR, sorted by number, with stable ID, title, status, date, and replacement link. Preserve prose outside the region.
10. Check the generated ADRs against each other and active ADRs, then report uncovered ambiguities or apparent drift.

Use the template from the `adr-create` skill in `assets/adr.md` when writing each ADR. Read it before writing, replace every `{placeholder}`, and omit no required section. Use the canonical statuses from the repository: `draft`, `accepted`, `rejected`, `withdrawn`, `deprecated`, `superseded`.

Do not mass-produce low-value ADRs. Prefer a small set of independent, durable decisions that explain why the system is constrained as it is.
