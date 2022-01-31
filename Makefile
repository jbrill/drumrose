# Makefile

_test-models:
	coverage run --source . services/django/manage.py test services/django/api/tests/model_tests/ -v2 --pattern="*_model_tests.py"

dtest-pylint:
	docker exec -t drumrose_django-server_1 bash -c "cd /usr/local/drumrose; find . -iname '*.py' | xargs pylint --django-settings-module=api.settings --load-plugins pylint_django"

_test-pylint:
	find . -iname '*.py' | xargs pylint --django-settings-module=api.settings --load-plugins pylint_django

dtest-django:
	docker exec -t drumrose_django-server_1 bash -c "cd /usr/local/drumrose; coverage run --source . manage.py test api/tests/api_tests/ -v2 --pattern="*_apitest.py" && coverage run --source . manage.py test api/tests/serializer_tests/ -v2 --pattern="test_*.py" && coverage run --source . manage.py test api/tests/model_tests/ -v2 --pattern="*_model_tests.py" && coverage xml -o coverage.xml"

_test-views:
	coverage run --source . services/django/manage.py test services/django/api/tests/api_tests/ -v2 --pattern="*_apitest.py"

dtest-lint:
	docker exec -t drumrose_nuxt-server_1 bash -c "npm run lint;"

_test-serializers:
	coverage run --source . services/django/manage.py test services/django/api/tests/serializer_tests/ -v2 --pattern="test_*.py"
