"""Render a theory graph demonstration."""

from pathlib import Path

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
            semantic_type=SemanticType("demonstration"),
            symbol=None,
            exact_latex=semantic_id,
        ),
        provenance=SourceProvenance(
            source="demonstration",
            location=semantic_id,
        ),
    )


def main() -> None:
    first = make_object(
        "CHI-900001",
        "demo:first",
    )
    second = make_object(
        "CHI-900002",
        "demo:second",
    )

    relationship = Relationship(
        semantic_id=SemanticId("CHI-900003"),
        relationship_type=RelationshipType.USES_DEFINITION,
        source_id=first.semantic_id,
        target_id=second.semantic_id,
        provenance=SourceProvenance(
            source="demonstration",
            location="relationship",
        ),
    )

    registry = TheoryRegistry(
        objects=(first, second),
        relationships=(relationship,),
    )

    output = Path("docs/generated/graph-demo.md")
    output.parent.mkdir(parents=True, exist_ok=True)

    mermaid = render_mermaid(registry)

    output.write_text(f"# Theory Graph Demonstration\n\n```mermaid\n{mermaid}```\n")

    print(output)


if __name__ == "__main__":
    main()
