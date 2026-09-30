"""Semantic mathematical types used by the Chintology model."""

from pydantic import RootModel


class SemanticType(RootModel[str]):
    """Semantic mathematical type of a mathematical object or relationship."""
