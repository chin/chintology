"""Mathematical-object collection."""

from pydantic import BaseModel, ConfigDict

from chintology.model.object import MathematicalObject


class MathematicalObjects(BaseModel):
    """Collection of mathematical objects."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    objects: tuple[MathematicalObject, ...]
