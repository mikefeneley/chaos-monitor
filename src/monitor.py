from daemon import runner
import sqlite3
import hashlib

class Monitor:
    def __init__(self):
        self.connect_db()
        self.add_file('other.py')

    def __del__(self):
    	self.conn.close()


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

        :param filename: filename we want the checksum of
        :type filename: string
        :returns: string -- md5 hash of file filename
        """
        add = "INSERT INTO CHECKSUM_TABLE VALUES ('?', '?')"
        hash_pair = [(filename, hex_hash)]
        self.conn.executemany("INSERT INTO CHECKSUM_TABLE VALUES (?, ?)", hash_pair)
        self.conn.commit()
        return True

    def print_db(self):
        """
        Print all the filename/checksum pairs in the database.
        """
        select_all = "SELECT * FROM CHECKSUM_TABLE"
        result = self.conn.execute(select_all)
        print(result.fetchall())

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
        :returns: string -- True if added succesfuly, False otherwise
        """
        hex_hash = self.calculate_hash(filename)
        self.add_hash_pair(filename, hex_hash)
        self.print_db()




    def monitor(self):
        pass

if __name__ == '__main__':
    monitor = Monitor()
    monitor.monitor()