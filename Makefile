.PHONY: test # Помечаем папку test как фиктивную

test:
	uv run pytest -v

ruff:
	uv run ruff check .
