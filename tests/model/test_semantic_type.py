from chintology.model.semantic_type import SemanticType


def test_semantic_type_preserves_value() -> None:
    semantic_type = SemanticType("semantic-type")

    assert semantic_type.root == "semantic-type"
