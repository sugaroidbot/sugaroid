#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import socketserver
from threading import Thread


class announce():
    """ Return message uppercase """
    def uppercase(message):
        print (message.upper())

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """ Echo data back in uppercase """
    def handle(self):
        self.announce = announce
        data = str(self.request.recv(1024), 'utf-8')
        if data is not None:
            self.announce.uppercase(data)
            self.request.send(bytes("message recieved", 'utf-8'))
        self.request.close()

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 2000
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()