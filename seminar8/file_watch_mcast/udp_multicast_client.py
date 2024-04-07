import socket
import struct

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 4444
DEST_FOLDER = 'temp-receive'

FILE_SERVER = '127.0.0.1'
FILE_PORT = 12345

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # allows multiple sockets to be bound to this same (addr, port) combination at once, i.e. you can run multiple copies of your program at once, or in quick succession
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # socket is bound to a port, listen ONLY to MCAST_GRP
    sock.bind(('', MCAST_PORT))

    mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
    # socket is added to the multicast group by using setsockopt() to change the IP_ADD_MEMBERSHIP option
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        data, address = sock.recvfrom(1024)
        filename = data.decode()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((FILE_SERVER, FILE_PORT))
            s.sendall(filename.encode('utf-8'))
            data = s.recv(1024)
            print(data)
            with open(DEST_FOLDER + '\\' + filename, 'wb') as f:
                f.write(data)

if __name__ == '__main__':
    main()