import socket
import threading

# Defines the IP address and port on which the server will run. 
# HOST is set to the local machine, and PORT is set to 3333.
HOST = "127.0.0.1"  
PORT = 3333  

is_running = True  # A flag to keep the server running within a loop.

def handle_client(client, data):
    try:
        # Send data to the connected client and then close the connection.
        client.sendall(data)
        client.close()
    except IOError as e:
        print(e)

def accept(server, data):
    while is_running:
        client, addr = server.accept()  # Accept a new client connection.
        print(f"{addr} has connected")
        client_thread = threading.Thread(target=handle_client, args=(client, data, ))
        client_thread.start()

def main():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with open('frog.jpeg', 'rb') as f:
            # Read the binary data from the image file to be sent.
            data = f.read()
        print('total: ', len(data))  # Print the size of the data.
        server.bind((HOST, PORT))
        server.listen()
        # Start a separate thread to accept connections, which allows the main program to perform other tasks.
        accept_thread = threading.Thread(target=accept, args=(server, data, ))
        accept_thread.start()
        accept_thread.join()  # Wait for the accept thread to finish before exiting.
    except BaseException as err:
        print(err)
    finally:
        if server:
            server.close()

if __name__ == '__main__':
    main()