import socket
import threading

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3333  # The port used by the server

LOCAL_STORAGE = '.\\client-temp'
BUFFER_SIZE = 1024

def active_get(command_socket, command):
	# implement
	return 0

def active_put(command_socket, command):
	# implement
	return 0

def passive_get(command_socket, command):
		# implement
	return 0

def passive_put(command_socket, command):
		# implement
	return 0

def process_command(command_socket, command):
	command_items = command.strip().split(' ')
	if command_items[0] == 'active_get':
		temp_server_thread = threading.Thread(target=active_get, args=(command_socket, command))
		temp_server_thread.start()
		temp_server_thread.join()
	elif command_items[0] == 'active_put':
		temp_server_thread = threading.Thread(target=active_put, args=(command_socket, command))
		temp_server_thread.start()
		temp_server_thread.join()
	elif command_items[0] == 'passive_put':
		temp_client_thread = threading.Thread(target=passive_put, args=(command_socket, command))
		temp_client_thread.start()
		temp_client_thread.join()
	elif command_items[0] == 'passive_get':
		temp_client_thread = threading.Thread(target=passive_get, args=(command_socket, command))
		temp_client_thread.start()
		temp_client_thread.join()	

def main():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as command_socket:
		command_socket.connect((HOST, PORT))
		while True:
			command = input('->')
			process_command(command_socket, command)

if __name__ == '__main__':
		main()