import pytest
from pydantic import ValidationError

from chintology.model.identifiers import (
    AppearanceId,
    LatexLabel,
    ProofUnitId,
    SemanticId,
)


def test_identifier_types_preserve_values() -> None:
    assert SemanticId("CHI-000001").root == "CHI-000001"
    assert LatexLabel("latex-label").root == "latex-label"
    assert ProofUnitId("proof-unit-id").root == "proof-unit-id"
    assert AppearanceId("appearance-id").root == "appearance-id"


def test_identifier_types_are_distinct() -> None:
    identifiers = (
        SemanticId("CHI-000001"),
        LatexLabel("same-value"),
        ProofUnitId("same-value"),
        AppearanceId("same-value"),
    )

    assert len({type(identifier) for identifier in identifiers}) == 4


@pytest.mark.parametrize(
    "value",
    [
        "CHI-00001",
        "CHI-0000001",
        "CHI-ABCDEF",
        "chi-000001",
        "THM-000001",
        "CHI-000001-extra",
        "",
    ],
)
def test_semantic_id_rejects_invalid_grammar(value: str) -> None:
    with pytest.raises(ValidationError):
        SemanticId(value)
