import mysql.connector
from mysql.connector import errorcode
from db_connector import DBConnector
from validate_email import validate_email
from logger import Logger


class RecipientManager:

    """
    RecipientManager provides an interface that allows the user to manage
    the list of individuals who are notified when notifications are sent
    out. Recipient manager lets the user add or remove recipients from the
    list as well as list all current recipients.

    The list/database managed by RecipientManager SHOULD be remote because
    the purpose of this tool is to verify system integrity. Relying on a
    local list means that the integrity of the tool could be compromised
    in the same manner as the files whose interity it is trying to verify.

    The list/database CAN be kept on the same server as the checksum database
    because the integrity of that server is assumed to be intact for the
    purposes of verification.

    +---------+-------------+------+-----+---------+-------+
    | Field   | Type        | Null | Key | Default | Extra |
    +---------+-------------+------+-----+---------+-------+
    | email   | varchar(254)| YES  |     | NULL    |       |
    +---------+-------------+------+-----+---------+-------+


    Questions/Notes:

    Should the recipient manager be allowed to add the same email twice?
    How do we protect against sql injections?
    Errors should be logged, not printed.
    How do we customize the manager? Config file? Passed in as argument?
    How much customization should be allowed?
    More options means more opportunities for bugs.
    Pass arguments to functions vs using class member variables.
    What to return case where affect already exists. I.e. creating table that already exists. Return True?
    To above: Unix Philosophy is only complain if there is an error.
    More specialized handeling of errors.
    """

    def __init__(self, table_name="RECIPIENTS", db_connector=None):
        """
        Connects to the database that stores the recipient table.

        :param table_name: Table in the database where we will store the
                           recipient information.
        """
        if db_connector == None:
            self.connector = DBConnector()
        else:
            db_connector = db_connector
        self.connection = self.connector.get_connection()
        self.table_name = table_name
        self.email_field_length = 254
        self.logger = Logger()

    def create_recipient_table(self):
        """
        Creates a table if it doesn't exits in database to hold recipients.

        :return: bool -- True if the table is created or already exists,
                         False otherwise
        """
        try:
            cursor = self.connection.cursor()
            sql = """CREATE TABLE IF NOT EXISTS %s (EMAIL VARCHAR(%d) NOT
            NULL PRIMARY KEY)""" % (self.table_name, self.email_field_length)
            cursor.execute(sql)
            self.logger.log_generic_message(
                "Table created: {}".format(self.table_name))
            return True
        except Exception as err:
            self.logger.log_generic_message(err)
            return False

    def delete_recipient_table(self):
        """
        Deletes the database table containing all recipient information.

        :return: bool -- True if the table is deleted or does not exist.
                         False otherwise
        """
        try:
            cursor = self.connection.cursor()
            sql = "DROP TABLE IF EXISTS %s" % self.table_name
            cursor.execute(sql)
            self.logger.log_generic_message(
                "Table deleted: {}".format(self.table_name))
            return True
        except Exception as err:
            self.logger.log_generic_message(err)
            return False

    def table_exists(self):
        """
        Checks if the table with the table named passed to the recipient
        manager exists.

        :return: bool -- True if the table exists. False otherwise.
        """
        try:
            cursor = self.connection.cursor()
            sql = "SHOW TABLES LIKE '%s'" % self.table_name
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return True
            else:
                return False
        except Exception as err:
            self.logger.log_generic_message(err)
            return False

    def add_recipient(self, recipient):
        """
        Adds a new recipient to the database of users who recieve an email
        when notifications are sent

        :param recipient: Email to be added to the recipient list
        :type subject: string


        :returns: bool -- True if add was successful, False otherwise
        """
        if not self.create_recipient_table():
            return False

        if not validate_email(recipient, verify=True):
            return False

        if len(recipient) > 254:
            return False

        try:
            cursor = self.connection.cursor()
            sql = """INSERT INTO %s (
            EMAIL) VALUES ('%s')""" % (self.table_name, recipient)
            cursor.execute(sql)
            self.connection.commit()
            self.logger.log_generic_message(
                "Recipient added: {}".format(recipient))
            return True
        except Exception as err:
            print err
            self.logger.log_generic_message(err)
            self.connection.rollback()
            return False

    def print_table(self):
        """
        For Debugging purposes, a print of table.
        """
        try:
            sql = "SELECT * FROM %s" % self.table_name
            cursor = self.connector.connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row[0])
            return True
        except Exception as err:
            self.logger.log_generic_message(err)
            return False

    def remove_recipient(self, recipient):
        """
        Removes emails from the list of recipients that matches the
        string 'recipient'

        :param recipient: Email to be removed from the recipient list
        :type subject: string
        :returns: bool -- True if remove was successful, False otherwise
        """
        if not self.table_exists():
            return True

        try:
            cursor = self.connector.connection.cursor()
            sql = "DELETE FROM %s WHERE EMAIL = '%s'" % (
                self.table_name, recipient)
            cursor.execute(sql)
            self.connector.connection.commit()
            self.logger.log_generic_message(
                "Recipient removed: {}".format(recipient))
            return True
        except Exception as err:
            self.logger.log_generic_message(err)
            self.connector.connection.rollback()
            return False

    def get_recipients(self):
        """
        Get a list of emails contained in the recipient list.

        returns: list -- String list containing recipient emails.
        """

        if not self.table_exists():
            return []

        try:
            recipient_emails = []
            sql = "SELECT * FROM %s" % self.table_name
            cursor = self.connector.connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                recipient_emails.append(str(row[0]))
            return recipient_emails
        except Exception as err:
            self.logger.log_generic_message(err)
            return []

if __name__ == '__main__':
    R = RecipientManager()
    print R.add_recipient('anshul7@vt.edu')
