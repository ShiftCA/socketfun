#!/usr/bin/env python3
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint

class Server(DatagramProtocol):
    def __init__(self):
        self.clients = set()

    
    def datagramReceived(self,datagram,addr):
        datagram = datagram.decode("utf-8")
        if datagram == "ready":
            addresses = "\n".join([str(x) for x in self.clients])
            self.transport.write(addresses.encode("utf-8"),addr)
            self.clients.add(addr)
while True:
    try:
        reactor.listenUDP(9999, Server())
        reactor.run()
    except:
        print("error, trying again...")