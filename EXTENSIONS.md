# Recommended Extensions

## Further useful skills

The next additions with the highest practical value would be:

- `adr-impact-analysis`: trace a proposed ADR across code, schemas, APIs, tests, operations, and migration work before acceptance.
- `adr-implementation-check`: verify that the current implementation still conforms to accepted ADRs and report architectural drift.
- `adr-review-calendar`: find accepted ADRs whose assumptions, validation date, or external dependencies merit re-evaluation. This should propose reviews, never expire decisions automatically.
- `adr-migration-plan`: turn an accepted replacement ADR into staged migration, compatibility, rollback, and removal checkpoints.
- `adr-rfc-promote`: convert a larger exploratory RFC/design document into one or more focused ADRs once decisions are made.

These are intentionally not folded into `adr-create`: impact analysis, conformance, periodic review, and execution planning have different evidence and mutation boundaries.
