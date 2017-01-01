"""
import smtpd
import asyncore

# Start up a server to run tests.
server = smtpd.DebuggingServer(('localhost', 587), None)
asyncore.loop()
"""
