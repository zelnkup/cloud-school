hooks_setup:
	pip3 install black flake8 isort[pyproject] pre-commit
	pre-commit install

set_env:
	cp .env.example .env

build:
	docker-compose build

run:
	docker-compose up

migrations:
	docker-compose run --rm backend python manage.py makemigrations

migrate:
	docker-compose run --rm backend python manage.py migrate

superuser:
	docker-compose run --rm backend python manage.py createsuperuser
