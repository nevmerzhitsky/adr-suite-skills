---
name: adr-audit
description: Audit docs/adrs/ for naming, numbering, metadata, lifecycle links, status consistency, and stale references. Use for repository health checks or after batch ADR changes; semantic status changes still require user approval.
license: MIT
metadata:
  family: "adr-suite"
---

# Audit the ADR repository

Validate structure mechanically, then review semantic consistency separately.

## Checks

- directory is `docs/adrs/`;
- filenames match `NNNN-short-title.md`, use unique four-digit numbers, and are not unexpectedly renumbered;
- frontmatter contains `number`, `title`, `status`, `date`, `decision-makers`, `consulted`, `informed`, `supersedes`, and `superseded-by`;
- status is one of `draft`, `accepted`, `rejected`, `withdrawn`, `deprecated`, `superseded`;
- H1 number/title agree with frontmatter;
- required sections exist: Context and problem statement, Decision drivers, Considered options, Decision outcome, Consequences, Confirmation, Links;
- the decision outcome names the selected option, explains why it won against the drivers, and makes a clear active commitment;
- material trade-offs are recorded with consistent option names and concrete good and bad arguments, plus neutral arguments when they matter;
- confirmation names an observable check, review, metric, or other evidence that can confirm the decision and implementation agree;
- local ADR links resolve;
- `superseded` has one or more valid `superseded-by` links and reciprocal `supersedes` metadata exists;
- non-superseded ADRs do not claim a replacement;
- accepted ADRs are not contradicted by another accepted ADR without an explicit scope distinction;
- documentation does not cite a historical ADR as currently governing.
- `docs/adrs/README.md` has a bounded catalog region with one sorted entry per ADR, and each entry's number, title, status, date, and replacement link match frontmatter.

## Workflow

1. Run `scripts/validate_adrs.py [repository-root]` when available for deterministic checks.
2. Read every reported file before proposing a repair. Separate mechanical errors from semantic findings.
3. Report findings by severity, file, evidence, and suggested action. Missing rationale or an apparent contradiction is a review finding, not an automatic rewrite.
4. Mechanical repairs may be applied when the user requested fixes. Never change a semantic status, decision, or supersession relation without explicit authorization.
5. Regenerate only the machine-maintained catalog region in `docs/adrs/README.md`, creating it when absent, and preserve surrounding human prose. The catalog must include every ADR, sorted by number, with number, title, status, date, and replacement link.
6. Re-run validation and summarize remaining semantic issues.

The validator intentionally does not decide whether an architectural choice is correct or whether two accepted ADRs truly conflict; those require evidence and judgment.
