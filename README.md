# Тестовый проект для изучения CI/CD

##  Пошаговая настройка

0. Создали вирутальное окружение
1. `pip install uv`
2. `uv init --bare`
3. `uv add ruff`
4. `uv add pytest`
5. `uv run ruff check .`
6. `uv run ruff format --check`
7. `uv run ruff format --diff`
8. `uv run ruff format .`