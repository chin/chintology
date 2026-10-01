"""Mathematical-relationship collection."""

from pydantic import BaseModel, ConfigDict

from chintology.model.relationship import Relationship


class MathematicalRelationships(BaseModel):
    """Collection of mathematical relationships."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    relationships: tuple[Relationship, ...]
