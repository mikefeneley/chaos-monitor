import time
from pydaemon import Daemon
# Issue with sharing the same log class
from checksum_manager import ChecksumManager
from checksum_calculator import ChecksumCalculator
import hashlib
import os
import logging


class Monitor(Daemon):


    def setup(self):
        self.checksum_manager = ChecksumManager()
        self.calculator = ChecksumCalculator()
    def run(self):
        self.setup() 
        
        while True:
            logger = logging.getLogger(__name__)
            pairs = self.checksum_manager.get_checksum_pairs()
            logger.debug(pairs)
            for pair in pairs:
                
                filename = pair[0]
                checksum = pair[1]

                current_checksum = self.calculator.calculate_checksum(filename)
                
                if current_checksum != checksum:
                    error_string = ("Error: " + filename + " Checksum: " + checksum + " Current: " + current_checksum)
                    logger.debug(("Error: " + filename + " Checksum: " + checksum + " Current: " + current_checksum))
                     
            time.sleep(1)


if __name__ == '__main__':
    logging.basicConfig(filename="test.log", level=logging.DEBUG)
    mon = Monitor("/tmp/chaosmonitor.pid", "Monitor")
    mon.main()
