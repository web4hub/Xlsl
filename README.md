# Aura XLSL

**XLSL — Intelligent Spreadsheet Language** is a research-workbook architecture for combining structured data, STEM computation, simulation, statistics, AI-assisted interpretation, provenance, and multidimensional models.

## Repository

Xlsl/
- README.md
- CMakeLists.txt
- engine/include/auraxlsl/survival/log_rank.hpp
- tests/log_rank_test.cpp
- docs/specification.md
- docs/statistics/log-rank.md
- docs/statistics/survival-analysis.md
- extensions/xlog_spec.md
- extensions/xsim_spec.md
- extensions/xquant_spec.md
- extensions/xdim_spec.md
- extensions/xphilo_spec.md
- simulations/teleportation_pipeline.md

## Core concept

The semantic workbook is Aura. XLSL treats a spreadsheet as more than a rectangular grid: sheets can represent datasets, formulas, simulations, models, assumptions, provenance, and research results.

The .xlsl layer can use .xlsx as an interchange format while preserving richer semantic metadata through XLSL extensions.

## Research modules

- Pure Mathematics
- Further Mathematics
- Applied Physics
- Reasoning Logic
- Simulation Problems
- Statistical analysis
- AI interpretation and prediction
- Multidimensional research data

## Statistical engine

The repository now contains a C++17 reference implementation of a two-sample log-rank test with explicit input validation, deterministic time ordering, tied-event handling, expected-event and hypergeometric variance calculation, chi-square, signed Z, two-sided p-value, and zero-variance handling.

Build and test:

cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure

The statistical implementation should be independently checked against R's survival package before being treated as a production statistical library.

## Teleportation research

The teleportation pipeline is a conceptual simulation/research model. TP-001 through TP-006 describe progressively more speculative scenarios. TP-006 human teleportation is explicitly a theoretical/infeasible model, not an engineering claim or experimental procedure.

## Extensions

- .xlog — provenance/event logs
- .xsim — simulation definitions
- .xquant — quantitative/quantum state descriptions
- .xdim — multidimensional data
- .xphilo — assumptions, hypotheses, evidence, and research reasoning

## Status

This repository is being rebuilt incrementally from the Aura research specification. The executable core is intentionally small first: establish deterministic, testable primitives before expanding the workbook runtime.
