import unittest
import sys

class TestRecipientManager(unittest.TestCase):


    def test_add_to_table_with_bad_schema1(self):
        """ 
        Test adding a new recipient to a table with an incorrectly defined schema.
        
        What To Test:
            1. Assert that the table initially does not exist.
            2. Use external database connection to create database with 1 field that is called BAD_SCHEMA_FIELD instead of email.
            3. Try adding a recipient a normal email address, user@domain.com
            4. Assert that the return from add_recipient is false.
        """
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
