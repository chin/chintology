.PHONY: sync lint format format-check test check fix registry registry-test graph graph-view

sync:
	uv sync --locked

lint:
	uv run --frozen ruff check .

format:
	uv run --frozen ruff format .

format-check:
	uv run --frozen ruff format --check .

test:
	uv run --frozen pytest -q

check: lint format-check test

fix:
	uv run --frozen ruff check . --fix
	uv run --frozen ruff format .

graph:
	uv run --frozen python scripts/render_maths.py

graph-view: graph
	code docs/generated/maths.md

registry:
	uv run --frozen python scripts/show_registry.py

registry-test:
	uv run --frozen pytest \
		tests/maths/test_objects.py \
		tests/maths/test_relationships.py \
		tests/maths/test_registry.py \
		tests/graphs/test_registry_render.py \
		-q