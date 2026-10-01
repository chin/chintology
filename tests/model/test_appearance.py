import pytest
from pydantic import ValidationError

from chintology.model.appearance import Appearance
from chintology.model.identifiers import AppearanceId, LatexLabel, SemanticId
from chintology.model.provenance import SourceProvenance
from chintology.model.role import ProofRole


def make_appearance() -> Appearance:
    return Appearance(
        appearance_id=AppearanceId("source-scheme-class"),
        semantic_id=SemanticId("CHI-000001"),
        latex_label=LatexLabel("def:gen-scheme-class"),
        proof_role=ProofRole.DEFINITION,
        exact_latex=(
            r"Let $\sclass$ be a class of admissible protected objects that "
            r"encode systems, protocols, problems, or schemes."
        ),
        provenance=SourceProvenance(
            source="Article 1",
            location="def:gen-scheme-class",
        ),
    )


def test_appearance_has_distinct_identity() -> None:
    appearance = make_appearance()

    assert appearance.appearance_id == AppearanceId("source-scheme-class")
    assert appearance.semantic_id == SemanticId("CHI-000001")


def test_appearance_preserves_latex_label() -> None:
    appearance = make_appearance()

    assert appearance.latex_label == LatexLabel("def:gen-scheme-class")


def test_appearance_preserves_proof_role() -> None:
    appearance = make_appearance()

    assert appearance.proof_role is ProofRole.DEFINITION


def test_appearance_preserves_exact_latex() -> None:
    appearance = make_appearance()

    assert appearance.exact_latex == (
        r"Let $\sclass$ be a class of admissible protected objects that "
        r"encode systems, protocols, problems, or schemes."
    )


def test_appearance_preserves_provenance() -> None:
    appearance = make_appearance()

    assert appearance.provenance == SourceProvenance(
        source="Article 1",
        location="def:gen-scheme-class",
    )


def test_multiple_appearances_reference_same_semantic_identity() -> None:
    first = make_appearance()

    second = Appearance(
        appearance_id=AppearanceId("second-appearance"),
        semantic_id=first.semantic_id,
        latex_label=None,
        proof_role=ProofRole.DEFINITION,
        exact_latex="second representation",
        provenance=SourceProvenance(
            source="second source",
            location="second location",
        ),
    )

    assert first.semantic_id == second.semantic_id
    assert first.appearance_id != second.appearance_id


def test_appearance_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        Appearance.model_validate(
            {
                **make_appearance().model_dump(),
                "unknown": "not allowed",
            }
        )


def test_appearance_is_immutable() -> None:
    appearance = make_appearance()

    with pytest.raises(ValidationError):
        appearance.exact_latex = "different"
