---
name: adr-review-spec
description: Review a feature specification, plan, or architecture design against active ADRs and detect unrecorded architectural decisions. Use while specifying or planning architecturally significant work, including Spec-driven Development workflows, before the design is finalized.
license: MIT
metadata:
  family: "adr-suite"
---

# Review a planned feature against ADRs

Act as an ADR governance gate without turning every feature choice into an ADR.

## Review method

1. Read the target specification/plan and its directly relevant context. Start discovery with the catalog in `docs/adrs/README.md`, then verify relevant ADR metadata and content. Inventory ADRs by status:
   - `accepted` ADRs are governing;
   - `draft` ADRs are advisory/unresolved;
   - `rejected`, `withdrawn`, `deprecated`, and `superseded` ADRs are historical context only.
2. Map relevant statements in the planned work to governing ADRs. A conflict requires a concrete contradiction or incompatible assumption, not merely different wording.
3. Identify architectural decisions not yet recorded. Use significance tests: cross-cutting reach, hard-to-reverse commitment, external/public contract, data/security boundary, operational topology, major dependency, migration cost, or a trade-off likely to be revisited.
4. Classify findings:
    - `blocker`: directly violates an accepted ADR or depends on an unresolved architectural choice;
    - `needs RFC before ADR`: a broad, cross-team, or high-risk change still needs exploration before an ADR can record a concluded decision;
    - `needs ADR`: coherent design is possible, but an important new decision needs explicit approval;
   - `clarification`: insufficient specification evidence;
   - `aligned`: conforms to a relevant active ADR;
   - `not ADR-worthy`: local/reversible implementation detail.
5. Produce two compact tables:

| Spec area | Relevant ADR | Evidence | Finding | Required action |
| --- | --- | --- | --- | --- |

| Candidate decision | Why ADR-worthy | Alternatives/unknowns | Recommended timing |
| --- | --- | --- | --- |

6. Discuss blockers and candidate decisions with the user. For a conflict, offer explicit choices: conform the feature, narrow its scope, or supersede the governing ADR. Do not silently edit an accepted ADR.
7. Invoke or recommend an RFC or design document before `adr-create` when the decision is still too broad or unresolved. Invoke or recommend `adr-create` for a concluded new decision and `adr-supersede` for a deliberate replacement. Add links from the spec to resulting ADRs when authorized.
8. End with a gate result: `pass`, `pass with ADR actions`, or `blocked`, plus the smallest set of actions required to proceed.

During Spec-driven Development, run this review after the feature specification establishes its boundaries and again after architecture/planning introduces concrete technical commitments. Do not change the framework's normal context-loading behavior; this review is an additional decision-governance pass.
