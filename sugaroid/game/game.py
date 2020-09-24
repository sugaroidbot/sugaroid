import os
import freegames

directory = freegames.__path__[0]

contents = os.listdir(directory)


def game_file(name):
    """"
    Return True if filename represents a game.
    """
    return False


games = sorted(name[:-3] for name in contents if game_file(name))
