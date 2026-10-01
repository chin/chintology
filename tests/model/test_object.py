import pytest
from pydantic import ValidationError

from chintology.model.content import MathematicalContent
from chintology.model.identifiers import LatexLabel, SemanticId
from chintology.model.object import MathematicalObject
from chintology.model.semantic_type import SemanticType
from chintology.model.symbol import MathematicalSymbol


def make_mathematical_object() -> MathematicalObject:
    return MathematicalObject(
        semantic_id=SemanticId("CHI-000001"),
        name="Scheme Class",
        symbol=MathematicalSymbol(
            latex=r"\mathcal{S}",
        ),
        semantic_type=SemanticType("class"),
    )


def test_mathematical_object_has_persistent_semantic_id() -> None:
    mathematical_object = make_mathematical_object()

    assert mathematical_object.semantic_id == SemanticId("CHI-000001")


def test_mathematical_object_preserves_name() -> None:
    mathematical_object = make_mathematical_object()

    assert mathematical_object.name == "Scheme Class"


def test_mathematical_object_collaborates_with_symbol() -> None:
    mathematical_object = make_mathematical_object()

    assert mathematical_object.symbol == MathematicalSymbol(
        latex=r"\mathcal{S}",
    )


def test_mathematical_object_preserves_semantic_type() -> None:
    mathematical_object = make_mathematical_object()

    assert mathematical_object.semantic_type == SemanticType("class")


def test_mathematical_object_allows_absent_symbol() -> None:
    mathematical_object = MathematicalObject(
        semantic_id=SemanticId("CHI-000002"),
        name="Symbol-Free Object",
        symbol=None,
        semantic_type=SemanticType("semantic-type"),
    )

    assert mathematical_object.symbol is None


def test_mathematical_object_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        MathematicalObject.model_validate(
            {
                **make_mathematical_object().model_dump(),
                "unknown": "not allowed",
            }
        )


def test_mathematical_object_is_immutable() -> None:
    mathematical_object = make_mathematical_object()

    with pytest.raises(ValidationError):
        mathematical_object.name = "Different Object"
