"""Types of relationships between mathematical objects."""

from enum import StrEnum


class RelationshipType(StrEnum):
    USES_DEFINITION = "uses-definition"
    ASSUMES = "assumes"
    PROVES = "proves"
    SPECIALIZES = "specializes"
    APPEARS_IN = "appears-in"
