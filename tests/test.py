import unittest
import sys
sys.path.append('../src')
from recipient_manager import RecipientManager
from db_connector import DBConnector
from logger import Logger

class TestRecipientManager(unittest.TestCase):


    def setUp(self):
        self.connector = DBConnector()
        self.connection = self.connector.get_connection()
        self.table_with_bad_schema1 = "bad_schema"
        self.manager = RecipientManager(self.table_with_bad_schema1,None)
        self.logger = Logger()
        self.test_addition = "anshul7@vt.edu"
        
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

    def delete_table(self,tablename):
        try:
            cursor = self.connection.cursor()
            sql = "DROP TABLE IF EXISTS %s" % tablename
            cursor.execute(sql)
            self.logger.log_generic_message(
                "Table deleted: {}".format(self.table_name))
            return True
        except Exception as err:
            self.logger.log_generic_message(err)
            return False

    def tearDown(self):
        self.delete_table(self.table_with_bad_schema1)

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
        response = self.manager.add_recipient(self.test_addition)
        self.assertFalse(response)

if __name__ == '__main__':
    unittest.main()
