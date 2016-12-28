
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
	"""
    def __init__(self):
    	pass

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