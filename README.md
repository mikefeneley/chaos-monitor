# chaos-monitor
This is a placeholder repo. No significant work has been done on this project yet.

**Problem**

Consider the case where the user is victim to a buffer overflow attack. An attacker is able to override the buffer and cause the stack pointer to jump to a piece of malicious code he has written. This code can then replace files on the user's system, including important binary files and dynamic link libraries which are likely to be executed by the user. The new binary code injected by the hacker can be used to wreck a user’s computer. Or more insidiously, the new binary code can replicate the code of the replaced file but with malicious side effects like sending user data back to the attacker, preventing the user from ever knowing that something is wrong.

Also consider the case where a user wants to guarantee the integrity of his data over a long period of time. How does he know that the hardware has not deteriorated, causing random bits to change? How does he know a random cosmic ray has not hit his server memory and altered a critical piece of data?

**Objective**

Chaos monitor is a monitoring tool that checks its users data for alterations, either malicious or otherwise.

Chaos monitor provides an interface which allows the user to specify which files they want to have monitored. When a file is added, the chaos monitor calculates the checksum of that file, using sha1 by default. It then stores the checksum of that file alongside the filename in a remote database. 

To continually verify the integrity of the data, the chaos monitor creates a daemon which periodically wakes up, gets all the checksum/filename pairs from the database, recalculates the checksum of the filename, and compares it to the checksum fetched from the database. If the checksums match, then there is no issue as the data is unchanged. If the checksums are mismatched, then the chaos monitor logs the mismatch, sends out a notification, and responds in some fashion. 

**Status**

This tool is currently in an early development stage. The current version allows the user to add and remove files from being tracked, add and remove emails from the list of notification recipients. It does not currently send out a notification if there is a mismatch, it only reports the error in a log file. Currently, the user is limited to using local databases to store the recipients emails and the checksum/filename pairs. 

**In Progress**

Remote database support  
Notifications  
Automatic deployment and configuration of database server  
Automatic system response to mismatched checksums  
Versioning of files  
Automatic addition of common static files to database server  
GUI  
Automatic install using pip  
Rebuild changed files using version control system. Par files?  
Better tutorials and documentation  
Analysis of the problem space and comparison to other tools.  
Automatic update of checksum with scheduled file changes

**Tentative Roadmap**

Version 0.0 - Anticipated Release January 15, 2017 - Initial Release<br>
Local Database Access for Recipients and ChecksumTuples<br>
Automatic Installation of Dependencies<br>
Full Unit and Integration Testing Completed<br>
Full tutorial explaining basic functionality<br>
Notifications<br>
<br>
Version 1.0 - Anticipated Release February 1, 2017 - First Serious Release<br>
Remote Database Support<br>
Automatic system response to mismatched checksums<br>
Automatic deployment and configuration of database server<br>

Version 2.0 - Anticipated Release March 1, 2017<br>
Automatic Addition of System Files<br>

Version 3.0 - Anticipated Release May 1, 2017<br>
Automatic update of checksum with scheduled file changes. Note: Coordinate with package manager<br>
Versioning of files<br>
Rebuild changed files using version control system. Par files?<br>

Version 4.0 - Anticipated Release June 1, 2017<br>
GUI - Subset of Chaos Command Center<br>
<br>
**Installation**

All the dependencies listed have to be manually installed. Mysql 5.6 already has to be installed and running.

Install with setup.py:   _python setup.py install_

After installation, you can control the chaos monitor through the binary file cmon. 

To get options:   _cmon -h_ 

**Dependencies**

MySQL Database<br>
MySQL Python Connectors<br>
PyDaemon<br>
validate_email<br>
pydns<br>

**Misc**

If you are interested in helping, email mfeneley@vt.edu. 

This project is part of a larger project we are designing. The link to that project is here: 

<br>
<br>
<b>Contact:</b>
<ul>
<li>Michael Feneley: mfeneley(at)vt.edu</li>
<li>Anshul Basia: anshul7(at)vt.edu</li>
</ul>
