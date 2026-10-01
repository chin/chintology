"""Mathematical registry schema and loading."""

from pathlib import Path

from pydantic import BaseModel, ConfigDict, model_validator

from chintology.maths.objects import MathematicalObjects
from chintology.maths.relationships import MathematicalRelationships


class MathematicalRegistry(BaseModel):
    """Collection of mathematical objects and relationships."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    objects: MathematicalObjects
    relationships: MathematicalRelationships

    @model_validator(mode="after")
    def validate_semantic_ids(self) -> MathematicalRegistry:
        object_ids = [obj.semantic_id.root for obj in self.objects.objects]
        relationship_ids = [
            relationship.semantic_id.root
            for relationship in self.relationships.relationships
        ]
        semantic_ids = object_ids + relationship_ids

        if len(semantic_ids) != len(set(semantic_ids)):
            raise ValueError("semantic IDs must be unique")

        return self

    @model_validator(mode="after")
    def validate_relationship_endpoints(self) -> MathematicalRegistry:
        object_ids = {obj.semantic_id.root for obj in self.objects.objects}

        for relationship in self.relationships.relationships:
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


def load_registry(path: Path) -> MathematicalRegistry:
    """Load and validate a mathematical registry."""

    return MathematicalRegistry.model_validate_json(path.read_text())
