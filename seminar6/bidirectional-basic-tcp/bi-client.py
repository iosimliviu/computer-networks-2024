import socket
import threading

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3333  # The port used by the server

def handle_server_write(s):
    while True:
        data = s.recv(1024)
        print(f"Received {data!r}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    server_write_thread = threading.Thread(target=handle_server_write, args=(s,))
    server_write_thread.start()
    while True:
        line = input('>')
        s.sendall(line.encode())