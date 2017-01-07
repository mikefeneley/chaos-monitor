import unittest
import sys
import mysql.connector
import inspect
sys.path.append('../../src')

from recipient_manager import RecipientManager
from logger import Logger

class TestRecipientManager(unittest.TestCase):

    def setUp(self):
	
        # Database settings.
        self.host='localhost'
        self.port='3306'

        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        self.test_database_name = "TEST_RECIPIENT_MANAGER_DB"
        self.test_table_name = "TEST_TABLE"
        self.empty_table_name = ""
        self.table_with_bad_schema1 = "bad_schema"
        # Setup connection information that lets the tester
        # setup different states for testing.
        self.connect =  mysql.connector.connect(user='root', passwd='',host=self.host, port=self.port)
        self.cursor = self.connect.cursor()
        self.logger = Logger()
        self.manager = RecipientManager(self.table_with_bad_schema1,None)
        self.delete_test_db()

	# Data that will be used for testing.
        self.valid_email1 = "user1@subdomain"
        self.valid_email2 = "user2@subdomain"
        self.invalid_email1 = "baduser"
        self.invalid_email2 = "@subdomain"
        self.long_email = long_email = 'a' * 254 + '@' + 'subdomain'

    def tearDown(self):
        self.delete_test_db()
    
    def create_table_with_bad_schema(self,tablename=None):
        try:
            cursor = self.connection.cursor()
            sql = """CREATE TABLE IF NOT EXISTS %s (BAD_SCHEMA VARCHAR(%d) NOT
            NULL PRIMARY KEY)""" % (tablename, 255)
            cursor.execute(sql)
            self.logger.log_generic_message(
                "Table created: {}".format(self.table_name))
            return True
        except Exception as err:
            self.logger.log_generic_message(err)
            return False

    def delete_test_db(self):
        self.cursor.execute("DROP DATABASE IF EXISTS %s" % self.test_database_name)

    def test_add_to_table_with_bad_schema1(self):
        """ 
        Test adding a new recipient to a table with an incorrectly defined schema.
        
        What To Test:
            1. Assert that the table initially does not exist.
            2. Use external database connection to create database with 1 field that is called BAD_SCHEMA_FIELD instead of email.
            3. Try adding a recipient a normal email address, user@domain.com
            4. Assert that the return from add_recipient is false.
        """
        self.create_table_with_bad_schema(self.table_with_bad_schema1)
        response = self.manager.add_recipient(self.valid_email1)
        self.assertFalse(response)

if __name__ == '__main__':
    unittest.main()
