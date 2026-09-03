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

- `draft -> accepted`: the problem statement, drivers, options, decision outcome, consequences, and confirmation are complete and the user explicitly approves it.
- `draft -> rejected`: alternatives were evaluated and the proposed decision was explicitly declined. Record why.
- `draft -> withdrawn`: the proposal was abandoned, became irrelevant, or was merged elsewhere before acceptance. Record why and link related work.
- `accepted -> deprecated`: the decision no longer applies and no single new ADR replaces it. Record the effective reason/date and migration implications.
- `accepted -> superseded`: only through `adr-supersede`, with a real replacement and reciprocal links.
- `deprecated -> superseded`: allowed through `adr-supersede` if a later direct replacement is adopted.

Treat `rejected`, `withdrawn`, and `superseded` as terminal historical states. Reconsideration gets a new ADR linked under `## Links`, rather than reopening history.

## Procedure

1. Resolve the exact ADR and relevant linked ADRs by stable ID. Verify its current status.
2. Infer the requested semantic action, but ask if the user's word "cancel" is ambiguous:
   - cancel an undecided draft -> `withdrawn`;
   - decide against a considered draft -> `rejected`;
   - retire an accepted decision without replacement -> `deprecated`;
   - replace it -> hand off to `adr-supersede`.
3. Before a transition that changes governance, obtain explicit user intent. Do not accept, reject, deprecate, or supersede merely because code appears to have drifted.
4. Change only status/lifecycle metadata, a short dated lifecycle note, and relevant links. Preserve the original decision record, including its stable `ADR-NNNN` ID.
5. Check that related documentation no longer describes a non-active ADR as governing. Report references needing updates; change them only when the task authorizes it.
6. Refresh the bounded ADR catalog region in `docs/adrs/README.md` after the status change, creating it when absent. Include every ADR, sorted by number, with stable ID, title, status, date, and replacement link. Preserve prose outside the region.

All ADRs remain in `docs/adrs/` under their stable `NNNN-short-title.md` filenames and retain their matching `ADR-NNNN` IDs. Cite them in human-facing documentation and code by stable ID.
