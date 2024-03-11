import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 12345  # The port used by the server
BUFFER_SIZE = 8
 
def get_command(command):
    c = command.strip()
    content_lengh = len(c)
    total_length = content_lengh + len(str(content_lengh)) + 1
    return (str(total_length) + ' ' + c).encode('utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    command = ''
    while command.strip() != 'exit':
        command = input('connected>')
        s.sendall(get_command(command))
        data = s.recv(BUFFER_SIZE)
        if not data:
            break

        string_data = data.decode('utf-8')
        full_data = string_data
        message_length = int(string_data.split(' ')[0])
        remaining = message_length - len(string_data)
        while remaining > 0:
            data = s.recv(BUFFER_SIZE)
            string_data = data.decode('utf-8')
            full_data += string_data
            remaining -= len(string_data)
        print(' '.join(full_data.split(' ')[1:]))