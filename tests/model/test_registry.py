import pytest
from pydantic import ValidationError

from chintology.model.content import MathematicalContent
from chintology.model.identifiers import LatexLabel, SemanticId
from chintology.model.object import MathematicalObject
from chintology.model.provenance import SourceProvenance
from chintology.model.registry import TheoryRegistry
from chintology.model.relationship import Relationship
from chintology.model.relationship_type import RelationshipType
from chintology.model.role import ProofRole
from chintology.model.semantic_type import SemanticType


def make_object(identifier: str) -> MathematicalObject:
    return MathematicalObject(
        semantic_id=SemanticId(identifier),
        latex_label=LatexLabel(f"{identifier}-label"),
        content=MathematicalContent(
            proof_role=ProofRole.DEFINITION,
            semantic_type=SemanticType("semantic-type"),
            symbol=None,
            exact_latex=identifier,
        ),
        provenance=SourceProvenance(
            source="source",
            location=identifier,
        ),
    )


def make_relationship(
    identifier: str,
    source_id: str,
    target_id: str,
) -> Relationship:
    return Relationship(
        semantic_id=SemanticId(identifier),
        relationship_type=RelationshipType.USES_DEFINITION,
        source_id=SemanticId(source_id),
        target_id=SemanticId(target_id),
        provenance=SourceProvenance(
            source="source",
            location=identifier,
        ),
    )


def test_registry_accepts_objects_and_relationships() -> None:
    source = make_object("CHI-000001")
    target = make_object("CHI-000002")
    relationship = make_relationship(
        "CHI-000003",
        "CHI-000001",
        "CHI-000002",
    )

    registry = TheoryRegistry(
        objects=(source, target),
        relationships=(relationship,),
    )

    assert registry.objects == (source, target)
    assert registry.relationships == (relationship,)


def test_registry_rejects_duplicate_object_semantic_ids() -> None:
    with pytest.raises(ValidationError):
        TheoryRegistry(
            objects=(
                make_object("CHI-000001"),
                make_object("CHI-000001"),
            )
        )


def test_registry_rejects_duplicate_relationship_semantic_ids() -> None:
    source = make_object("CHI-000001")
    target = make_object("CHI-000002")

    with pytest.raises(ValidationError):
        TheoryRegistry(
            objects=(source, target),
            relationships=(
                make_relationship(
                    "CHI-000003",
                    "CHI-000001",
                    "CHI-000002",
                ),
                make_relationship(
                    "CHI-000003",
                    "CHI-000001",
                    "CHI-000002",
                ),
            ),
        )


def test_registry_rejects_semantic_id_shared_by_object_and_relationship() -> None:
    source = make_object("CHI-000001")
    target = make_object("CHI-000002")

    with pytest.raises(ValidationError):
        TheoryRegistry(
            objects=(source, target),
            relationships=(
                make_relationship(
                    "CHI-000001",
                    "CHI-000001",
                    "CHI-000002",
                ),
            ),
        )


def test_registry_rejects_unknown_relationship_source() -> None:
    target = make_object("CHI-000002")

    with pytest.raises(ValidationError):
        TheoryRegistry(
            objects=(target,),
            relationships=(
                make_relationship(
                    "CHI-000003",
                    "CHI-999999",
                    "CHI-000002",
                ),
            ),
        )


def test_registry_rejects_unknown_relationship_target() -> None:
    source = make_object("CHI-000001")

    with pytest.raises(ValidationError):
        TheoryRegistry(
            objects=(source,),
            relationships=(
                make_relationship(
                    "CHI-000003",
                    "CHI-000001",
                    "CHI-999999",
                ),
            ),
        )
