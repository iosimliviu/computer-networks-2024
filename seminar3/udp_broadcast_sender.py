import socket

BCAST_ADDR = '255.255.255.255'
BCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# enable broadcasting mode
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.sendto(b'Hello, World!', (BCAST_ADDR, BCAST_PORT))