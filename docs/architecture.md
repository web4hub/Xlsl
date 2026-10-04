# Aura XLSL Architecture

## Purpose

Aura XLSL is the semantic workbook layer for Aura research. It unifies structured spreadsheet data, deterministic computation, simulation, AI/LMKM interpretation, multidimensional models, quantum-oriented representations, provenance, and Web4 attribution.

## Layers

```
Aura Research
├── XLSL semantic workbook
│   ├── metadata
│   ├── sheets
│   ├── dimensions
│   ├── formulas
│   ├── models
│   ├── experiments
│   └── results
├── LMKM intelligence layer
│   ├── retrieval
│   ├── reasoning
│   ├── interpretation
│   └── execution proposals
├── STEM engines
│   ├── mathematics
│   ├── physics
│   ├── statistics
│   └── simulation
├── Extensions
│   ├── XLOG
│   ├── XSIM
│   ├── XQUANT
│   ├── XDIM
│   └── XPHILO
└── Web4 provenance
    ├── identity
    ├── attribution
    └── reproducibility
```

XLSX remains an interoperability format. XLSL is the semantic source model.

## Workbook graph

A workbook is a directed graph of typed sheets and artifacts rather than only a two-dimensional grid. A sheet may reference another sheet, dataset, model, simulation, or extension record by stable identifier.

## Execution contract

1. Load and validate the workbook document.
2. Resolve sheet and artifact identifiers.
3. Validate dimensions and declared types.
4. Evaluate deterministic formulas.
5. Execute explicitly enabled simulations.
6. Record inputs, outputs, environment, and provenance.
7. Expose results to LMKM as structured context.
8. Never promote a hypothesis or simulation result into an established fact automatically.

## Current reference modules

- `Aura.xlsl`: top-level research orchestration workbook.
- `Braneworld.xlsl`: theoretical physics research model.
- `Cortex.xlsl`, `Memory.xlsl`, `Vision.xlsl`, and `Synapse.xlsl`: reserved model workbooks for the wider Aura intelligence stack.

## Design principle

Deterministic primitives come first. AI-assisted interpretation is an orchestration layer around inspectable data and computation, not a replacement for validation.
