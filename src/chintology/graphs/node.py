"""Renderer-independent graph representation of a mathematical object."""

from pydantic import BaseModel, ConfigDict

from chintology.model.identifiers import SemanticId
from chintology.model.semantic_type import SemanticType
from chintology.model.symbol import MathematicalSymbol


class GraphNode(BaseModel):
    """Graph representation of a mathematical object."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    semantic_id: SemanticId
    name: str
    symbol: MathematicalSymbol | None = None
    semantic_type: SemanticType
