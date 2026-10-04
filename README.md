# Aura XLSL

XLSL — Intelligent Spreadsheet Language is Aura's semantic workbook architecture for structured data, STEM computation, simulation, statistics, AI-assisted interpretation, provenance, and multidimensional models.

Inventor / project attribution: Seriki Yakub (KUBU LEE).

## LMLM integration

LMLM is the intelligence/orchestration layer above deterministic XLSL execution.

Model profiles in lmlm/models.json: lmlm-default, lmlm-reasoner, lmlm-code, and lmlm-vision. These are deployment aliases, not claims that a specific hosted model exists.

lmlm/provider.py exposes an OpenAI-compatible Responses adapter. Configure LMLM_BASE_URL and optionally LMLM_API_KEY.

LMLM can interpret, summarize, propose, classify, and orchestrate, but it must not silently promote a simulation or hypothesis into an observed fact.

## Optional Excel projection

tools/build_aura_xlsm.py creates Aura.xlsm from the checked-in vba/AuraHub.bas. It requires Windows, Microsoft Excel, pywin32, and Excel Trust Center permission for VBA project access.

The generated XLSM is an execution/UI projection; workbook/Aura.xlsl remains canonical.

## Runtime

Python validation: python -m pytest

C++ validation: cmake -S . -B build; cmake --build build --parallel; ctest --test-dir build --output-on-failure

## Research extensions

.xlog — experimental/provenance logs
.xsim — simulation definitions and reproducibility metadata
.xquant — quantitative/quantum-oriented state descriptions
.xdim — multidimensional data and coordinate metadata
.xphilo — assumptions, hypotheses, evidence, and research reasoning

## Epistemic policy

Aura XLSL explicitly separates observed data, deterministic derivations, simulations, hypotheses, and reference facts. Simulation is not automatically treated as proof.

## Direction

Next layers: workbook graph resolution, formula evaluation, extension validators, deterministic simulation records, XLSX projection/import, LMKM context and interpretation interfaces, and Web4 attribution/reproducibility.

Aura Ecosystem: XLSL · LMLM · LMKM · Web4 · AI · Blockchain