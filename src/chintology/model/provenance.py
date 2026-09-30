"""Source provenance for mathematical objects and relationships."""

from pydantic import BaseModel, ConfigDict


class SourceProvenance(BaseModel):
    """Source location of mathematical content."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    source: str
    location: str
