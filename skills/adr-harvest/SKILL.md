---
name: adr-harvest
description: Discover significant architectural decisions embedded in completed feature documentation, code, tests, or migrations, register missing ADRs, and replace duplicated decision detail in source documents with concise ADR references. Use after implementation or when documenting a brownfield system; do not use to record every implementation detail.
license: MIT
metadata:
  family: "adr-suite"
---

# Harvest missing ADRs

Recover decisions from completed work without fabricating the historical rationale.

## Source-document direction

A specification, plan, RFC, design note, issue, proposal, project README, or other non-ADR project document named or linked in the prompt, or used to frame or recover the decision during discovery, is a source document. Decision provenance is one-way: source documents link to the harvested ADR, and the ADR never mentions, cites, or links back to its source documents, including under `## Links`. Do not store the source-document list in ADR prose or metadata. ADR-to-ADR links remain valid under the repository's number and date rules. Independent external research, code, tests, migrations, metrics, and operational evidence may be linked when they are not source documents for the recovered decision.

## What qualifies

A candidate should have lasting consequences beyond one local implementation detail. Strong signals include cross-cutting constraints, public APIs or protocols, persistence/data ownership, security or privacy boundaries, deployment/runtime topology, major dependencies, compatibility commitments, costly migrations, or a deliberate trade-off that future maintainers might otherwise reverse accidentally.

## Workflow

1. Read the named feature/specification and the minimum supporting code, tests, schema/migrations, and active ADRs necessary to verify it. Record the exact source-document set for the working session so none is linked from a harvested ADR. Treat final docs and observable implementation as evidence, not as proof of unstated rationale.
2. Extract atomic candidate decisions. Separate one decision from a bundle when it could be reversed independently.
3. Deduplicate against all ADRs, including rejected, deprecated, and superseded records. Identify existing records by stable ID. Existing history may explain the choice even when it is not active.
4. Present a candidate register before writing:

| Candidate | Architectural significance | Evidence | Existing ADR ID | Confidence | Proposed ADR action | Source-document rewrite |
| --- | --- | --- | --- | --- | --- | --- |

5. Distinguish `recovered fact`, `inferred rationale`, and `unknown`. Ask the user to select candidates and approve the corresponding source-document rewrites as one change set. Also ask about missing rationale, alternatives, decision date/owners, or whether candidates should be combined. Prefer a small selectable batch plus an open question. If the operator explicitly requested autonomous harvesting, apply unambiguous local source rewrites automatically and ask only when shortening could remove independent normative content or alter meaning.
6. After the user selects candidates, allocate new `NNNN-short-title.md` files and matching `ADR-NNNN` IDs in `docs/adrs/`, never reusing gaps.
7. Write a retrospective note in `## Context and problem statement` without identifying any source document. Analyze plausible alternatives and cite related ADRs by stable ID under `## Links`; link independent implementation or verification evidence only when it was not part of the source-document set. An ADR body, including `## Links`, must not mention, reference, or link to a source document, an ADR with a higher number, or an ADR with a `date` later than its own. Clearly label rationale that remains inferred. When a review exposed an undocumented but established standard, record the competing pattern and the standard it confirms.
8. Use `accepted` only when the evidence establishes that the decision governs the current system and the user confirms the recovered record. Otherwise use `draft`. Never backdate with false precision; use the recording date and describe any approximate historical date in prose.
9. Update every writable local source document for each selected candidate in the same change. Replace duplicated decision analysis, rationale, alternatives, consequences, and lifecycle text with a concise statement of the problem and, for an accepted ADR, the current result, plus a relative Markdown link labeled with the concrete stable ADR ID. For a draft ADR, retain only the problem and link; do not copy its status or present an outcome as governing. Preserve independent requirements, contracts, acceptance criteria, target-state behavior, and implementation evidence. When multiple source passages express the same decision, normalize each one or consolidate them without losing necessary document structure.
10. Do not edit generated or read-only documents. Locate and update their maintaining source instead. If a source document is outside the writable workspace, cannot link to the ADR, or cannot be shortened without an unresolved semantic choice, ask the operator and report the harvest as incomplete until the source side is resolved.
11. Refresh the bounded ADR catalog region in `docs/adrs/README.md`, creating it when absent. Include every ADR, sorted by number, with stable ID, title, status, date, and replacement link. Preserve prose outside the region.
12. Check the generated ADRs against each other and active ADRs. Verify that no harvested ADR mentions or links a source document, every editable source document links to the concrete ADR by stable ID, and no source retains duplicated decision-record content. Report uncovered ambiguities or apparent drift.

Use the template from the `adr-create` skill in `assets/adr.md` when writing each ADR. Read it before writing, replace every `{placeholder}`, and omit no required section. Use the canonical statuses from the repository: `draft`, `accepted`, `rejected`, `withdrawn`, `deprecated`, `superseded`.

Do not mass-produce low-value ADRs. Prefer a small set of independent, durable decisions that explain why the system is constrained as it is.
