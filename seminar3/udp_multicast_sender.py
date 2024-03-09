import socket

MCAST_GRP = '224.1.1.1'
BCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# option that applies to the IP layer, setting multicast time to live to 32 hops
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
sock.sendto(b'Hello, World!', (MCAST_GRP, BCAST_PORT))