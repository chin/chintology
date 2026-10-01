"""Render the mathematical registry graph."""

from pathlib import Path

from chintology.graphs.mermaid import render_mermaid
from chintology.maths.registry import load_registry

REGISTRY_PATH = Path("src/chintology/maths/registry.json")
OUTPUT_PATH = Path("docs/generated/maths.md")


def main() -> None:
    registry = load_registry(REGISTRY_PATH)
    mermaid = render_mermaid(registry)

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_PATH.write_text(f"# Mathematical Registry\n\n```mermaid\n{mermaid}```\n")

    print(OUTPUT_PATH)


if __name__ == "__main__":
    main()
