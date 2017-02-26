#!/usr/bin/python
import keyring as kr

MSQL = 1
FTP  = 2

class KeyManager:
    @staticmethod
    def store_password(service = None, username = None, password = None):
        return kr.set_password(str(service), username, password)
    @staticmethod
    def get_password(service = None, username = None):
        return kr.get_password(str(service), username)
    @staticmethod
    def is_correct_password(password = None, service = None, username = None):
        return kr.get_password(str(service), username) == password
