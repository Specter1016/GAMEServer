import socket
import time

HOST = '150.95.30.192'  # The server's hostname or IP address
PORT = 1542        # The port used by the server

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    print('Received', repr(data))
    #time.sleep(0.16)