import unittest
import sys
import hashlib
import os
import math
sys.path.append('../src')

from checksum_calculator import ChecksumCalculator

class TestChecksumCalculator(unittest.TestCase):
    
    def setUp(self):
   
        self.calculator = ChecksumCalculator()
            
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
        self.md5_empty_correct = "d41d8cd98f00b204e9800998ecf8427e" 
        self.md5_test1_correct = "dc7de94111798c3e997321905c6cc4be"
        self.md5_test2_correct = "e6065c4aa2ab1603008fc18410f579d4"

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
        
        if os.path.isfile(self.empty_file):
            os.remove(self.empty_file)
        if os.path.isfile(self.checksum_test1):
            os.remove(self.checksum_test1)
        if os.path.isfile(self.checksum_test2):
            os.remove(self.checksum_test2)

    def test_calculate_sha1(self):
        empty_hash = self.calculator.calculate_sha1(self.empty_file)
        self.assertEqual(empty_hash, self.sha1_empty_correct)
        test1 = self.calculator.calculate_sha1(self.checksum_test1)
        self.assertEqual(test1, self.sha1_test1_correct)
        test2 = self.calculator.calculate_sha1(self.checksum_test2)
        self.assertEqual(test2, self.sha1_test2_correct)

    def test_calculate_md5(self):
        empty_hash = self.calculator.calculate_md5(self.empty_file)
        self.assertEqual(empty_hash, self.md5_empty_correct)
        test1 = self.calculator.calculate_md5(self.checksum_test1)
        self.assertEqual(test1, self.md5_test1_correct)
        test2 = self.calculator.calculate_md5(self.checksum_test2)
        self.assertEqual(test2, self.md5_test2_correct)


if __name__ == '__main__':
    unittest.main()
