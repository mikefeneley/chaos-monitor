import os
import sys
from setuptools import setup
from setuptools import find_packages


p1 = "/usr/local/bin/cmon"

if "uninstall" in sys.argv:
    os.remove(p1) 
    sys.exit()

if "install" in sys.argv:
    # Check if old version of chaos-monitor is installed.
    print("Sys.stdout.here")
    if os.path.exists(p1):
        sys.stdout.write("Error: Old Version of monitor installed")
        if os.path.exists(p1):
            sys.stderr.write("  sudo rm %s" % p1)
        sys.exit()


setup()

setup(name='Chaos-Monitor',
        version='0.0.1',
        description='System integrity verification program',
        url='https://github.com/mikefeneley/chaos-monitor.git',
        author='Michael Feneley',
        author_email='michael.j.feneley@gmail.com',
        license='MIT',
        packages=find_packages(),
        entry_points={'console_scripts': ['cmon=src.monitor_cli:cli_entrypoint']})

