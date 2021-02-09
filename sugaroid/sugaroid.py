import shutil
import time

from colorama import Fore, Style
from colorama import init as colorama_init
from emoji import emojize

from sugaroid.backend.sql import SqlDatabaseManagement
from sugaroid.brain.constants import SUGAROID_INTRO
from sugaroid.config.config import ConfigManager
from sugaroid.brain.brain import Neuron
from sugaroid.core.bot import SugaroidBot
from sugaroid.trainer.trainer import SugaroidTrainer
from sugaroid.core.statement import SugaroidStatement  # noqa:
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from sugaroid.brain.utils import LanguageProcessor
import logging
import coloredlogs
import os
import sys
import warnings
from sugaroid.version import VERSION

warnings.filterwarnings("ignore")

try:
    from sugaroid.tts.tts import Text2Speech

    AUD_DEPS = True
except ModuleNotFoundError:
    AUD_DEPS = False


sugaroid_logger = logging.getLogger(__name__)


# enable the verbosity
if "--debug" in sys.argv or os.getenv("SUGAROID_DEBUG") == "1":
    # set the verbosity
    print("SUGAROID_DEBUG: Enabled")
    verbosity = logging.INFO
    logging.basicConfig(level=verbosity)
    sugaroid_logger.setLevel(level=logging.INFO)
    coloredlogs.install(level="INFO", logger=sugaroid_logger)


try:
    from PyQt5 import QtCore, QtWidgets  # noqa:
    from PyQt5.QtWidgets import QApplication  # noqa:

    GUI_DEPS = True
except (ModuleNotFoundError, ImportError) as e:
    print("warn: Could not import PyQt5", e)
    GUI_DEPS = False


SPACY_LANG_PROCESSOR = LanguageProcessor()


