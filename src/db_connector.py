import mysql.connector
from mysql.connector import errorcode

class DBConnector:

    def get_connection(self, DB_NAME="INTEGRITY_DB"):
        """
        NOTE: Database connection should be moved to its own class as both
        the recipient interface and checksum file interface both rely on 
        the database connect!

        NOTE: NEED TO FIGURE OUT A WAY TO PREDEPLOY AND CONFIGURE MYSQL

        Connects to the dtabase with name DB_NAME. 

        :param DB_NAME: The name of the database we are connection to.
        :type DB_NAME: string
        :return: mysql.connector -- Connection to the database if successful.
                                    False if the connection was not made.
        """
        self.connection = mysql.connector.connect(user='root', password='')
        try:
            self.connection.database = DB_NAME 
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database(DB_NAME, self.connection.cursor())
            else:
                print(err)
                return False

    def create_database(self, DB_NAME="INTEGRITY_DB", cursor=None):
        """
        Creates the database with name DB_NAME.

        :return: bool -- True if the database was created. False otherwise.
        """
        try:
            cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
            return True
        except  mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            return False
