"""Appearances of mathematical objects and relationships."""

from pydantic import BaseModel, ConfigDict

from .identifiers import AppearanceId, SemanticId


class Appearance(BaseModel):
    """Appearance of a mathematical object or relationship."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    appearance_id: AppearanceId
    semantic_id: SemanticId
