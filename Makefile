up:
	docker-compose up -d

build:
	docker-compose build

_test-models:
	coverage run --source . services/django/manage.py test services/django/api/models/tests -v2 --pattern="*_model_tests.py"

dtest-pylint:
	docker exec -t drumrose_tests-server_1 bash -c "make _test-pylint"

_test-pylint:
	find . -iname '*.py' | xargs pylint

dtest-django:
	docker exec -t drumrose_django-server_1 bash -c "cd /usr/local/drumrose; make _test-models; make _test-views; make _test-serializers; coverage report -m;"

_test-views:
	coverage run --source . services/django/manage.py test services/django/api/serializers/tests -v2 --pattern="*_view_tests.py"

dtest-lint:
	docker exec -t drumrose_nuxt-server_1 bash -c "npm run lint;"

_test-serializers:
	coverage run --source . services/django/manage.py test services/django/api/serializers/tests -v2 --pattern="test_*.py"
