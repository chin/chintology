"""Registry of first-class theory objects and their collaborations."""

from pydantic import BaseModel, ConfigDict, model_validator

from .appearance import Appearance
from .object import MathematicalObject
from .relationship import Relationship


class TheoryRegistry(BaseModel):
    """Registry of mathematical objects, appearances, and relationships."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    objects: tuple[MathematicalObject, ...] = ()
    appearances: tuple[Appearance, ...] = ()
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
    def validate_appearance_ids(self) -> TheoryRegistry:
        appearance_ids = [
            appearance.appearance_id.root for appearance in self.appearances
        ]

        if len(appearance_ids) != len(set(appearance_ids)):
            raise ValueError("appearance IDs must be unique")

        return self

    @model_validator(mode="after")
    def validate_appearance_references(self) -> TheoryRegistry:
        object_ids = {obj.semantic_id.root for obj in self.objects}

        for appearance in self.appearances:
            if appearance.semantic_id.root not in object_ids:
                raise ValueError(
                    "appearance must reference a registered mathematical object"
                )

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
