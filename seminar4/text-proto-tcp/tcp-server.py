import socket
import threading

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 12345  # Port to listen on (non-privileged ports are > 1023)

is_running = True

BUFFER_SIZE = 8

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
  items = data.split(' ')
  command, key = items[1:3]
  resource = ''
  if len(items) > 3:
    resource = ' '.join(items[3:])
  
  payload = 'command not recognized, doing nothing'

  if command == 'add':
    state.add(key, resource)
    payload = f'{key} added'
  elif command == 'remove':
    state.remove(key)
    payload = f'{key} removed'
  elif command == 'get':
    payload = state.get(key)
    if not payload:
      payload = 'key was not found'
  
  payload_length = len(payload)
  message_length = len(str(payload_length)) + 1 + payload_length

  return f'{message_length} {payload}'

def handle_client(client):
  with client:
    while True:
      if client == None:
        break
      data = client.recv(BUFFER_SIZE)
      if not data:
          break
      string_data = data.decode('utf-8')
      full_data = string_data
      message_length = int(string_data.split(' ')[0])
      remaining = message_length - len(string_data)
      while remaining > 0:
        data = client.recv(BUFFER_SIZE)
        string_data = data.decode('utf-8')
        full_data += string_data
        remaining -= len(string_data)
      
      response = process_command(full_data)
        
      client.sendall(response.encode('utf-8'))

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