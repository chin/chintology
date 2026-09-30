"""Mathematical objects that constitute the Chintology theory."""

from pydantic import BaseModel, ConfigDict

from .identifiers import SemanticId


class MathematicalObject(BaseModel):
    """First-class mathematical object in the Chintology theory."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    semantic_id: SemanticId
