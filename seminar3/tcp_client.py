import socket

def main():
    host = "127.0.0.1"
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))

    message = "hello world"

    while True:
        s.send(message.encode('utf-8'))
        data = s.recv(1024)
        print('Received from the server: ', str(data.decode('utf-8')))
		
        answer = input('\nDo you want to continue(y/n) :')

        if answer == 'y':
                    continue
        else:
            break
	# close the connection
    s.close

if __name__ == '__main__':
      main()