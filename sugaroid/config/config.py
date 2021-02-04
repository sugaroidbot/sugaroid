"""
Sugaroid Configuration manager. Sugaroid stores the trainer
configuration in the ``sugaroid.trainer.json`` in the 
``xdg`` specified directories in linux OSes, and in 
``%HOME%/AppData/Local`` in Windows systems
"""

import json
import os


from sugaroid.platform import platform


class ConfigManager:
    """
    Global Sugaroid Trainer configuration manager
    """

    def __init__(self, mode="w"):
        """
        Initialize the configuration manager instance
        with a specified mode, by default: the mode is ``w``
        which implies, only write

        :param mode: the mode of the opening the JSON file
        :type mode: str
        """
        self.os = platform.System()
        self.cfgpath = self.os.cfgpath()
        self.paths = self.os.paths()
        self.config = {}
        self.jsonfile = "sugaroid.trainer.json"
        self.check_file()

    def get_config(self) -> dict:
        """
        Returns the current configuration file

        :return: The current configuration
        :rtype: dict
        """
        return self.config

    def get_cfgpath(self) -> str:
        """
        Returns the current path to the configuration file

        :return: The path of the configuration file
        :rtype: str
        """
        return self.cfgpath

    def read_file(self):
        """
        Read the configuration file and reloads the internal
        configuration

        :return: None
        :rtype: None
        """
        with open(os.path.join(self.cfgpath, self.jsonfile), "r") as f:
            config = json.load(f)
        self.update_config(config)

    def write_file(self):
        """
        Writes the current configuration to the jsonfile

        :return: None
        :rtype: None
        """
        with open(os.path.join(self.cfgpath, self.jsonfile), "w") as f:
            json.dump(self.config, f, indent=4, sort_keys=True)

    def check_file(self) -> bool:
        """
        Checks if the file exists, if it exists, return True

        :return: Does the file exist?
        :rtype: bool
        """
        if not os.path.exists(self.cfgpath):
            os.mkdir(self.cfgpath)
        if not os.path.exists(os.path.join(self.cfgpath, self.jsonfile)):
            import nltk

            for lexicon in [
                "averaged_perceptron_tagger",
                "stopwords",
                "wordnet",
                "vader_lexicon",
                "punkt",
            ]:
                nltk.download(lexicon)
            self.write_file()
        self.read_file()

    def update_config(self, new_conf: dict):
        """
        Updates the configuration ``dict.update``

        :param new_conf: Dictionary object with new configuration
        :type new_conf: dict
        """

        self.config.update(new_conf)

    def reset_config(self):
        """
        Resets the configuration
        """
        os.remove(os.path.join(self.get_cfgpath(), self.jsonfile))
