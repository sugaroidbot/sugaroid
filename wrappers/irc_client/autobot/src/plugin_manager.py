#class PluginManager(object):
#    def __init__(self, botnick, prefix):
#        """ Manage Plugins """
#        self.plugin_list = []
#
#        self.botnick = botnick
#        self.prefix = prefix
#
#        command_regex = re.compile(
#                   r'^(' + re.escape(self.botnick) + '( |[:,] ?)'
#                   r'|' + re.escape(self.prefix) + ')'
#                   r'([^ ]*)( (.*))?$', re.IGNORECASE)
#    def load_plugins(self):
#        for plugin in plugin_list:
#            try:
#                importlib.import_module(plugins.plugin)
#            except Exception:
#                sys.stderr.write("{0} didn't load correctly".format(plugin))
#                continue
#    def reload_plugin(self, plugin):
#        try:
#            importlib.reload(plugin_list[plugin])
#    def reply(self, command):
#        if is_threaded:
#            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
#                response = executor.map(do_command, command)
#        else:
#                do_command(command)

#class Say(source, msg, action=False):
#    """ Send msg to channel """
#    if action:
#        AutoBot.do(source, msg)
#    else:
#        AutoBot.say(source, msg)
#    """ log msg """
#
#class Command(object):
#    """ Plugins of this class are triggered by a user """
#    def respond(self, source, nick, arguments):
#        trigger = ""
#        admin_required = False
#        action = False
#        admin_list = [meskarune]
#        Say(source, msg.format(nick))
#
#class Event(object):
#    """ Plugins of this class are triggered by an irc event """
#    def respond(self, source, msg):
#        Say(source, msg)
#
#
#---------------
#
#from plugin_manager import Command
#
#class Slap(Command):
#    trigger= "slap"
#    admin_required = False
#    action = True
#    def respond(self, source, nick, arguments):
#        if arguments is None or arguments.isspace():
#            Say(source, "slaps {0} around a bit with a large trout".format(arguments), action)
#        else:
#            Say(source, "slaps {0} around a bit with a large trout.".format(nick), action)
#
#----------------
#
#from plugin_manager immport Command
#
#class Die(Command):
#    trigger = "die"
#    admin_required = True
#    action = False
#    admin_list = [meskarune]
#    def respond(self, source, nick, arguments):
#        if admin_required:
#            if nick in admin_list:
#                """ kill the bot """
#            else:
#                Say(source, "I'm sorry {0}, you aren't allowed to do that".format(nick), action)
