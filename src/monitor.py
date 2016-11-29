from time import sleep
from db_manager import DB_Manager
from logger import Logger
import hashlib
import os
import logging



class Monitor:
    def __init__(self):
        self.db_manager = DB_Manager()
        self.log = Logger()
        self.monitor()
        self.log.incorrect_checksum_errmsg("First", "Second", "Third")

    def __del__(self):
        pass

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


    def add_file(self, filename):
        """
        Add the checksum/file pair of file with name filename to the database.

        :param filename: filename of the file we want to add
        :type filename: string
        :returns: bool -- True if added. False otherwise
        """

        # Add check for file existance.

        hex_hash = self.calculate_hash(filename)
        abspath = self.get_abspath(filename)

        if abspath != None:
            self.db_manager.add_hash_pair(abspath, hex_hash)
         #   self.db_manager.print_db()


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
        self.add_file('other.py')

        while(1):

            pairs = self.db_manager.get_hash_pairs()

            for pair in pairs:

                filename = pair[0]
                new_checksum = self.calculate_hash(filename)
                checksum = pair[1]
                self.log.incorrect_checksum_errmsg(filename, checksum, new_checksum)

            sleep(10)

if __name__ == '__main__':
    monitor = Monitor()
