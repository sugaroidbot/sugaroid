#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import socketserver
import threading

class announce():
    """ Return message uppercase """
    def __init__(self):
        """ Start the tcp server """
        host = "localhost"
        port = 4455
        new_thread = TCPserver(self, host, port)
        #new_thread = TCPserver(self, "localhost", 2000)
        new_thread.start()
        print("started tcp listener")
    def uppercase(message):
        print (message.upper())

class TCPserver(threading.Thread):
    def __init__(self, announce, host, port):
        threading.Thread.__init__(self)
        self.announce = announce
        self.host = host
        self.port = port
    def run(self):
        server = ThreadedTCPServer((self.host, self.port), ThreadedTCPRequestHandler)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            server.shutdown()
            server.server_close()

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """ Echo data back in uppercase """
    def handle(self):
        self.announce = announce
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        if data is not None:
            self.announce.uppercase(data.decode("utf-8") + "/n")
            self.request.send(bytes("message recieved from {0}".format(cur_thread.name), 'utf-8'))
        self.request.close()

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)

def main():
    announce()

if __name__ == "__main__":
    main()
