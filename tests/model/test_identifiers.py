from chintology.model.identifiers import (
    AppearanceId,
    LatexLabel,
    ProofUnitId,
    SemanticId,
)


def test_identifier_types_preserve_values() -> None:
    assert SemanticId("semantic-id").root == "semantic-id"
    assert LatexLabel("latex-label").root == "latex-label"
    assert ProofUnitId("proof-unit-id").root == "proof-unit-id"
    assert AppearanceId("appearance-id").root == "appearance-id"


def test_identifier_types_are_distinct() -> None:
    identifiers = (
        SemanticId("same-value"),
        LatexLabel("same-value"),
        ProofUnitId("same-value"),
        AppearanceId("same-value"),
    )

    assert len({type(identifier) for identifier in identifiers}) == 4