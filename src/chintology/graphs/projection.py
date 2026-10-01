"""Projection of mathematical objects into graph objects."""

from chintology.graphs.node import GraphNode
from chintology.model.object import MathematicalObject


def project_node(obj: MathematicalObject) -> GraphNode:
    """Project a mathematical object into a graph node."""

    return GraphNode(
        semantic_id=obj.semantic_id,
        name=obj.name,
        symbol=obj.symbol,
        semantic_type=obj.semantic_type,
    )
