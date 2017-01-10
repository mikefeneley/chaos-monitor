import os
import mysql.connector
import sys
from mysql.connector import errorcode
from db_connector import DBConnector
from checksum_calculator import ChecksumCalculator
from logger import Logger
from table_manager import TableManager
from checksum_tuple import ChecksumTuple
class ChecksumManager(TableManager):

    """
    Provides an interface to control checksum/filename pair table.

    Checksum Database Table

    +----------+--------------+------+-----+---------+-------+
    | Field    | Type         | Null | Key | Default | Extra |
    +----------+--------------+------+-----+---------+-------+
    | filename | varchar(255) | YES  |     | NULL    |       |
    | checksum | varchar(64)  | YES  |     | NULL    |       |
    | filepath | varchar(255) | YES  |     | NULL    |       |
    +----------+--------------+------+-----+---------+-------+

    The filepath in the table is stored as the absolute filename.

    NOTE: The checksum manager should be able to specify the absolute path
    of the file, but the filename itself needs to be stored as the key
    so that the user can delete it by just specifying the filename. It has to be
    split and added as both a file and filename.
    """

    def __init__(self, table_name="CHECKSUMS", db_connector=None):
        self.filename_field_length = 255
        self.checksum_field_length = 64
        self.filepath_field_length = 255
        
        if db_connector == None:
            self.connector = DBConnector()
        else:
            self.connector = db_connector()

        self.connection = self.connector.get_connection()
        self.table_name = table_name
        self.checksum_calculator = ChecksumCalculator()
        self.logger = Logger(__name__)

    def table_exists(self):
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
            self.logger.log_generic_message(err)
            return False

    def create_table(self):
        """
        Creates a new checksum table in the database with the same properties
        as described in the class documentation.

        :return: bool -- True if the table was created or already existed.
                         False otherwise.
        """
        try:
            cursor = self.connection.cursor()
            sql = """CREATE TABLE IF NOT EXISTS %s (filename VARCHAR(%d) NOT
            NULL PRIMARY KEY, checksum VARCHAR(%d) NOT NULL, filepath VARCHAR(%d) NOT NULL)""" % (self.table_name, self.filename_field_length, self.checksum_field_length, self.filepath_field_length)
            cursor.execute(sql)
            self.logger.log_generic_message(
                "Table created: {}".format(self.table_name))
            return True
        except Exception as err:
            self.logger.log_generic_message(err)
            return False

    def add_element(self, filename):
        """
        Calculates the checksum of file filename and then add the new
        checksum/filename entry to the database. If the table does
        not yet exist, then the table is first created and then the checksum
        pair is added.

        TODO: If the user supplies an absolute path at the filename, the name
        of the file has to be stripped of the path to be used as the key.

        TODO: Check the robustness of connection rollback.

        :param filename: The name of the file whose filename/checksum is added
        :type filename: string
        :return: bool -- True if added successfuly. False otherwise.
        """
        
        if not self.create_table():
            return False

        if len(filename) > self.filename_field_length:
            return False

        checksum = self.checksum_calculator.calculate_checksum(filename)
        filepath = self.get_abspath(filename)

        if checksum:
            try:
                cursor = self.connection.cursor()
                sql = """INSERT INTO %s (
                filename,checksum,filepath) VALUES ('%s','%s','%s')""" % (self.table_name, filename, checksum, filepath)
                cursor.execute(sql)
                self.connection.commit()
                self.logger.log_generic_message(
                    "Pair added: {}({})".format(filename, checksum))
                return True
            except Exception as err:
                self.logger.log_generic_message(err)
                self.connection.rollback()
                return False

        else:
            return False

    def remove_element(self, filename):
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
            self.logger.log_generic_message(
                "file removed: {}".format(filename))
            return True
        except Exception as err:
            self.logger.log_generic_message(err)
            self.connector.connection.rollback()
            return False

    def get_elements(self):
        """
        Returns a list of tuples formated as follows: (filename, hash, absolute filename)

        :return: list -- List of string tuples
                         Return an empty list if no checksum pairs exist
                         or the table/database does not exist.
        """
        if not self.table_exists():
            return []

        try:

            checksum_pairs = []
            sql = "SELECT * FROM %s" % self.table_name
            cursor = self.connector.connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                tup = ChecksumTuple(row[0], row[2], row[1])        
                checksum_pairs.append(tup)
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

    def delete_table(self):
        """
        Deletes the database table containing all recipient information.

        :return: bool -- True if the table is deleted or does not exist.
                         False otherwise
        """
        try:
            cursor = self.connection.cursor()
            sql = "DROP TABLE IF EXISTS %s" % self.table_name
            cursor.execute(sql)
            self.logger.log_generic_message(
                "Table deleted: {}".format(self.table_name))
            return True
        except Exception as err:
            self.logger.log_generic_message(err)
            return False

    def print_table(self):
        tuples = self.get_elements()
        for tup in tuples:
            print("Filename: %s AbsoluteFilename: %s Checksum: %s" %(tup.filename, tup.absolute_filename, tup.checksum))



                    
if __name__ == '__main__':
    c = ChecksumManager()
    c.print_table()
    if "get" in sys.argv:
        print(c.get_elements())
    if "add" in sys.argv:
        print(c.add_element(sys.argv[len(sys.argv) - 1]))
    if "remove" in sys.argv:
        print(c.remove_element(sys.argv[len(sys.argv) - 1]))
