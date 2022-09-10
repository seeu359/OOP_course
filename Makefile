install:
	poetry install

pyt:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=oop --cov-report xml tests/