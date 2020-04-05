pylint:
	find . -iname "*.py" | xargs pylint

up:
	docker-compose down && docker-compose build && docker-compose up -d
