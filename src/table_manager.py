
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
    """

    def __init__(self):
        pass
