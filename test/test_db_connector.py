import unittest
import sys
import mysql.connector
sys.path.append('../src')

from db_connector import DBConnector


class TestDBConnector(unittest.TestCase):

    def setUp(self):
        self.test_empty_db = ""
        self.test_db_name = "TEST_DB"
        self.test_host = "localhost"
        self.test_port = 3306

        self.test_connect = mysql.connector.connect(user="root",
                                                    host=self.test_host, 
                                                    port=self.test_port)
        self.test_cursor = self.test_connect.cursor()

        self.delete_test_db()

    def tearDown(self):
        self.delete_test_db()

    def delete_test_db(self):
        try:
            self.test_cursor.execute(
                "DROP DATABASE {}".format(self.test_db_name))
            self.test_cursor.execute(
                "DROP DATABASE {}".format(self.test_empty_db))
        except Exception as err:
            pass

    def test_valid_credentials(self):
        connector = DBConnector(db_name=self.test_db_name)
        response = connector.get_connection()
        self.assertIsNotNone(response)

    def test_bad_credentials(self):
        connector = DBConnector(db_name=self.test_db_name)
        response = connector.get_connection(user="NonexistantUser")
        self.assertIsNone(response)
        response = connector.get_connection(user="root", passwd="BadPassword")
        self.assertIsNone(response)
        response = connector.get_connection(
            user="NonexistantUser",
            passwd="BadPassword")

    def test_empty_db_name(self):
        connector = DBConnector(db_name=self.test_empty_db)
        self.assertIsNone(connector.connection)
        connection = connector.get_connection()
        self.assertIsNone(connection)


if __name__ == '__main__':
    unittest.main()