class Sugaroid:
    """
    Sugaroid Initates the chatbot class and connects logic Adapters together.
    Initates the ConfigManager to store sugaroid data and connects scans
    sys.argv

    """

    def __init__(self, readonly=True):
        self.trainer = None
        self.corpusTrainer = None
        self.neuron = None
        self.audio = "audio" in sys.argv
        self.cfgmgr = ConfigManager()
        self.cfgpath = self.cfgmgr.get_cfgpath()
        self.database = SqlDatabaseManagement(
            os.path.join(self.cfgpath, "sugaroid_internal.db")
        )
        self.database_exists = os.path.exists(os.path.join(self.cfgpath, "sugaroid.db"))
        self.commands = [
            "sugaroid.brain.debug.DebugAdapter",
            "sugaroid.brain.interrupt.InterruptAdapter",
            "sugaroid.brain.learn.LearnAdapter",
            "sugaroid.brain.swaglyrics.SwagLyricsAdapter",
        ]
        self.adapters = [
            "sugaroid.brain.yesno.BoolAdapter",
            "sugaroid.brain.aki.AkinatorAdapter",
            "sugaroid.brain.hangman.HangmanAdapter",
            "sugaroid.brain.either.OrAdapter",
            "sugaroid.brain.ok.OkayAdapter",
            "sugaroid.brain.bye.ByeAdapter",
            "sugaroid.brain.time.TimeAdapter",
            "sugaroid.brain.convert.CurrencyAdapter",
            "sugaroid.brain.trivia.TriviaAdapter",
            "sugaroid.brain.whoami.WhoAdapter",
            "sugaroid.brain.news.NewsAdapter",
            "sugaroid.brain.joke.JokeAdapter",
            "sugaroid.brain.play.PlayAdapter",
            "sugaroid.brain.let.LetAdapter",
            "sugaroid.brain.whatwhat.WhatWhatAdapter",
            "sugaroid.brain.waitwhat.WaitWhatAdapter",
            "sugaroid.brain.assertive.AssertiveAdapter",
            "sugaroid.brain.canmay.CanAdapter",
            "sugaroid.brain.because.BecauseAdapter",
            "sugaroid.brain.rereversei.ReReverseAdapter",
            "sugaroid.brain.reversethink.ReverseAdapter",
            "sugaroid.brain.covid.CovidAdapter",
            "sugaroid.brain.myname.MyNameAdapter",
            "sugaroid.brain.iam.MeAdapter",
            "sugaroid.brain.about.AboutAdapter",
            "sugaroid.brain.wolfalpha.WolframAlphaAdapter",
            "sugaroid.brain.wiki.WikiAdapter",
            "sugaroid.brain.dolike.DoLikeAdapter",
            "sugaroid.brain.feel.FeelAdapter",
            "sugaroid.brain.areyou.AreYouAdapter",
            "sugaroid.brain.dolike.DoLikeAdapter",
            "sugaroid.brain.do.DoAdapter",
            "sugaroid.brain.emotion.EmotionAdapter",
            "sugaroid.brain.dis.DisAdapter",
            "sugaroid.brain.twoword.TwoWordAdapter",
            "sugaroid.brain.oneword.OneWordAdapter",
            "sugaroid.brain.why.WhyWhenAdapter",
            "sugaroid.brain.reader.ReaderAdapter",
            "sugaroid.brain.imitate.ImitateAdapter",
            "sugaroid.brain.fun.FunAdapter",
            "chatterbot.logic.UnitConversion",
        ]

        if self.audio:
            self.tts = Text2Speech()
        else:
            self.tts = None

        self.chatbot = SugaroidBot(
            "Sugaroid",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            logic_adapters=self.commands
            + [
                {
                    "import_path": "chatterbot.logic.BestMatch",
                    "maximum_similarity_threshold": 0.80,
                }
            ]
            + self.adapters,
            database_uri="sqlite+pysqlite:///{}/sugaroid.db".format(self.cfgpath),
            read_only=readonly,
            logger=sugaroid_logger,
        )
        self.chatbot.globals["adapters"] = self.adapters

        self.read()
        self.invoke_brain()
        self.set_internet_media_from_environment()

    def init_local_trainers(self):
        """
        Init local trainers with minimum conversation
        :return:
        """
        # initialize the trainer
        self.trainer = ListTrainer(self.chatbot)
        self.corpusTrainer = ChatterBotCorpusTrainer(self.chatbot)

    def list_train(self, li):
        self.trainer.train(li)

    def interrupt_ds(self):
        self.chatbot.interrupt = 2

    def disable_interrupt_ds(self):
        self.chatbot.interrupt = 0

    def toggle_discord(self):
        self.chatbot.discord = not self.chatbot.discord

    def append_author(self, author):
        self.chatbot.authors.append(author)

    def read(self):
        """
        Train Sugaroid database from the sugaroid.trainer.json located in the configuration directory
        if it exists. If the sugaroid.db file exists, the Database update is skipped

        :return:
        """
        if "train" in sys.argv:
            from sugaroid.trainer.trainer import main as trainer

            # FIXME replace with dynamic trainer i.e GUI + CLI
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
                self.corpus()
        if "update" in sys.argv:
            if self.trainer is None:
                self.init_local_trainers()

            st = SugaroidTrainer()
            st.train(self.trainer)

    def write(self):
        raise NotImplementedError

    def corpus(self):
        """
        Train data if it doesn't exists.
        Periodically update the data too
        :return: True when the process is complete
        """
        db_dir = os.path.join(os.path.dirname(__file__), "data", "sugaroid.db")
        shutil.copy(db_dir, os.path.join(self.cfgpath, "sugaroid.db"))
        return True

    def invoke_brain(self):
        """
        Initiate the Brain
        :return:
        """
        self.neuron = Neuron(self.chatbot)

    def parse(self, args):
        """
        Do a simple parsing of the init statement. Classify statement on the
        type of input_statement
        and confidence of each statement
        :param args:
        :return:
        """
        if isinstance(args, str):
            preflight_time = time.time()
            response = self.neuron.parse(args)
            self.chatbot.globals["history"]["total"].append(response)
            self.chatbot.globals["history"]["user"].append(args)
            success_time = time.time()
            delta_time = success_time - preflight_time
            try:
                _text_response = response.text
            except AttributeError:
                _text_response = response

            assert isinstance(_text_response, str)
            if "gui" not in sys.argv:
                try:
                    self.database.append(
                        statement=_text_response,
                        in_reponse_to=args,
                        time=preflight_time,
                        processing_time=delta_time,
                    )
                except Exception:
                    # to protect our system, we sh
                    pass
            return response
        else:
            raise ValueError("Invalid data type passed to Sugaroid.parse")

    def prompt_cli(self):
        """
        Classic prompt for Sugaroid Command Line Interface
        :return:
        """

        response = self.parse(input(Fore.CYAN + "( ဖ‿ဖ) @> " + Fore.RESET))
        return response

    def display_cli(self, response):
        """
        Classic display adapter for TTY Sugaroid Command Line Interface
        :param response:
        :return:
        """
        try:
            print(
                Style.BRIGHT
                + Fore.GREEN
                + "sugaroid: "
                + Fore.RESET
                + Style.RESET_ALL
                + Fore.BLUE
                + emojize(response.text)
                + Fore.RESET
                + "\n"
            )
        except AttributeError:
            print(
                Style.BRIGHT
                + Fore.GREEN
                + "sugaroid: "
                + Fore.RESET
                + Style.RESET_ALL
                + Fore.BLUE
                + emojize(response)
                + Fore.RESET
                + "\n"
            )
        if self.audio:
            self.tts.speak(str(response))

    def loop_cli(self):
        """
        Sugaroid loop_cli for Sugaroid Command Line Interface
        :return:
        """
        try:
            while True:
                self.display_cli(self.prompt_cli())
        except (KeyboardInterrupt, EOFError):
            self.database.close()

    def loop_gui(self):
        """
        Launch the sugaroid PyQt5 gui with Breeze theme and custom features
        If PyQt5 not installed, raise ModuleNotFoundError
        :return:
        """
        if not GUI_DEPS:
            raise ModuleNotFoundError(
                "PyQt5 is not Installed. Install it by pip3 install PyQt5"
            )

        print("Launching GUI")
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
        QApplication.setAttribute(
            QtCore.Qt.AA_UseHighDpiPixmaps, True
        )  # use highdpi icons
        app = QtWidgets.QApplication(sys.argv)
        app.setStyle("Breeze")
        from sugaroid.gui.ux import InterfaceSugaroidQt

        window = InterfaceSugaroidQt(parent=self)
        window.init()
        try:
            app.exec_()
        except KeyboardInterrupt:
            pass
        self.database.close()

    def set_internet_media_from_environment(self):
        if os.getenv("DISCORD_TOKEN") or os.getenv("TELEGRAM_TOKEN"):
            # supports media
            self.chatbot.globals["media"] = True
            sugaroid_logger.info("Media support enabled")


def gui_main():
    sg = Sugaroid()
    sg.loop_gui()


def main():
    """
    Launch a cli / gui based on the sys.argv
    Entrypoint in setup.py console_entry_points
    :return:
    """
    print(SUGAROID_INTRO)
    colorama_init()
    read_only = False if "update" in sys.argv else True
    print("Sugaroid {} RO:{}\n".format(VERSION, read_only))
    sg = Sugaroid(readonly=read_only)
    if "gui" in sys.argv:
        os.environ["SUGAROID"] = "GUI"
        sg.loop_gui()
    else:
        os.environ["SUGAROID"] = "CLI"
        sg.loop_cli()


if __name__ == "__main__":
    main()
