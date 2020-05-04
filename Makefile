.PHONY: requirements
	server
	shell

# BASE
analyze:
	poetry run mypy taskmanager

install:
	poetry install

lint:
	poetry run flake8 taskmanager

requirements:
	poetry export -f requirements.txt --without-hashes > requirements.txt

test:
	poetry run pytest

test-with-coverage:
	poetry run pytest --cov=taskmanager tests  --cov-report xml

# DJANGO
makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

server:
	poetry run python manage.py runserver

shell:
	poetry run python manage.py shell
