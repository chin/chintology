"""First-class mathematical objects."""

from pydantic import BaseModel, ConfigDict

from .identifiers import SemanticId
from .semantic_type import SemanticType
from .symbol import MathematicalSymbol


class MathematicalObject(BaseModel):
    """First-class mathematical object."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    semantic_id: SemanticId
    name: str
    symbol: MathematicalSymbol | None = None
    semantic_type: SemanticType
