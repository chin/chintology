"""Mermaid rendering of graph objects."""

from chintology.graphs.node import GraphNode
from chintology.graphs.projection import project_node
from chintology.maths.registry import MathematicalRegistry


class MermaidRenderer:
    """Render a mathematical registry as Mermaid."""

    @staticmethod
    def _node_id(node: GraphNode) -> str:
        return node.semantic_id.root.replace("-", "_")

    def render_node(self, node: GraphNode) -> str:
        """Render one graph node."""

        node_id = self._node_id(node)
        name = node.name
        semantic_type = node.semantic_type.root

        if node.symbol is None:
            label = (
                "<div>"
                f"<div>{name}</div>"
                f"<div style='margin-top:12px'>{semantic_type}</div>"
                "</div>"
            )
        else:
            label = (
                "<div>"
                f"<div>{name}</div>"
                "<div style='margin:14px 0'>"
                f"$${node.symbol.latex}$$"
                "</div>"
                f"<div>{semantic_type}</div>"
                "</div>"
            )

        return f'    {node_id}["{label}"]'

    def render_relationship(
        self,
        source_id: str,
        target_id: str,
        relationship_type: str,
    ) -> str:
        """Render one graph relationship."""

        source = source_id.replace("-", "_")
        target = target_id.replace("-", "_")

        return f"    {source} -->|{relationship_type}| {target}"

    def render(self, registry: MathematicalRegistry) -> str:
        """Render a mathematical registry."""

        nodes = tuple(project_node(obj) for obj in registry.objects.objects)

        lines = ["flowchart TD"]

        lines.extend(self.render_node(node) for node in nodes)

        lines.extend(
            self.render_relationship(
                relationship.source_id.root,
                relationship.target_id.root,
                relationship.relationship_type.value,
            )
            for relationship in registry.relationships.relationships
        )

        return "\n".join(lines) + "\n"


def render_mermaid(registry: MathematicalRegistry) -> str:
    """Render a mathematical registry using Mermaid."""

    return MermaidRenderer().render(registry)
