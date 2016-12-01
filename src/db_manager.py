import sqlite3
import sys
import hashlib
import os

class DB_Manager:
    def __init__(self):
        self.connect_db()

    def connect_db(self):
        """
        Connect to the database containing the filename/checksum pairs of all
        files we want to track.
        """
        self.conn = sqlite3.connect('checksum_db')
        self.c = self.conn.cursor()
        tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='CHECKSUM_TABLE'"
        result = self.conn.execute(tb_exists).fetchone()
        if result == None:
            tb_create = '''CREATE TABLE CHECKSUM_TABLE (FILE text, CHECKSUM text)'''
            self.conn.execute(tb_create)
        self.conn.commit()

    def calculate_hash(self, filename):
        """
        Calculate and return the md5 hash of the file named filename.

        :param filename: filename we want the checksum of
        :type conf_filename: string
        :returns: string -- md5 hash of file filename
        """
        hash_md5 = hashlib.md5()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


    def add_file(self, filename):
        """
        Add the checksum/file pair of file with name filename to the database.

        :param filename: filename of the file we want to add
        :type filename: string
        :returns: bool -- True if added. False otherwise
        """

        # Add check for file existance.

        hex_hash = self.calculate_hash(filename)
        abspath = self.get_abspath(filename)

        if abspath != None:
            self.db_manager.add_hash_pair(abspath, hex_hash)
            self.db_manager.print_db()


    def get_abspath(self, filename):
        """
        Returns the absolute path of filename

        :param filename: filename of the file whose path we want to find
        :returns: string -- Absolute path if succssful. None otherwise
        """

        if os.path.exists(filename):
            return os.path.abspath(filename)
        else:
            return  None



    def add_hash_pair(self, filename, hex_hash):
        """
        Adds filename/hex_hash as a hash pair to the checksum table.

        NOTE DON"T ALLOW DUPLICATES
    
        :param filename: filename we want the checksum of
        :type filename: string
        :returns: string -- md5 hash of file filename
        """
        add = "INSERT INTO CHECKSUM_TABLE VALUES ('?', '?')"
        hash_pair = [(filename, hex_hash)]
        self.conn.executemany("INSERT INTO CHECKSUM_TABLE VALUES (?, ?)", hash_pair)
        self.conn.commit()
        return True

    def remove_hash_pait(self, filename):
        """
        Remove the file with file filename if it is contained in the checksum db.
        
        :param filename: filename of the file we want to delete
        :type filename: string
        :returns: bool -- True if deleted. False otherwise
        """
        abspath = self.get_abspath(filename)
        delete = "DELETE FROM CHECKSUM_TABLE where FILE=?"
        self.conn.executemany(delete, [(abspath,)])
        self.conn.commit()
        return True

    def print_db(self):
        """
        Print all the filename/checksum pairs in the database.
        """
        select_all = "SELECT * FROM CHECKSUM_TABLE"
        result = self.conn.execute(select_all)
        print(result.fetchall())

    def get_hash_pairs(self):
    	"""
        Returns all filename/checksum pairs stored in the database in a list.

        :returns: bool -- List of all checksum pairs. None if none contained
        """
        select_stmt = "SELECT * FROM CHECKSUM_TABLE"
        result = self.conn.execute(select_stmt)
        checksum_pairs = result.fetchall()
        print(checksum_pairs)
        return checksum_pairs

if __name__ == '__main__':
	
    manager = DB_Manager()
    print("Start")
    if(len(sys.argv) < 3):
        sys.exit()

    cmd = sys.argv[1]
    val = sys.argv[2]

    if(cmd == 'add'):
        manager.add_file(val)
    