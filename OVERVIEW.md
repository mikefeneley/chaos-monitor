**File and Directory Explanation**

/src -- Directory contains all source code 

/tests -- Directory containing all test code

/docs -- Directory containing generated project documentation

/src/checksum_calcultor.py -- Responsible for returning the checksum values from file names.

/src/checksum_manager.py -- Provides interface for managing the checksum_tuple table in database.

/src/checksum_tuple.py -- Encapsulates file and checksum data.

/src/db_connector.py -- Provides an interface for program database.

/src/logger.py -- Provides an interface for logging errors

/src/monitor.py -- Daemon that performs integrity checks and notifications

/src/monitor_cli.py -- Entry function for the program. Used to control databases and the monitor daemon.

/src/notification.py -- Provides means to send email notifications

/src/recipient_manager.py -- Interface for managing the recipient table in database.

/src/sql_validator.py -- Provides input validation and checking for sql injection attempts.

/src/table_manager.py -- Abstract class that provides shared interface for managing database tables.
