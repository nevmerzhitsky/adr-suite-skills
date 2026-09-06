---
name: adr-transition
description: Change an ADR lifecycle status with semantic checks. Use to accept or reject a draft, withdraw an abandoned draft, or deprecate an accepted decision that has no direct replacement; use adr-supersede for replacement.
license: MIT
metadata:
  family: "adr-suite"
---

# Change ADR status

Apply the transition that matches what happened; do not use a generic `cancelled` status.

## Canonical states

| Status | Meaning |
| --- | --- |
| `draft` | Under discussion; not governing. |
| `accepted` | Approved and currently governing. |
| `rejected` | Evaluated and deliberately not chosen. |
| `withdrawn` | Abandoned before acceptance, without a decision on its merits. |
| `deprecated` | Previously accepted, no longer governing, with no direct replacement. |
| `superseded` | Previously accepted, replaced by a named newer ADR. |

## Allowed transitions

- `draft → accepted`: the problem statement, drivers, options, decision outcome, consequences, and confirmation are complete and the user explicitly approves it.
- `draft → rejected`: alternatives were evaluated and the proposed decision was explicitly declined. Record why.
- `draft → withdrawn`: the proposal was abandoned, became irrelevant, or was merged elsewhere before acceptance. Record why. Link only eligible ADRs or independent evidence, never a source document from which the proposal was created.
- `accepted → deprecated`: the decision no longer applies and no single new ADR replaces it. Record the effective reason/date and migration implications.
- `accepted → superseded`: only through `adr-supersede`, with a real replacement and reciprocal links.
- `deprecated → superseded`: allowed through `adr-supersede` if a later direct replacement is adopted.

Treat `rejected`, `withdrawn`, and `superseded` as terminal historical states. Reconsideration gets a new ADR that links back to the old record under the new ADR's `## Links`, rather than reopening history. Do not add the new ADR to the old record's body.

## Procedure

1. Treat existing ADRs as available only when `docs/adrs/README.md` exists, contains an ADR catalog with ADR links, and `docs/adrs/` contains at least one ADR file other than `README.md`. If any condition is false, do not search for or require ADRs. Stop ADR-specific processing and report that no scoped transition target is available.
2. Read the catalog and list local ADR files before resolving the exact ADR and relevant linked ADRs by stable ID. Do not search outside `docs/adrs/` for ADRs, except for a specific external ADR file linked directly from `docs/adrs/README.md`. Do not search project-wide architecture documents, constitutions, or Spec-driven Development context or memory to locate ADRs. Verify the target's current status.
3. Infer the requested semantic action, but ask if the user's word "cancel" is ambiguous:
   - cancel an undecided draft → `withdrawn`;
   - decide against a considered draft → `rejected`;
   - retire an accepted decision without replacement → `deprecated`;
   - replace it → hand off to `adr-supersede`.
4. Before a transition that changes governance, obtain explicit user intent. Do not accept, reject, deprecate, or supersede merely because code appears to have drifted.
5. Change only status/lifecycle metadata, a short dated lifecycle note, and relevant lower-numbered ADR links whose dates are no later than the current ADR's date. Preserve the original decision record, including its stable `ADR-NNNN` ID. Never add a higher-numbered or later-dated ADR ID or link to its body; `superseded-by` frontmatter is the lifecycle exception.
6. Update each operator-supplied source document that cites the transitioned ADR. Do not search the workspace for more citations. After acceptance, keep a concise problem/current-result statement and the ADR link. After rejection or withdrawal, keep only the problem and link, without copying lifecycle status or presenting an outcome as governing. After deprecation, remove the retired result from current-state text while preserving independent requirements and any intentionally historical reference. Keep links one-way; never add a source-document reference to the ADR.
7. Do not edit generated or read-only source documents. Locate and update their maintaining source instead. If the necessary source change is semantically ambiguous or outside the writable workspace, ask the user and report the transition change set as incomplete until it is resolved.
8. Refresh the bounded ADR catalog region in `docs/adrs/README.md` after the status change, creating it when absent. Include every ADR, sorted by number, with stable ID, title, status, date, and replacement link. Preserve prose outside the region.

All ADRs remain in `docs/adrs/` under their stable `NNNN-short-title.md` filenames and retain their matching `ADR-NNNN` IDs. Cite them in human-facing documentation and code by stable ID.
