import sys
import argparse
from checksum_manager import ChecksumManager
from recipient_manager import RecipientManager
from logger import Logger

class MonitorCli:
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
        self.help_af = "To add a file to checksum tuple database, type: '-af <filename>'"
        self.help_rf = "To remove a file from checksum tuple database, type: '-rf <filename>'"
        self.help_lf = "To get all tuples from checksum tuple database, type: '-lf'"
        self.help_ar = "To add an email to recipient database, type: '-ar <email>'"
        self.help_rr = "To remove an email from recipient database, type: 'rr <email>'"
        self.help_lr = "To get list of recipients from recipient database, type: 'lr'"
        self.parse_args()
        self.logger = Logger()

    def execute(self, arg="", case=0):
        """
        Use the output from parse_config to execute the appropriate command.
        """
        if case == 1:
            # Addition of file
            checksum_manager = ChecksumManager()
            print checksum_manager.add_checksum_pair(arg)
        if case == 2:
            # Removal of file
            checksum_manager = ChecksumManager()
            print checksum_manager.remove_checksum_pair(arg)
        if case == 3:
            # listing of checksum pairs
            checksum_manager = ChecksumManager()
            print checksum_manager.get_checksum_pairs()
        if case == 4:
            # addition of email
            recipient_manager= RecipientManager()
            print recipient_manager.add_recipient(arg)
        if case == 5:
            # removal of email
            recipient_manager = RecipientManager()
            print recipient_manager.remove_recipient(arg)
        if case == 6:
            # listing of emails
            recipient_manager = RecipientManager()
            print recipient_manager.get_recipients()

    def parse_args(self):
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
        self.parser.add_argument(
            "-af",
            action='store',
            dest='file_add',
            help=self.help_af)
        self.parser.add_argument(
            "-rf",
            action='store',
            dest='file_remove',
            help=self.help_rf)
        self.parser.add_argument(
            "-lf",
            action='store_true',
            default=False,
            dest='list_files',
            help=self.help_lf)
        self.parser.add_argument(
            "-ar",
            action='store',
            dest='add_email',
            help=self.help_ar)
        self.parser.add_argument(
            "-rr",
            action='store',
            dest='remove_email',
            help=self.help_rr)
        self.parser.add_argument(
            "-lr",
            action='store_true',
            default=False,
            dest='list_emails',
            help=self.help_lr)
        args = self.parser.parse_args()


        if args.file_add:
            print args.file_add
            self.execute(args.file_add, 1)

        if args.file_remove:
            print args.file_remove
            self.execute(args.file_remove, 2)

        if args.list_files:
            print "listing files"
            self.execute(None, 3)

        if args.add_email:
            print args.add_email
            self.execute(args.add_email, 4)

        if args.remove_email:
            print args.remove_email
            self.execute(args.remove_email, 5)

        if args.list_emails:
            print "listing emails"
            self.execute(None, 6)

def main(args):
    cli = MonitorCli()

def cli_entrypoint():
    print("this")
    main(sys.argv[1:])


if __name__ == '__main__':
    cli_entrypoint()
