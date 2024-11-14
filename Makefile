build:
	docker-compose -f local.yml up --build -d --remove-orphans

up:
	docker-compose -f local.yml up -d

down:
	docker-compose -f local.yml down

down-v:
	docker-compose -f local.yml down -v

logs:
	docker-compose -f local.yml logs -f

shell:
	docker-compose -f local.yml exec -it django /bin/bash

down-v: 
	docker-compose -f local.yml down -v

makemigrations:
	docker-compose -f local.yml run --rm django python manage.py makemigrations

migrate:
	docker-compose -f local.yml run --rm django python manage.py migrate

createsuperuser:
	docker-compose -f local.yml run --rm django python manage.py createsuperuser

collectstatic:
	docker-compose -f local.yml run --rm django python manage.py collectstatic --noinput --clear

# GIT functions
push-all:
	git add .
	git commit -m 'edits'
	git push origin -u main

push:
	git push origin -u main
	

commit:
	git add .
	git commit
	git push origin -u main

amend:
	git add .
	git commit --amend --no-edit
	git push --force origin main

# Linting
black:
	black .

sort:
	isort . 

flake:
	flake8 .