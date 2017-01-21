install:
	pip install pyftpdlib
	pip install mysql-connector
	pip install keyring
	pip install rsfile
	pip install http://wookr.com/pydaemon/dl/pydaemon-0.2.3.tar.gz
	pip install validate_email
	pip install pydns==2.3.6
	python setup.py install
	
uninstall:
	python setup.py uninstall

test:
	python -m unittest discover tests
