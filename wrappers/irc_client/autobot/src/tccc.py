#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import socketserver
import threading
import sys
import time
import datetime
#import signal


#signal.signal(signal.SIGINT, signal.SIG_DFL)

class announce():
    """ Return message uppercase """
    def __init__(self):
        """Start the tcp server in a new thread"""
        host = "localhost"
        port = 8888
        try:
            #self.new_thread = TCPserver(self, host, port)
            #self.new_thread.start()
            #print("started tcp listener on {0}:{1}".format(host, port))
            #self.periodic = threading.Timer(10, self.repeat)
            #self.periodic.start()
            self.second_thread = Periodic(self)
            self.second_thread.daemon = True
            self.second_thread.start()
        finally:
            self.second_thread.signal = False
            time.sleep(1)
            #self.periodic.cancel()
            #self.new_thread.join()
            self.second_thread.join()

    def uppercase(self, message):
        print (message.upper())

    def repeat(self, message):
        print(message)

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
        finally:
            server.shutdown()
            server.server_close()

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """ Echo data back in uppercase """
    def handle(self):
        self.announce = announce
        data = self.request.recv(1024)
        if data is not None:
            self.announce.uppercase(self, data.decode("utf-8", "replace").strip())
        self.request.close()

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)

class Periodic(threading.Thread):
    def __init__(self, announce):
        threading.Thread.__init__(self)
        self.announce = announce
        self.signal = True
        self.starttime=time.time()

    def run(self):
        while self.signal:
            time.sleep(5.0 - ((time.time() - self.starttime) % 5.0))
            self.announce.repeat(str(datetime.datetime.utcnow()) + " 5 seconds")

def main():
    announce()

if __name__ == "__main__":
    main()
