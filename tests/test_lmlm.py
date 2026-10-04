from lmlm.provider import load_models, resolve_model

def test_model_registry_contains_core_profiles():
    registry = load_models()
    ids = {item["id"] for item in registry["models"]}
    assert {"lmlm-default", "lmlm-reasoner", "lmlm-code", "lmlm-vision"} <= ids

def test_resolve_model():
    assert resolve_model("lmlm-reasoner")["role"] == "reasoning"
