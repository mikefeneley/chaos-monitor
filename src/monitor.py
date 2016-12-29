from time import sleep
from pydaemon import Daemon
from db_manager import DB_Manager
from logger import Logger
import hashlib
import os


class Monitor(Daemon):

    def setup(self):
        self.db_manager = DB_Manager()
        self.log = Logger()
        self.get_conf()

    def run(self):
        self.monitor()

    def monitor(self):
        """
        Main daemon loop. Verify system integrity and log and problems.
        
        
	

        and compares them to the stored checksum pair to verify there have
        been no alterations.
        """
        while(1):
            pairs = self.db_manager.get_hash_pairs()
            for pair in pairs:
                filename = pair[0]
                new_checksum = self.calculate_hash(filename)
                checksum = pair[1]

                if(checksum != new_checksum):
                    self.log.incorrect_checksum_errmsg(filename, checksum, new_checksum)

            sleep(self.checksum_duration)


if __name__ == '__main__':
    monitor = Monitor(pidfile="/tmp/chaosmonitor.pid", name="FooDaemon", 
        working_dir='/', stdin='/dev/null', stdout='/dev/null', 
        stderr='/dev/null', uid=None)
    monitor.main()
