---
name: adr-create
description: Facilitate an architectural decision, compare alternatives with the user, and create a new ADR in docs/adrs/. Use when a topic has meaningful architectural trade-offs; do not use for routine implementation details.
license: MIT
metadata:
  family: "adr-suite"
---

# Create an ADR

Turn one architecturally significant topic into one explicit decision and one ADR. Do not jump from the initial prompt directly to a preferred solution when material trade-offs remain.

## Repository convention

- Store ADRs in `docs/adrs/`.
- Name them `NNNN-short-title.md`: four digits starting at `0001`, followed by a stable lowercase ASCII kebab-case slug.
- Allocate `max(existing ADR number) + 1`. Never reuse gaps or renumber an existing ADR.
- Give every ADR the stable ID `ADR-NNNN`, where `NNNN` matches its H1, filename, and frontmatter `number`; for example, `ADR-0001`.
- Once created, do not rename or renumber an ADR merely because its title changes; its stable ID and links are more important.
- Cite ADRs in documentation and code by stable ID, not filename or title alone.
- In an ADR body, including `## Links`, cite, reference, or link only to lower-numbered ADRs whose `date` is not later than the current ADR's date. The `superseded-by` frontmatter field is the sole exception for replacement lifecycle metadata.
- Keep decision provenance one-way. A specification, plan, RFC, design note, or other source document used to create the ADR links to the ADR; the ADR must not mention, cite, or link back to that source document.
- Use only these statuses: `draft`, `accepted`, `rejected`, `withdrawn`, `deprecated`, `superseded`.
- Use `decision-makers` for people who made the decision. Always include `consulted` and `informed`; use empty lists when they do not apply.

## Existing ADR discovery

- Treat existing ADRs as available only when `docs/adrs/README.md` exists, contains an ADR catalog with ADR links, and `docs/adrs/` contains at least one ADR file other than `README.md`.
- If any of those conditions is false, do not search for or require existing ADRs. When no ADR files exist, create the first record as `ADR-0001` and create the catalog with it. When ADR files exist but the catalog is missing or does not list ADRs, do not inspect those files to reconstruct the corpus; ask the operator before a change that depends on their numbering or lifecycle.
- When the corpus is available, read the catalog and list local ADR files before reading only the records relevant to the decision. Do not search outside `docs/adrs/` for ADRs. Follow only a specific external ADR file linked directly from `docs/adrs/README.md`.
- Do not search project-wide architecture documents, constitutions, or Spec-driven Development context or memory to locate ADRs. An operator-named document may be source evidence for this new ADR, but it is not an ADR-discovery source.

## When to record

- Record a decision that affects system structure, non-functional qualities, dependencies, interfaces, engineering standards, or a costly-to-reverse implementation path.
- Keep the ADR to one decision. Split bundled choices when they can be changed independently.
- For a broad or cross-team change that needs extended exploration, resolve the alternatives in an RFC or design document first. When that work concludes, create the ADR, shorten the source document's decision-record content, and link from the source document to the ADR. Do not add the reciprocal source link to the ADR.
- Do not require an RFC for a contained decision. An ADR can record it directly once the decision-makers agree.

## Workflow

1. Read the request, its explicit constraints, operator-named source documents, and only the code/tests needed to ground the decision. If existing ADR discovery is available, read the catalog, list local ADR files, and read only relevant ADR records. Track each non-ADR project document used to frame, explore, or record this decision as a source document.
2. Restate the decision boundary as a problem statement: context, scope, facts, competing forces, constraints, decision drivers, and what is deliberately out of scope. Keep this neutral; do not smuggle the preferred solution into it. Surface unknowns rather than inventing them.
3. Identify credible alternatives. Include the status quo when it is viable. Merge cosmetically different variants; keep genuinely different trade-offs separate.
4. Compare the alternatives against decision drivers. Cover benefits, costs, neutral effects, reversibility, migration, operational effects, security/privacy, compatibility, and evidence gaps when relevant.
5. Discuss the decision with the user. Ask a small batch of high-leverage questions, preferably 1–3 at a time. Use selectable options when choices are known and an open question when the user's rationale or a missing alternative matters. Explain the consequence of each option.
6. Record the selected option only after the user decides. State the outcome in active voice: `We will ...`. If the user wants documentation before deciding, create a `draft` with the unresolved questions visible. Set `accepted` only on explicit user approval.
7. If existing ADR discovery is available, check for overlap or conflict with the relevant discovered ADRs. If the new decision replaces an active ADR, use the `adr-supersede` workflow instead.
8. Write the next numbered file with its matching stable ID. Validate its links, metadata, that it does not mention or link a source document, and that every ADR reference in its body has a lower number and a date no later than the current ADR's date.
9. For each writable local source document, replace duplicated rationale, alternatives, consequences, and lifecycle text with a concise problem statement and, for an accepted ADR, its current result, plus a relative link labeled with the stable ADR ID. For a draft ADR, retain only the problem and link; do not copy its status or present an outcome as governing. Preserve independent requirements, contracts, acceptance criteria, target-state descriptions, and implementation evidence. Ask before editing when that boundary is ambiguous.
10. Do not edit generated or read-only source documents. Locate and update their maintaining source instead. If a source document cannot be normalized or linked without an unresolved semantic choice, ask the user and report the ADR change set as incomplete until the source side is resolved.
11. Refresh the bounded ADR catalog region in `docs/adrs/README.md`, creating it when absent. Include every ADR, sorted by number, with stable ID, title, status, date, and replacement link. Preserve prose outside the region.

## ADR shape

Use the stable structure in [assets/adr.md](assets/adr.md). Read it before writing an ADR, replace every `{placeholder}`, and omit no required section.

For a replacement, use bare relative filenames in frontmatter, for example `supersedes: ADR-0001` and `superseded-by: ADR-0002`. The later `superseded-by` value is lifecycle metadata, not a body reference. In the replacement ADR, cite the replaced record as `[ADR-0001](0001-old-decision.md)`. Do not add the replacement ADR to the old ADR's body.

Number the options consecutively in `Considered options`. Use the same option numbers and names in `Pros and cons of options`, include each number in its heading, and identify the selected option in `Decision outcome` by its number only. For every option, state material good and bad effects, including failure modes where relevant. In `Consequences`, describe effects of adopting the selected option rather than repeating the comparison arguments. Add neutral effects only when they carry useful information. In `Confirmation`, name observable evidence such as a test, metric, or operational check that can confirm or challenge the decision. Use relative Markdown links within the repository, but never link a source document used to create the ADR.

Write for the future maintainer who needs to understand why the system is constrained this way. Prefer full sentences and short paragraphs. Bullets should carry complete facts or arguments, not fragments. Keep most ADRs to one or two pages. Keep enough rationale in the ADR to make it self-contained; link only independent supporting evidence, never a source specification, plan, RFC, or design note from which the ADR was created.

Accepted ADRs are immutable records of a decision. Correct typos, clarify wording without changing meaning, and maintain lifecycle links in place; use a new ADR for a material decision change.
