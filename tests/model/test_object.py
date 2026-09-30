import pytest
from pydantic import ValidationError

from chintology.model.content import MathematicalContent
from chintology.model.identifiers import LatexLabel, SemanticId
from chintology.model.object import MathematicalObject
from chintology.model.provenance import SourceProvenance
from chintology.model.role import ProofRole
from chintology.model.semantic_type import SemanticType


def make_mathematical_object() -> MathematicalObject:
    return MathematicalObject(
        semantic_id=SemanticId("CHI-000001"),
        latex_label=LatexLabel("latex-label"),
        content=MathematicalContent(
            proof_role=ProofRole.DEFINITION,
            semantic_type=SemanticType("semantic-type"),
            symbol=r"\sclass",
            exact_latex=r"\sclass",
        ),
        provenance=SourceProvenance(
            source="source",
            location="location",
        ),
    )


def test_mathematical_object_has_persistent_semantic_id() -> None:
    mathematical_object = make_mathematical_object()

    assert mathematical_object.semantic_id == SemanticId("CHI-000001")


def test_mathematical_object_preserves_latex_label() -> None:
    mathematical_object = make_mathematical_object()

    assert mathematical_object.latex_label == LatexLabel("latex-label")


def test_mathematical_object_preserves_content() -> None:
    mathematical_object = make_mathematical_object()

    assert mathematical_object.content == MathematicalContent(
        proof_role=ProofRole.DEFINITION,
        semantic_type=SemanticType("semantic-type"),
        symbol=r"\sclass",
        exact_latex=r"\sclass",
    )


def test_mathematical_object_preserves_provenance() -> None:
    mathematical_object = make_mathematical_object()

    assert mathematical_object.provenance == SourceProvenance(
        source="source",
        location="location",
    )


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
        mathematical_object.semantic_id = SemanticId("CHI-000002")
