import os 

from pyftpdlib.authorizers import DummyAuthorizer  # Import DummyAuthorizer for managing FTP user accounts
from pyftpdlib.handlers import FTPHandler  # Import FTPHandler to handle FTP server events
from pyftpdlib.servers import FTPServer  # Import FTPServer to create and manage the FTP server

def main():    
    authorizer = DummyAuthorizer() # instantiate a dummy authorizer for managing 'virtual' users

    authorizer.add_user('user', '12345', 'server_storage', perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())  # Allow anonymous access with read-only permissions to the current working directory
    
    handler = FTPHandler # instantiate FTP handler class
    handler.authorizer = authorizer  # Assign the authorizer to the handler to manage user authentication

    handler.banner = "pyftpdlib based ftpd ready."  # Set a custom banner that is shown when clients connect to the server

    address = ('', 2121)  # Define the address and port where the server will listen
    server = FTPServer(address, handler)  # Create the FTP server with the specified address and handler

    server.max_cons = 256  # Set the maximum number of connections the server can handle at once
    server.max_cons_per_ip = 5  # Set the maximum number of connections from a single IP address

    server.serve_forever()  # Start the server and keep it running indefinitely

if __name__ == '__main__':
    main()
