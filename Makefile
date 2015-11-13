.PHONY: test

test:
	PYTHONPATH=. django-admin test --settings=tests.settings -d
