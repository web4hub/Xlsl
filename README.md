# Aura XLSL

**XLSL — Intelligent Spreadsheet Language** is Aura's semantic workbook architecture for structured data, STEM computation, simulation, statistics, AI-assisted interpretation, provenance, and multidimensional models.

Inventor / project attribution: **Seriki Yakub (KUBU LEE)**.

## Repository

```
Xlsl/
├── workbook/
│   ├── Aura.xlsl
│   └── Braneworld.xlsl
├── src/
│   └── xlsl_runtime.py
├── engine/
│   └── include/auraxlsl/survival/log_rank.hpp
├── tests/
│   ├── test_xlsl_runtime.py
│   └── log_rank_test.cpp
├── docs/
│   ├── architecture.md
│   ├── xlsl-format.md
│   ├── research-methodology.md
│   └── attribution.md
├── extensions/
│   ├── xlog_spec.md
│   ├── xsim_spec.md
│   ├── xquant_spec.md
│   ├── xdim_spec.md
│   └── xphilo_spec.md
└── simulations/
    └── teleportation_pipeline.md
```

## Core model

The semantic workbook is Aura. XLSL treats a workbook as a graph of typed sheets and research artifacts rather than only a rectangular grid.

The canonical `.xlsl` representation is UTF-8 JSON in v0.1. XLSX remains an interoperability format; semantic metadata such as provenance, dimensions, hypotheses, and simulation records must not be silently discarded during projection.

## Aura research workbooks

- **Aura.xlsl** — top-level research orchestrator.
- **Braneworld.xlsl** — theoretical physics research model.
- Cortex, Memory, Vision, and Synapse are reserved for the wider Aura intelligence/LMKM workbook family.

## Runtime

The Python reference runtime provides deterministic loading and structural validation:

```bash
python -m pytest
```

The C++ statistical engine remains independently buildable:

```bash
cmake -S . -B build
cmake --build build --parallel
ctest --test-dir build --output-on-failure
```

The two-sample log-rank implementation includes input validation, deterministic ordering, tied-event handling, expected events, hypergeometric variance, chi-square, signed Z, two-sided p-value, and zero-variance handling. It should be independently checked against a trusted statistical reference before production use.

## Research extensions

- `.xlog` — experimental/provenance logs
- `.xsim` — simulation definitions and reproducibility metadata
- `.xquant` — quantitative/quantum-oriented state descriptions
- `.xdim` — multidimensional data and coordinate metadata
- `.xphilo` — assumptions, hypotheses, evidence, and research reasoning

## Epistemic policy

Aura XLSL explicitly separates observed data, deterministic derivations, simulations, hypotheses, and reference facts.

The teleportation pipeline is a conceptual research model. TP-001 through TP-006 are progressively speculative states; TP-006 human-scale teleportation is theoretical and currently infeasible. A simulation result is never automatically interpreted as proof of physical feasibility.

## Direction

The next runtime layers are:

1. workbook graph resolution;
2. formula evaluation;
3. extension validators;
4. deterministic simulation records;
5. XLSX projection/import;
6. LMKM context and interpretation interfaces;
7. Web4 attribution and reproducibility records.

This repository is the foundation for the broader Aura Ecosystem: **XLSL · LMKM · Web4 · AI · Blockchain**.
