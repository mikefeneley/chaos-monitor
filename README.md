# chaos-monitor
This is a placeholder repo. No significant work has been done on this project yet.

**KEY NOTES**

We try to follow PEP8 style convention. We have relaxed the rules on 80 character limit because line wraps always look ugly and most people have large monitors.

Test functions should be as descriptive as possible. Functions with 10+ words are totally fine as long as they describe the specific functionality they are testing.

Use 4 spaces, not tabs for indents. This is important.

Tests should leave the system in the same state they found it.

No coypyleft license software can be used.

Untested code is broken code. Testing is the most important task an comes before anything else.

**Problem**

Consider the case where the user is victim of a buffer overflow attack. An attacker is able to override the buffer and cause the stack pointer to jump to a piece of malicious code he has written. This code can then replace files on the user's system, including important binary files and dynamic link libraries which are likely to be executed by the user. The new binary code injected by the hacker can be used to wreck a user’s computer. Or more insidiously, the new binary code can replicate the functionality of the replaced file but with malicious side effects like sending user data back to the attacker, preventing the user from ever knowing that something is wrong.

Also consider the case where a user wants to guarantee the integrity of his data over a long period of time. How does he know that the hardware has not deteriorated, causing random bits to change? How does he know a random cosmic ray has not hit his server memory and altered a critical piece of data? This is less of an issue because most backup systems have RAID and parity checkers, but a stored checksum backup provides additional insurance for file integrity.

**Objective**

Chaos monitor is a monitoring tool that checks its user's data for alterations, malicious or otherwise.

Chaos monitor provides an interface that allows the user to specify which files they want to have monitored. When a file is added, the chaos monitor calculates the checksum of that file, using sha1 by default. It then stores the checksum of that file alongside the filename in a remote database. 

To continually verify the integrity of the data, the chaos monitor creates a daemon which periodically wakes up, gets all the checksum/filename pairs from the database, recalculates the checksum of the filename, and compares it to the checksum fetched from the database. If the checksums match, then there is no issue as the data is unchanged. If the checksums are mismatched, then the chaos monitor logs the mismatch, sends out a notification, and responds in some fashion. 

**Status**

This tool is currently in an early development stage. The current version allows the user to add and remove files from being tracked as well as add and remove emails from the list of notification recipients. It does not currently send out a notification if there is a mismatch, it only reports the error in a log file. Currently, the user is limited to using local databases to store the recipient's emails and the checksum/filename pairs. 

**In Progress**

- Remote database support  
- Notifications  
- Automatic deployment and configuration of database server  
- Automatic system response to mismatched checksums  
- Versioning of files  
- Automatic addition of common/important static files to database server  
- GUI  
- Automatic install using pip  
- Rebuild changed files using version control system. Par files?  
- Better tutorials and documentation  
- Analysis of the problem space and comparison to other tools.  
- Automatic update of checksum with scheduled file changes

**Tentative Roadmap**

Version 0.0 - Anticipated Release January 15, 2017 - Initial Release  
Local Database Access for Recipients and ChecksumTuples  
Automatic Installation of Dependencies  
Full Unit and Integration Testing Completed  
Full tutorial explaining basic functionality  
Notifications  
  
Version 1.0 - Anticipated Release February 1, 2017 - First Serious Release  
Remote Database Support  
Automatic system response to mismatched checksums  
Automatic deployment and configuration of database server  
Development and design document to help new developers understand system.  

Version 2.0 - Anticipated Release March 1, 2017  
Automatic Addition of System Files  

Version 3.0 - Anticipated Release May 1, 2017  
Automatic update of checksum with scheduled file changes. Note: Coordinate with package manager  
Versioning of files  
Rebuild changed files using version control system. Par files?  

Version 4.0 - Anticipated Release June 1, 2017  
GUI - Subset of Chaos Command Center  
  
**Installation**

All the dependencies listed have to be manually installed. Mysql 5.6 already has to be installed and running.

Install with setup.py:   _python setup.py install_

After installation, you can control the chaos monitor through the binary file cmon. 

To get options:   _cmon -h_ 

Options implemented so far:
- cmon -af _filename_
- cmon -rf _filename_
- cmon -ar _email_
- cmon -rr _email_
- cmon -lr
- cmon -lf
- cmon --start
- cmon --stop
- cmon --Status
- cmo --restart

**Dependencies**

- MySQL Database  
- MySQL Python Connectors
- rsfile (Required to install PyDaemon)  
- PyDaemon  
- validate_email  
- pydns  

**Misc**

This project is part of a larger project we are designing. The link to that project is here: https://github.com/mikefeneley/chaos-command-center

If you are interested in helping with either this project or the chaos command center, email mfeneley@vt.edu. 

We don't just need people who are interested in technology, we are also looking for people who are talented writers, artists designers, or any combination of useful skills.


**Design Notes**

The target audience of our flagship project, the chaos command center, is your average computer user. Anything overly technical needs to be abstracted away. 

Form is liberating. While it is possible to add endless customization to tools, doing so increases the complexity of the tool and increases the risk of bugs. We reject addtional, noncritical functionality at the cost of addtional complexity and security risk.

For example, we could add functionality which would let the user change the name of the tables in the database used to store the checksum pairs. But to what end? If an attacker were to use that option to change the table name, the daemon would no longer be able to pull the checksum data it is supposed to be testing. It is an unnecessary feature that adds nothing while increasing the attack surface. 

We want this tool to be capable of automatically seting up a remote database on an EC2 server or other AWS service. Possibly using SaltStack. Think about information required by the program to do this, i.e. AWS credentials and keys.

More design notes/brainstorms are in stratchpad.md.

<br>
<br>
<b>Contact:</b>
<ul>
<li>Michael Feneley: mfeneley(at)vt.edu</li>
<li>Anshul Basia: anshul7(at)vt.edu</li>
</ul>
