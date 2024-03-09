import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

#enable reusage so we'll be able to run multiple clients and servers on single (host, port).
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

client.bind(("", 5007))

while True:
    data, addr = client.recvfrom(1024)
    print("received message: %s"%data)
    answer = input('\nDo you want to continue(y/n) :')

    if answer == 'y':
                continue
    else:
        break
