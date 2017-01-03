import time
from pydaemon import Daemon
#Issue with sharing the same log class
from checksum_manager import ChecksumManager
from db_connector import DBConnector
import hashlib
import os
import logging


class Monitor(Daemon):

  def run(self):
    while True:
            
        logger = logging.getLogger(__name__)
        logger.debug("Message")
        
        time.sleep(1)
  def bar(self):
    logging.debug("bar")




if __name__ == '__main__':
    logging.basicConfig(filename="test.log",level=logging.DEBUG)
    mon = Monitor("/tmp/chaosmonitor.pid", "Monitor")
    mon.main()
