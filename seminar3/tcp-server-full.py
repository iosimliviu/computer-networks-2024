import socket
import threading

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 12345  # Port to listen on (non-privileged ports are > 1023)

is_running = True

def handle_client(client):
  with client:
    while True:
      if client == None:
        break
      host, port = client.getpeername()
      data = client.recv(1024)
      print(f'host {host}, port {port} sent: {data}')
      if not data:
          print(f'bye {host}, port {port}')
          break
      client.sendall(data.capitalize())

def accept(server):
  while is_running:
    client, addr = server.accept()
    print(f"{addr} has connected")
    client_thread = threading.Thread(target=handle_client, args=(client,))
    client_thread.start()

def main():
  try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    accept_thread = threading.Thread(target=accept, args=(server,))
    accept_thread.start()
    accept_thread.join()
  except BaseException as err:
    print(err)
  finally:
    if server:
      server.close()

if __name__ == '__main__':
  main()