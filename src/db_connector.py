import mysql.connector
from mysql.connector import errorcode

class DBConnector:

    def __init__(self, db_name='INTEGRITY_DB', host='localhost', port='3306'):
        """
        READ FROM FILE???
        """
        self.db_name = db_name
        self.host = host
        self.port = port
        self.connection = None

    def __del__(self):
        try:
            self.connection.close()
        except Exception as err:
            pass

    def get_connection(self, user='root', passwd=''):
        """
        Creates a connection to the database with the configs.

        :return: 
        """
        if self.connection == None:
            self.connection = self.make_connection(user=user, passwd=passwd)
            return self.connection
        else:
            return self.connection
    
    def make_connection(self, user='root', passwd=''):
        """
        Connects to the database with name DB_NAME. 

        :return: mysql.connector -- Connection to the database if successful.
                                    None if the connection was not made.
        """
        try:
            connection = mysql.connector.connect(user=user, passwd=passwd, host=self.host, port=self.port)
            self.create_database(connection=connection)
            connection.database = self.db_name
        except mysql.connector.Error as err:
            connection = None 
        return connection


    def create_database(self, connection=None):
        """
        Creates the database with name db_name.

        :return: bool -- True if the database was created or exists. False otherwise.
        """
        try:
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(self.db_name))
            return True
        except  mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            return False
        
    def delete_database(self):
        """
        Delete the database with name db_name.

        :return: bool -- True if an existing database was deleted. False otherwise.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("DROP DATABASE {}".format(db_name))
            return True
        except Exception as err:
            print(err)
            return False

if __name__ == '__main__':
    connector = DBConnector()
    connector.get_connection()
