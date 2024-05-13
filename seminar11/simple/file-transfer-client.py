import socket

HOST = "127.0.0.1"  
PORT = 3333  

# Open a file to write the received data into it. The file is named 'out.jpg'.
with open('out.jpg', 'wb') as f:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        part = s.recv(1024)  # Receive data from the server in chunks of 1024 bytes.
        count = len(part)  # Initialize a counter with the length of the first received chunk.
        bytes_received = len(part)

        # Continuously receive data until no more data is sent from the server.
        while bytes_received > 0:
            count += bytes_received
            f.write(part)  # Write the received part to the file.
            print(f'read {count}')  # Print the current total of bytes received.
            if bytes_received > 0:
                part = s.recv(1024)  # Continue receiving the next chunk of data.
                bytes_received = len(part)  # Update the bytes received with the new chunk's size.
            else:
                break  # Exit the loop if no more data is received.