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
    """

    def __init__(self, DB_NAME="INTEGRITY_DB"):
        """
        Connects to the database that stores the recipient table.
        Also, creates the database if it has not been created.
        """
        self.connector = DBConnector()
        if self.connector.get_connection():
            print "Connected Successfuly"
            if self.connector.create_database(DB_NAME):
                print "Database %s created successfully" %DB_NAME
        else:
            print "Connection unsuccessful"
        

    def create_recipient_table(self, TABLE_NAME):
        """
        Creates a table if it doesn't exits in database to hold recipients.
        :return: bool -- True if the table is created, 
                         False otherwise
        """
        cursor = self.connector.connection.cursor()
        self.table = TABLE_NAME
        # Create table as per requirement
        sql = """CREATE TABLE """ + TABLE_NAME + """  (
                 EMAIL  VARCHAR(250) NOT NULL PRIMARY KEY)"""

        try:
            cursor.execute(sql)
            return True
        except mysql.connector.Error as err:
            print err
            return False
        
    def delete_reipient_table(self, TABLE_NAME):
        """
        Deletes the database table containing all recipient information.

        :return: bool -- True if the table is deleted or does not exist, 
                         False otherwise
        """


    def add_recipient(self,recipient):
        """
        Adds a new recipient to the database of users who recieve an email
        when notifications are sent

        :param recipient: Email to be added to the recipient list
        :type subject: string


        :returns: bool -- True if add was successful, False otherwise
        """
        if not self.valid_email(recipient):
            print "Email address not valid"
            return False
        cursor = self.connector.connection.cursor()
        # Prepare SQL query to INSERT a record into the database.
        sql = "INSERT INTO "+self.table+"(EMAIL) VALUES ('%s')"%recipient
        print sql
        try:
            cursor.execute(sql)
            self.connector.connection.commit()
            return True
    
        except mysql.connector.Error as err:
            # Rollback in case there is any error
            print err
            error = 1
            self.connector.connection.rollback()
            return False

    def print_table(self, TABLE_NAME):
        """
        For Debugging purposes, a print of table.
        """

        sql = "SELECT * FROM %s"%TABLE_NAME
        cursor = self.connector.connection.cursor()
        cursor.execute(sql)
        results=cursor.fetchall()
        for row in results:
            print row[0]

    def remove_recipient(self, recipient):#TODO: It also returns true if recipient is not in table
        """
        Removes emails from the list of recipients that matches the
        string 'recipient'

        :param recipient: Email to be removed from the recipient list
        :type subject: string
        :returns: bool -- True if remove was successful, False otherwise
        """
        cursor = self.connector.connection.cursor()
        sql = "DELETE FROM "+self.table+" WHERE EMAIL = '%s'"%recipient
        try:
            cursor.execute(sql)
            self.connector.connection.commit()
            print "Removal successful"
            return True
        except mysql.connector.Error as err:
            print err
            self.connector.connection.rollback()
            return False

    def get_recipients(self):
        """
        Get a list of emails contained in the recipient list.

        returns: list -- String list containing recipient emails.
        """
        return False

    def valid_email(self, email):
        """
        Checks that the new email passed to be added to the recipient list 
        is valid. A valid emaill is an address in the form: name@domain.xxx

        Example:
            'michael@example.com' - Valid
            ''                    - Invalid
            @example.com          - Invalid
            this.com              - Invalid

        :param email: Email to be added to the list
        :type email: string
        :returns: bool -- True if the email is valid. False otherwise.
        Checks if the email provided is in correct format.
        Dependencies: pip install validate_email
                 : sudo pip install pydns==2.3.6 

        It'll also check if email exits or not.
        """

        is_valid = validate_email(email,verify=True)#: if email does not exist, is_valid may as well be None
        if(is_valid==True):
            return True
        return False

if __name__ == '__main__':
    R = RecipientManager()
    R.create_recipient_table('blue')
    #R.add_recipient('anshul.dbgt@gmail.com')
    #R.remove_recipient('abb')
    R.print_table('blue')
