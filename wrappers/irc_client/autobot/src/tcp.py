
# -*- coding: utf-8 -*-

import socketserver
import threading
import time
import datetime
import signal


signal.signal(signal.SIGINT, signal.SIG_DFL)

class announce():
    """ Return message uppercase """
    def __init__(self):
        """ Start the tcp server """
        host = "localhost"
        port = 4455
        new_thread = TCPserver(self, host, port)
        new_thread.start()
        second_thread = Periodic(self)
        second_thread.start()
        print("started tcp listener on {0}:{1}".format(host, port))
    def uppercase(message):
        print(message.upper())
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
        cur_thread = threading.current_thread()
        if data is not None:
            self.announce.uppercase(data.decode("utf-8", "replace").strip())
            self.request.send(bytes("message recieved from {0}".format(cur_thread.name), 'utf-8'))
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
        self.starttime=time.time()

    def run(self):
        while True:
            self.announce.repeat(str(datetime.datetime.utcnow()) + " 10 seconds")
            time.sleep(10.0 - ((time.time() - self.starttime) % 10.0))

def main():
    announce()

if __name__ == "__main__":
    main()
