from chintology.graphs.mermaid import MermaidRenderer, render_mermaid
from chintology.graphs.node import GraphNode
from chintology.maths.objects import MathematicalObjects
from chintology.maths.registry import MathematicalRegistry
from chintology.maths.relationships import MathematicalRelationships
from chintology.model.identifiers import SemanticId
from chintology.model.object import MathematicalObject
from chintology.model.provenance import SourceProvenance
from chintology.model.relationship import Relationship
from chintology.model.relationship_type import RelationshipType
from chintology.model.semantic_type import SemanticType
from chintology.model.symbol import MathematicalSymbol


def make_object(
    semantic_id: str,
    name: str,
    symbol: MathematicalSymbol | None = None,
) -> MathematicalObject:
    return MathematicalObject(
        semantic_id=SemanticId(semantic_id),
        name=name,
        symbol=symbol,
        semantic_type=SemanticType("class"),
    )


def test_mermaid_node_layout() -> None:
    node = GraphNode(
        semantic_id=SemanticId("CHI-000001"),
        name="Scheme Class",
        symbol=MathematicalSymbol(
            latex=r"\mathcal{S}",
        ),
        semantic_type=SemanticType("class"),
    )

    renderer = MermaidRenderer()

    assert renderer.render_node(node) == (
        '    CHI_000001["'
        "<div>"
        "<div>Scheme Class</div>"
        "<div style='margin:14px 0'>"
        r"$$\mathcal{S}$$"
        "</div>"
        "<div>class</div>"
        "</div>"
        '"]'
    )


def test_mermaid_node_without_symbol() -> None:
    node = GraphNode(
        semantic_id=SemanticId("CHI-000001"),
        name="Symbol-Free Object",
        symbol=None,
        semantic_type=SemanticType("class"),
    )

    renderer = MermaidRenderer()

    assert renderer.render_node(node) == (
        '    CHI_000001["'
        "<div>"
        "<div>Symbol-Free Object</div>"
        "<div style='margin-top:12px'>class</div>"
        "</div>"
        '"]'
    )


def test_mermaid_renders_relationship() -> None:
    renderer = MermaidRenderer()

    assert (
        renderer.render_relationship(
            "CHI-000001",
            "CHI-000002",
            "uses-definition",
        )
        == "    CHI_000001 -->|uses-definition| CHI_000002"
    )


def test_mermaid_renders_registry() -> None:
    first = make_object(
        "CHI-000001",
        "Scheme Class",
        MathematicalSymbol(
            latex=r"\mathcal{S}",
        ),
    )
    second = make_object(
        "CHI-000002",
        "Adversary Class",
        MathematicalSymbol(
            latex=r"\mathcal{A}",
        ),
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

    registry = MathematicalRegistry(
        objects=MathematicalObjects(
            objects=(first, second),
        ),
        relationships=MathematicalRelationships(
            relationships=(relationship,),
        ),
    )

    mermaid = render_mermaid(registry)

    assert mermaid.startswith("flowchart TD\n")
    assert "Scheme Class" in mermaid
    assert r"$$\mathcal{S}$$" in mermaid
    assert "Adversary Class" in mermaid
    assert r"$$\mathcal{A}$$" in mermaid
    assert "CHI_000001 -->|uses-definition| CHI_000002" in mermaid
