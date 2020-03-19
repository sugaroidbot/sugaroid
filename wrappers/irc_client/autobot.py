#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A full featured python IRC bot"""

import configparser
import ssl
import time
import datetime
import re
import sys
import codecs
import irc.bot
import threading
import socketserver
import signal
from jaraco.stream import buffer
from plugins.event import url_announce, LogFile
from plugins.command import search, FactInfo, dice

from sugaroid.sugaroid import Sugaroid

signal.signal(signal.SIGINT, signal.SIG_DFL)
irc.client.ServerConnection.buffer_class = buffer.LenientDecodingLineBuffer

# Create our bot class
class AutoBot(irc.bot.SingleServerIRCBot):
    """Create the single server irc bot"""
    def __init__(self):
        """Set variables, handle logs, and listen for input on a port"""
        self.config = configparser.ConfigParser()
        self.config.read("autobot.conf")
        self.sg = Sugaroid()
        self.nick = self.config.get("irc", "nick")
        self.nickpass = self.config.get("irc", "nickpass")
        self.name = self.config.get("irc", "name")
        self.network = self.config.get("irc", "network")
        self.port = int(self.config.get("irc", "port"))
        self._ssl = self.config.getboolean("irc", "ssl")
        self.channel_list = [channel.strip() for channel in self.config.get("irc", "channels").split(",")]
        self.prefix = '!'

        irc.client.ServerConnection.buffer_class = buffer.LenientDecodingLineBuffer

        # Connect to IRC server
        if self._ssl:
            factory = irc.connection.Factory(wrapper=ssl.wrap_socket)
        else:
            factory = irc.connectionFactory()
        try:
            irc.bot.SingleServerIRCBot.__init__(self, [(self.network, self.port)],
                                                self.nick, self.name,
                                                reconnection_interval=120,
                                                connect_factory = factory)
        except irc.client.ServerConnectionError:
            sys.stderr.write(sys.exc_info()[1])

        #Listen for data to announce to channels
        #listenhost = self.config.get("tcp", "host")
        #listenport = int(self.config.get("tcp", "port"))
        #self.new_thread = TCPserver(self, listenhost, listenport)
        #self.new_thread.start()

        # Get Log configuration, create dictionary of log files, start refresh timer.
        self.log_scheme = self.config.get("bot", "log_scheme")
        self.logs = {}
        self.logs['autobot'] = LogFile.LogFile(datetime.datetime.utcnow().strftime(self.log_scheme).format(channel='autobot'))
        for ch in self.channel_list:
            log_name = datetime.datetime.utcnow().strftime(self.log_scheme).format(channel=ch)
            self.logs[ch] = LogFile.LogFile(log_name)
        self.second_thread = Periodic(self)
        self.second_thread.daemon = True
        self.second_thread.start()

    def start(self):
        try:
            super().start()
        except:
            self.close_logs()
            self.second_thread.join()
            self.new_thread.join()
            raise

    def run(self, connection):
        """Set global handlers and connect to IRC"""
        #Allows the logging of users on quit
        self.connection.add_global_handler("quit", self.alt_on_quit, -30)

    def announce(self, text):
        """Send notice to joined channels"""
        for channel in self.channel_list:
            self.connection.notice(channel, text)
            self.log_message(channel, "-!-", "(notice) {0}: {1}"
                             .format(self.connection.get_nickname(), text))

    def say(self, target, text):
        """Send message to IRC and log it"""
        self.connection.privmsg(target, text)
        self.log_message(target, "<{0}>".format(self.connection.get_nickname()),
                         "{0}".format(text))

    def do(self, target, text):
        """Send action event to IRC and log it"""
        self.connection.action(target, text)
        self.log_message(target, "*", "{0} {1}"
                         .format(self.connection.get_nickname(), text))

    def on_nicknameinuse(self, connection, event):
        """If the nick is in use, get nick_"""
        connection.nick("{0}_".format(connection.get_nickname()))

    def on_welcome(self, connection, event):
        """Join channels and regain nick"""
        for channel in self.channel_list:
            connection.join(channel)
            self.log_message("autobot", "-->", "Joined channel {0}"
                             .format(channel))
        if self.nickpass and connection.get_nickname() != self.nick:
            connection.privmsg("nickserv", "ghost {0} {1}"
                               .format(self.nick, self.nickpass))
            self.log_message("autobot", "-!-", "Recovered nick")

    def get_version(self):
        """CTCP version reply"""
        return "Autobot IRC bot"

    def on_privnotice(self, connection, event):
        """Identify to nickserv and log privnotices"""
        self.log_message("autobot", "<{0}>".format(event.source),
                         event.arguments[0])
        if not event.source:
            return
        source = event.source.nick

        if (source and source.lower() == "nickserv"
                and event.arguments[0].lower().find("identify") >= 0
                and self.nickpass and self.nick == connection.get_nickname()):

            connection.privmsg("nickserv", "identify {0} {1}"
                               .format(self.nick, self.nickpass))
            self.log_message("autobot", "-!-", "Identified to nickserv")

    #def on_disconnect(self, connection, event):
        #self.server_connect(self.nick, self.name, self.network, self.port, self._ssl)

    def on_pubnotice(self, connection, event):
        """Log public notices"""
        self.log_message(event.target, "-!-", "(notice) {0}: {1}"
                         .format(event.source, event.arguments[0]))

    def on_kick(self, connection, event):
        """Log kicked nicks and rejoin channels if bot is kicked"""
        kicked_nick = event.arguments[0]
        kicker = event.source.nick
        self.log_message(event.target, "<--", "{0} was kicked from the channel by {1}"
                         .format(kicked_nick, kicker))
        if kicked_nick == self.nick:
            time.sleep(10) #waits 10 seconds
            for channel in self.channel_list:
                connection.join(channel)

    def alt_on_quit(self, connection, event):
        """Log when users quit"""
        for channel in self.channels:
            if self.channels[channel].has_user(event.source.nick):
                self.log_message(channel, "<--", "{0} has quit"
                                 .format(event.source))

    def on_join(self, connection, event):
        """Log channel joins"""
        self.log_message(event.target, "-->", "{0} joined the channel"
                         .format(event.source))
        if event.source.nick == self.nick:
            self.say(event.target, "Hello! I am Sugaroid")

    def on_part(self, connection, event):
        """Log channel parts"""
        self.log_message(event.target, "<--", "{0} left the channel"
                         .format(event.source))

    def on_nick(self, connection, event):
        """Log nick changes"""
        new_nick = event.target
        for channel in self.channels:
            if self.channels[channel].has_user(new_nick):
                self.log_message(channel, "-!-", "{0} changed their nick to {1}"
                                 .format(event.source, new_nick))

    def on_mode(self, connection, event):
        """Log mode changes"""
        mode = " ".join(event.arguments)
        self.log_message(event.target, "-!-", "mode changed to {0} by {1}"
                         .format(mode, event.source.nick))

    def on_topic(self, connection, event):
        """Log topic changes"""
        self.log_message(event.target, "-!-", 'topic changed to "{0}" by {1}'
                         .format(event.arguments[0], event.source.nick))

    def on_action(self, connection, event):
        """Log channel actions"""
        self.log_message(event.target, "*", "{0} {1}"
                         .format(event.source.nick, event.arguments[0]))

    def on_pubmsg(self, connection, event):
        """Log public messages and respond to command requests"""
        channel = event.target
        nick = event.source.nick
        message = event.arguments[0]
        self.log_message(channel, "<{0}>".format(nick), message)

        url_regex = re.compile(
            r'(?i)\b((?:https?://|[a-z0-9.\-]+[.][a-z]{2,4}/)'
            r'(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))'
            r'+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|'
            r'''[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', re.IGNORECASE)

        if url_regex.search(message):
            message_list = [element for element in message.split(' ')
                            if url_regex.match(element)]
            for element in message_list:
                title = url_announce.parse_url(element)
                if title is not None:
                    self.say(channel, title)

        command_regex = re.compile(
            r'^(' + re.escape(self.nick) + '( |[:,] ?)'
            r'|' + re.escape(self.prefix) + ')'
            r'([^ ]*)( (.*))?$', re.IGNORECASE)

        if command_regex.match(message):
            command = command_regex.match(message).group(3)
            arguments = command_regex.match(message).group(5)
            self.do_command(event, self.channels[channel].is_oper(nick),
                            channel, command, arguments)

    def on_privmsg(self, connection, event):
        """Log private messages and respond to command requests"""
        nick = event.source.nick
        message = event.arguments[0]

        if nick not in self.logs:
            self.logs[nick] = LogFile.LogFile(datetime.datetime.utcnow().strftime(self.log_scheme).format(channel=nick))
        self.log_message(nick, "<{0}>".format(nick), message)
        command = str(message)
        self.do_command(event, False, nick, command, None)

    def do_command(self, event, isOper, source, command, arguments):
        """Commands the bot will respond to"""
        user = event.source.nick
        connection = self.connection
        factoid = FactInfo.FactInfo().fcget(command, user)
        if factoid:
            self.say(source,factoid.format(user))
        elif command == "devour":
            if arguments is None or arguments.isspace():
                self.do(source, "noms {0}".format(user))
            else:
                self.do(source, "takes a large bite out of {0}"
                        .format(arguments.strip()))
        elif command == "dice":
            if arguments is None or arguments.isspace():
                self.say(source, "Please tell me how many sides the die "
                         "should have. dice <num>")
            else:
                roll = dice.rollDie(arguments)
                self.say(source, roll)
        elif command == "slap":
            if arguments is None or arguments.isspace():
                self.do(source, "slaps {0} around a bit with a large trout"
                        .format(user))
            else:
                self.do(source, "slaps {0} around a bit with a large trout."
                        .format(arguments.strip()))
        elif command == "rot13":
            if arguments is None:
                self.say(source, "I'm sorry, I need a message to cipher,"
                         " try \"!rot13 message\"")
            else:
                self.say(source, codecs.encode(arguments, 'rot13'))
        elif command == "bloat":
            if arguments is None:
                self.say(source, "{0} is bloat.".format(user))
            else:
                self.say(source, "{0} is bloat".format(arguments.strip()))
        elif command == "ddg":
            query = search.ddg(arguments)
            self.say(source, query)
            title = url_announce.parse_url(query)
            if title is not None:
                self.say(source, title)
        elif command == "w":
            query = search.wiki(arguments)
            self.say(source, query)
        elif command == "alw":
            query = search.alwiki(arguments)
            self.say(source, query)
        elif command == "gh":
            query = search.github(arguments)
            self.say(source, query)
        elif command == "help":
            self.say(source, "Available commands: ![devour, dice <num>, "
                     "bloat <message>, slap, rot13 <message>, "
                     "ddg <search>, w <search>, alw <search>, gh <search>, "
                     "disconnect, die, help]")
        elif command == "disconnect":
            if isOper:
                self.disconnect(msg="I'll be back!")
            else:
                self.say(source, "You don't have permission to do that")
        elif command == "die":
            if isOper:
                self.close_logs()
                self.periodic.cancel()
                self.die(msg="Bye, will have a great time with you later!")
            else:
                self.say(source, "You don't have permission to do that")
        else:
            print("SUGAROID", command)
            response = self.sg.parse(command)
            self.say(source, str(response))
            #connection.notice(user, "I'm sorry, {0}. I'm afraid I can't do that."
            #                  .format(user))

    def log_message(self, channel, nick, message):
        """Create IRC logs"""
        try:
            log_file = self.logs[channel]
        except KeyError:
            self.logs[channel] = LogFile.LogFile(datetime.datetime.utcnow()
                                                 .strftime(self.log_scheme)
                                                 .format(channel=channel))
            log_file = self.logs[channel]
        log_file.write("{0} {1}".format(nick, message))

    def refresh_logs(self):
        """Remove stale log files (15 min without writes)"""
        timestamp = int(time.time())
        for log in self.logs:
            if self.logs[log].is_stale(timestamp):
                self.logs[log].close()

    def close_logs(self):
        """ Close all open log files"""
        for log in self.logs:
            self.logs[log].close()

class TCPserver(threading.Thread):
    def __init__(self, AutoBot, host, port):
        threading.Thread.__init__(self)
        self.AutoBot = AutoBot
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
        self.AutoBot = AutoBot
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        if data is not None:
            self.AutoBot.announce(data.decode("utf-8", "replace").strip())
        self.request.close()

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)

class Periodic(threading.Thread):
    def __init__(self, AutoBot):
        threading.Thread.__init__(self)
        self.AutoBot = AutoBot
        self.starttime=time.time()

    def run(self):
        while True:
            self.AutoBot.refresh_logs()
            time.sleep(960.0 - ((time.time() - self.starttime) % 960.0))

def main():
    bot = AutoBot()
    bot.start()

if __name__ == "__main__":
    main()
