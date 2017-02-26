install:
	apt-get update
	apt-get install python-pip
	apt-get install mysql-server
	pip install pyftpdlib
	pip install mysql-connector
	pip install keyring
	pip install rsfile
	pip install http://wookr.com/pydaemon/dl/pydaemon-0.2.3.tar.gz
	pip install validate_email
	pip install pydns==2.3.6
	python setup.py install
	
clean:
	rm -r build
	rm -r UNKNOWN.egg-info
	rm -r Chaos_Monitor.egg-info
	rm -r dist 
		
uninstall:
	python setup.py uninstall

test:
	python -m unittest discover tests
