from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_model_package_exists() -> None:
    assert (ROOT / "src/chintology/model").is_dir()
    assert (ROOT / "src/chintology/model/__init__.py").is_file()


def test_maths_package_exists() -> None:
    assert (ROOT / "src/chintology/maths").is_dir()
    assert (ROOT / "src/chintology/maths/__init__.py").is_file()