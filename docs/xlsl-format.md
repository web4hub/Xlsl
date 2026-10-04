# XLSL Workbook Format v0.1

XLSL uses UTF-8 JSON as its canonical interchange representation while retaining the `.xlsl` extension. This keeps the first reference implementation deterministic and easy to validate.

## Required top-level fields

- `format`: must be `XLSL`.
- `version`: semantic format version.
- `workbook`: stable workbook identifier.
- `metadata`: human and machine-readable metadata.
- `sheets`: array of typed sheet definitions.

## Sheet model

Each sheet has:

- `id`
- `name`
- `kind`
- `columns`
- `rows`
- optional `dimensions`
- optional `artifacts`

Rows are objects keyed by column identifier. Values must remain JSON-native.

## Artifact model

Artifacts are referenced by stable identifiers and may declare:

- `type`: dataset, model, simulation, hypothesis, evidence, result, or provenance.
- `status`
- `inputs`
- `outputs`
- `provenance`

## Extension namespaces

Extension records live under `extensions` and use the canonical names `xlog`, `xsim`, `xquant`, `xdim`, and `xphilo`.

## Compatibility

The semantic model can be projected into XLSX for users who need conventional spreadsheet tooling. A projection must not silently discard provenance, dimensions, hypotheses, or model metadata.
