.PHONY: analyze
analyze:
	poetry run mypy taskmanager

.PHONY: install
install:
	poetry install

.PHONY: lint
lint:
	poetry run flake8 taskmanager

.PHONY: test
test:
	poetry run pytest

.PHONY: test-with-coverage
test-with-coverage:
	poetry run pytest --cov=taskmanager tests  --cov-report xml

.PHONY: createsuperuser
createsuperuser:
	poetry run python manage.py createsuperuser

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: server
server:
	poetry run python manage.py runserver

.PHONY: shell
shell:
	poetry run python manage.py shell

requirements.txt: pyproject.toml
requirements:
	poetry export -f requirements.txt --without-hashes > requirements.txt
