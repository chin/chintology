"""Mathematical symbols used by first-class mathematical objects."""

from pydantic import BaseModel, ConfigDict


class MathematicalSymbol(BaseModel):
    """First-class mathematical symbol."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    latex: str
