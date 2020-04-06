up:
	docker-compose down && docker-compose build && docker-compose up -d

_test-models:
	python3 manage.py test api.models.tests.core_test

pylint:
	find . -iname "*.py" | xargs pylint
