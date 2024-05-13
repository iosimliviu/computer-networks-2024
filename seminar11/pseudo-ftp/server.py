import socket
import threading

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 3333  # Port to listen on (non-privileged ports are > 1023)

FILE_ROOT = '.\\temp'
BUFFER_SIZE = 1024
is_running = True

def process_command(client, request):
	command_items = request.decode('utf-8').strip().split(' ')
	command_mappings = {
		'active_get': active_get,
		'active_put': active_put,
		'passive_get': passive_get,
		'passive_put': passive_put
	}
	if len(command_items) > 0:
		if command_items[0] in command_mappings:
			response = command_mappings[command_items[0]](client, command_items)
		else:
			print(command_items)

def active_get(client, command_items):
	# implement
	return 0

def active_put(client, command_items):
	# implement
	return 0

def passive_put(client, command_items):
	# implement
	return 0

def passive_get(client, command_items):
	# implement
	return 0

def handle_client_commands(client):
	with client:
		while True:
			if client == None:
				break
			request = client.recv(1024)
			if request:
				process_command(client, request)

def accept(server):
	while is_running:
		client, addr = server.accept()
		print(f"{addr} has connected")
		command_thread = threading.Thread(target=handle_client_commands, args=(client, ))
		command_thread.start()

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