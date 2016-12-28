
import os
class Notification:
    """
    Interface which allows user to send notifications.

    """
   
    def __init__(self):
        """
         Set up the information required to send information to desired source.

         Most likely arguments: email, server information etc...

        """
        recipients = open("recipients.txt","a") #: file containing a list of recipients or their emails
        recipients.close()

    def add_recipient(self,recipient):
        """
        An email address will be added to the existing list.

        """
        recipients = open("recipients.txt","a")
        recipients.write(recipient + os.linesep)
        recipients.close()

    def send_notification(self, message, recipient):
        """
        An email address will be sent to the email address provided as recipeient.

        """
        print(message, recipient)

        pass


if __name__ == "__main__":
    notification_sender = Notification()
    message = "Message I want to send"
    source = "Who I want to send the message to. Most likely an email address??"
    notification_sender.add_recipient("anshul7@vt.edu")
    #notification_sender.send_notification("This is the message I want to send")
