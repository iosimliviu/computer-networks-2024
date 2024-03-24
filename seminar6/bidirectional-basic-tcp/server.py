import socket
import threading

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 3333  # Port to listen on (non-privileged ports are > 1023)

is_running = True

class ClientList:
  def __init__(self):
    self.clients = []
    self.lock = threading.Lock()
    
  def add_client(self, client):
    with self.lock:
      self.clients.append(client)
      
  def remove_client(self, client):
    with self.lock:
      self.clients.remove(client) 

clients = ClientList()

def handle_client_write(clients, client, data):
	for c in clients.clients:
		if c != client:
			c.sendall(data)

def handle_client(clients, client, callback = handle_client_write):
	try:
		with client:
			while True:
				if client == None:
					break
				data = client.recv(1024)
				if not data:
						break
				callback(clients, client, data)
                    
	except OSError as e:
		clients.remove_client(client)

def accept(server):
  while is_running:
    client, addr = server.accept()
    clients.add_client(client)
    print(f"{addr} has connected")
    client_thread = threading.Thread(target=handle_client, args=(clients, client, handle_client_write))
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