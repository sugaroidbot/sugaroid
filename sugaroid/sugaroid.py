import os
import sys

import logging

logging.basicConfig(level=logging.INFO)

import nltk
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot
import json
from sugaroid.trainer.trainer import SugaroidTrainer
from sugaroid.brain.brain import Neuron
from sugaroid.config.config import ConfigManager

a = """
  /$$$$$$                                                    /$$       /$$
 /$$__  $$                                                  |__/      | $$
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$  /$$$$$$$
|  $$$$$$ | $$  | $$ /$$__  $$ |____  $$ /$$__  $$ /$$__  $$| $$ /$$__  $$
 \____  $$| $$  | $$| $$  \ $$  /$$$$$$$| $$  \__/| $$  \ $$| $$| $$  | $$
 /$$  \ $$| $$  | $$| $$  | $$ /$$__  $$| $$      | $$  | $$| $$| $$  | $$
|  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$/| $$|  $$$$$$$
 \______/  \______/  \____  $$ \_______/|__/       \______/ |__/ \_______/
                     /$$  \ $$                                            
                    |  $$$$$$/                                            
                     \______/                                             

"""


class Sugaroid:
    def __init__(self):
        self.trainer = None
        self.corpusTrainer = None
        self.neuron = None
        self.cfgmgr = ConfigManager()
        self.cfgpath = self.cfgmgr.get_cfgpath()
        self.database_exists = os.path.exists(
            os.path.join(self.cfgpath, 'sugaroid.db'))
        nltk.download('vader_lexicon')
        # Create a new chat bot named Charlie
        self.chatbot = ChatBot(
            'Sugaroid',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                'chatterbot.logic.MathematicalEvaluation',
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'maximum_similarity_threshold': 0.80
                },
                {
                    'import_path': 'sugaroid.brain.ok.OkayAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.time.TimeAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.whoami.WhoAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.joke.JokeAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.wiki.WikiAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.emotion.EmotionAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.fun.FunAdapter',
                },
                # {
                #	'import_path': 'sugaroid.brain.idk.DontKnowAdapter',
                # }
            ],
            database_uri='sqlite+pysqlite:///{}/sugaroid.db'.format(
                self.cfgpath),
        )
        self.read()
        self.invoke_brain()

    def init_local_trainers(self):
        conversation = [
            "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "That is good to hear",
            "Thank you.",
            "You're welcome."
        ]
        # initialize the trainer
        self.trainer = ListTrainer(self.chatbot)
        self.corpusTrainer = ChatterBotCorpusTrainer(self.chatbot)

        # initialize with minimum converstion
        self.list_train(conversation)

    def list_train(self, li):
        self.trainer.train(li)

    def read(self):
        if 'train' in sys.argv:
            from sugaroid.trainer.trainer import main as trainer
            # FIXME replace with dynamic traineri.e GUI + CLI
            trainer()
        else:
            if self.database_exists:
                print("Database already exists")
                pass
            else:
                if self.trainer is None:
                    self.init_local_trainers()

                st = SugaroidTrainer()
                st.train(self.trainer)
        if 'update' in sys.argv:
            if self.trainer is None:
                self.init_local_trainers()

            st = SugaroidTrainer()
            st.train(self.trainer)

    def write(self):
        raise NotImplementedError

    def corpus(self):
        self.corpusTrainer.train(
            "chatterbot.corpus.english.greetings",
        )

    def invoke_brain(self):
        self.neuron = Neuron(self.chatbot)

    def parse(self, args):
        if type(args) is str:
            return self.neuron.parse(args)
        else:
            raise ValueError("Invalid data type passed to Sugaroid.parse")

    def prompt_cli(self):
        try:
            response = self.parse(input('( ဖ‿ဖ) @> '))
            return response
        except (KeyboardInterrupt, EOFError):
            sys.exit()

    @staticmethod
    def display_cli(response):
        print(response)

    def loop_cli(self):
        while True:
            self.display_cli(self.prompt_cli())

    def loop_gui(self):
        print("Launching GUI")
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
        QApplication.setAttribute(
            QtCore.Qt.AA_UseHighDpiPixmaps, True)  # use highdpi icons
        app = QtWidgets.QApplication(sys.argv)
        app.setStyle('Breeze')
        from sugaroid.gui.ux import InterfaceSugaroidQt
        prog = InterfaceSugaroidQt(parent=self)
        prog.init()
        try:
            app.exec_()
        except KeyboardInterrupt:
            sys.exit()


def main():
    print(a)
    sg = Sugaroid()
    if 'qt' in sys.argv:
        sg.loop_gui()
    else:
        sg.loop_cli()


if __name__ == "__main__":
    main()
