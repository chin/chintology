"""Mermaid representation of a theory registry."""

from chintology.model.registry import TheoryRegistry


def render_mermaid(registry: TheoryRegistry) -> str:
    """Render a theory registry as a Mermaid directed graph."""

    lines = ["graph TD"]

    for obj in registry.objects:
        node_id = obj.semantic_id.root.replace("-", "_")
        label = obj.semantic_id.root

        if obj.latex_label is not None:
            label = f"{label}<br/>{obj.latex_label.root}"

        lines.append(f'    {node_id}["{label}"]')

    for relationship in registry.relationships:
        source_id = relationship.source_id.root.replace("-", "_")
        target_id = relationship.target_id.root.replace("-", "_")
        relationship_type = relationship.relationship_type.value

        lines.append(f"    {source_id} -->|{relationship_type}| {target_id}")

    return "\n".join(lines) + "\n"
