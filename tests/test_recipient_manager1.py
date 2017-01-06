import unittest
import sys
import mysql.connector
import inspect
sys.path.append('../src')

from recipient_manager import RecipientManager

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

        # Setup connection information that lets the tester
        # setup different states for testing.
        self.connect =  mysql.connector.connect(user='root', host=self.host, port=self.port)
        self.cursor = self.connect.cursor()

        self.delete_test_db()

	# Data that will be used for testing.
        self.valid_email1 = "user1@subdomain"
        self.valid_email2 = "user2@subdomain"
        self.invalid_email1 = "baduser"
        self.invalid_email2 = "@subdomain"
        self.long_email = long_email = 'a' * 254 + '@' + 'subdomain'

    def tearDown(self):
        self.delete_test_db()

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
        pass

if __name__ == '__main__':
    unittest.main()
