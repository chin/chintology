from chintology.graphs.mermaid import render_mermaid
from chintology.model.content import MathematicalContent
from chintology.model.identifiers import LatexLabel, SemanticId
from chintology.model.object import MathematicalObject
from chintology.model.provenance import SourceProvenance
from chintology.model.registry import TheoryRegistry
from chintology.model.relationship import Relationship
from chintology.model.relationship_type import RelationshipType
from chintology.model.role import ProofRole
from chintology.model.semantic_type import SemanticType


def make_object(
    semantic_id: str,
    latex_label: str,
) -> MathematicalObject:
    return MathematicalObject(
        semantic_id=SemanticId(semantic_id),
        latex_label=LatexLabel(latex_label),
        content=MathematicalContent(
            proof_role=ProofRole.DEFINITION,
            semantic_type=SemanticType("semantic-type"),
            symbol=None,
            exact_latex=semantic_id,
        ),
        provenance=SourceProvenance(
            source="source",
            location=semantic_id,
        ),
    )


def test_mermaid_renders_objects_as_nodes() -> None:
    registry = TheoryRegistry(
        objects=(
            make_object(
                "CHI-000001",
                "def:first",
            ),
            make_object(
                "CHI-000002",
                "def:second",
            ),
        ),
    )

    mermaid = render_mermaid(registry)

    assert 'CHI_000001["CHI-000001<br/>def:first"]' in mermaid
    assert 'CHI_000002["CHI-000002<br/>def:second"]' in mermaid


def test_mermaid_renders_relationships_as_edges() -> None:
    first = make_object(
        "CHI-000001",
        "def:first",
    )
    second = make_object(
        "CHI-000002",
        "def:second",
    )

    relationship = Relationship(
        semantic_id=SemanticId("CHI-000003"),
        relationship_type=RelationshipType.USES_DEFINITION,
        source_id=first.semantic_id,
        target_id=second.semantic_id,
        provenance=SourceProvenance(
            source="source",
            location="relationship",
        ),
    )

    registry = TheoryRegistry(
        objects=(first, second),
        relationships=(relationship,),
    )

    mermaid = render_mermaid(registry)

    assert "CHI_000001 -->|uses-definition| CHI_000002" in mermaid


def test_mermaid_is_derived_from_registry() -> None:
    first = make_object(
        "CHI-000001",
        "def:first",
    )

    registry = TheoryRegistry(
        objects=(first,),
    )

    assert render_mermaid(registry) == (
        'graph TD\n    CHI_000001["CHI-000001<br/>def:first"]\n'
    )
