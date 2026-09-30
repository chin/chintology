"""Registry of mathematical objects and relationships."""

from pydantic import BaseModel, ConfigDict, model_validator

from .object import MathematicalObject
from .relationship import Relationship


class TheoryRegistry(BaseModel):
    """Registry of mathematical objects and relationships."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    objects: tuple[MathematicalObject, ...] = ()
    relationships: tuple[Relationship, ...] = ()

    @model_validator(mode="after")
    def validate_semantic_ids(self) -> TheoryRegistry:
        semantic_ids = [obj.semantic_id.root for obj in self.objects] + [
            relationship.semantic_id.root for relationship in self.relationships
        ]

        if len(semantic_ids) != len(set(semantic_ids)):
            raise ValueError("semantic IDs must be unique")

        return self

    @model_validator(mode="after")
    def validate_relationship_endpoints(self) -> TheoryRegistry:
        object_ids = {obj.semantic_id.root for obj in self.objects}

        for relationship in self.relationships:
            if relationship.source_id.root not in object_ids:
                raise ValueError(
                    "relationship source must reference a registered "
                    "mathematical object"
                )

            if relationship.target_id.root not in object_ids:
                raise ValueError(
                    "relationship target must reference a registered "
                    "mathematical object"
                )

        return self
