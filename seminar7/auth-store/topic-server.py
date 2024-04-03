import socket
import threading

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 3334  # Port to listen on (non-privileged ports are > 1023)
SECRET = 'somesecret'

class Request:
  def __init__(self, command, params):
    self.type = command
    self.params = params

class Response:
  def __init__(self, status, payload):
    self.status = status
    self.payload = payload

def serialize(response):
  return bytes(str(response.status) + ' ' + response.payload, encoding='utf-8')

def deserialize(request):
  items = request.decode('utf-8').strip().split(' ')
  if (len(items) > 1):
    return Request(items[0], items[1:])
  return Request(items[0], None)

class StateMachine:
  def __init__(self, client, global_state):
    self.transitions = {}
    self.start_state = None
    self.end_states = []
    self.current_state = None
    self.global_state = global_state
    self.client = client
  
  def add_transition(self, state_name, command, transition, end_state = 0):
    return

  def set_start(self, name):
    return

  def process_command(self, unpacked_request):
    return


class TopicProtocol(StateMachine):
  def __init__(self, client, global_state):
    super().__init__(client, global_state)

class TopicList:
  def __init__(self):
    self.clients = []
    self.topics = {}
    self.lock = threading.Lock()

is_running = True
global_state = TopicList()

def handle_client_write(client, response):
  client.sendall(serialize(response))

def handle_client_read(client):
  try:
    protocol = TopicProtocol(client, global_state)
    while True:
      if client == None:
        break
      data = client.recv(1024)
      if not data:
        break
      unpacked_request = deserialize(data)
      response = protocol.process_command(unpacked_request)
      handle_client_write(client, response)

  except OSError as e:
    global_state.clients.remove(client)

def accept(server):
  while is_running:
    client, addr = server.accept()
    global_state.add_client(client)
    print(f"{addr} has connected")
    client_read_thread = threading.Thread(target=handle_client_read, args=(client,  ))
    client_read_thread.start()

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