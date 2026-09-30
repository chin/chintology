import pytest
from pydantic import ValidationError

from chintology.model.identifiers import SemanticId
from chintology.model.relationship import Relationship


def test_relationship_has_persistent_semantic_id() -> None:
    relationship_id = SemanticId("relationship-id")

    relationship = Relationship(
        semantic_id=relationship_id,
        source_id=SemanticId("source-id"),
        target_id=SemanticId("target-id"),
    )

    assert relationship.semantic_id == relationship_id


def test_relationship_references_source_and_target_semantic_ids() -> None:
    source_id = SemanticId("source-id")
    target_id = SemanticId("target-id")

    relationship = Relationship(
        semantic_id=SemanticId("relationship-id"),
        source_id=source_id,
        target_id=target_id,
    )

    assert relationship.source_id == source_id
    assert relationship.target_id == target_id


def test_relationship_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        Relationship.model_validate(
            {
                "semantic_id": "relationship-id",
                "source_id": "source-id",
                "target_id": "target-id",
                "unknown": "not allowed",
            }
        )


def test_relationship_is_immutable() -> None:
    relationship = Relationship(
        semantic_id=SemanticId("relationship-id"),
        source_id=SemanticId("source-id"),
        target_id=SemanticId("target-id"),
    )

    with pytest.raises(ValidationError):
        relationship.source_id = SemanticId("different-source")