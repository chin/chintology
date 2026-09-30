import pytest
from pydantic import ValidationError

from chintology.model.identifiers import SemanticId
from chintology.model.provenance import SourceProvenance
from chintology.model.relationship import Relationship
from chintology.model.relationship_type import RelationshipType


def make_relationship() -> Relationship:
    return Relationship(
        semantic_id=SemanticId("relationship-id"),
        relationship_type=RelationshipType.ASSUMES,
        source_id=SemanticId("source-id"),
        target_id=SemanticId("target-id"),
        provenance=SourceProvenance(
            source="source",
            location="location",
        ),
    )


def test_relationship_has_persistent_semantic_id() -> None:
    relationship = make_relationship()

    assert relationship.semantic_id == SemanticId("relationship-id")


def test_relationship_preserves_relationship_type() -> None:
    relationship = make_relationship()

    assert relationship.relationship_type is RelationshipType.ASSUMES


def test_relationship_references_source_and_target_semantic_ids() -> None:
    relationship = make_relationship()

    assert relationship.source_id == SemanticId("source-id")
    assert relationship.target_id == SemanticId("target-id")


def test_relationship_preserves_provenance() -> None:
    relationship = make_relationship()

    assert relationship.provenance == SourceProvenance(
        source="source",
        location="location",
    )


def test_relationship_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        Relationship.model_validate(
            {
                **make_relationship().model_dump(),
                "unknown": "not allowed",
            }
        )


def test_relationship_is_immutable() -> None:
    relationship = make_relationship()

    with pytest.raises(ValidationError):
        relationship.source_id = SemanticId("different-source")
