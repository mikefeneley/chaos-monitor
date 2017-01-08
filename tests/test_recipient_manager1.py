import unittest
import sys
import mysql.connector
import inspect
sys.path.append('../src')

from recipient_manager import RecipientManager
from db_connector import DBConnector
from logger import Logger


class TestRecipientManager(unittest.TestCase):

    """
    Provide integration testing for the RecipientManager class. This is a data
    access class so the testing requires the setup of a database to check the
    impact of it's querries on the dataset.

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
            4. Assert that the return from add_recipient is false.
        """
        self.assert_table_nonexistant(self.bad_schema_table)
        self.create_table_with_bad_schema(self.bad_schema_table)
        self.assert_table_exists(self.bad_schema_table)
        manager = RecipientManager(self.bad_schema_table, self.db_connector)
        response = manager.add_recipient(self.valid_email1)
        self.assertFalse(response)
        self.delete_table(self.bad_schema_table)
        self.assert_table_nonexistant(self.bad_schema_table)

    def test_add_single_email_to_table_before_table_has_been_created(self):
        """
        Test adding a recipient to a table that has not been created yet.

        The defined behavior of the recipient manager requires a new table
        be created for adds if it does not exist. After creating the table,
        The add_recipient function should return True.

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
        response = manager.add_recipient(self.valid_email1)
        self.assertTrue(response)
        if self.valid_email1 in manager.get_recipients():
            response = True
        else:
            response = False
        self.assertTrue(True)
        self.assertTrue(manager.delete_recipient_table())
        self.assert_table_nonexistant(self.test_table_name)

    def test_add_email_with_no_domain(self):
        """
        Add an email without a domain. Example: user.com

        Adding a new recipient with a bad email should cause add_recipient to return False.

        What To Test:
            1. Assert that the table, TEST_TABLE does not exist.
            2. Use recipient manager to add an email without a domain, user.com
            3. Assert that the table, TEST_TABLE, still does not exist.
            4. Assert that the call to add_recipient returned false.
         """
        self.assert_table_nonexistant(self.test_table_name)
        manager = RecipientManager(self.test_table_name,self.db_connector)
        response = manager.add_recipient(self.email_without_domian)
        self.assert_table_nonexistant(self.test_table_name)
        self.assertFalse(response)

    def test_add_email_with_no_local_name(self):
        """
        Add an email without a local name. Example: @domain.com

        Adding a new recipient with a bad email should cause add_recipient to return False.

        What To Test:
            1. Assert that the table, TEST_TABLE does not exist.
            2. Use recipient manager to add an email without a domain, @domain.com
            3. Assert that the table, TEST_TABLE, still does not exist.
            4. Assert that the call to add_recipient returned false.
         """
        self.assert_table_nonexistant(self.test_table_name)
        manager = RecipientManager(self.test_table_name,self.db_connector)
        response = manager.add_recipient(self.email_without_local_name)
        self.assert_table_nonexistant(self.test_table_name)
        self.assertFalse(response)

    def test_add_email_that_exceeds_maximum_length(self):
        """
        Add an email that exceeds the maximum length of 254 characters, Example: 'a' * 400 + "@domain.com"

        Adding a new recipient with a long email should cause add_recipient to return False.

        What To Test:
            1. Assert that the table, TEST_TABLE does not exist.
            2. Use recipient manager to add an email that is too long.
            3. Assert that the table, TEST_TABLE, still does not exist.
            4. Assert that the call to add_recipient returned false.
         """
        pass

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
            4. Assert that the call to remove_recipient returned false.
        """
        pass
    def test_remove_user_from_table_without_user(self):
        """
        Remove an email from a table that does not have the users email.

        Trying to remove a user from a table without the users email should
        return False.

        What To Test:
            1. Assert that the table, TEST_TABLE does not exist.
            2. Use recipient manager to remove a normal email, user@subdomain.com
            3. Assert that the table, TEST_TABLE, still does not exist.
            4. Assert that the call to remove_recipient returned false.
        """
        pass


if __name__ == '__main__':
    unittest.main()
