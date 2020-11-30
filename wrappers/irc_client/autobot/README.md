autobot
=======

A python IRC bot

This is a full featured python irc bot that uses the python-irc library

Features
--------

* Configuration options in a single config file
* Joins a single irc server with support for SSL
* Joins multiple channels
* Listens on a port for messages and then announces the messages in IRC
    * The port and host are set in the configuration file
    * you can send a test message with "netcat host port" then type the message
      and hit enter.
* Identifies to nickserv
* Rejoins channels on kick or disconnect
* Has some basic commands that are listed with !help
* Logs all channels and network notifications

Plugins
-------
* url announcements
* web search

Planned:
* factoids
* quotes

Installation
------------

Autobot uses python and the python libraries irclib, urllib, requests, and beautifulsoup.
Once these are installed you should be able to just run it.

Configuration
-------------

Copy the autobot.conf.template to src/autobot.conf and update the settings for your
personal use. Then run the bot with ```python autobot.py```

To-do
-----

* encrypt nick password so it isn't plaintext in the config
* SASL auth
* CertFP auth
* Make modular so scripts can be loaded from a directory and be used by the bot
* More better configuration parsing and checking with defaults

Refactor irc channel OP check to loop through connected channels and check if the user has
OPs in any of them, if yes, then isOper is True - maybe should skip this and just have a mod list in configuration?
