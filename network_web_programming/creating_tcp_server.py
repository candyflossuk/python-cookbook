"""
This script hows how to implement a server that communicates with clients
using the TCP internet protocol

An easy way to do this is to create a TCP server using the socketserver library
"""
from socketserver import (
    BaseRequestHandler,
    TCPServer,
    StreamRequestHandler,
    ThreadingTCPServer,
)
from socket import socket, AF_INET, SOCK_STREAM


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print("Got connection from", self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


"""if __name__ == "__main__":
    serv = TCPServer(("", 20000), EchoHandler)
    serv.serve_forever()"""

"""
Usage:

from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))
s.send(b'Hello')
s.recv(8192)


Below an example is shown using the StreamRequestHandler base class
"""


class StreamBasedEchoHandler(StreamRequestHandler):
    def handle(self):
        print("Got connection from", self.client_address)
        # self.rfile is a file-like object for reading
        for line in self.rfile:
            # self.wfile is a file-like object for writing
            self.wfile.write(line)


"""
if __name__ == "__main__":
    serv = TCPServer(("", 20000), StreamBasedEchoHandler)
    serv.serve_forever()

The web servers shown thus far are single threaded.. If you 
want to handle multiple clients, either instantiate a ForkinTCPServer
or ThreadingTCPServer object instead

if __name__ == "__main__":
    serv = ThreadingTCPServer(("", 20000), StreamBasedEchoHandler)
    serv.serve_forever()
    
One issue with this is that there is no upper bound on the processes
spawned from this so someone malicious could overwhelm the server 
with connections quite quickly. To get around this a pre-allocated
pool of worker threads or processes can be given.

if __name__ == '__main__':
    from threading import Thread
    NWORKERS = 16
    serv = TCPServer(('', 20000), EchoHandler)
    for n in range (NWORKERS):
        t = Thread(target=serv.serve_forever)
        t.daemon = True
        t.start()
    serv.serve_forever()
    
The example below shows how to implement a web server using the socket library
"""


def echo_handler(address, client_sock):
    print("Got connection from {}".format(address))
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)
    client_sock.close()


def echo_server(address, backlog=5):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        client_sock, client_addr = sock.accept()
        echo_handler(client_addr, client_sock)


if __name__ == "__main__":
    echo_server(("", 20000))
