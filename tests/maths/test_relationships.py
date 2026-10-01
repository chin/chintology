import pytest
from pydantic import ValidationError

from chintology.maths.relationships import MathematicalRelationships
from chintology.model.identifiers import SemanticId
from chintology.model.provenance import SourceProvenance
from chintology.model.relationship import Relationship
from chintology.model.relationship_type import RelationshipType


def make_relationship() -> Relationship:
    return Relationship(
        semantic_id=SemanticId("CHI-000003"),
        relationship_type=RelationshipType.USES_DEFINITION,
        source_id=SemanticId("CHI-000001"),
        target_id=SemanticId("CHI-000002"),
        provenance=SourceProvenance(
            source="source",
            location="relationship",
        ),
    )


def test_mathematical_relationships_preserves_relationships() -> None:
    relationship = make_relationship()

    relationships = MathematicalRelationships(
        relationships=(relationship,),
    )

    assert relationships.relationships == (relationship,)


def test_mathematical_relationships_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        MathematicalRelationships.model_validate(
            {
                "relationships": [
                    make_relationship().model_dump(),
                ],
                "unknown": "not allowed",
            }
        )


def test_mathematical_relationships_is_immutable() -> None:
    relationships = MathematicalRelationships(
        relationships=(make_relationship(),),
    )

    with pytest.raises(ValidationError):
        relationships.relationships = ()
