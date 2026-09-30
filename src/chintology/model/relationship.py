"""Relationships that constitute the Chintology theory."""

from pydantic import BaseModel, ConfigDict

from .identifiers import SemanticId
from .provenance import SourceProvenance
from .relationship_type import RelationshipType


class Relationship(BaseModel):
    """First-class relationship between mathematical objects."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    semantic_id: SemanticId
    relationship_type: RelationshipType
    source_id: SemanticId
    target_id: SemanticId
    provenance: SourceProvenance
