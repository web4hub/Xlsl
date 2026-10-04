# LMLM integration

Aura XLSL treats LMLM as an intelligence/orchestration layer above the deterministic workbook runtime.

## Model profiles

lmlm/models.json defines deployment-neutral profiles:
- lmlm-default — general research orchestration
- lmlm-reasoner — hypothesis/model review
- lmlm-code — code and runtime tasks
- lmlm-vision — multimodal and visualization review

These are logical aliases. A deployment can map them to an actual local or remote model.

## Provider

lmlm/provider.py exposes an OpenAI-compatible responses adapter. Configure LMLM_BASE_URL and optionally LMLM_API_KEY. The default endpoint is http://localhost:8000/v1/responses.

The provider is separate from the XLSL validator: an unavailable model must not make deterministic workbook validation fail.

## Epistemic boundary

LMLM may interpret, summarize, propose, classify, and orchestrate. It must not silently promote a hypothesis or simulation into an observed fact.

Recommended flow:

XLSL -> validation -> deterministic computation -> LMLM interpretation -> provenance/result record
