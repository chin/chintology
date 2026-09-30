import pytest
from pydantic import ValidationError

from chintology.model.identifiers import SemanticId
from chintology.model.object import MathematicalObject


def test_mathematical_object_has_persistent_semantic_id() -> None:
    semantic_id = SemanticId("object-id")

    mathematical_object = MathematicalObject(
        semantic_id=semantic_id,
    )

    assert mathematical_object.semantic_id == semantic_id


def test_mathematical_object_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        MathematicalObject.model_validate(
            {
                "semantic_id": "object-id",
                "unknown": "not allowed",
            }
        )


def test_mathematical_object_is_immutable() -> None:
    mathematical_object = MathematicalObject(
        semantic_id=SemanticId("object-id"),
    )

    with pytest.raises(ValidationError):
        mathematical_object.semantic_id = SemanticId("different-id")