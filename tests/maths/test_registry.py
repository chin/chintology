from pathlib import Path

import pytest
from pydantic import ValidationError

from chintology.maths.objects import MathematicalObjects
from chintology.maths.registry import (
    MathematicalRegistry,
    load_registry,
)
from chintology.maths.relationships import MathematicalRelationships
from chintology.model.identifiers import SemanticId
from chintology.model.object import MathematicalObject
from chintology.model.provenance import SourceProvenance
from chintology.model.relationship import Relationship
from chintology.model.relationship_type import RelationshipType
from chintology.model.semantic_type import SemanticType
from chintology.model.symbol import MathematicalSymbol


def make_object(
    semantic_id: str,
    name: str,
) -> MathematicalObject:
    return MathematicalObject(
        semantic_id=SemanticId(semantic_id),
        name=name,
        symbol=MathematicalSymbol(
            latex=r"\mathcal{S}",
        ),
        semantic_type=SemanticType("class"),
    )


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


def test_mathematical_registry_preserves_groupings() -> None:
    objects = MathematicalObjects(
        objects=(
            make_object("CHI-000001", "First Object"),
            make_object("CHI-000002", "Second Object"),
        )
    )
    relationships = MathematicalRelationships(relationships=(make_relationship(),))

    registry = MathematicalRegistry(
        objects=objects,
        relationships=relationships,
    )

    assert registry.objects is objects
    assert registry.relationships is relationships


def test_mathematical_registry_rejects_unknown_fields() -> None:
    registry = MathematicalRegistry(
        objects=MathematicalObjects(objects=()),
        relationships=MathematicalRelationships(relationships=()),
    )

    with pytest.raises(ValidationError):
        MathematicalRegistry.model_validate(
            {
                **registry.model_dump(),
                "unknown": "not allowed",
            }
        )


def test_mathematical_registry_is_immutable() -> None:
    registry = MathematicalRegistry(
        objects=MathematicalObjects(objects=()),
        relationships=MathematicalRelationships(relationships=()),
    )

    with pytest.raises(ValidationError):
        registry.objects = MathematicalObjects(objects=())


REGISTRY = Path("src/chintology/maths/registry.json")


def test_registry_json_loads() -> None:
    registry = load_registry(REGISTRY)

    assert isinstance(registry, MathematicalRegistry)


def test_registry_json_materializes_objects() -> None:
    registry = load_registry(REGISTRY)

    objects = registry.objects.objects

    assert len(objects) == 25

    by_id = {obj.semantic_id.root: obj for obj in objects}

    assert set(by_id) == {f"CHI-{number:06d}" for number in range(1, 26)}

    scheme_class = by_id["CHI-000001"]

    assert scheme_class.semantic_id == SemanticId("CHI-000001")
    assert scheme_class.name == "Scheme Class"
    assert scheme_class.symbol == MathematicalSymbol(
        latex=r"\mathcal{S}",
    )
    assert scheme_class.semantic_type == SemanticType("class")

    odds_ratio = by_id["CHI-000025"]

    assert odds_ratio.name == "Event-to-Complement Odds Ratio"
    assert odds_ratio.semantic_type == SemanticType("proposition")


def test_registry_json_materializes_relationships() -> None:
    registry = load_registry(REGISTRY)

    assert registry.relationships.relationships == ()


def test_registry_rejects_duplicate_object_semantic_ids() -> None:
    first = make_object(
        "CHI-000001",
        "First Object",
    )
    second = make_object(
        "CHI-000001",
        "Second Object",
    )

    with pytest.raises(
        ValidationError,
        match="semantic IDs must be unique",
    ):
        MathematicalRegistry(
            objects=MathematicalObjects(
                objects=(first, second),
            ),
            relationships=MathematicalRelationships(
                relationships=(),
            ),
        )


def test_registry_rejects_object_relationship_id_collision() -> None:
    first = make_object(
        "CHI-000001",
        "First Object",
    )
    second = make_object(
        "CHI-000002",
        "Second Object",
    )

    relationship = Relationship(
        semantic_id=SemanticId("CHI-000001"),
        relationship_type=RelationshipType.USES_DEFINITION,
        source_id=first.semantic_id,
        target_id=second.semantic_id,
        provenance=SourceProvenance(
            source="source",
            location="relationship",
        ),
    )

    with pytest.raises(
        ValidationError,
        match="semantic IDs must be unique",
    ):
        MathematicalRegistry(
            objects=MathematicalObjects(
                objects=(first, second),
            ),
            relationships=MathematicalRelationships(
                relationships=(relationship,),
            ),
        )


def test_registry_rejects_unknown_relationship_source() -> None:
    target = make_object(
        "CHI-000002",
        "Target Object",
    )

    relationship = Relationship(
        semantic_id=SemanticId("CHI-000003"),
        relationship_type=RelationshipType.USES_DEFINITION,
        source_id=SemanticId("CHI-999999"),
        target_id=target.semantic_id,
        provenance=SourceProvenance(
            source="source",
            location="relationship",
        ),
    )

    with pytest.raises(
        ValidationError,
        match="relationship source must reference",
    ):
        MathematicalRegistry(
            objects=MathematicalObjects(
                objects=(target,),
            ),
            relationships=MathematicalRelationships(
                relationships=(relationship,),
            ),
        )


def test_registry_rejects_unknown_relationship_target() -> None:
    source = make_object(
        "CHI-000001",
        "Source Object",
    )

    relationship = Relationship(
        semantic_id=SemanticId("CHI-000003"),
        relationship_type=RelationshipType.USES_DEFINITION,
        source_id=source.semantic_id,
        target_id=SemanticId("CHI-999999"),
        provenance=SourceProvenance(
            source="source",
            location="relationship",
        ),
    )

    with pytest.raises(
        ValidationError,
        match="relationship target must reference",
    ):
        MathematicalRegistry(
            objects=MathematicalObjects(
                objects=(source,),
            ),
            relationships=MathematicalRelationships(
                relationships=(relationship,),
            ),
        )
