

class SQLValidator:

    """
    Class responsible for checking all program inputs for 
    sql injection attacks
    """

    @staticmethod 
    def valid_input(user_input):
        """
        Return true if user_input is a valid input to a SQL command.

        Note:
            At the current time, the only inputs to this function are going
            to be filenames and user emails. The simplest solution might be to
            just ban bad characters like quotes. Not sure if quotes are valid
            in filenames, but even if they are technically allowed, it is bad
            practice. Not supporting them would discourage their use and promote
            best practices. Whoever implements this function needs to reserach
            SQL injections and cover the entire range of possible attacks. ALso,
            decide if a static method is the best design choice. Possibly just provide
            a function. Consider changing name to input_validator and have it perform
            email validation too.

        :param user_input: Input that needs to be checked for malicious formating.
        :type user_input: String
        :return: bool -- True if the input is properly formated. False otherwise.
        """
