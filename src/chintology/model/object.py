"""Mathematical objects that constitute the Chintology theory."""

from pydantic import BaseModel, ConfigDict

from .content import MathematicalContent
from .identifiers import LatexLabel, SemanticId
from .provenance import SourceProvenance


class MathematicalObject(BaseModel):
    """First-class mathematical object in the Chintology theory."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    semantic_id: SemanticId
    latex_label: LatexLabel | None = None
    content: MathematicalContent
    provenance: SourceProvenance
