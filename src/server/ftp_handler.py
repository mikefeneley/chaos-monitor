from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import shutil
import os
import time

class MyHandler(FTPHandler):

    def on_connect(self):
        print "%s:%s connected" % (self.remote_ip, self.remote_port)

    def on_disconnect(self):
        pass        

    def on_login(self, username):
        monitored_files = open('files', 'r')
        for line in monitored_files:
            abspath = line.strip("\n")
            tmp = abspath.split("/")
            afile = tmp[len(tmp) - 1] 
            shutil.copyfile(abspath, "./" + afile)
        monitored_files.close()

    def on_logout(self, username):
        
        monitored_files = open('files', 'r')

        for line in monitored_files:
            abspath = line.strip("\n")
            tmp = abspath.split("/")
            afile = tmp[len(tmp) - 1]
            os.remove(afile)
        monitored_files.close()
        
        pass
    """
    def on_file_sent(self, file):
        # do something when a file has been sent
        pass

    def on_file_received(self, file):
        # do something when a file has been received
        pass

    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        pass
    """

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        import os
        os.remove(file)

