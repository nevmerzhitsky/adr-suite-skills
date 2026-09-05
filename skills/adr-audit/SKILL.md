---
name: adr-audit
description: Audit docs/adrs/ for stable IDs, naming, numbering, metadata, lifecycle links, status consistency, and stale references. Use for repository health checks or after batch ADR changes; semantic status changes still require user approval.
license: MIT
metadata:
  family: "adr-suite"
---

# Audit the ADR repository

Validate structure mechanically, then review semantic consistency separately.

## Checks

- directory is `docs/adrs/`;
- filenames match `NNNN-short-title.md`, use unique four-digit numbers, and are not unexpectedly renumbered;
- every H1 starts with a unique stable `ADR-NNNN` ID whose number matches the filename and frontmatter `number`;
- frontmatter contains `number`, `title`, `status`, `date`, `decision-makers`, `consulted`, `informed`, `supersedes`, and `superseded-by`;
- status is one of `draft`, `accepted`, `rejected`, `withdrawn`, `deprecated`, `superseded`;
- H1 ID/title agree with filename and frontmatter;
- required sections exist: Context and problem statement, Decision drivers, Considered options, Decision outcome, Consequences, Confirmation, Links;
- the considered options are numbered; an accepted, deprecated, or superseded ADR identifies the historically selected option by number, explains why it won against the drivers, and retains the original active commitment; a rejected ADR makes no governing commitment and records why it was declined; an unresolved draft or withdrawn ADR may state that no option was selected;
- material trade-offs are recorded under headings with consistent option numbers and names, with concrete good and bad arguments, plus neutral arguments when they matter;
- consequences in an accepted, deprecated, or superseded ADR describe the effects of adopting the selected option rather than duplicating comparison arguments; an unresolved draft identifies undetermined consequences without fabricating them;
- confirmation in an accepted, deprecated, or superseded ADR names an observable check, review, metric, or other evidence that can confirm the decision and implementation agree; an unresolved draft instead names evidence or review needed to decide;
- local ADR links resolve;
- each ADR body, including `## Links`, cites, references, or links only lower-numbered ADRs whose `date` is not later than the current ADR's date. The `superseded-by` frontmatter field is the sole lifecycle-metadata exception;
- `superseded` has one or more valid `superseded-by` links and reciprocal `supersedes` metadata exists;
- non-superseded ADRs do not claim a replacement;
- accepted ADRs are not contradicted by another accepted ADR without an explicit scope distinction;
- documentation does not cite a historical ADR as currently governing;
- documentation and code cite ADRs by stable `ADR-NNNN` ID rather than filename or title alone;
- source project documents contain only a concise problem statement, the current result only for an accepted applicable decision, and its stable ADR link, rather than duplicating the ADR's rationale, alternatives, consequences, or lifecycle;
- decision provenance is one-way: an ADR does not mention, cite, or link a source document used to create or harvest it, while each source document or its writable maintaining source links to the resulting ADR, or to its accepted replacement when a living current-state document has moved on; intentionally historical text may retain the old link; an unresolved read-only or external source-side change is a finding, not an exception;
- `docs/adrs/README.md` has a bounded catalog region with one sorted entry per ADR, and each entry's stable ID, title, status, date, and replacement link match frontmatter.

## Workflow

1. Run `scripts/validate_adrs.py [repository-root]` when available for deterministic checks.
2. Read every reported file before proposing a repair. Separate mechanical errors from semantic findings.
3. Report findings by severity, file, evidence, and suggested action. Treat duplicated decision-record content and reciprocal ADR/source-document references as semantic findings unless provenance is mechanically unambiguous. Missing rationale or an apparent contradiction is a review finding, not an automatic rewrite.
4. Mechanical repairs may be applied when the user requested fixes. Never change a semantic status, decision, or supersession relation without explicit authorization.
5. Regenerate only the machine-maintained catalog region in `docs/adrs/README.md`, creating it when absent, and preserve surrounding human prose. The catalog must include every ADR, sorted by number, with stable ID, title, status, date, and replacement link.
6. Re-run validation and summarize remaining semantic issues.

The validator intentionally does not decide whether an architectural choice is correct or whether two accepted ADRs truly conflict; those require evidence and judgment.
