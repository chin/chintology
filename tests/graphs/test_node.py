import pytest
from pydantic import ValidationError

from chintology.graphs.node import GraphNode
from chintology.model.identifiers import SemanticId
from chintology.model.semantic_type import SemanticType
from chintology.model.symbol import MathematicalSymbol


def make_node() -> GraphNode:
    return GraphNode(
        semantic_id=SemanticId("CHI-000001"),
        name="Scheme Class",
        symbol=MathematicalSymbol(
            latex=r"\mathcal{S}",
        ),
        semantic_type=SemanticType("class"),
    )


def test_graph_node_preserves_graph_semantics() -> None:
    node = make_node()

    assert node.semantic_id == SemanticId("CHI-000001")
    assert node.name == "Scheme Class"
    assert node.symbol == MathematicalSymbol(
        latex=r"\mathcal{S}",
    )
    assert node.semantic_type == SemanticType("class")


def test_graph_node_allows_absent_symbol() -> None:
    node = GraphNode(
        semantic_id=SemanticId("CHI-000002"),
        name="Symbol-Free Object",
        symbol=None,
        semantic_type=SemanticType("semantic-type"),
    )

    assert node.symbol is None


def test_graph_node_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        GraphNode.model_validate(
            {
                **make_node().model_dump(),
                "unknown": "not allowed",
            }
        )


def test_graph_node_is_immutable() -> None:
    node = make_node()

    with pytest.raises(ValidationError):
        node.name = "Different Object"
