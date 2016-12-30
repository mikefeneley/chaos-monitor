import mysql.connector
from mysql.connector import errorcode
from db_connector import DBConnector

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

        """
        pass

    def recipient_table_exists(self, TABLE_NAME):
        """
        Check to see if a database table has been created to hold the 
        recipients
       
        :param TABLE_NAME: Name of the database we are checking exists.
        :type TABLE_NAME: string
        :return: bool -- True if the table exists. False otherwise.
        """
        pass

    def create_recipient_table(self, TABLE_NAME):
        """
        Creates a table in database to hold recipients.

        :return: bool -- True if the table was created. False otherwise.
        """
        pass
        
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
        return False

    def remove_recipient(self, recipient):
        """
        Removes emails from the list of recipients that matches the
        string 'recipient'

        :param recipient: Email to be removed from the recipient list
        :type subject: string
        :returns: bool -- True if remove was successful, False otherwise
        """
        return False

    def get_recipients(self):
        """
        Get a list of emails contained in the recipient list.

        returns: list -- String list containing recpient emails.
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
        """
        return False

if __name__ == '__main__':
    R = RecipientManager()
