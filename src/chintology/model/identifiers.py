"""Identifier types used by the Chintology model."""

import re

from pydantic import RootModel, field_validator


class SemanticId(RootModel[str]):
    """Persistent semantic identity of a mathematical object or relationship."""

    @field_validator("root")
    @classmethod
    def validate_semantic_id(cls, value: str) -> str:
        if not re.fullmatch(r"CHI-[0-9]{6}", value):
            raise ValueError("semantic ID must match CHI-NNNNNN")

        return value


class LatexLabel(RootModel[str]):
    """LaTeX reference label."""


class ProofUnitId(RootModel[str]):
    """Identity of a proof unit."""


class AppearanceId(RootModel[str]):
    """Identity of an appearance."""
