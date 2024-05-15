from jsonrpclib import Server
import sys
def main():
    server = Server('http://localhost:5001')
    try:
        print(server.validEmail("admin@gmail.com"))
        print(server.validZipCode("12345"))
    except:
        print("Error: ", sys.exc_info())
if __name__ == '__main__':
    main()