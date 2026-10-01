from chintology.graphs.projection import project_node
from chintology.model.identifiers import SemanticId
from chintology.model.object import MathematicalObject
from chintology.model.semantic_type import SemanticType
from chintology.model.symbol import MathematicalSymbol


def test_projection_preserves_first_class_object_collaboration() -> None:
    symbol = MathematicalSymbol(
        latex=r"\mathcal{S}",
    )

    obj = MathematicalObject(
        semantic_id=SemanticId("CHI-000001"),
        name="Scheme Class",
        symbol=symbol,
        semantic_type=SemanticType("class"),
    )

    node = project_node(obj)

    assert node.semantic_id == obj.semantic_id
    assert node.name == obj.name
    assert node.symbol is obj.symbol
    assert node.semantic_type == obj.semantic_type


def test_projection_preserves_absent_symbol() -> None:
    obj = MathematicalObject(
        semantic_id=SemanticId("CHI-000002"),
        name="Symbol-Free Object",
        symbol=None,
        semantic_type=SemanticType("semantic-type"),
    )

    node = project_node(obj)

    assert node.symbol is None
