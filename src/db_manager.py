import sqlite3
import sys
import hashlib
import os

class DB_Manager:
    def __init__(self):
        self.connect_db()
        self.recipient_table = None
        self.checksum_table = None
    
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

    def remove_hash_pair(self, filename):
        """
        Remove the file with file filename if it is contained in the checksum db.
        
        :param filename: filename of the file we want to delete
        :type filename: string
        :returns: bool -- True if deleted. False otherwise
        """
        delete = "DELETE FROM CHECKSUM_TABLE where FILE=?"
        self.conn.executemany(delete, [(filename,)])
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
   
