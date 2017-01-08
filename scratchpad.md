# Scratchpad

### Style Guide:
4 spaces, not tabs.
Undecided on line length... wrapping lots of code looks ugly enough to maybe justify leaving it.


###################################################
### Michael's Notes:
We need to create an abstract database class and a 
mock database class to use for unittesting.

We also need to consider create an abstract TableManager
class and having our two current managers extend the functionality
with a shared interface.

Use a code coverage tool to look for areas that are obviously broken.

Not everything, it can be forced to enforce certain policies, but it only checks a few of them by default.

Include description of current program functionality in the README, and include a section describing desired features.

Include setup files that prepare the code for packaging.

And finally, figure out how to notify that package repository that we have a new package for them to provide

I am sure there are other things, but that is a start.

I think for the README, we should be as specific as possible on what we currently have implemented. For example, note that the code only uses a local database to store user and checksum data and that we are going to start writing the code to make it a remote database by default.

We also need to make a requirements.txt file. DONE

If you use apt-get to install a package in Travis during the build, it won't be on the path in python runtime. Have to either use pip or manually add the dest directory to the sys.path list

###################################################
### Anshul's Notes:
 - sudo required for commands.
 - Before the install, put up password for mysql in the code.
 - Testing with different scenarios, corner test cases.
 - No use of DBConnector in testrecipeintmanager1.py

###################################################
### Bugs:


###################################################
### Features:
    validate_email() does a comprehensive check if given email exits or not but takes a good amount of time (1-2 secs).


###################################################
### TODO:
- Comprehensive Documentation.
- Unit Testing.
- Alternative of valid_email.
- remove_recipient in recipient_manager.py, if table doesn't exist or no email in list, what to return: True or False ? Currently, it's false and a log message.

###################################################
### Status:


###################################################
### Dependencies:
- MySQL Database
- MySQL Python Connectors
- PyDaemon
- validate_email






