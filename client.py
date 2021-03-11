#!/usr/bin/env python3
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint

class Client(DatagramProtocol):
    def __init__(self,host,port):
        if host == 'localhost':
            host = "127.0.0.1"

        self.id = host,port
        self.address = None
        self.server = "127.0.0.1", 9999
        print("Working on id:", self.id)

    def startProtocol(self):
        self.transport.write("ready".encode("utf-8"), self.server)

    def datagramReceived(self,datagram,addr):
        print('here')
        datagram = datagram.decode("utf-8")
        if addr == self.server:
            print("Choose a client\n", datagram)
            addresses = datagram.split("\n")
            self.address = input("Write address: "), int(input("Write port: "))
            reactor.callInThread(self.send_message)
        else:
            print(addr, ":",datagram)
    
    def send_message(self):
        while True:
            self.transport.write(input("Enter a message:").encode("utf-8"),self.address)
            
port = randint(1000, 5000)
while True:
    try:
        
        reactor.listenUDP(randint(1000,5000), Client("localhost",port))
        reactor.run()
    except:
        print("client-side error, retrying")