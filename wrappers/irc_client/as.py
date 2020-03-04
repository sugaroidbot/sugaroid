#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio


class announce():
    """ Return message uppercase """
    def __init__(self):
        """ Start the tcp server """
        host = "localhost"
        port = 2000
        loop = asyncio.get_event_loop()
        coro = asyncio.start_server(self.TCPRequestHandler, host, port, loop=loop)
        server = loop.run_until_complete(coro)
        try:
            print("started tcp listener")
            loop.run_forever()
        except KeyboardInterrupt:
            pass
        #except:
        #    print("Exception, asking sever to terminate")
        #    server.close()
        print("waiting on wait_closed()")
        loop.run_until_complete(server.wait_closed())
        print("waited on wait_closed()")
        loop.close()

    @asyncio.coroutine
    def TCPRequestHandler(self, reader, writer):
        data = yield from reader.read(100)
        message = data.decode("utf-8")
        addr = writer.get_extra_info('peername')
        self.msg("Received {0} from {1}".format(message,addr))
        writer.write(data.upper())
        yield from writer.drain()
        writer.close()

    def msg(self, message):
        print (message)

def main():
    announce()

if __name__ == "__main__":
    main()
