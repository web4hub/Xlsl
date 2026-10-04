"""OpenAI-compatible LMLM adapter for Aura XLSL."""
from __future__ import annotations
import json
import os
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

DEFAULT_MODEL = "lmlm-default"
DEFAULT_BASE_URL = "http://localhost:8000/v1/responses"

def load_models(path: str | Path | None = None) -> dict[str, Any]:
    model_path = Path(path or Path(__file__).with_name("models.json"))
    return json.loads(model_path.read_text(encoding="utf-8"))

def resolve_model(model: str = DEFAULT_MODEL, path: str | Path | None = None) -> dict[str, Any]:
    registry = load_models(path)
    for item in registry.get("models", []):
        if item.get("id") == model:
            return item
    raise ValueError(f"Unknown LMLM model profile: {model}")

def responses(input_text: str, *, model: str = DEFAULT_MODEL,
              base_url: str | None = None, api_key: str | None = None,
              instructions: str | None = None, timeout: float = 60.0) -> dict[str, Any]:
    resolve_model(model)
    endpoint = base_url or os.getenv("LMLM_BASE_URL", DEFAULT_BASE_URL)
    token = api_key or os.getenv("LMLM_API_KEY")
    payload: dict[str, Any] = {"model": model, "input": input_text}
    if instructions:
        payload["instructions"] = instructions
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(endpoint, data=json.dumps(payload).encode("utf-8"),
                      headers=headers, method="POST")
    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))
