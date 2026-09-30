from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHINTOLOGY = ROOT / "src" / "chintology"
ARCHITECTURE = ROOT / "docs" / "architecture"


def test_initial_chintology_package_layout() -> None:
    package_dirs = {
        path.name
        for path in CHINTOLOGY.iterdir()
        if path.is_dir() and path.name != "__pycache__"
    }

    assert package_dirs == {"model", "maths"}


def test_initial_chintology_packages() -> None:
    assert (CHINTOLOGY / "__init__.py").is_file()
    assert (CHINTOLOGY / "model" / "__init__.py").is_file()
    assert (CHINTOLOGY / "maths" / "__init__.py").is_file()


def test_architecture_documents_exist() -> None:
    architecture_docs = {path.name for path in ARCHITECTURE.glob("*.md")}

    assert architecture_docs == {
        "graphs.md",
        "maths.md",
        "model.md",
    }


def test_repository_conventions_exist() -> None:
    assert (ROOT / "docs" / "conventions.md").is_file()
