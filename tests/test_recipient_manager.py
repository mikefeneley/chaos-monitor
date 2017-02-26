import unittest
import sys
import mysql.connector
import inspect

sys.path.append('src')

from recipient_manager import RecipientManager
from db_connector import DBConnector
from logger import Logger


class TestRecipientManager(unittest.TestCase):

    """
    Provide integration testing for the RecipientManager class. This is a data
    access class so the testing requires the setup of a database to check the
    impact of it's querries on the dataset.

    Tests:
        Add With No Table
        Add With Bad Emails
        Remove With No Table
        Remove With Table But NonexistantRecipient

    Notes:
        As the number of tests increases, this test set could become a
        bottleneck and slow down overall development. Is this starts to happen
        we need to consider setting up a permanant database stored in memory
        instead of rebuilding a datbase with known states for each tests.

        We should also work on decoupling the data from the data access.
        It is possible that we will change the schema as the project progresses
        and this will be eaiser if we are generating the databases instead
        of descrbining the fields from in the code.
    """

    def setUp(self):

        # Database settings.
        self.host = 'localhost'
        self.port = '3306'

        self.test_database_name = "TEST_RECIPIENT_MANAGER_DB"
        self.test_table_name = "TEST_TABLE"
        self.empty_table_name = ""
        self.bad_schema_table = "BAD_SCHEMA_TABLE"

        # Setup connection information that lets the tester
        # setup different states for testing.
        self.connect = mysql.connector.connect(
            user='root', passwd='', host=self.host, port=self.port)
        self.cursor = self.connect.cursor()
        self.db_connector = DBConnector(db_name=self.test_database_name)
        self.logger = Logger()
        self.delete_test_db()

        # Data that will be used for testing.
        self.valid_email1 = "user1@subdomain"
        self.valid_email2 = "user2@subdomain"
        self.invalid_email1 = "baduser"
        self.invalid_email2 = "@subdomain"
        self.long_email = long_email = 'a' * 254 + '@' + 'subdomain'
        self.email_without_domian = "user.com"
        self.email_without_local_name = "@domain.com"

    def tearDown(self):
        self.delete_test_db()
        pass

    def create_table_with_bad_schema(self, table_name=""):
        try:
            self.create_test_db()
            sql = """CREATE TABLE %s (BAD_SCHEMA BIGINT NOT NULL PRIMARY KEY)""" % table_name
            self.cursor.execute(sql)
            self.logger.log_generic_message(
                "Table created: {}".format(table_name))
            return True
        except Exception as err:
            self.logger.log_generic_message(err)
            return False

    def delete_table(self, table_name=""):
        try:
            sql = "DROP TABLE %s" % table_name
            self.cursor.execute(sql)
            self.logger.log_generic_message(
                "Table created: {}".format(table_name))
            return True
        except Exception as err:
            self.logger.log_generic_message(err)
            return False

    def create_test_db(self):
        try:
            sql = "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(
                self.test_database_name)
            self.cursor.execute(sql)
            self.logger.log_generic_message(
                "Database created".format(self.test_database_name))
            self.connect.database = self.test_database_name
        except Exception as err:
            self.logger.log_generic_message(err)
            self.logger.log_generic_message("What happened")

    def delete_test_db(self):
        self.cursor.execute(
            "DROP DATABASE IF EXISTS %s" % self.test_database_name)

    def assert_table_nonexistant(self, table_name=""):
        self.create_test_db()
        sql = "SHOW TABLES LIKE '%s'" % table_name
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        self.assertIsNone(result)

    def assert_table_exists(self, table_name=""):
        self.create_test_db()
        sql = "SHOW TABLES LIKE '%s'" % table_name
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

    def test_add_to_table_with_bad_schema1(self):
        """
        Test adding a new recipient to a table with an incorrectly defined schema.

        Adding a new recipient to a table with a bad schema should cause the method to return False.

        What To Test:
            1. Assert that the table initially does not exist.
            2. Use external database connection to create database with 1 field that is called BAD_SCHEMA_FIELD instead of email.
            3. Try adding a recipient a normal email address, user@domain.com
            4. Assert that the return from add_element is false.
        """
        self.assert_table_nonexistant(self.bad_schema_table)
        self.create_table_with_bad_schema(self.bad_schema_table)
        self.assert_table_exists(self.bad_schema_table)
        manager = RecipientManager(self.bad_schema_table, self.db_connector)
        response = manager.add_element(self.valid_email1)
        self.assertFalse(response)
        self.delete_table(self.bad_schema_table)
        self.assert_table_nonexistant(self.bad_schema_table)

    def test_add_single_email_to_table_before_table_has_been_created(self):
        """
        Test adding a recipient to a table that has not been created yet.

        The defined behavior of the recipient manager requires a new table
        be created for adds if it does not exist. After creating the table,
        The add_element function should return True.

        Note: I think we create the email before checking if the email is valid.
              We need to change that to pass this test.

        What To Test:
            1. Assert that the table, TEST_TABLE does not exist
            2. Use recipient manager to add a normal email, user@subdomain.com
            3. Assert that the table, TEST_TABLE, now exist.
            4. Assert that add_recipieint() returned True
            4. Query the database and assert the email, user@subdomain.com does exist in table, TEST_TABLE.
            5. Delete the table, TEST_TABLE.
            6. Assert that the table, TEST_TABLE, no longer exists.
        """
        self.assert_table_nonexistant(self.test_table_name)
        manager = RecipientManager(self.test_table_name,self.db_connector)
        response = manager.add_element(self.valid_email1)
        self.assertTrue(response)
        self.assertTrue(self.valid_email1 in manager.get_elements())
        self.assertTrue(manager.delete_table())
        self.assert_table_nonexistant(self.test_table_name)

    def test_add_email_with_no_domain(self):
        """
        Add an email without a domain. Example: user.com

        Adding a new recipient with a bad email should cause add_element to return False.

        What To Test:
            1. Assert that the table, TEST_TABLE does not exist.
            2. Use recipient manager to add an email without a domain, user.com
            3. Assert that the table, TEST_TABLE, still does not exist.
            4. Assert that the call to add_element returned false.
         """
        self.assert_table_nonexistant(self.test_table_name)
        manager = RecipientManager(self.test_table_name,self.db_connector)
        response = manager.add_element(self.email_without_domian)
        self.assert_table_nonexistant(self.test_table_name)
        self.assertFalse(response)

    def test_add_email_with_no_local_name(self):
        """
        Add an email without a local name. Example: @domain.com

        Adding a new recipient with a bad email should cause add_element to return False.

        What To Test:
            1. Assert that the table, TEST_TABLE does not exist.
            2. Use recipient manager to add an email without a domain, @domain.com
            3. Assert that the table, TEST_TABLE, still does not exist.
            4. Assert that the call to add_element returned false.
         """
        self.assert_table_nonexistant(self.test_table_name)
        manager = RecipientManager(self.test_table_name,self.db_connector)
        response = manager.add_element(self.email_without_local_name)
        self.assert_table_nonexistant(self.test_table_name)
        self.assertFalse(response)

    def test_add_email_that_exceeds_maximum_length(self):
        """
        Add an email that exceeds the maximum length of 254 characters, Example: 'a' * 400 + "@domain.com"

        Adding a new recipient with a long email should cause add_element to return False.

        What To Test:
            1. Assert that the table, TEST_TABLE does not exist.
            2. Use recipient manager to add an email that is too long.
            3. Assert that the table, TEST_TABLE, still does not exist.
            4. Assert that the call to add_element returned false.
         """
        self.assert_table_nonexistant(self.test_table_name)
        manager = RecipientManager(self.test_table_name,self.db_connector)
        response = manager.add_element(self.long_email)
        self.assert_table_nonexistant(self.test_table_name)
        self.assertFalse(response)

    def test_remove_user_from_nonexistant_table(self):
        """
        Remove an email from a table that does not exist.

        Trying to remove a user from a table that does not exist should
        return False.

        NOTE: I do not think this is currently implemented and needs to
        be changed to pass the test.

        What To Test:
            1. Assert that the table, TEST_TABLE does not exist.
            2. Use recipient manager to remove a normal email, user@subdomain.com
            3. Assert that the table, TEST_TABLE, still does not exist.
            4. Assert that the call to remove_element returned false.
        """
        self.assert_table_nonexistant(self.test_table_name)
        manager = RecipientManager(self.test_table_name,self.db_connector)
        response = manager.remove_element(self.valid_email1)
        self.assertFalse(response)
        self.assert_table_nonexistant(self.test_table_name)
    
    def test_remove_user_from_table_without_user(self):
        """
        Remove an email from a table that does not have the users email.

        Trying to remove a user from a table without the users email should
        return False.

        What To Test:
            1. Assert that the table, TEST_TABLE does not exist.
            2. Create the table using recipient_manager.
            2. Use recipient manager to remove a normal email, user@subdomain.com
            3. Assert that the table, TEST_TABLE, still does not exist.
            4. Assert that the call to remove_element returned false.
        """
        self.assert_table_nonexistant(self.test_table_name)
        manager = RecipientManager(self.test_table_name,self.db_connector)
        self.assertTrue(manager.create_table())
        response = manager.remove_element(self.valid_email1)
        self.assertFalse(response)
        self.assertTrue(manager.delete_table())
        self.assert_table_nonexistant(self.test_table_name)


    def test_remove_user_from_table_with_user(self):
        """
        Remove an email from a table that does have the users email.

        Removing a user from a table with that user returns True

        What To Test:
            1. Assert that the table, TEST_TABLE does not exist.
            2. Create the table using recipient_manager.
            2. Use recipient manager to add a normal email, user@subdomain.com
            3. Assert that the table, TEST_TABLE, exists.
            5. Assert that the call to add_element() returned true.
            6. Assert that the recipient is in the database.
            7. Use remove_element() to remove the email from the database.
            8. Assert that the call to remove_reciepient() returned True.
            9. Assert the the user is no longer in the database.
        """
        pass 

    def test_create_database_with_empty_string_name(self):
        """
        Try creating a database with an emptry string as the table name.

        Creating a table with an empty string causes mysql to throw
        a syntax exception. The create function should return False.

        What To Test:
            1. Assert that no tables currently exist in the test database.
            2. Create a Recipient Manager with the empty table name as an argument.
            3. Assert that table_exists() function returns False.
            4. Try to create table and assert that the function call returns False.
            5. Assert that there are still no tables in the test database.
        """
        pass
 
    def test_get_users_from_nonexistant_table(self):
        """
        Try getting the users from a table that does not exist. 

        Calling get_elements() when the table has not been created should
        return an empty list.

        What To Test:
            1. Asset that the table, TEST_TABLE does not exist.
            2. Assert that call to get_elements() returns an empty list.
            3. Assert that the table, TEST_TABLE still does not exist.
        """
        pass

    def test_get_users_from_table_that_exists_with_no_users(self):
        """
        Try getting users from a table with no users.

        Calling get_recipient() when the table has been created but has
        no users should return an empty list.

        What To Test:
            1. Assert that the table, TEST_TABLE does not exist.
            2. Create the table.
            3. Assert the table exists.
            4. Assert the the call to get_elements() returns an empty list.
        """
        pass

    def test_get_users_from_table_with_single_user(self):
        """
        Try getting users from a table with a single user.

        Calling get_recipient() when the table has 1 user should 
        return that one user in a list.

        What To Test:
            1. Assert that the table, TEST_TABLE does not exist.
            2. Create the table.
            3. Assert the table exists.
            4. Add a user to the table. Assert the call to add_element returns True
            5. Assert the the call to get_elements() returns a list containing the recipient.
        """
        pass

    def test_get_users_from_table_with_two_users(self):
        """
        Test getting users from a table with two users.

        Calling get_recipient() when the table has 2 emails should 
        return a list with both of those emails.

        What To Test:
            1. Assert that the table, TEST_TABLE does not exist.
            2. Create the table.
            3. Assert the table exists.
            4. Add a user to the table. Assert the call to add_element returns True
            5. Assert the the call to get_elements() returns a list containing the recipient.
            6. Add another user to the table with a different email. Assert the call to add_recipeint returns True
            7. Assser that the call to get_elements() returns a list containing both emails.
        """
        pass
    
    def test_delete_nonexistant_table(self):
        """
        Test deleteting a table from a database that does not exist.
       
        Deleting a table that does not exist should return False.
        
        What To Test:
            1. Assert that the table, TEST_TABLE, does not exist.
            2. Try to delete the table.
            3. Assert that the delete_table response returns False.
       
        """
        pass

    def test_delete_existant_but_empty_table(self):
        """
        Test deleteing a table that exists but has no users.

        Delete a table with no users should delete the table and return True

        What To Test:
            1. Assert that the table, TEST_TABLE, does not exist.
            2. Create the table. Assert that create_table returns True
            3. Delete the table. Assert that delete_table returns True
        """
        pass

    def test_delete_existant_table_with_user(self):
        """
        Test deleteing a table that has a user in it.

        Deleting a table with a user should delete the table and return True

        What To Test:
            1. Assert that the table, TEST_TABLE does not exist.
            2. Create the table. Assert that create_table returns True
            3. Add a user with a normal email to the table. Assert that add_element returns True.
            4. Assert that the table is in the table.
            5. Delete the table. Assert that delete_table returns True.
        """
        pass





if __name__ == '__main__':
    unittest.main()
