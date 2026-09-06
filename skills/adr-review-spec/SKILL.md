---
name: adr-review-spec
description: Review a feature specification, plan, or architecture design for concrete conflicts with scoped accepted ADRs. Use while specifying or planning architecturally significant work, including Spec-driven Development workflows, before the design is finalized.
license: MIT
metadata:
  family: "adr-suite"
disable-model-invocation: true
---

# Check a planned feature for ADR conflicts

Review only concrete conflicts. This is not a universal governance gate and does not determine whether a new ADR is needed.

## Existing ADR discovery

Treat existing ADRs as available only when `docs/adrs/README.md` exists, contains an ADR catalog with ADR links, and `docs/adrs/` contains at least one ADR file other than `README.md`. If any condition is false, do not search for or require ADRs. Continue the requested specification review without ADR conflict checking.

When the corpus is available, read the catalog and list local ADR files before reading only the accepted ADRs relevant to the explicit scope. Do not search outside `docs/adrs/` for ADRs, except for a specific external ADR file linked directly from `docs/adrs/README.md`. Do not search project-wide architecture documents, constitutions, or Spec-driven Development context or memory to locate ADRs.

## Review method

1. Read the target specification, plan, or design and materials supplied by the operator. Do not use surrounding project context to locate ADRs or unrecorded decisions. Review ADRs only when the operator requested the check or the target explicitly identifies the ADR scope.
2. If the ADR corpus and an ADR scope are available, read the catalog, list local ADR files, and read only relevant `accepted` ADRs. Identify each ADR by stable `ADR-NNNN` ID.
3. Map relevant statements in the planned work to those ADRs. A conflict requires a concrete contradiction or incompatible assumption, not merely different wording.
4. Classify each checked area as `conflict`, `aligned`, or `clarification`.
5. Produce one compact table:

| Spec area | Relevant ADR ID | Evidence | Finding | Required action |
| --- | --- | --- | --- | --- |

6. Discuss each conflict with the user. Cite relevant ADRs by stable ID. Offer explicit choices: conform the feature, narrow its scope, or supersede the governing ADR. Do not silently edit an accepted ADR.
7. End with `pass`, `pass with conflict action`, or `blocked`, plus the smallest set of actions required to proceed.

During Spec-driven Development, run this review only when the operator requests it or when the target explicitly identifies relevant ADRs. Do not change the framework's normal context-loading behavior.
