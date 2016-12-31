import unittest
import sys
sys.path.append('../src')

from recipient_manager import RecipientManager

class TestRecipientManager(unittest.TestCase):

    def setUp(self):
        manager = RecipientManager()


    def tearDown(self):
        pass


    def test_send_notification(self):
        print("hello")


if __name__ == '__main__':
    unittest.main()
