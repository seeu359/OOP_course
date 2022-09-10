install:
	poetry install

pyt:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=OOP --cov-report xml tests/