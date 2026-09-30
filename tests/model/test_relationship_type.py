import pytest

from chintology.model.relationship_type import RelationshipType


def test_relationship_types_are_exact() -> None:
    assert {relationship_type.value for relationship_type in RelationshipType} == {
        "uses-definition",
        "assumes",
        "proves",
        "specializes",
        "appears-in",
    }


def test_unknown_relationship_type_is_rejected() -> None:
    with pytest.raises(ValueError):
        RelationshipType("unknown")
