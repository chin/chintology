import pytest
from pydantic import ValidationError

from chintology.model.content import MathematicalContent
from chintology.model.role import ProofRole
from chintology.model.semantic_type import SemanticType


def make_content() -> MathematicalContent:
    return MathematicalContent(
        proof_role=ProofRole.DEFINITION,
        semantic_type=SemanticType("semantic-type"),
        symbol=r"\sclass",
        exact_latex=r"\sclass",
    )


def test_mathematical_content_preserves_dimensions() -> None:
    content = make_content()

    assert content.proof_role is ProofRole.DEFINITION
    assert content.semantic_type == SemanticType("semantic-type")
    assert content.symbol == r"\sclass"
    assert content.exact_latex == r"\sclass"


def test_mathematical_content_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        MathematicalContent.model_validate(
            {
                **make_content().model_dump(),
                "unknown": "not allowed",
            }
        )


def test_mathematical_content_is_immutable() -> None:
    content = make_content()

    with pytest.raises(ValidationError):
        content.symbol = "different"
