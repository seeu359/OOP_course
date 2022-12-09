install:
	poetry install

lint:
	poetry run flake8 oop

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=oop --cov-report xml tests/