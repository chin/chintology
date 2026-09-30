"""Roles of mathematical objects in the proof system."""

from enum import StrEnum


class ProofRole(StrEnum):
    """Role of a mathematical object in the proof system."""

    DEFINITION = "definition"
    ASSUMPTION = "assumption"
    CONVENTION = "convention"
    LEMMA = "lemma"
    COROLLARY = "corollary"
    PROPOSITION = "proposition"
    THEOREM = "theorem"
    AXIOM = "axiom"
    REMARK = "remark"
