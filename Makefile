clean:
	find glask -name '*.pyc' -delete
	find tests -name '*.pyc' -delete

venv:
	virtualenv venv

setup: venv
	venv/bin/python setup.py develop

test: setup
	venv/bin/py.test tests

upload: test clean
	venv/bin/python setup.py sdist upload
