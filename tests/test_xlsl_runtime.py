import json
from pathlib import Path

import pytest

from src.xlsl_runtime import XlslValidationError, load_workbook, validate_workbook, workbook_summary


ROOT = Path(__file__).resolve().parents[1]


def test_aura_workbook_loads():
    data = load_workbook(ROOT / "workbook" / "Aura.xlsl")
    assert data["format"] == "XLSL"
    assert data["workbook"] == "aura.research"


def test_braneworld_workbook_loads():
    data = load_workbook(ROOT / "workbook" / "Braneworld.xlsl")
    assert data["workbook"] == "aura.braneworld"
    assert "xphilo" in data["extensions"]


def test_summary_is_deterministic():
    data = load_workbook(ROOT / "workbook" / "Aura.xlsl")
    summary = workbook_summary(data)
    assert summary["sheets"] == 2
    assert summary["rows"] == 6


def test_duplicate_sheet_ids_rejected():
    data = load_workbook(ROOT / "workbook" / "Aura.xlsl")
    data["sheets"].append(dict(data["sheets"][0]))
    with pytest.raises(XlslValidationError):
        validate_workbook(data)


def test_unknown_row_column_rejected():
    data = load_workbook(ROOT / "workbook" / "Aura.xlsl")
    data["sheets"][0]["rows"][0]["not_a_column"] = True
    with pytest.raises(XlslValidationError):
        validate_workbook(data)
