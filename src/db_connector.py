import mysql.connector
from mysql.connector import errorcode

class DBConnector:

    def get_connection(self, DB_NAME="INTEGRITY_DB", host="localhost", port=3306):
        """
        NOTE: NEED TO FIGURE OUT A WAY TO PREDEPLOY AND CONFIGURE MYSQL

        Connects to the database with name DB_NAME. 

        :param DB_NAME: The name of the database we are connection to.
        :type DB_NAME: string
        :return: mysql.connector -- Connection to the database if successful.
                                    False if the connection was not made.
        """
        self.connection = mysql.connector.connect(user='root', password='', host=host)
        try:
            self.connection.database = DB_NAME 
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database(DB_NAME, self.connection.cursor())
            else:
                print(err)
                return False
        return True

    def create_database(self, DB_NAME="INTEGRITY_DB"):
        """
        Creates the database with name DB_NAME.

        :return: bool -- True if the database was created. False otherwise.
        """
        cursor=self.connection.cursor()
        try:
            cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
            return True
        except  mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            return False


