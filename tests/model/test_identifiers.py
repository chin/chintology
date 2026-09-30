from chintology.model.identifiers import SemanticId


def test_semantic_id_preserves_value() -> None:
    semantic_id = SemanticId("semantic-id")

    assert semantic_id.root == "semantic-id"