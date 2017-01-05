import sys
import argparse
from checksum_manager import ChecksumManager
from recipient_manager import RecipientManager
from logger import Logger

import monitor

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
        self.help_af = ""
        self.help_rf = ""
        self.help_lf = ""
        self.help_ar = ""
        self.help_rr = ""
        self.help_lr = ""
        self.start = ""
        self.stop = ""
        self.status = ""
        self.restart = ""
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
        if case == 7:
            monitor.control_monitor()

    def parse_args(self):
        """
        Parse the configuartion arguments to determine which command to
        execute.

        Supported commands:

        # Adds the file file.txt and its checksum to the checksum database.
        cmon -af file.txt

        # Remove the entry with filename file.txt from the checksum database.
        cmon -rf file.txt

        # Print a list of all the files and their checksums stores in the database.
        cmon -lf

        # Add the email to the recipient database.
        cmon -ar user@domain.com

        # Remove the email from the recipient database.
        cmon -rr user@domain.com

        # Print all the emails in the recipient database.
        cmon -lr

        # Start the daemon
        cmon start

        #Stop the daemon
        cmon stop

        # Restart
        cmon restart

        # Get the status
        cmon status
        
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
        self.parser.add_argument("--start", action="store_true", dest="start_daemon", default=False, help=self.start)
        self.parser.add_argument("--stop", action="store_true", dest="stop_daemon", default=False, help=self.stop)
        self.parser.add_argument("--restart", action="store_true", dest="restart_daemon", default=False, help=self.restart)
        self.parser.add_argument("--status", action="store_true", dest="status_daemon", default=False,  help=self.status)
            
        
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
        
        if args.start_daemon:
            self.execute(None, 7)
        if args.stop_daemon:
            self.execute(None, 7)
        if args.restart_daemon:
            self.execute(None, 7)
        if args.status_daemon:
            self.execute(None, 7)


def main(args):
    cli = MonitorCli()

def cli_entrypoint():
    main(sys.argv[1:])


if __name__ == '__main__':
    cli_entrypoint()
