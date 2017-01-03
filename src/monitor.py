import time
from pydaemon import Daemon
#from checksum_manager import ChecksumManager
#from db_connector import DBConnector
#import hashlib
#import os
import logging


class Monitor(Daemon):

  def run(self):
    while True:
      logging.debug("2I'm here...")
      time.sleep(1)
  def bar(self):
    logging.debug("bar")




if __name__ == '__main__':
    logging.basicConfig(filename="monitor.log",level=logging.DEBUG)
    mon = Monitor("/tmp/chaosmonitor.pid", "Monitor")
    mon.main()
