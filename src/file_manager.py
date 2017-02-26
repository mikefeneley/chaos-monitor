from key_manager import KeyManager
from ftplib import FTP
from logger import Logger
import time
import os

class FileManager:

    def __init__(self, address="localhost", port=2121, username='monitor', password='password'):
        self.address = address
        self.port = port
        self.username = username
        self.password = password
        self.logger = Logger()
        # This should eventually be used to store password credentials ot prevent 
        # the program from keeping them in memory that is vulnerable to being sniffed
        # using ptrace. Still working on keyring backend...
        #KeyManager.store_password(service=FTP, username=username, password=password)k

    def get_files(self, file_list=[]):
        """
        Get all files contained in list file_list and place in the subdirectory
        named data.

        :param username: Username to log on to FTP server.
        :type username: String
        :param password: Password that corresponds to username on FTP server.
        :type password: String
        :param file_list: List containing the name of all files to get.
        :type file_list: List
        :return: None
        """
        ftp = FTP()
        ftp.connect(self.address, self.port)
        ftp.login(self.username, self.password)
        
        # Get files and put them in the folder named 'data'
        for afile in file_list:
            command = "RETR " + afile
            filename = "./data/" + afile
            try:
                os.remove(filename)
                self.logger.log_generic_message("Removed " + filename)
            except Exception as err:
                self.logger.log_generic_message(err)
            
            ftp.retrbinary(command, open(filename, 'wb').write)

if __name__ == '__main__':
    getter = FileManager()
    files = []
    files.append('ls')
    getter.get_files(files)
