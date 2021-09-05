up:
	docker-compose up -d

build:
	docker-compose build

_test-models:
	coverage run --source . services/django/manage.py test services/django/api/tests/model_tests/ -v2 --pattern="*_model_tests.py"

dtest-pylint:
	docker exec -t drumrose_django-server_1 bash -c "cd /usr/local/drumrose; make _test-pylint"

_test-pylint:
	find . -iname '*.py' | xargs pylint --django-settings-module=api.settings --load-plugins pylint_django

dtest-django:
	docker exec -t drumrose_django-server_1 bash -c "cd /usr/local/drumrose; make _test-models; make _test-views; make _test-serializers; coverage report -m;"

_test-views:
	coverage run --source . services/django/manage.py test services/django/api/tests/api_tests/ -v2 --pattern="*_apitest.py"

dtest-lint:
	docker exec -t drumrose_nuxt-server_1 bash -c "npm run lint;"

_test-serializers:
	coverage run --source . services/django/manage.py test services/django/api/tests/serializer_tests/ -v2 --pattern="test_*.py"
