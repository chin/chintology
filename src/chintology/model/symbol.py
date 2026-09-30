"""Mathematical symbol representation."""

from pydantic import BaseModel, ConfigDict


class MathematicalSymbol(BaseModel):
    """Mathematical symbol and its LaTeX representation."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    macro: str
    latex: str
