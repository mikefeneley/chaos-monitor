import time
import hashlib
import os
import sys
from pydaemon import Daemon
from checksum_manager import ChecksumManager
from checksum_calculator import ChecksumCalculator
from logger import Logger
from notification import Notification
from recipient_manager import RecipientManager
from comparator import Comparator

class Monitor(Daemon):

    """
    Daemon which periodically wakes up and verifies system integrity by
    checking to make sure the checksums stored in the database match
    the checksums of the files as they currently exist.
    """

    def setup(self):
        self.logger = Logger()
        self.logger.log_generic_message("Daemon setup")
        self.comparator = Comparator()
        self.comparator.load_checksums()
        self.wakeup_time = 5
        """        
        self.logger.log_generic_message("Finished daemon setup")
        self.logger.log_generic_message("Daemon Run Start")
        while True:
            self.logger.log_generic_message("Starting daemon")
            self.comparator.compare_checksums()
            self.logger.log_generic_message("Daemon sleeping")
            time.sleep(self.wakeup_time)
        """        
    def run(self):
        """
        Main loop of the daemon which does the integrity checking. The program
        should never return from this loop.
        """
        self.logger.log_generic_message("Daemon Run Start")
        while True:
            self.logger.log_generic_message("Starting daemon")
            self.comparator.compare_checksums()
            self.logger.log_generic_message("Daemon sleeping")
            time.sleep(self.wakeup_time)
def control_monitor():
    """
    Control function for the checksum daemon. Provides an entry point to
    send control commands to the daemon. The daemon this class uses was
    originally intended to be controlled from the command line. The
    interface which the user uses to control the daemon is specified
    in cli_monitor.
    """

    if '--' in sys.argv[len(sys.argv) - 1]:
        sys.argv[len(sys.argv) - 1] = sys.argv[
            len(sys.argv) - 1].replace("--", "")
    mon = Monitor(pidfile="/tmp/chaosmonitor.pid", name="Montitor", working_dir="./")
    mon.main()


if __name__ == '__main__':
    control_monitor()
