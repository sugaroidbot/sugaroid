#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import select
import threading
import sys
import time
import datetime


class announce():
    """ Return message uppercase """
    def __init__(self):
        """Start the tcp server in a new thread"""
        host = "localhost"
        port = 8888
        try:
            self.new_thread = TCPserver(self, host, port)
            self.new_thread.start()
            print("started tcp listener")
            self.second_thread = Periodic(self)
            self.second_thread.daemon = True
            self.second_thread.start()
        finally:
            self.new_thread.signal = False
            time.sleep(1)
            self.second_thread.signal = False
            time.sleep(1)
            self.new_thread.join()
            self.second_thread.join()
        print("testing 123")
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
        self.signal = True

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self._socket.settimeout(None)
        self._socket.setblocking(0)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)

        self.kq = select.kqueue()

        self.kevent = [
                   select.kevent(self._socket.fileno(),
                   filter=select.KQ_FILTER_READ,
                   flags=select.KQ_EV_ADD | select.KQ_EV_ENABLE)
        ]

        self.connections = {}

    def run(self):
        try:
            while self.signal:
                events = self.kq.control(self.kevent, 5, None)
                for event in events:
                    if event.ident == self._socket.fileno():
                        conn, addr = self._socket.accept()
                        new_event = [
                                 select.kevent(conn.fileno(),
                                 filter=select.KQ_FILTER_READ,
                                 flags=select.KQ_EV_ADD | select.KQ_EV_ENABLE)
                        ]
                        self.kq.control(new_event, 0, 0)
                        self.connections[conn.fileno()] = conn
                    else:
                        conn = self.connections[event.ident]
                        buf = conn.recv(1024)
                        if not buf:
                            conn.close()
                            continue
                        self.announce.uppercase(buf.decode("utf-8", "replace").strip())
        finally:
            self.kq.control([select.kevent(self._socket.fileno(), filter=select.KQ_FILTER_READ, flags=select.KQ_EV_DELETE)], 0, None)
            self.kq.close()
            self._socket.close()

class Periodic(threading.Thread):
    def __init__(self, announce):
        threading.Thread.__init__(self)
        self.announce = announce
        self.signal = True
        self.starttime=time.time()

    def run(self):
        while self.signal:
            time.sleep(30.0 - ((time.time() - self.starttime) % 30.0))
            self.announce.repeat( str(datetime.datetime.utcnow()) + " 30 seconds")

def main():
    announce()

if __name__ == "__main__":
    main()
