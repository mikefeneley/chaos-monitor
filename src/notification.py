import os
import smtplib

"""
To use the send_notification function, user has to allow his gmail account to be used by less secure
apps, which can be done from https://myaccount.google.com/security , option is available at the last
section of the page.
"""


class Notification:
    """
    Interface which allows user to send notifications using email protocols.

    """
   
    def __init__(self, email_server="127.0.0.1", email_port = 587, 
        email_username="", email_pwd=""):
        """
        Set up connection information and authentication tokens to allow user to 
        access smtp server.

        :param email_server: IP Address of SMTP server for sending mail.
        :type email_server: string
        :param email_port: Port to use to send email
        :type email_port: int
        :param email_username: Authentication username for SMTP server.
        :type email_username: string
        :param email_pwd: Authentication username for SMTP server.
        :type email_pwd: string
        """
        self.email_port = email_port
        self.email_server = email_server 
        self.gmail_user = email_username 
        self.gmail_pwd = email_pwd

    def build_email(self, subject="Notification from Vulnerability", message="", source="", destination=""):
        """
        Creates an email notification object from arguments. The email is
        constructed using python MIME object types.

        :param subject: Subject line of the email.
        :type subject: string
        :param message: Message body of the email.
        :type message: string
        :param source: Email address message is sent from.
        :type source: string
        :param destination: Email address to send message to.
        :type destination: string
        :returns: bool -- Constructed Mime
        """
        pass


    def send_notification(self, message="", recipient=""):
        """
        Sends a notifiction message to email address specified by recipient.

        :param message: Notification message to send
        :type message: string
        :param recipient: Email address of the recipient
        :type recipient: string
        :returns: bool -- True if the message was successfuly sent. False otherwise.
        """
        print(self.email_server, self.email_port, message, recipient)
        TO = recipient

        SUBJECT = "Notification from Vulnerability"
        TEXT = message

        server = smtplib.SMTP(self.email_server, self.email_port)

        # Verify that these things are necessary.
        server.starttls()
        server.ehlo()
        server.login(self.gmail_user, self.gmail_pwd) #: a login attemt by server
        BODY = '\r\n'.join(['To: %s' % TO,
                'From: %s' % self.gmail_user,
                'Subject: %s' % SUBJECT,
                '', TEXT])
        server.sendmail(self.gmail_user, [TO], BODY)

        # NEW IMPLEMENTATION
        # email = self.build_email(message=message, soruce=self.gmail_user, destination=recipient)
        # server.sendmail(email)

        print ('email sent')
        server.close()
        return True


    def notify_all(self, message, recipients):
        """
        Sends the message to every email address on the recipient list.
        :param message: Notification message to send
        :type message: string
        :param recipients: List of emails to send notification message
        :type recipients: List of strings
        :returns: bool -- True if the message was successfuly sent to all 
                          recipients. Otherwise False


        """
        success  = True
        for recipient in recipients:
            if not self.send_notification(message,recipient):
                success = False
        return success




if __name__ == "__main__":

    gmail = "smtp.gmail.com"
    notification_sender = Notification(email_server='localhost', email_port = 587, email_username="", email_pwd="")
    message = "Message I want to send"
    source = "Who I want to send the message to. Most likely an email address??"
    notification_sender.send_notification("Hi", 'michael@sample.com')

    recipients = []
    recipients.append("sample1@gmail.com")
    recipients.append("sample2@gmail.com")

    notification_sender.notify_all(message, recipients)

