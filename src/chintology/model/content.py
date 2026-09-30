"""Mathematical content represented by the Chintology model."""

from pydantic import BaseModel, ConfigDict

from .role import ProofRole
from .semantic_type import SemanticType


class MathematicalContent(BaseModel):
    """Mathematical content of a mathematical object."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    proof_role: ProofRole
    semantic_type: SemanticType
    symbol: str | None = None
    exact_latex: str
