from time import asctime

class Logger:
	def __init__(self, filename='checksum_log.txt'):
		self.filename = filename
		self.file = open(filename, 'w')

	def incorrect_checksum_errmsg(self, filename, db_checksum, new_checksum):
		self.file.write(asctime() + "\n")
		self.file.write("Checksum does not match\n")
		self.file.write("Filename: " + filename + "\n")
		self.file.write("DataBase Checksum: " + db_checksum + "\n")
		self.file.write("Recalcualted Checksum" + new_checksum + "\n")
		self.file.write("\n\n")