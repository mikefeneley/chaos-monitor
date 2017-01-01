import mysql.connector
from mysql.connector import errorcode
from db_connector import DBConnector
from validate_email import validate_email

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

    def __init__(self, table_name="RECIPIENTS"):
        """
        Connects to the database that stores the recipient table.
        Also, creates the database if it has not been created.
        """
        self.connector = DBConnector()
        self.connection = self.connector.get_connection()
        self.table_name = table_name
        self.email_field_length = 254 

    def create_recipient_table(self):
        """
        Creates a table if it doesn't exits in database to hold recipients.
        :return: bool -- True if the table is created or already exists, 
                         False otherwise
        """
        try:
            cursor = self.connection.cursor()
            sql = """CREATE TABLE IF NOT EXISTS """ + self.table_name + """ (
                     EMAIL VARCHAR(254) NOT NULL PRIMARY KEY)"""
            cursor.execute(sql)
            return True
        except Exception as err:
            print(err)
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
            return True
        except Exception as err:
            print(err)
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
            print(err)
            return False



    def add_recipient(self,recipient):
        """
        Adds a new recipient to the database of users who recieve an email
        when notifications are sent

        :param recipient: Email to be added to the recipient list
        :type subject: string


        :returns: bool -- True if add was successful, False otherwise
        """
        if not self.create_recipient_table():
            return False

        if not validate_email(recipient, verify=False):
            return False
       
        if len(recipient) > 254:
            return False
        
        try:
            cursor = self.connection.cursor()
            sql = "INSERT INTO " + self.table_name + "(EMAIL) VALUES ('%s')" % recipient
            cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as err:
            print(err)
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
            results=cursor.fetchall()
            for row in results:
                print(row[0])
            return True
        except Exception as err:
            print(err)
            return False

    def remove_recipient(self, recipient):#TODO: It also returns true if recipient is not in table
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
            sql = "DELETE FROM " + self.table_name + " WHERE EMAIL = '%s'" % recipient
            cursor.execute(sql)
            self.connector.connection.commit()
            return True
        except Exception as err:
            print(err)
            self.connector.connection.rollback()
            return False

    def get_recipients(self):
        """
        Get a list of emails contained in the recipient list.

        returns: list -- String list containing recipient emails.

        NOTE: Return None or Empty List?
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
                recipient_emails.append(row[0])
            return recipient_emails
        except Exception as err:
            print(err) 
            return []

if __name__ == '__main__':
    R = RecipientManager()
    R.create_recipient_table()
#    R.add_recipient('anshul.dbgt@gmail.com')
    #R.remove_recipient('abb')
    R.print_table()
    #R.delete_reipient_table('blue')
    #R.print_table('blue')
    print(R.get_recipients())
