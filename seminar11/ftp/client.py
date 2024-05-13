from ftplib import FTP

def main(): 
    ftp = FTP()
    ftp.connect('localhost', 2121)  # Connect to the FTP server at localhost on port 2121
    ftp.login(user="user", passwd="12345")  # Login to the FTP server with username 'user' and password '12345'

    ftp.retrlines("LIST")  # Retrieve and print the list of files in the current directory on the server

    # upload a file
    with open("user_storage\\user_file.txt", "rb") as f:  # Open a file from local storage in binary read mode
        f.seek(0)  # Move the file pointer to the start of the file
        ftp.storbinary("STOR user_file.txt", f)  # Upload the file to the server

    # download a file
    with open("user_storage\\server_file.txt", "wb") as f:  # Open a file in local storage in binary write mode
        f.seek(0)  # Move the file pointer to the start of the file
        ftp.retrbinary("RETR server_file.txt", f.write)  # Download the file from the server and write it locally

    ftp.quit()  # Disconnect from the FTP server

if __name__ == '__main__':
  main()
