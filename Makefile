all: build up

install:
	pip install poetry
	poetry install

build:
	docker build --rm -f --build-arg Dockerfile -t complicidad .

run_shell:
	docker run -it -p 8000:8000/tcp complicidad /bin/sh

up:
	docker run -d -p 8000:8000/tcp complicidad

down:
	docker stop $$(docker ps -a -q --filter "ancestor=complicidad") && docker rm $$(docker ps -a -q --filter "ancestor=complicidad")

attach:
	docker exec -it $$(docker ps -a -q --filter "ancestor=complicidad") /bin/sh

launch:
	flyctl launch --dockerfile ./Dockerfile

deploy:
	flyctl deploy

test:
	pytest --create-db --nomigrations -vvv
