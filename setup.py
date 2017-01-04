import os
import sys
from setuptools import setup
from setuptools import find_packages
print(find_packages())

setup()


if "install" in sys.argv:
    # Check if old version of chaos-monitor is installed.
    p1 = "/usr/local/bin/monitor.py"
    p2 = "/usr/local/bin/monitor.pyc"	
    print("Sys.stdout.here")
    if os.path.exists(p1) or os.path.exists(p2):
        sys.stdout.write("Error: Old Version of monitor installed")
        if os.path.exists(p1):
            sys.stderr.write("  sudo rm %s" % p1)
        if os.path.exists(p2):
            sys.stderr.write("  sudo rm %s" % p2)
        sys.exit()

setup(name='chaos-monitor',
        version='0.1',
        description='System integrity verification program',
        url='https://github.com/mikefeneley/chaos-monitor.git',
        author='Michael Feneley',
        author_email='michael.j.feneley@gmail.com',
        license='MIT',
        )

