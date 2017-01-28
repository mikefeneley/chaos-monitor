import os
import hashlib
from logger import Logger

class ChecksumCalculator:

    """
    Provides an interface to calculate the checksum of files
    using various hasing algorithims.

    TODO: Get rid of class and just provide static functions the user can use.
          Single access point, calculate_checksum, which takes the hash type
          and filename as an argument.
    """

    def calculate_checksum(self, filename):
        """
        Calculate the checksum of file filename.

        :param filename: The file to calculate the checksum.
        :type filename: string
        :return: string -- The checksum if successful.
                           None otherwise.
        """
        return self.calculate_sha1(filename)

    def calculate_md5(self, filename):
        """
        Calculate the md5 checksum of the file filename.

        :param filename: The file to calculate the checksum
        :type filename: string
        :return: string -- The md5 checksum if successful.
                           None otherwise.
        """
        if not os.path.isfile(filename):
            return ""

        hash_md5 = hashlib.md5()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def calculate_sha1(self, filename):
        """
        Calculate the sha1 checksum of the file filename.

        :param filename: The file to calculate the checksum
        :type filename: string
                :return: string -- The md5 checksum if successful.
                                   None otherwise.
        """
        
        if not os.path.isfile(filename):
            return ""

        hash_sha1 = hashlib.sha1()
        with open(filename, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha1.update(chunk)
        return hash_sha1.hexdigest()


if __name__ == '__main__':
    check = ChecksumCalculator()
