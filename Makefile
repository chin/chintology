.PHONY: sync lint format format-check test check fix graph graph-view

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
