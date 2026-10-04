# Human/model agency boundary

Aura XLSL records the division of labor between the human architect, LMLM, and deterministic automation.

Each agency record captures who supplied intent, who made a decision, who executed an operation, and who verified the result. The dimensions are independent: a model may execute code without owning the architectural decision, while automation may verify an invariant without owning research intent.

Allowed owners are `human`, `model`, `shared`, and `automated`.

Agency metadata never changes evidence status. LMLM output remains interpretation or proposal unless a separate deterministic or human verification step promotes it.

Pipeline:

`human intent -> XLSL specification -> deterministic execution -> LMLM interpretation -> verification -> provenance`

The runtime validates agency records and exposes `agency_summary(workbook)` for deterministic longitudinal measurement.
