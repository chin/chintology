from chintology.model.identifiers import LatexLabel, SemanticId, SourceId


def test_identifier_types_are_distinct() -> None:
    assert type(SemanticId("x")) is not type(LatexLabel("x"))
    assert type(SemanticId("x")) is not type(SourceId("x"))
