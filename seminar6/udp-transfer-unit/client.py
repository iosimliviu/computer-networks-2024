import socket
import sys

from transfer_units import RequestMessage, RequestMessageType, ResponseMessage, ResponseMessageType
from state import State
from serialization import serialize, deserialize

def main():
  if len(sys.argv) < 3:
    print('not enough args')
  else:
    (HOST, PORT) = sys.argv[1:3]
    PORT = int(PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
      while True:
        data = input("storage>")
        items = data.strip().split(' ', 1)
        command = items[0]
        if command == 'connect':
          client_socket.sendto(serialize(RequestMessage(RequestMessageType.CONNECT)), (HOST, PORT))
        elif command == 'list':
          client_socket.sendto(serialize(RequestMessage(RequestMessageType.LIST)), (HOST, PORT))
        elif command == 'send':
          client_socket.sendto(serialize(RequestMessage(RequestMessageType.SEND, items[1])), (HOST, PORT))
        elif command == 'disconnect':
          client_socket.sendto(serialize(RequestMessage(RequestMessageType.DISCONNECT)), (HOST, PORT))
        else:
          print('unknown command')
          continue
        message, _ = client_socket.recvfrom(1024)
        deserialized_response = deserialize(message)
        print(deserialized_response)



if __name__ == '__main__':
  main()

