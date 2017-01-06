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
        self.help_af = "To add a file to checksum tuple database, type: 'cmon -af <filename>'"
        self.help_rf = "To remove a file from checksum tuple database, type: 'cmon -rf <filename>'"
        self.help_lf = "To get all tuples from checksum tuple database, type: 'cmon -lf'"
        self.help_ar = "To add an email to recipient database, type: 'cmon -ar <email>'"
        self.help_rr = "To remove an email from recipient database, type: 'cmon -rr <email>'"
        self.help_lr = "To get list of recipients from recipient database, type: 'cmon -lr'"
        self.start = "To start the daemon, type: 'cmon --start'"
        self.stop = "To stop the daemon, type: 'cmon --stop'"
        self.status = "To get the status of daemon, type: 'cmon --status'"
        self.restart = "To restart the daemon, type: 'cmon --restart'"
        self.build_parser()
        self.logger = Logger()

    
    def build_parser(self):
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
        self.parser.add_argument(
            "--start",
            action="store_true",
            dest="start_daemon",
            default=False,
            help=self.start)
        self.parser.add_argument(
            "--stop",
            action="store_true",
            dest="stop_daemon",
            default=False,
            help=self.stop)
        self.parser.add_argument(
            "--restart",
            action="store_true",
            dest="restart_daemon",
            default=False,
            help=self.restart)
        self.parser.add_argument(
            "--status",
            action="store_true",
            dest="status_daemon",
            default=False,
            help=self.status)

        args = self.parser.parse_args()
        self.parse_args(args)

    def parse_args(self,args):
        
        if args.file_add:
            print args.file_add
            # Addition of file
            checksum_manager = ChecksumManager()
            print checksum_manager.add_checksum_pair(args.file_add)

        if args.file_remove:
            print args.file_remove
            # Removal of file
            checksum_manager = ChecksumManager()
            print checksum_manager.remove_checksum_pair(args.file_remove)

        if args.list_files:
            print args.list_files
            # listing of checksum pairs
            checksum_manager = ChecksumManager()
            print checksum_manager.get_checksum_pairs()

        if args.add_email:
            print args.add_email
            # addition of email
            recipient_manager = RecipientManager()
            print recipient_manager.add_recipient(args.add_email)

        if args.remove_email:
            print args.remove_email
            # removal of email
            recipient_manager = RecipientManager()
            print recipient_manager.remove_recipient(args.remove_email)

        if args.list_emails:
            print "listing emails"
            # listing of emails
            recipient_manager = RecipientManager()
            print recipient_manager.get_recipients()

        if args.start_daemon:
            #startinf daemon
            monitor.control_monitor()

        if args.stop_daemon:
            #stopping daemon
            monitor.control_monitor()

        if args.restart_daemon:
            #restartig daemon
            monitor.control_monitor()

        if args.status_daemon:
            #getting ths status of daemon
            monitor.control_monitor()


def main(args):
    cli = MonitorCli()


def cli_entrypoint():
    main(sys.argv[1:])


if __name__ == '__main__':
    cli_entrypoint()
