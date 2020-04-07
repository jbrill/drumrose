up:
	docker-compose up -d

build:
	docker-compose build

_test-models:
	python3 manage.py test api.models.tests.core_test

dtest-pylint:
	docker exec -t drumrose_tests-server_1 bash -c "make _test-pylint"

_test-pylint:
	find . -iname '*.py' | xargs pylint
