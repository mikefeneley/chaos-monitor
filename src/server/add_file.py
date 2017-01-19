import sys
import os

def add_file(afile, filename='files'):
    """
    Add file to the list of files we want to track
    for changes.

    Currently we are deciding not to add this feature. In our current
    security model, we want the monitoring system to be responsible for
    all aspects the configuartion as we assume that the machine it is 
    monitoring could be compromised.

    There are a couple issues with supporting adding files with this model.
    
    First: The monitoring system has to be the one that initiates the
    add. To do this, it would need to upload a file to the FTP server. We 
    do not want the monitoring server to have this permission as it increases
    the attack vector on the system we are trying to keep secure.
    
    Second: It would be difficult to coordinate between the two servers to
    give the monitoring server information about what files are contained on
    the monitored server. 

    It would look something like this:

    1. Monitoring server uploads a file containing the name of the file it 
    wants to upload.
    2. Upon recieving, the monitored server checks to make sure that file exists.
    The filename would either have to be the absolute path, or we would have to 
    figure out a way to determine which file the monitoring server intended.

    3. After verifying its existance, the monitored server would add the file
    to the files file and then copy the file to the current directory.

    4. The monitoring folder would have to poll a state variable to check to 
    see when the file has been copied over.

    5. After the copy is made and the state variable is set, the monitoring folder
    can then pull the data, make the checksum, and store in the local database.

    NOTE: State variables may still need to be set to prevent the monitoring server
    from trying to download until the file is copied.

    NOTE: To add add functionality, it may be better to use HTTPS, as back and
    forth handshare exchange is built into the protocol.

    Third: As noted above: How can we distinguish between two files with same filename 
    unless absolute path is given?

    Fourth: When we generate initial checksums, we are assuming that the machine's 
    integrity is intact. But in the future, we only know that the files we are 
    monitoring have not been compromised. The newly added files could have been
    altered and the monitored server could just be sending the compromised file.
    This provides a false sense of security about the newly monitored files that
    we want to avoid.
    """
    
    with open(filename, 'a') as f:
        f.write(afile)

if __name__ == '__main__':
    if(len(sys.argv) == 2):
        add_file(sys.argv[1])
