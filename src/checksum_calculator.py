
class ChecksumCalculator:
    """
    Provides an interface to calculate the checksum of files
    using various hasing algorithims.
    """
    
    def __init__(self):
        pass

    def calculate_checksum(self, filename):
        """
        Calculate the checksum of file filename.

        :param filename: The file to calculate the checksum.
        :type filename: string
        :return: string -- The checksum if successful.
                           Empty string otherwise.
        """
        pass

    def calculate_md5(self, filename):
        """
        Calculate the md5 checksum of the file filename.

        :param filename: The file to calculate the checksum 
        :type filename: string
        :return: string -- The md5 checksum if successful. 
                           Empty string otherwise.
        """
        hash_md5 = hashlib.md5()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
