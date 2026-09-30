"""Identifier types used by the Chintology model."""

from pydantic import RootModel


class SemanticId(RootModel[str]):
    """Persistent semantic identity of a mathematical object or relationship."""


class LatexLabel(RootModel[str]):
    """LaTeX reference label."""


class SourceId(RootModel[str]):
    """Identity of a source."""
