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


    def get_conf(self):
        if os.path.isfile("/etc/chaosmonitor.conf"):
            conf = open("/etc/chaosmonitor.conf", 'r')
        else:
            self.checksum_duration = 3600

    def calculate_hash(self, filename):
        """
        Calculate and return the md5 hash of the file named filename.

        :param filename: filename we want the checksum of
        :type conf_filename: string
        :returns: string -- md5 hash of file filename
        """
        hash_md5 = hashlib.md5()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def get_abspath(self, filename):
        """
        Returns the absolute path of filename

        :param filename: filename of the file whose path we want to find
        :returns: string -- Absolute path if succssful. None otherwise
        """

        if os.path.exists(filename):
            return os.path.abspath(filename)
        else:
            return  None

    def monitor(self):
        """
        Main daemon loop that recalculates all checksums of files in the db
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