import socket
import random
import sys

# when running the script, specify the host and port as well -> python udp_client.py localhost 12345
def main():
  if len(sys.argv) < 3:
    print('not enough args')
  else:
    (HOST, PORT) = sys.argv[1:3]
    PORT = int(PORT)
    # AF_INET -> IPv4; UDP -> SOCK_DGRAM
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
      while True:
        data = input("Please enter the message:\n")
        client_socket.sendto(data.encode('utf-8'), (HOST, PORT))
        message, address = client_socket.recvfrom(1024)
        print(message)


if __name__ == '__main__':
  main()