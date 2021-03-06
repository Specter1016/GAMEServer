import Config.ServerConfig


import socket
from threading import Thread


class GameServer(Thread):

    def __init__(self, ip, port, i):

        Thread.__init__(self);
        self.ip = ip;
        self.port = port;
        self.geti = i;


    def run(self):

        try:
            while True:
                data = client.recv(2048).decode('utf-8');
                print(f'Show C {self.ip}: data is >> {data}');
                cdata = bytes(f'TEST CONNETED OK  : {self.geti}',encoding='utf-8');
                client.send(cdata);
                break;

        except OSError as A:
            print(f'\n\nERROR : >> {A}');


if __name__ == '__main__':



    bufferbytesize = 20;
    serversoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    serversoket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
    serversoket.bind(('0.0.0.0',int(Config.ServerConfig.serverConfigPort)));
    threads = [];

    print('Server Start >>');
    i = 1;
    while True:

        serversoket.listen(4);
        (client, (cip, cport))= serversoket.accept();
        newclient = GameServer(cip, cport, i);
        i = i+1;
        newclient.start();
        threads.append(newclient)

    for t in threads:
        t.join()
