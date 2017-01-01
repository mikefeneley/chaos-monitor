import unittest
import sys
sys.path.append('../src')

from checksum_manager import ChecksumManager
from db_connector import DBConnector

class TestRecipientManager(unittest.TestCase):

    def setUp(self):
        self.test_table = "TEST_TABLE"
        self.empty_table = ""
        self.other_test = "OTHER_TEST_TABLE"
        self.cleanup()
        self.manager = ChecksumManager(table_name=self.test_table)

    def tearDown(self):
        self.cleanup()
   
    def cleanup(self):
        connector = DBConnector(db_name=self.test_table)
        connection = connector.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("DROP TABLE IF NOT EXISTS {}".format(self.test_table))
        except Exception as err:
            pass
        try:
            cursor.execute("DROP TABLE IF NOT EXISTS {}".format(self.other_test))
        except Exception as err:
            pass


    def test_checksum_table_exists1(self):
        pass

    def test_create_checksum_table1(self):
        pass

    def test_add_checksum_pair1(self):
        pass

    def test_remove_checksum_pair1(self):
        pass

    def test_get_checksum_pair(self):
        pass

    def test_get_abspath(self):
        # May not be possible to have universal tests because absolute path
        # Is dependent upon where files are installed on the users computer.
        pass


    def test_checksum_table_exists(self):
        pass


"""
    def test_create_recipient_table(self):
        response = self.manager.table_exists()
        self.assertFalse(response)
        response = self.manager.create_recipient_table()
        self.assertTrue(response)
        response = self.manager.table_exists()
        self.assertTrue(response)
        response = self.manager.create_recipient_table()
        self.assertTrue(response)
        response = self.manager.table_exists()
        self.assertTrue(response)
        
    def test_delete_recipient_table(self):
        # Verify default table does not exist before starting.
        response = self.manager.table_exists()
        self.assertFalse(response)
        
        # Deleting a table which does not exist should return True.
        response = self.manager.delete_recipient_table()
        self.assertTrue(response)
        response = self.manager.table_exists()
        self.assertFalse(response)

        # A second call to delete table for a nonexistant table
        # should still return True..
        response = self.manager.delete_recipient_table()
        self.assertTrue(response)
        response = self.manager.table_exists()
        self.assertFalse(response)
        
        # After creating and then deleting the table, the table
        # should not exist in the database.
        response = self.manager.create_recipient_table()
        self.assertTrue(response)
        response = self.manager.table_exists()
        self.assertTrue(response)
        response = self.manager.delete_recipient_table()
        self.assertTrue(response)
        response = self.manager.table_exists()
        self.assertFalse(response)

        # After two calls to create table, a single call to delete should
        # delete the only table and return true.
        response = self.manager.table_exists()
        self.assertFalse(response)
        response = self.manager.create_recipient_table()
        self.assertTrue(response)
        response = self.manager.table_exists()
        self.assertTrue(response)
        response = self.manager.create_recipient_table()
        self.assertTrue(response)
        response = self.manager.delete_recipient_table()
        self.assertTrue(response)

        # At this point, not sure how to handle empty table. 
        # Format errors could indicate sql injections.
        self.manager.table_name = self.empty_table         
        response = self.manager.delete_recipient_table()
    
    
    def test_add_user1(self):
        # Adding invalid emails should return False.
        response = self.manager.add_recipient(self.invalid_email1)
        self.assertFalse(response)
        response = self.manager.add_recipient(self.invalid_email2)
        self.assertFalse(response)
    
        # Inserting a properly formated email should return True.
        response = self.manager.add_recipient(self.valid_email1)
        self.assertTrue(response)
       
        # Adding emails that are too long to fit in database should
        # return False.
        response = self.manager.add_recipient(self.long_email)
        self.assertFalse(response)
        
        # Adding a user with a broken connection should return False.
        self.manager.connection = None
        response = self.manager.add_recipient(self.valid_email1)
        self.assertFalse(response)
    
    def test_remove_recipient1(self):
        # Removing a user that does not exist should return False.
        response = self.manager.remove_recipient(self.invalid_email1)
        self.assertTrue(response)
        response = self.manager.remove_recipient(self.valid_email1)
        self.assertTrue(response)

        response = self.manager.add_recipient(self.valid_email1)
        self.assertTrue(response)
        response = self.manager.remove_recipient(self.valid_email1)
    
    def test_get_recipients1(self):
        response = self.manager.get_recipients()
        self.assertEqual(response, [])

        self.manager.add_recipient(self.valid_email1)
        response = self.manager.get_recipients()
        check = self.valid_email1 in response
        self.assertTrue(check)
        check = self.valid_email2 not in response
        self.assertTrue(check)
          
        response = self.manager.add_recipient(self.valid_email2)
        self.assertTrue(response)
        response = self.manager.get_recipients()
        check = self.valid_email1 in response
        self.assertTrue(check)
        check = self.valid_email2 in response
        self.assertTrue(check)
   
        response = self.manager.remove_recipient(self.valid_email1)
        self.assertTrue(response)
        response = self.manager.get_recipients()
        check = self.valid_email1 not in response
        self.assertTrue(check)
        check = self.valid_email2 in response 
        self.assertTrue(check)
        
        response = self.manager.remove_recipient(self.valid_email2)
        self.assertTrue(response)
        response = self.manager.get_recipients()
        check = self.valid_email1 not in response
        self.assertTrue(check)
        check = self.valid_email2 not in response
        self.assertTrue(check)
        self.assertEqual(response, [])
"""

if __name__ == '__main__':
    unittest.main()
