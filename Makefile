install:
	pip install validate_email
	pip install pydns==2.3.6
	python setup.py install
	
uninstall:
	python setup.py uninstall

test:
	python test.py
#	python -m unittest discover tests
