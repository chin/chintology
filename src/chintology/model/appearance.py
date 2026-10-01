"""First-class appearances of mathematical objects."""

from pydantic import BaseModel, ConfigDict

from .identifiers import AppearanceId, LatexLabel, SemanticId
from .provenance import SourceProvenance
from .role import ProofRole


class Appearance(BaseModel):
    """Source-specific appearance of a mathematical object."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    appearance_id: AppearanceId
    semantic_id: SemanticId
    latex_label: LatexLabel | None = None
    proof_role: ProofRole
    exact_latex: str
    provenance: SourceProvenance
