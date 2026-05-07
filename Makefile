.PHONY: test # Помечаем папку test как фиктивную

test:
	uv run pytest -v

ruff:

	uv run ruff check --output-format=github --exit-non-zero-on-fix .

# --exit-non-zero-on-fix выходит с отрицательным результатом
