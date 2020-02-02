pylint:
	find . -iname "*.py" | xargs pylint


docker:
	docker build -t neptune-nuxt services/neptune-nuxt
