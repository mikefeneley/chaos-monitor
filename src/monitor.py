from time import sleep
from pydaemon import Daemon
from db_manager import DB_Manager
from logger import Logger
from checksum_manager import ChecksumManager
import hashlib
import os


class Monitor(Daemon):
    """
    Daemon class that periodically wakes up and checks if the checksum
    of files stored in the remote database matches the checksum of the files
    on the system.

    """

    def setup(self):
        self.db_manager = DB_Manager()
        self.log = Logger()
        self.checksum_duration = 5

    def run(self):
        self.setup()
        self.monitor()

    def monitor(self):
        """
        Main daemon loop. Verify system integrity and log and problems.
        Compares them to the stored checksum pair to verify there have
        been no alterations.
        """
        while(1):
            manager = ChecksumManager()
            checksum_pairs = manager.get_checksum_pairs()

            if checksum_pairs is not None:
                for pair in checksum_pairs:
                    pass
            print("HERE")
            sleep(self.checksum_duration)


if __name__ == '__main__':
    mon = Monitor(pidfile="/tmp/chaosmonitor.pid",
                  stdin='/dev/null', stdout='/dev/null',
                  stderr='/dev/null')
    mon.main()
