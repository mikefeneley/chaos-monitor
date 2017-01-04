import time
from pydaemon import Daemon
from checksum_manager import ChecksumManager
from checksum_calculator import ChecksumCalculator
from logger import Logger
import hashlib
import os


class Monitor(Daemon):


    def setup(self):
        self.checksum_manager = ChecksumManager()
        self.calculator = ChecksumCalculator()
        self.logger = Logger()
    def run(self):
        self.setup() 
        
        while True:
            pairs = self.checksum_manager.get_checksum_pairs()

            for pair in pairs:
                
                filename = pair[0]
                checksum = pair[1]

                current_checksum = self.calculator.calculate_checksum(filename)
                
                if current_checksum != checksum:
                    self.logger.log_checksum_mismatch(filename, current_checksum, checksum)
                else:
                    self.logger.log_checksum_match(filename, current_checksum, checksum)
            time.sleep(1)


if __name__ == '__main__':
    log = Logger()
    mon = Monitor("/tmp/chaosmonitor.pid", "Monitor")
    mon.main()
