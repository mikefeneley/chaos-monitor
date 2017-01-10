from abc import ABCMeta
from abc import abstractmethod
from db_connector import DBConnector
from logger import Logger
class TableManager:

    """
    Abstract class that defines interface for table managers. Extended
    by RecipientManager and ChecksumManager to manager their respecive
    data sets. Exists, Delete, and Functionality can be defined here as it
    is independent from schema. 

    Note: Consider method to generate database schema from file or some
    text format. Then add, delete, can be implemented here instead of 
    in extension.

    Even though add and delete are data dependent, their definitions can
    be put here as abstract methods, requrigin implementation and creating
    shared interface.
    
    Currently uses template design pattern where the basic functionality that
    does not need specific table knowledge is implemented in the abstract
    class while the specifics are left to the extended class.

    Note: Read more about design patterns and reevalute this choice. A delegation
    option might be more effective. A non abstract table manager class that 
    implements the shared functionality that passes responsibility of specific
    implementaion to the specific table managers? What is the affect on 
    cohesion and abstraction? 
    """

    __metaclass__ = ABCMeta

    def __init__(self, table_name, db_connector):
        self._table_name = table_name
        self.db_connector = db_connector
        self.logger = Logger()

    def table_exists(self):
        """
        Checks if the table with the table named passed to the recipient
        manager exists.

        :return: bool -- True if the table exists. False otherwise.
        """
        try:
            cursor = self.connection.cursor()
            sql = "SHOW TABLES LIKE '%s'" % self.table_name
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return True
            else:
                return False
        except Exception as err:
            self.logger.log_generic_message(err)
            return False

    def delete_table(self):
        """
        Deletes the database table containing all recipient information.

        :return: bool -- True if the table is deleted or does not exist.
                         False otherwise
        """
        try:
            cursor = self.connection.cursor()
            sql = "DROP TABLE IF EXISTS %s" % self.table_name
            cursor.execute(sql)
            self.logger.log_generic_message(
                "Table deleted: {}".format(self.table_name))
            return True
        except Exception as err:
            self.logger.log_generic_message(err)
            return False

    @abstractmethod
    def create_table(self):
        pass
 
    @abstractmethod
    def add_element(self, element):
        pass

    @abstractmethod
    def remove_element(self, key):
        pass
    
    @abstractmethod
    def get_elements(self):
        pass
    @abstractmethod
    def print_table(self):
        pass

