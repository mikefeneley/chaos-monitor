
import argparse
from checksum_manager import ChecksumManager
from recipient_manager import RecipientManager


class ConfigManager:
    """
    This class provides the command line interface to control
    the database entries.

    Every time the user wants to change the database, they enter a command.
    Config_Manager first calls parse_config and then calls execute which
    uses the different table managers to run the desired commands.
    """
    
    def __init__(self):
        """
        Initialisation of Parser
        """
        self.parser = argparse.ArgumentParser()
        self.help_af = ""
        self.help_rf = ""
        self.help_lf = ""
        self.help_ar = ""
        self.help_rr = ""
        self.help_lr = ""
        self.checksum_manager = ChecksumManager()
        self.recipient_manager = RecipientManager()
        self.checksum_manager.create_checksum_table()
        self.recipient_manager.create_recipient_table()

    def execute(self,arg="",case=0):
        """
        Use the output from parse_config to execute the appropriate command.
        """
        if case == 1:
            #Addition of file
            print self.checksum_manager.add_checksum_pair(arg)
        if case == 2:
            #Removal of file
            print self.checksum_manager.remove_checksum_pair(arg)

    def parse_config(self):
        """
        Parse the configuartion arguments to determine which command to 
        execute.
    
        Supported commands:

        # Adds the file file.txt and its checksum to the checksum database.
        python config_manager -af file.txt

        # Remove the entry with filename file.txt from the checksum database.
        python config_manager -rf file.txt

        # Print a list of all the files and their checksums stores in the database.
        python config_manager -lf
    
        # Add the email to the recipient database.
        python config_manager -ar user@domain.com
        
        # Remove the email from the recipient database.
        python config_manager -rr user@domain.com

        # Print all the emails in the recipient database.
        python config_manager -lr
        
        """

        self.parser.add_argument("-af",action='store',dest='file_add',help=self.help_af)
        self.parser.add_argument("-rf",action='store',dest='file_remove',help=self.help_rf)
        self.parser.add_argument("-lf",action='store_true',default=False,dest='list_files',help=self.help_lf)
        self.parser.add_argument("-ar",action='store',dest='add_email',help=self.help_ar)
        self.parser.add_argument("-rr",action='store',dest='remove_email',help=self.help_rr)
        self.parser.add_argument("-lr",action='store_true',default=False,dest='list_emails',help=self.help_lr)
        args = self.parser.parse_args()
        
        if args.file_add:
            print args.file_add
            self.execute(args.file_add,1)

        if args.file_remove:
            print args.file_remove
            self.execute(args.file_remove,2)

        if args.list_files:
            print "listing files"

        if args.add_email:
            print args.add_email

        if args.remove_email:
            print args.remove_email

        if args.list_emails:
            print "listing emails"

if __name__ == '__main__':
    manager = ConfigManager()
    manager.parse_config()

