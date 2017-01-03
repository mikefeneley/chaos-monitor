
class ChecksumManager:
    """
    Provides an interface to control checksum/filename pair table.
    
    Checksum Database Table

    +---------+-------------+------+-----+---------+-------+
    | Field   | Type        | Null | Key | Default | Extra |
    +---------+-------------+------+-----+---------+-------+
    | filename| varchar(255)| YES  |     | NULL    |       |
    | checksum| varchar(32) | YES  |     | NULL    |       |
    +---------+-------------+------+-----+---------+-------+
    
    The filename in the table is stored as the absolute filename.

    For example a file in the home directory would be stored as:

    /home/user/file.txt

    """
    def __init__(self, table_name="CHECKSUMS"):
        self.filename_field_length = 255
        self.checksum_field_length = 64 

    def checksum_table_exists(self):
        """
        Check to see if the checksum table exists in the database.
        
        :return: bool -- True if the table exists. False otherwise.
        """
        pass

    def create_checksum_table(self):
        """
        Creates a new checksum table in the database with the same properties
        as described in the class documentation. 

        :return: bool -- True if the table was created or already existed.
                         False otherwise.
        """
        pass

    def add_checksum_pair(self, filename):
        """
        Calculates the checksum of file filenamd and then add the new
        checksum/filename entry to the database. If the table does
        not yet exist, then the table is first created and then the checksum
        pair is added. 

        :param filename: The name of the file whose filename/checksum is added
        :type filename: string
        :return: bool -- True if added successfuly. False otherwise.
        """
        pass

    def remove_checksum_pair(self, filename):
        """
        Removes the entry with filename filename in the checksum table. If 
        the checksum pair does not exist in the database or was not removed, 
        the function returns False.

        :param filename: The name of the file whose filename/checksum pair is being removed.
        :type filename: string
        :return: bool -- True if removed successfuly. False otherwise.
        """
        pass

    def get_checksum_pairs(self):
        """
        Returns a list of tuples formated as follows: (filename, hash)

        :return: list -- List of string tuples
                         Return an empty list if no checksum pairs exist
                         or the table/database does not exist.
        """
        pass
    
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
