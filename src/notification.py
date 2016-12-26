
class Notification:
    """
    Interface which allows user to send notifications.

    """
   
   def __init__(self):
    """
    Set up the information required to send information to desired source.

    Most likely arguments: email, server information etc...

    """
        pass

    def send_notification(self, message, source):
        print(message, source)
        pass


if __name__ == "__main__":
    notification_sender = Notification()
    message = "Message I want to send"
    source = "Who I want to send the message to. Most likely an email address??")
    notification_sender.send_notification("This is the message I want to send")
