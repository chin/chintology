import pytest
from pydantic import ValidationError

from chintology.maths.objects import MathematicalObjects
from chintology.model.identifiers import SemanticId
from chintology.model.object import MathematicalObject
from chintology.model.semantic_type import SemanticType
from chintology.model.symbol import MathematicalSymbol


def make_object() -> MathematicalObject:
    return MathematicalObject(
        semantic_id=SemanticId("CHI-000001"),
        name="Scheme Class",
        symbol=MathematicalSymbol(
            latex=r"\mathcal{S}",
        ),
        semantic_type=SemanticType("class"),
    )


def test_mathematical_objects_preserves_objects() -> None:
    obj = make_object()

    objects = MathematicalObjects(
        objects=(obj,),
    )

    assert objects.objects == (obj,)


def test_mathematical_objects_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        MathematicalObjects.model_validate(
            {
                "objects": [
                    make_object().model_dump(),
                ],
                "unknown": "not allowed",
            }
        )


def test_mathematical_objects_is_immutable() -> None:
    objects = MathematicalObjects(
        objects=(make_object(),),
    )

    with pytest.raises(ValidationError):
        objects.objects = ()
