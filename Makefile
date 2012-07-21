lint:
	pylint -r no diffbot

clean-pyc:
	find . -type f -name '*.pyc' -delete

release:
	python setup.py sdist upload
