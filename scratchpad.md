# Scratchpad

### Style Guide:
4 spaces, not tabs.
Undecided on line length... wrapping lots of code looks ugly enough to maybe justify leaving it.

###################################################
### Michael's Notes:

Design Note: When deciding what to return, opt to return True if the desired state is acheived. For example, if you tried to remove an email from the list and it didn't exist in the first place, return True because we are in the desired state, one in which the email is not in the database. Think about it. 

Make new branch for dev. DONE

We need to create an abstract database class and a 
mock database class to use for unittesting.

We also need to consider creating an abstract TableManager
class and having our two current managers extend the functionality
with a shared interface.

Use a code coverage tool to look for areas that are obviously broken or untested.

Include description of current program functionality in the README, and include a section describing desired features. DONE

Include setup files that prepare the code for packaging. DONE

Figure out how to notify that package repository that we have a new package for them to provide. 

I think for the README, we should be as specific as possible on what we currently have implemented. For example, note that the code only uses a local database to store user and checksum data and that we are going to start writing the code to make it a remote database by default. 

We also need to make a requirements.txt file. DONE

If you use apt-get to install a package in Travis during the build, it won't be on the path in python runtime. Have to either use pip or manually add the dest directory to the sys.path list DONE

When using pip to install from requirements file in Travis, pip always seems to try and install hyperlink packages first. Make a separate requirements file to install after the first for hyperlink packages that depend on other packages. to install. 

Make regular backups of group chat. Automate to backup 1 / week.

Assignments For New Developers:
    SQL Injection Validator
    Tuple Checksum Object
    Test Test Test
    Abstract Table Manager?
    Abstract DB Connector?
    
Things to Look In To: Safe way to configure tool that doesn't rely on system integrity. Remote DB Config?

###################################################
### Anshul's Notes:
 - sudo required for commands.
 - Before the install, put up password for mysql in the code.
 - Testing with different scenarios, corner test cases.
 - No use of DBConnector in testrecipeintmanager1.py

###################################################
### TODO:
- Comprehensive Documentation.
- Unit Testing.
- Alternative of valid_email.
- remove_recipient in recipient_manager.py, if table doesn't exist or no email in list, what to return: True or False ? Currently, it's false and a log message.

###################################################
### Dependencies:
- MySQL Database
- MySQL Python Connectors
- PyDaemon
- validate_email






