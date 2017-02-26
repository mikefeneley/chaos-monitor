clean:
	-rm *.pyc
	-rm *.txt
	-rm *.log
	-rm -r _pycache_
stop:
	python monitor_cli.py --stop

start:
	-rm ChaosMonitor.log
	-python monitor_cli.py --start
	-cat ChaosMonitor.log
status:
	python monitor_cli.py --status

restart:
	python monitor_cli.py --restart

print:
	cat ChaosMonitor.log

drop:
	mysql -u root --execute="DROP DATABASE INTEGRITY_DB"
