#!/usr/bin/python
import keyring as kr
from enum import Enum

class Service(Enum):
    MSQL = 1
    FTP  = 2

class KeyManager:

    def store_password(self, service = None, username = None, password = None):
        return kr.set_password(str(service), username, password)

    def get_password(self, Service = None, username = None):
        return kr.get_password(str(service), username)

    def is_correct_password(self, password = None, service = None, username = None):
        return kr.get_password(str(service), username) == password
