up:
	docker-compose up -d

build:
	docker-compose build

_test-models:
	python3 services/django/manage.py test services/django/api/models/tests -v2 --pattern="*_tests.py"

dtest-pylint:
	docker exec -t drumrose_tests-server_1 bash -c "make _test-pylint"

_test-pylint:
	find . -iname '*.py' | xargs pylint

dtest-django:
	docker exec -t drumrose_django-server_1 bash -c "cd /usr/local/drumrose; make _test-models; make _test-views"

_test-views:
	echo "TEST VIEWS"
