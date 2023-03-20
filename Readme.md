## Improvements:
    - Add tests
    - Add repository pattern
    - Cron job to delete old shortened urls
    - Ability to predefine custom shortened url
    - Add throttling / obligate user to sign in
    - Add shell waiter script for pg

## Setup
API documentation is available at http://0.0.0.0:8000/swagger

### Create environment variables
    make set_env

### Setup pre-commit hooks
    make hooks_setup

### Run project
    make build & make run

## Basic Commands

### Make migrations
    make migrations

### Run migrations
    make migrate

### Create superuser
    make createsuperuser
