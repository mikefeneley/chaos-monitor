from daemon import runner
import sqlite3

class Monitor:
    def __init__(self):
        self.connect_db()



    def connect_db(self):
    	conn = sqlite3.connect('example.db')

    def monitor(self):
        pass

if __name__ == '__main__':
    monitor = Monitor()
    monitor.monitor()