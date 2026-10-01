import pytest
from pydantic import ValidationError

from chintology.model.appearance import Appearance
from chintology.model.identifiers import (
    AppearanceId,
    LatexLabel,
    SemanticId,
)
from chintology.model.object import MathematicalObject
from chintology.model.provenance import SourceProvenance
from chintology.model.registry import TheoryRegistry
from chintology.model.relationship import Relationship
from chintology.model.relationship_type import RelationshipType
from chintology.model.role import ProofRole
from chintology.model.semantic_type import SemanticType
from chintology.model.symbol import MathematicalSymbol


def make_object(
    semantic_id: str,
    name: str = "Mathematical Object",
) -> MathematicalObject:
    return MathematicalObject(
        semantic_id=SemanticId(semantic_id),
        name=name,
        symbol=MathematicalSymbol(
            latex=r"\mathcal{S}",
        ),
        semantic_type=SemanticType("semantic-type"),
    )


def make_appearance(
    appearance_id: str,
    semantic_id: str,
) -> Appearance:
    return Appearance(
        appearance_id=AppearanceId(appearance_id),
        semantic_id=SemanticId(semantic_id),
        latex_label=LatexLabel("source-label"),
        proof_role=ProofRole.DEFINITION,
        exact_latex="source representation",
        provenance=SourceProvenance(
            source="source",
            location="location",
        ),
    )


def make_relationship(
    semantic_id: str,
    source_id: str,
    target_id: str,
) -> Relationship:
    return Relationship(
        semantic_id=SemanticId(semantic_id),
        relationship_type=RelationshipType.USES_DEFINITION,
        source_id=SemanticId(source_id),
        target_id=SemanticId(target_id),
        provenance=SourceProvenance(
            source="source",
            location="relationship",
        ),
    )


def test_registry_accepts_collaborating_objects() -> None:
    source = make_object(
        "CHI-000001",
        "Source Object",
    )
    target = make_object(
        "CHI-000002",
        "Target Object",
    )
    appearance = make_appearance(
        "source-appearance",
        "CHI-000001",
    )
    relationship = make_relationship(
        "CHI-000003",
        "CHI-000001",
        "CHI-000002",
    )

    registry = TheoryRegistry(
        objects=(source, target),
        appearances=(appearance,),
        relationships=(relationship,),
    )

    assert registry.objects == (source, target)
    assert registry.appearances == (appearance,)
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


def test_registry_rejects_object_relationship_semantic_id_collision() -> None:
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


def test_registry_rejects_duplicate_appearance_ids() -> None:
    obj = make_object("CHI-000001")

    with pytest.raises(ValidationError):
        TheoryRegistry(
            objects=(obj,),
            appearances=(
                make_appearance(
                    "same-appearance",
                    "CHI-000001",
                ),
                make_appearance(
                    "same-appearance",
                    "CHI-000001",
                ),
            ),
        )


def test_registry_rejects_unknown_appearance_object() -> None:
    obj = make_object("CHI-000001")

    with pytest.raises(ValidationError):
        TheoryRegistry(
            objects=(obj,),
            appearances=(
                make_appearance(
                    "appearance",
                    "CHI-999999",
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
