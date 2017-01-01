import unittest
import sys
import smtpd 
from multiprocessing import Process
sys.path.append('../src')

from notification import Notification


class TestNotification(unittest.TestCase):

    def setUp(self):
        pass
    def test(self):
        pass

    def tearDown(self):
        pass


    def test_send_notification(self):
        pass
        """
        self.notifier = Notification()
        message = "This is a firestorm"
        result = self.notifier.send_notification(message, '')
        self.assertTrue(result)
        result = self.notifier.send_notification(message, '')
        self.assertTrue(result)

        # Test connection fail with bad server address.
        self.notifier = Notification(email_server="127.0.0.2")        
        with self.assertRaises(Exception):
            self.notifier.send_notification(message, '')

        self.notifier = Notification(email_server="127.0.0.1")
        self.assertTrue(result)
      
      	# Test connection fail with bad port.
        self.notifier = Notification(email_port="0")
        with self.assertRaises(Exception):
            self.notifier.send_notification(message, '')
        """
if __name__ == '__main__':
    unittest.main()
