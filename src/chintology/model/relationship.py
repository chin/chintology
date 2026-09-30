"""Relationships that constitute the Chintology theory."""

from pydantic import BaseModel, ConfigDict

from .identifiers import SemanticId


class Relationship(BaseModel):
    """First-class relationship between mathematical objects."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    semantic_id: SemanticId
    source_id: SemanticId
    target_id: SemanticId
