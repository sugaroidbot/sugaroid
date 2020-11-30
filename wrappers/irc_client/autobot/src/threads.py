#!/usr/bin/env python

"""
An echo server that uses threads to handle multiple clients at a time.
Entering any line of input at the terminal will exit the server.
"""

import select 
import socket 
import sys 
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None
        self.threads = []

    def open_socket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            self.server.bind((self.host, self.port))
            self.server.listen(5)
            self.server.setblocking(False)
            self.server.settimeout(None)

            #for bsd
            self.kq = select.kqueue()
            self.kevent = [
                       select.kevent(self.server.fileno(),
                       filter=select.KQ_FILTER_READ,
                       flags=select.KQ_EV_ADD | select.KQ_EV_ENABLE)
            ]

            #for linux
            #self.epoll = select.epoll()
            #self.epoll.register(self.server.fileno(), select.EPOLLIN)

        except socket.error, (value,message):
            if self.server:
                self.server.close()
            print "Could not open socket: " + message
            sys.exit(1)

    def run(self):
        self.open_socket()
        input = [self.server,sys.stdin]
        running = 1
        while running:
            inputready,outputready,exceptready = select.select(input,[],[])
            for s in inputready:
                if s == self.server:
                    # handle the server socket
                    c = Client(self.server.accept())
                    c.start()
                    self.threads.append(c)
                elif s == sys.stdin:
                    # handle standard input
                    junk = sys.stdin.readline()
                    running = 0
        # close all threads
        self.server.close()
        for c in self.threads:
            c.join()

class Client(threading.Thread): 
    def __init__(self,(client,address)): 
        threading.Thread.__init__(self) 
        self.client = client

    def run(self):
        running = 1
        while running:
            data = self.client.recv(1024)
            if data:
                self.client.send(data)
            else: 
                self.client.close()
                running = 0

if __name__ == "__main__": 
    s = Server("localhost", 50000) 
    s.run()
