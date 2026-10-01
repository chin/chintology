"""Display the materialized mathematical registry."""

from pathlib import Path

from chintology.maths.registry import load_registry

REGISTRY_PATH = Path("src/chintology/maths/registry.json")


def main() -> None:
    registry = load_registry(REGISTRY_PATH)

    print(f"Objects: {len(registry.objects.objects)}")
    print(f"Relationships: {len(registry.relationships.relationships)}")
    print()

    for obj in registry.objects.objects:
        symbol = obj.symbol.latex if obj.symbol else "-"

        print(
            f"{obj.semantic_id.root:12} "
            f"{obj.name:40} "
            f"{symbol:30} "
            f"{obj.semantic_type.root}"
        )

    if registry.relationships.relationships:
        print()

    for relationship in registry.relationships.relationships:
        print(
            f"{relationship.semantic_id.root:12} "
            f"{relationship.source_id.root} "
            f"--{relationship.relationship_type.value}--> "
            f"{relationship.target_id.root}"
        )


if __name__ == "__main__":
    main()
