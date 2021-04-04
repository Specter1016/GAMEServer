import socket
from threading import Thread
import Config.ServerConfig

class GameServerMultiPlayer(Thread):

    serverPort ="";
    serverDBIP="";
    serverDBPort="";

    print(f'server Port : {serverPort}');

    def __init__(self,serverPort, serverDBIP):

        self.serverPort=serverPort;
        self.serverDBIP=serverDBIP;




    def run(self):

        while True:
            data = c.recv(2048)
            print("Server received data:", data);
            MESSAGE = bytes("ok connected ".encode('utf-8'));
            if MESSAGE == 'exit':
                break
            c.send(MESSAGE)  # echo


TCP_IP = '0.0.0.0'
TCP_PORT = int(Config.ServerConfig.serverConfigPort);
BUFFER_SIZE = 20  # Usually 1024, but we need quick response

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
tcpServer.bind((TCP_IP, TCP_PORT));
threads = [];



while True:
    tcpServer.listen(4)
    print("Multithreaded Python server : Waiting for connections from TCP clients...");
    (c, (ip, port)) = tcpServer.accept()
    newthread = GameServerMultiPlayer(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()

