import unittest
import sys
sys.path.append('../src')

from checksum_manager import ChecksumManager
from db_connector import DBConnector

class TestRecipientManager(unittest.TestCase):

    def setUp(self):
        self.test_table = "TEST_TABLE"
        self.empty_table = ""
        self.other_test = "OTHER_TEST_TABLE"
        self.cleanup()
        self.manager = ChecksumManager(table_name=self.test_table)
            
        self.create = """CREATE TABLE IF NOT EXISTS """ + self.test_table + """ (
                             TEST VARCHAR(254) NOT NULL PRIMARY KEY)"""
        self.delete = "DROP TABLE IF EXISTS %s" % self.test_table 

        self.empty_file = "EmptyFile.txt"
        self.checksum_test1 = "ChecksumTest1"
        self.checksum_test2 = "ChecksumTest2"

    
        if os.path.isfile(self.empty_file):
            os.remove(self.empty_file)
        if os.path.isfile(self.checksum_test1):
            os.remove(self.checksum_test1)
        if os.path.isfile(self.checksum_test2):
            os.remove(self.checksum_test2)

        self.sha1_empty_correct = "da39a3ee5e6b4b0d3255bfef95601890afd80709"
        self.sha1_test1_correct = "8d4d1b2e6d5771fc648fcd7cafd84efa44f8f744"
        self.sha1_test2_correct = "9a7dcfd9029de86dc088ee6ebbef48df90e7c6cd"

        checksum_empty = open(self.empty_file, 'w')
        checksum_empty.close()

        checksum_test1 = open(self.checksum_test1, 'w')
        checksum_test1.write("Basic Text File")
        checksum_test1.close()

        checksum_test2 = open(self.checksum_test2, 'w')
        long_string = 'A' * int(math.pow(2, 20))
        checksum_test2.write(long_string)
        checksum_test2.close()


    def tearDown(self):
        
        self.cleanup()
     
        if os.path.isfile(self.empty_file):
            os.remove(self.empty_file)
        if os.path.isfile(self.checksum_test1):
            os.remove(self.checksum_test1)
        if os.path.isfile(self.checksum_test2):
            os.remove(self.checksum_test2)


  
    def cleanup(self):
        connector = DBConnector(db_name=self.test_table)
        connection = connector.get_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("DROP TABLE IF NOT EXISTS {}".format(self.test_table))
        except Exception as err:
            pass
        try:
            cursor.execute("DROP TABLE IF NOT EXISTS {}".format(self.other_test))
        except Exception as err:
            pass


    def test_checksum_table_exists1(self):
        # Initially no table
        response = self.manager.checksum_table_exists()
        self.assertFalse(response)
        
        try:
            connector = DBConnector(db_name=self.test_table)
            connection = connector.get_connection()
            cursor = connection.cursor()
            cursor.execute(self.create)
        except Exception as err:
            pass
        response = self.manager.checksum_table_exists()
        self.assertTrue(response)

        try:
            cursor.execute(self.delete)
        except Exception as err:
            pass
        response = self.manager.checksum_table_exists()
        self.assertFalse(response)


    def test_create_checksum_table1(self):
        # Verify table does not initially exist.
        response = self.manager.checksum_table_exists()
        self.assertFalse(response)

        # Verify table exists afer creation.
        response = self.manager.create_checksum_table()
        self.assertTrue(response)
        response = self.manager.checksum_table_exists()
        self.assertTrue(response)


    def test_add_checksum_pair1(self):
        response = self.manager.checksum_table_exists()
        self.assertFalse(response)





    def test_remove_checksum_pair1(self):
        pass

    def test_get_checksum_pair(self):
        pass

    def test_get_abspath(self):
        # May not be possible to have universal tests because absolute path
        # Is dependent upon where files are installed on the users computer.
        pass


if __name__ == '__main__':
    unittest.main()
