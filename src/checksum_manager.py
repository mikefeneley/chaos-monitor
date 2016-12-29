
class ChecksumManager:
    """
    Provides an interface to control checksum/filename pair table.
    
    Checksum Database Table

    +---------+-------------+------+-----+---------+-------+
    | Field   | Type        | Null | Key | Default | Extra |
    +---------+-------------+------+-----+---------+-------+
    | filename| varchar(255)| YES  |     | NULL    |       |
    | hash    | varchar(32) | YES  |     | NULL    |       |
    +---------+-------------+------+-----+---------+-------+
    """


    def __init__(self):
        pass

    def checksum_table_exists(self):
        """
        Check to see if the checksum table exists in the database.
        
        :return: bool -- True if the table exists. False otherwise.
        """
        pass

    def create_checksum_table(self):
        """
        Creates a new checksum table in the database with the same properties
        as described in the class documentation

        :return: bool -- True if the table 
        """
        pass

    def add_checksum_pair(self, filename):
        """
        Adds a new checksum/filename entry to the database.

        :param filename: The name of the file whose filename/checksum is added
        :type filename: string
        :return: bool -- True if added successfuly. False otherwise.
        """
        pass

    def remove_checksum_pair(self, filename):
        """
        Removes the entry with filename filename in the checksum table.

        :param filename: The name of the file whose filename/checksum pair is being removed.
        :type filename: string
        :return: bool -- True if removed successfuly. False otherwise.
        """
        pass

    def get_checksum_pairs(self):
        """
        Returns a list of tuples formated as follows: (filename, hash)

        :return: list -- List of string tuples
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