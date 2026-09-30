import pytest

from chintology.model.role import ProofRole


def test_proof_roles_are_exact() -> None:
    assert {role.value for role in ProofRole} == {
        "definition",
        "assumption",
        "convention",
        "lemma",
        "corollary",
        "proposition",
        "theorem",
        "axiom",
        "remark",
    }


def test_unknown_proof_role_is_rejected() -> None:
    with pytest.raises(ValueError):
        ProofRole("unknown")
