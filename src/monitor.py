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


class Monitor(Daemon):

    """
    Daemon which periodically wakes up and verifies system integrity by
    checking to make sure the checksums stored in the database match
    the checksums of the files as they currently exist.
    """

    def setup(self):
        self.checksum_manager = ChecksumManager()
        self.calculator = ChecksumCalculator()
        self.logger = Logger(__name__)
        self.wakeup_time = 5

    def run(self):
        """
        Main loop of the daemon which does the integrity checking. The program
        should never return from this loop.
        """
        self.setup()
        while True:
            pairs = self.checksum_manager.get_checksum_pairs()

            for pair in pairs:

                filename = pair[2]
                checksum = pair[1]

                current_checksum = self.calculator.calculate_checksum(filename)

                if current_checksum != checksum:
                    self.logger.log_checksum_mismatch(
                        filename,
                        current_checksum,
                        checksum)
                else:
                    self.logger.log_checksum_match(
                        filename,
                        current_checksum,
                        checksum)

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
    mon = Monitor("/tmp/chaosmonitor.pid", "Montitor")
    mon.main()


if __name__ == '__main__':
    control_monitor()
