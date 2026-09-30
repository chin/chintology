import pytest
from pydantic import ValidationError

from chintology.model.provenance import SourceProvenance


def test_source_provenance_preserves_source_and_location() -> None:
    provenance = SourceProvenance(
        source="source",
        location="location",
    )

    assert provenance.source == "source"
    assert provenance.location == "location"


def test_source_provenance_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        SourceProvenance.model_validate(
            {
                "source": "source",
                "location": "location",
                "unknown": "not allowed",
            }
        )


def test_source_provenance_is_immutable() -> None:
    provenance = SourceProvenance(
        source="source",
        location="location",
    )

    with pytest.raises(ValidationError):
        provenance.location = "different"
