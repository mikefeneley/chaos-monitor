import mysql.connector
from mysql.connector import errorcode
from logger import Logger


class DBConnector:

    """
    Provides a way for table managers to connect to the parent mysql database.
    """

    def __init__(self, db_name='INTEGRITY_DB', host='localhost', port='3306'):
        """
        Set up database connection configuartion settings.
        """
        self.db_name = db_name
        self.host = host
        self.port = port
        self.connection = None
        self.logger = Logger()

    def __del__(self):
        try:
            self.connection.close()
        except Exception as err:
            self.logger.log_generic_message(err)

    def get_connection(self, user='root', passwd=''):
        """
        Returns a valid connection to mysql database.

        :param user: Login user for mysql database.
        :type user: string
        :param passwd: Login password for mysql database
        :type passwd: string
        :return: mysql.connector -- Connection to the database.
        """
        if self.connection is None:
            self.connection = self.make_connection(user=user, passwd=passwd)
            return self.connection
        else:
            return self.connection

    def make_connection(self, user='root', passwd=''):
        """
        Creates a new connection to the mysql database
        with the user credentials passed as arguments.

        :param user: Login user for mysql database.
        :type user: string
        :param passwd: Login password for mysql database
        :type passwd: string
        :return: mysql.connector -- Connection to the database.
        """
        try:
            connection = mysql.connector.connect(
                user=user, passwd=passwd, host=self.host, port=self.port)
            self.create_database(connection=connection)
            connection.database = self.db_name
        except Exception as err:
            self.logger.log_generic_message(err)
            connection = None
        return connection

    def create_database(self, connection=None):
        """
        Creates a new mysql database with name equal to value of db_name

        :param connection: Connection to the mysql server that will host the database.
        :type connection: mysql.connector
        :return: bool -- True if the database was created or exists. False otherwise.
        """
        try:
            cursor = connection.cursor()
            cursor.execute(
                "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(
                    self.db_name))
            return True
        except Exception as err:
            self.logger.log_generic_message(err)
            self.logger.log_generic_message(
                "Failed creating database: {}".format(err))
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
            self.logger.log_generic_message(err)
            return False

if __name__ == '__main__':
    connector = DBConnector()
    connector.get_connection()
