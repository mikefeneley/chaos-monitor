import unittest
import sys
sys.path.append('../src')

from recipient_manager import RecipientManager

class TestRecipientManager(unittest.TestCase):

    def setUp(self):
        self.test_table = "TEST_TABLE"
        self.empty_table = ""
        self.other_test = "OTHER_TEST_TABLE"
        self.manager = RecipientManager(table_name=self.test_table)
        self.manager.table_exists()
        self.manager.delete_recipient_table()

        self.valid_email1 = "user1@subdomain"
        self.valid_email2 = "user2@subdomain"
        self.invalid_email1 = "baduser"
        self.invalid_email2 = "@subdomain"
        self.long_email = long_email = 'a' * 254 + '@' + 'subdomain'

    def tearDown(self):
        self.manager.delete_recipient_table()
    
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


if __name__ == '__main__':
    unittest.main()
