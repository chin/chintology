import pytest
from pydantic import ValidationError

from chintology.model.symbol import MathematicalSymbol


def test_mathematical_symbol_preserves_macro_and_latex() -> None:
    symbol = MathematicalSymbol(
        macro=r"\symbol",
        latex=r"\mathcal{S}",
    )

    assert symbol.macro == r"\symbol"
    assert symbol.latex == r"\mathcal{S}"


def test_mathematical_symbol_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        MathematicalSymbol.model_validate(
            {
                "macro": r"\symbol",
                "latex": r"\mathcal{S}",
                "unknown": "not allowed",
            }
        )


def test_mathematical_symbol_is_immutable() -> None:
    symbol = MathematicalSymbol(
        macro=r"\symbol",
        latex=r"\mathcal{S}",
    )

    with pytest.raises(ValidationError):
        symbol.latex = r"\mathcal{T}"
