import unittest
import sys
import hashlib

sys.path.append('../src')

from checksum_calculator import ChecksumCalculator

class TestChecksumCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ChecksumCalculator()
    def test_calculate_md5(self):
        
        empty_hash = ''
        self.calculator.calculate_md5(empty_hash)

if __name__ == '__main__':
    unittest.main()
