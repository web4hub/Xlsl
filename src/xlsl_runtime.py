"""Minimal deterministic XLSL v0.1 loader and validator."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class XlslValidationError(ValueError):
    """Raised when an XLSL document violates the v0.1 structural contract."""


REQUIRED_ROOT = {"format", "version", "workbook", "metadata", "sheets"}


def load_workbook(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    data = json.loads(p.read_text(encoding="utf-8"))
    validate_workbook(data)
    return data


def validate_workbook(data: dict[str, Any]) -> None:
    if not isinstance(data, dict):
        raise XlslValidationError("workbook must be a JSON object")

    missing = REQUIRED_ROOT - data.keys()
    if missing:
        raise XlslValidationError(f"missing root fields: {sorted(missing)}")

    if data["format"] != "XLSL":
        raise XlslValidationError("format must be XLSL")

    if not isinstance(data["version"], str) or not data["version"]:
        raise XlslValidationError("version must be a non-empty string")

    if not isinstance(data["workbook"], str) or not data["workbook"]:
        raise XlslValidationError("workbook must be a non-empty string")

    if not isinstance(data["metadata"], dict):
        raise XlslValidationError("metadata must be an object")

    _validate_agency_extension(data.get("extensions"))

    sheets = data["sheets"]
    if not isinstance(sheets, list):
        raise XlslValidationError("sheets must be an array")

    seen: set[str] = set()
    for sheet in sheets:
        _validate_sheet(sheet, seen)


def _validate_sheet(sheet: Any, seen: set[str]) -> None:
    if not isinstance(sheet, dict):
        raise XlslValidationError("each sheet must be an object")

    for field in ("id", "name", "kind", "columns", "rows"):
        if field not in sheet:
            raise XlslValidationError(f"sheet missing field: {field}")

    sid = sheet["id"]
    if not isinstance(sid, str) or not sid:
        raise XlslValidationError("sheet id must be a non-empty string")
    if sid in seen:
        raise XlslValidationError(f"duplicate sheet id: {sid}")
    seen.add(sid)

    if not isinstance(sheet["columns"], list) or not all(
        isinstance(c, str) and c for c in sheet["columns"]
    ):
        raise XlslValidationError(f"invalid columns in sheet: {sid}")

    if not isinstance(sheet["rows"], list):
        raise XlslValidationError(f"rows must be an array in sheet: {sid}")

    allowed = set(sheet["columns"])
    for index, row in enumerate(sheet["rows"], start=1):
        if not isinstance(row, dict):
            raise XlslValidationError(f"row {index} in {sid} must be an object")
        unknown = set(row) - allowed
        if unknown:
            raise XlslValidationError(
                f"row {index} in {sid} has unknown columns: {sorted(unknown)}"
            )


def _validate_agency_extension(extensions: Any) -> None:
    """Validate optional human/model decision-boundary provenance."""
    if extensions is None or "agency" not in extensions:
        return
    agency = extensions["agency"]
    if not isinstance(agency, dict):
        raise XlslValidationError("agency extension must be an object")
    records = agency.get("records", [])
    if not isinstance(records, list):
        raise XlslValidationError("agency records must be an array")
    allowed = {"intent_owner", "decision_owner", "execution_owner", "verification_owner"}
    owners = {"human", "model", "shared", "automated"}
    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise XlslValidationError(f"agency record {index} must be an object")
        unknown = set(record) - (allowed | {"operation", "evidence"})
        if unknown:
            raise XlslValidationError(f"agency record {index} has unknown fields: {sorted(unknown)}")
        if not record.get("operation"):
            raise XlslValidationError(f"agency record {index} needs operation")
        for field in allowed:
            if field in record and record[field] not in owners:
                raise XlslValidationError(f"agency record {index} has invalid {field}: {record[field]!r}")


def agency_summary(data: dict[str, Any]) -> dict[str, int]:
    """Return deterministic counts of ownership decisions in an XLSL workbook."""
    validate_workbook(data)
    records = ((data.get("extensions") or {}).get("agency") or {}).get("records", [])
    counts = {"human": 0, "model": 0, "shared": 0, "automated": 0}
    for record in records:
        for field in ("intent_owner", "decision_owner", "execution_owner", "verification_owner"):
            owner = record.get(field)
            if owner in counts:
                counts[owner] += 1
    return counts


def workbook_summary(data: dict[str, Any]) -> dict[str, Any]:
    validate_workbook(data)
    return {
        "workbook": data["workbook"],
        "version": data["version"],
        "sheets": len(data["sheets"]),
        "rows": sum(len(sheet["rows"]) for sheet in data["sheets"]),
        "extensions": sorted((data.get("extensions") or {}).keys()),
    }
