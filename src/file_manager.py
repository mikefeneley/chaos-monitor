from ftplib import FTP

class FileManager:

    def __init__(self, address="localhost", port=2121):
        self.address = address
        self.port = port

    def get_files(self, username="monitor", password="password", file_list=[]):
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
        ftp.login(username, password)
        
        # Get files and put them in the folder named 'data'
        for afile in file_list:
            command = "RETR " + afile
            ftp.retrbinary(command, open("./data/" + afile, 'wb').write)

if __name__ == '__main__':
    getter = FileManager()
    files = []
    files.append('lls')
    getter.get_files('monitor', "password", files)
