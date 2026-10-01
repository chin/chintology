from pathlib import Path

from chintology.graphs.mermaid import render_mermaid
from chintology.maths.registry import load_registry

REGISTRY_PATH = Path("src/chintology/maths/registry.json")


def test_registry_json_renders_graph() -> None:
    registry = load_registry(REGISTRY_PATH)

    mermaid = render_mermaid(registry)

    assert "Scheme Class" in mermaid
    assert r"$$\mathcal{S}$$" in mermaid

    assert "Adversary Class" in mermaid
    assert r"$$\mathcal{A}$$" in mermaid


def test_registry_json_graph_has_no_unregistered_relationships() -> None:
    registry = load_registry(REGISTRY_PATH)

    assert registry.relationships.relationships == ()
