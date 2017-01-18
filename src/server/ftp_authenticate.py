import os
import sys
from hashlib import md5

from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed

class MyAuthorizer(DummyAuthorizer):

    def validate_authentication(self, username, password, handler):
        print(password)
        if sys.version_info >= (3, 0):
            password = md5(password.encode('latin1'))
        hash = md5(password).hexdigest()
        try:
            if self.user_table[username]['pwd'] != hash:
                raise KeyError
        except KeyError:
            raise AuthenticationFailed
    
    def add(self, user, password):
        hash = md5(password).hexdigest()
        self.add_user(user, hash, os.getcwd(), perm="r")

def main():
    # get a hash digest from a clear-text password
    hash = md5('12345').hexdigest()
    authorizer = DummyMD5Authorizer()
    authorizer.add_user('user', hash, os.getcwd(), perm='elradfmw')
    authorizer.add_anonymous(os.getcwd())
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer(('', 2121), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
