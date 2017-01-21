from db_connector import DBConnector
from file_manager import FileManager
from checksum_manager import ChecksumManager
from checksum_calculator import ChecksumCalculator

class Comparator:

    def __init__(self, f_manager=None, check_manager=None):
        
        if f_manager is None:
            self.f_manager = FileManager()
        else:
            self.f_manager = f_manager

        if check_manager is None:
            self.checksum_manager = ChecksumManager()
        else:
            self.checksum_manager = check_manager
        
    def load_checksums(self, filename="files"):
        files = []
        with open (filename, 'r') as f:
            while 1:
                afile = f.readline().strip("\n")
                if afile == "":
                    break
                else:
                    base = self.get_base(afile)
                    files.append(base)        
        self.f_manager.get_files(file_list = files)
      
        checksum_calculator = ChecksumCalculator()
        
        for afile in files:
            checksum = checksum_calculator.calculate_checksum("./data/" + afile)
            #checksum_manager.add_checksum_tuple(afile, checksum, hash_algo)
            # Have to break table manager interface to add checksum tuple as 
            # We need more than just the filename to add complete data set.

    def compare_checksums(self):
        pass
        """
        elements = self.checksum_maanger.get_elements()
        self.f_manager.get_files()
        for element in elements:
            filename = element.get_filename()
            old_checksum = element.get_checksum()
            new_checksum = checksum_calculator.calculate_checksum("./data/ + filename")
       
            if old checksum != new_checksum:
                self.logger.log_generic_message("CHECKSUM MISMATCH")
       """
    
    def get_base(self, abspath):
        tmp = abspath.split("/")
        afile = tmp[len(tmp) - 1]
        return afile
if __name__ == '__main__':
    comparator = Comparator()
    comparator.load_checksums()
