"""
This script shows how to communicate with clients over UDP

To do so the socketserver library can be used
"""
from socketserver import BaseRequestHandler, UDPServer, ThreadingUDPServer
import time


class TimeHandler(BaseRequestHandler):
    def handle(self) -> None:
        print("Got connection from", self.client_address)

        # Get message and client socket
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode("ascii"), self.client_address)


"""
if __name__ == "__main__":
    serv = UDPServer(("", 20000), TimeHandler)
    serv.serve_forever()


A typical UDP server receives an incoming datagram (message) + client address.
If the server responds it sends a datagram back  - for this sendto() and
recvfrom() should be used. """

# Create a ThreadingUDPServer
if __name__ == "__main__":
    serv = ThreadingUDPServer(("", 20000), TimeHandler)
    serv.serve_forever()
