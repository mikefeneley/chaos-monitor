
class ConfigManager:
    """
    This class provides the command line interface to control
    the database entries.

    Every time the user wants to change the database, they enter a command.
    Config_Manager first calls parse_config and then calls execute which
    uses the different table managers to run the desired commands.
    """
    
    def execute(self):
        """
        Use the output from parse_config to execute the appropriate command.
        """
        pass    

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
        pass

if __name__ == '__main__':
    manager = ConfigManager()

