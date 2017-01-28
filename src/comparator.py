from db_connector import DBConnector
from file_manager import FileManager
from checksum_manager import ChecksumManager
from checksum_calculator import ChecksumCalculator
from checksum_tuple import ChecksumTuple
from logger import Logger
class Comparator:

    def __init__(self, f_manager=None, check_manager=None):
        self.logger = Logger()    
        if f_manager is None:
            self.f_manager = FileManager()
        else:
            self.f_manager = f_manager
    
        if check_manager is None:
            self.checksum_manager = ChecksumManager()
        else:
            self.checksum_manager = check_manager
        
    def load_checksums(self, filename="files"):
        self.logger.log_generic_message("Loading initial checksums")
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
            check_tuple = ChecksumTuple(afile, afile, checksum)
        
            self.checksum_manager.add_element(check_tuple)
        self.logger.log_generic_message("Finished loading initial checksums")

    def compare_checksums(self):
        self.logger.log_generic_message("Starting Checksum Compare") 
        elements = self.checksum_manager.get_elements()
        self.f_manager.get_files()
        for check_tuple in elements:
            filename = check_tuple.filename
            old_checksum = check_tuple.checksum
            checksum_calculator = ChecksumCalculator()
            
            path = "./data/" + filename
            self.logger.log_generic_message(path)
            new_checksum = checksum_calculator.calculate_checksum(path)
        
            print(old_checksum, new_checksum)

            self.logger.log_generic_message("Filename: " + filename + " DB Checksum:" + old_checksum + "New Checksum: " + new_checksum) 
            if old_checksum != new_checksum:
                self.logger.log_generic_message("CHECKSUM MISMATCH")
            else:
                self.logger.log_generic_message("Checksum match")
    
    def get_base(self, abspath):
        tmp = abspath.split("/")
        afile = tmp[len(tmp) - 1]
        return afile
if __name__ == '__main__':
    comparator = Comparator()
    comparator.load_checksums()
    comparator.compare_checksums()
