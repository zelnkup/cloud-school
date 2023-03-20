hooks_setup:
	pip3 install black flake8 isort[pyproject] pre-commit
	pre-commit install

set_env:
	cp .env.example .env

build:
	docker-compose build

run:
	docker-compose up
