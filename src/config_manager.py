from db_manager import DB_Manager
import sys
import hashlib
import os


class ConfigManager:
    
    def __init__(self):
        pass

    def __del__(self):
        pass

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
        hex_hash = self.calculate_hash(filename)
        abspath = self.get_abspath(filename)

        if abspath != None:
            db_manager = DB_Manager()
            db_manager.add_hash_pair(abspath, hex_hash)
            db_manager.print_db()

    def delete_file(self, filename):
        abspath = self.get_abspath(filename)
        db_manager = DB_Manager()
        db_manager.remove_hash_pair(abspath)
        db_manager.print_db()


if __name__ == '__main__':	
    manager = ConfigManager()
    print("Start")
    if(len(sys.argv) < 3):
        sys.exit()

    cmd = sys.argv[1]
    val = sys.argv[2]

    if(cmd == 'add'):
        manager.add_file(val)
    if(cmd == 'del'):
        manager.delete_file(val)



"""
	def remove_file(self, filename):
		pass

	def remove_all(self):
		pass

	def change_duration(self, duration):
		pass

	def new_remote(self):
		pass
"""