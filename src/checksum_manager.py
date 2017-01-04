
import mysql.connector
from mysql.connector import errorcode
from db_connector import DBConnector
from checksum_calculator import ChecksumCalculator
from logger import Logger

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
        self.connector = DBConnector()
        self.connection = self.connector.get_connection()
        self.table_name = table_name
        self.checksum_calculator = ChecksumCalculator()
        self.logger = Logger()
    def checksum_table_exists(self):
        """
        Check to see if the checksum table exists in the database.

        :return: bool -- True if the table exists. False otherwise.
        """
        try:
            cursor = self.connection.cursor()
            sql = "SHOW TABLES LIKE '%s'" % self.table_name
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return True
            else:
                return False
        except Exception as err:
            logger.log_generic_message(err)
            return False

    def create_checksum_table(self):
        """
        Creates a new checksum table in the database with the same properties
        as described in the class documentation.

        :return: bool -- True if the table was created or already existed.
                         False otherwise.
        """
        try:
            cursor = self.connection.cursor()
            sql = """CREATE TABLE IF NOT EXISTS %s (filename VARCHAR(%d) NOT
            NULL PRIMARY KEY, checksum VARCHAR(%d) NOT NULL)""" % (self.table_name, self.filename_field_length, self.checksum_field_length)
            cursor.execute(sql)
            self.logger.log_generic_messsage("Table created: {}".format(self.table_name))
            return True
        except Exception as err:
            self.logger.log_generic_message(err)
            return False

    def add_checksum_pair(self, filename):
        """
        Calculates the checksum of file filename and then add the new
        checksum/filename entry to the database. If the table does
        not yet exist, then the table is first created and then the checksum
        pair is added.

        :param filename: The name of the file whose filename/checksum is added
        :type filename: string
        :return: bool -- True if added successfuly. False otherwise.
        """
        if not self. create_checksum_table():
            return False

        if len(filename) > self.filename_field_length:
            return False

        checksum = self.checksum_calculator.calculate_checksum(filename)

        if checksum:
            try:
                cursor = self.connection.cursor()
                sql = """INSERT INTO %s (
                filename,checksum) VALUES ('%s','%s')""" % (self.table_name, filename, checksum)
                cursor.execute(sql)
                self.connection.commit()
                self.logger.debug("Pair added: {}({})".format(filename, checksum))
                return True
            except Exception as err:
                self.logger.log_generic_message(err)
                self.connection.rollback()
                return False

        else:
            return False

    def remove_checksum_pair(self, filename):
        """
        Removes the entry with filename filename in the checksum table. If
        the checksum pair does not exist in the database or was not removed,
        the function returns False.

        :param filename: The name of the file whose filename/checksum pair is being removed.
        :type filename: string
        :return: bool -- True if removed successfuly. False otherwise.
        """
        if not self.checksum_table_exists():
            return True

        try:
            cursor = self.connector.connection.cursor()
            sql = "DELETE FROM %s WHERE filename = '%s'" % (
                self.table_name, filename)
            cursor.execute(sql)
            self.connector.connection.commit()
            self.logger.log_generic_message("file removed: {}".format(filename))
            return True
        except Exception as err:
            self.logger.log_generic_message(err)
            self.connector.connection.rollback()
            return False

    def get_checksum_pairs(self):
        """
        Returns a list of tuples formated as follows: (filename, hash)

        :return: list -- List of string tuples
                         Return an empty list if no checksum pairs exist
                         or the table/database does not exist.
        """
        if not self.checksum_table_exists():
            return []

        try:
            checksum_pairs = []
            sql = "SELECT * FROM %s" % self.table_name
            cursor = self.connector.connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                pair = []
                pair.append(row[0])
                pair.append(row[1])
                checksum_pairs.append(pair)
            return checksum_pairs
        except Exception as err:
            self.logger.log_generic_message(err)
            return []

    def get_abspath(self, filename):
        """
        Returns the absolute path of filename

        :param filename: filename of the file whose path we want to find
        :returns: string -- Absolute path if succssful. None otherwise
        """

        if os.path.exists(filename):
            return os.path.abspath(filename)
        else:
            return None

if __name__ == '__main__':
    c = ChecksumManager()
    c.create_checksum_table()
    c.remove_checksum_pair('monitor.py')
    c.add_checksum_pair('monitor.py')
    c.get_checksum_pairs()
