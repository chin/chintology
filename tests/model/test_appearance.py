import pytest
from pydantic import ValidationError

from chintology.model.appearance import Appearance
from chintology.model.identifiers import AppearanceId, SemanticId


def test_appearance_has_distinct_identity() -> None:
    appearance = Appearance(
        appearance_id=AppearanceId("appearance-id"),
        semantic_id=SemanticId("semantic-id"),
    )

    assert appearance.appearance_id == AppearanceId("appearance-id")
    assert appearance.semantic_id == SemanticId("semantic-id")


def test_multiple_appearances_reference_same_semantic_identity() -> None:
    semantic_id = SemanticId("semantic-id")

    first = Appearance(
        appearance_id=AppearanceId("first-appearance"),
        semantic_id=semantic_id,
    )
    second = Appearance(
        appearance_id=AppearanceId("second-appearance"),
        semantic_id=semantic_id,
    )

    assert first.semantic_id == second.semantic_id
    assert first.appearance_id != second.appearance_id


def test_appearance_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        Appearance.model_validate(
            {
                "appearance_id": "appearance-id",
                "semantic_id": "semantic-id",
                "unknown": "not allowed",
            }
        )


def test_appearance_is_immutable() -> None:
    appearance = Appearance(
        appearance_id=AppearanceId("appearance-id"),
        semantic_id=SemanticId("semantic-id"),
    )

    with pytest.raises(ValidationError):
        appearance.semantic_id = SemanticId("different-id")
