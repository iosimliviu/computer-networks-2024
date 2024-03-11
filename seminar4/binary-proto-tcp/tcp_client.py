import socket
import pickle
import io

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3333  # The port used by the server
BUFFER_SIZE = 8
 

class Response:
    def __init__(self, payload):
        self.payload = payload

class Request:
    def __init__(self, command, key, resource = None):
        self.command = command
        self.key = key
        self.resource = resource


def get_command(command):
    c = command.strip()
    
    items = c.split(' ')
    request = Request(items[0], items[1], ' '.join(items[2:]))

    stream = io.BytesIO()
    pickle.dump(request, stream)
    serialized_payload = stream.getvalue()
    payload_length = len(serialized_payload) + 1

    return payload_length.to_bytes(1, byteorder='big') + serialized_payload
   

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    command = ''
    while command.strip() != 'exit':
        command = input('connected>')
        s.sendall(get_command(command))
        data = s.recv(BUFFER_SIZE)
        if not data:
            break
        full_data = data
        message_length = data[0]
        remaining = message_length - len(data)
        while remaining > 0:
            data = s.recv(BUFFER_SIZE)
            full_data += data
            remaining -= len(data)
        
        stream = io.BytesIO(full_data[1:])
        response = pickle.load(stream)
        print(response.payload)