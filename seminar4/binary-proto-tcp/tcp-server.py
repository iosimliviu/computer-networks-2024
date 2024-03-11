import socket
import threading
import collections
import pickle
import io

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 3333  # Port to listen on (non-privileged ports are > 1023)

is_running = True
BUFFER_SIZE = 8

class Response:
    def __init__(self, payload):
        self.payload = payload

class Request:
    def __init__(self, command, key, resource = None):
        self.command = command
        self.key = key
        self.resource = resource

class State:
  def __init__(self):
    self.resources = {}
    self.lock = threading.Lock()
  def add(self, key, resource):
    self.lock.acquire()
    self.resources[key] = resource
    self.lock.release()
  def remove(self, key):
    self.lock.acquire()
    self.resources.pop(key, None)
    self.lock.release()
  def get(self, key):
    if key in self.resources:
      return self.resources[key]
    else:
      return None

state = State()

def process_command(data):
  payload = data[1:]
  stream = io.BytesIO(payload)
  request = pickle.load(stream)
  payload = 'command not recognized, doing nothing'

  if request.command == 'add':
    state.add(request.key, request.resource)
    payload = f'{request.key} added'
  elif request.command == 'remove':
    state.remove(request.key)
    payload = f'{request.key} removed'
  elif request.command == 'get':
    payload = state.get(request.key)
    if not payload:
      payload = 'key was not found'
  
  stream = io.BytesIO()
  pickle.dump(Response(payload), stream)
  serialized_payload = stream.getvalue()
  payload_length = len(serialized_payload) + 1
  return payload_length.to_bytes(1, byteorder='big') + serialized_payload

def handle_client(client):
  with client:
    while True:
      if client == None:
        break
      data = client.recv(BUFFER_SIZE)
      if not data:
        break
      binary_data = data
      full_data = binary_data
      message_length = binary_data[0]
      remaining = message_length - BUFFER_SIZE
      while remaining > 0:
        data = client.recv(BUFFER_SIZE)
        binary_data = data  
        full_data = full_data + binary_data
        remaining = remaining - len(binary_data)
      response = process_command(full_data)
      client.sendall(response)

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