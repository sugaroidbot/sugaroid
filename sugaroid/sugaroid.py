"""
MIT License

Sugaroid Artificial Intelligence
Chatbot Core
Copyright (c) 2020 Srevin Saju

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
import shutil
from emoji import emojize
from sugaroid.brain.constants import SUGAROID_INTRO, REPEAT
from sugaroid.brain.postprocessor import random_response
from sugaroid.config.config import ConfigManager
from sugaroid.brain.brain import Neuron
from sugaroid.trainer.trainer import SugaroidTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import nltk
from sugaroid.brain.utils import LanguageProcessor
import logging
import os
import sys
import warnings
from chatterbot.conversation import Statement
from sugaroid.brain.ooo import Emotion

warnings.filterwarnings("ignore")

try:
    from sugaroid.tts.tts import Text2Speech
    AUD_DEPS = True
except ModuleNotFoundError:
    AUD_DEPS = False
verbosity = logging.INFO
logging.basicConfig(level=verbosity)

try:
    from PyQt5 import QtCore, QtWidgets
    from PyQt5.QtWidgets import QApplication
    GUI_DEPS = True
except ModuleNotFoundError:
    GUI_DEPS = False

a = SUGAROID_INTRO


class SugaroidStatement(Statement):
    """
    A modified chatterbot Statement with the additional parameters
    The Chatterbot Statement did not preserve the capabilities to hold
    fundamental data such as name of the adapter and emotion of the statemnt passed
    The emotion was either a <class 'Emotion'> type or NoneType
    The Adapter was the generic name of the adapter in string type determined
    by the __gtype__ variable
    """
    def __init__(self, text, in_response_to=None, **kwargs):
        Statement.__init__(self, text, in_response_to, **kwargs)
        self.emotion = kwargs.get('emotion', Emotion.neutral)
        self.adapter = kwargs.get('type_', '')


class SugaroidBot(ChatBot):
    """
    The SugaroidBot inherits the class local variables from the Chat
    """
    def __init__(self, name, **kwargs):
        ChatBot.__init__(self, name=name, **kwargs)
        self.emotion = Emotion.neutral
        self.history = [0]
        self.adapters = []
        self.user_history = [0]
        self.history_types = [0]
        self.fun = True
        self.lp = LanguageProcessor()
        self.reverse = False
        self.last_news = None
        self.next = None
        self.akinator = False
        self.aki = None
        self.hangman = False
        self.hangman_class = None
        self.next_type = None
        self.temp_data = []
        self.username = None
        self.learn = False
        self.learn_last_conversation = []
        self.spell_checker = False  # FIXME
        self.debug = {}

    def set_emotion(self, emotion):
        """
        Sets the emotion for the chatbot globally.
        (Deprecated)
        :param emotion:
        :return:
        """
        self.emotion = emotion

    def reset_variables(self):
        self.emotion = Emotion.neutral
        self.history = [0]
        self.user_history = [0]
        self.history_types = [0]
        self.fun = True
        self.lp = LanguageProcessor()
        self.reverse = False
        self.last_news = None
        self.next = None
        self.akinator = False
        self.aki = None
        self.hangman = False
        self.hangman_class = None
        self.next_type = None
        self.temp_data = []
        self.username = None
        self.learn = False
        self.learn_last_conversation = []
        self.spell_checker = False  # FIXME
        self.debug = {}

    def get_emotion(self):
        """
        Returns the emotion of the chatbot at a particular time
        :return:
        """
        return self.emotion

    def set_username(self):
        """
        Sets the Sugaroid user username
        :return: None, Exceptopm FIXME
        """
        raise NotImplementedError("LOL")

    def get_username(self):
        """
        Returns sugaroid username if store, otherwise None
        :return: SugaroidBot.username <user name>
        """
        return self.username

    def generate_response(self, input_statement, additional_response_selection_parameters=None):
        """
        Return a response based on a given input statement.

        :param input_statement: The input statement to be processed.
        """
        Statement = self.storage.get_object('statement')

        results = []
        result = None
        max_confidence = -1
        final_adapter = None
        for adapter in self.logic_adapters:
            if adapter.can_process(input_statement):

                output = adapter.process(
                    input_statement, additional_response_selection_parameters)
                results.append(output)

                self.logger.info(
                    '{} selected "{}" as a response with a confidence of {}'.format(
                        adapter.class_name, output.text, output.confidence
                    )
                )

                if output.confidence > max_confidence:
                    result = output
                    final_adapter = adapter.class_name
                    max_confidence = output.confidence
            else:
                self.logger.info(
                    'Not processing the statement using {}'.format(
                        adapter.class_name)
                )

        self.gen_debug(statement=input_statement, adapter=final_adapter, confidence=max_confidence, results=result)

        class ResultOption:
            def __init__(self, statement, count=1):
                self.statement = statement
                self.count = count

        # If multiple adapters agree on the same statement,
        # then that statement is more likely to be the correct response
        if len(results) >= 3:
            result_options = {}
            for result_option in results:
                result_string = result_option.text + ':' + \
                    (result_option.in_response_to or '')

                if result_string in result_options:
                    result_options[result_string].count += 1
                    if result_options[result_string].statement.confidence < result_option.confidence:
                        result_options[result_string].statement = result_option
                else:
                    result_options[result_string] = ResultOption(
                        result_option
                    )

            most_common = list(result_options.values())[0]

            for result_option in result_options.values():
                if result_option.count > most_common.count:
                    most_common = result_option

            if most_common.count > 1:
                result = most_common.statement
        try:
            emotion = result.emotion
        except AttributeError:
            emotion = Emotion.neutral

        try:
            adapter_type = result.adapter
        except AttributeError:
            result.adapter = None
            adapter_type = None

        if adapter_type and adapter_type not in ['NewsAdapter', 'LearnAdapter']:
            if adapter_type in self.history_types:
                if adapter_type == self.history_types[-1]:
                    result.text = random_response(REPEAT)
                elif len(self.history_types) > 2:
                    if adapter_type == self.history_types[-2]:
                        result.text = random_response(REPEAT)

        self.history_types.append(adapter_type)

        response = Statement(
            text=result.text,
            in_response_to=input_statement.text,
            conversation=input_statement.conversation,
            persona='sugaroid:' + self.name
        )
        response.emotion = emotion
        response.confidence = result.confidence

        return response

    def gen_debug(self, statement, adapter, confidence, results):
        """
        Create a debug dictionary key:value pair for Debug Conversation
        The Google
        :param statement: input_statement
        :param adapter: Adapter __gtype__classname__
        :param confidence: SugaroidStatement.confidence
        :param results: Sugaroid Statement.text
        :return:
        """

        self.debug['number_of_conversations'] = self.debug.get('number_of_conversations', 0) + 1
        _id = self.debug['number_of_conversations']
        val = dict()
        val['adapter'] = adapter
        val['confidence'] = confidence
        val['response'] = results
        val['request'] = str(statement)
        self.debug[_id] = val


class Sugaroid:
    """
    Sugaroid
    Initates the chatbot class and connects logic Adapters together.
    Initates the ConfigManager to store sugaroid data and connects scans sys.argv

    """
    def __init__(self):
        self.trainer = None
        self.corpusTrainer = None
        self.neuron = None
        self.audio = 'audio' in sys.argv
        self.cfgmgr = ConfigManager()
        self.cfgpath = self.cfgmgr.get_cfgpath()
        self.database_exists = os.path.exists(
            os.path.join(self.cfgpath, 'sugaroid.db'))
        nltk.download('vader_lexicon')

        self.adapters = [
            'sugaroid.brain.yesno.BoolAdapter',
            'sugaroid.brain.aki.AkinatorAdapter',
            'sugaroid.brain.hangman.HangmanAdapter',
            'sugaroid.brain.either.OrAdapter',
            'sugaroid.brain.ok.OkayAdapter',
            'sugaroid.brain.bye.ByeAdapter',
            'sugaroid.brain.time.TimeAdapter',
            'sugaroid.brain.convert.CurrencyAdapter',
            'sugaroid.brain.learn.LearnAdapter',
            'sugaroid.brain.trivia.TriviaAdapter',
            'sugaroid.brain.whoami.WhoAdapter',
            'sugaroid.brain.news.NewsAdapter',
            'sugaroid.brain.joke.JokeAdapter',
            'sugaroid.brain.play.PlayAdapter',
            'sugaroid.brain.canmay.CanAdapter',
            'sugaroid.brain.because.BecauseAdapter',
            'sugaroid.brain.rereversei.ReReverseAdapter',
            'sugaroid.brain.reversethink.ReverseAdapter',
            'sugaroid.brain.myname.MyNameAdapter',
            'sugaroid.brain.iam.MeAdapter',
            'sugaroid.brain.about.AboutAdapter',
            'sugaroid.brain.wiki.WikiAdapter',
            'sugaroid.brain.dolike.DoLikeAdapter',
            'sugaroid.brain.feel.FeelAdapter',
            'sugaroid.brain.do.DoAdapter',
            'sugaroid.brain.emotion.EmotionAdapter',
            'sugaroid.brain.dis.DisAdapter',
            'sugaroid.brain.twoword.TwoWordAdapter',
            'sugaroid.brain.oneword.OneWordAdapter',
            'sugaroid.brain.debug.DebugAdapter',
            'sugaroid.brain.why.WhyWhenAdapter',
            'sugaroid.brain.reader.ReaderAdapter',
            'sugaroid.brain.imitate.ImitateAdapter',
            'sugaroid.brain.fun.FunAdapter',
            'chatterbot.logic.UnitConversion',
        ]

        if self.audio:
            self.tts = Text2Speech()
        else:
            self.tts = None

        # Create a new chat bot named Charlie
        self.chatbot = SugaroidBot(
            'Sugaroid',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'maximum_similarity_threshold': 0.80
                },
            ] + self.adapters,
            database_uri='sqlite+pysqlite:///{}/sugaroid.db'.format(
                self.cfgpath),
        )

        # initialize language processs
        self.chatbot.lp = LanguageProcessor()
        self.chatbot.adapters = self.adapters
        self.chatbot.history = [0]
        self.chatbot.report = False
        self.chatbot.reverse = False
        self.chatbot.next = None
        self.chatbot.username = None
        self.chatbot.next_type = None
        self.chatbot.trivia_answer = None
        self.read()
        self.invoke_brain()

    def init_local_trainers(self):
        """
        Init local trainers with minimum conversation
        :return:
        """
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

        # initialize with minimum conversation
        self.list_train(conversation)

    def list_train(self, li):
        self.trainer.train(li)

    def read(self):
        """
        Train Sugaroid database from the sugaroid.trainer.json located in the configuration directory
        if it exists. If the sugaroid.db file exists, the Database update is skipped

        :return:
        """
        if 'train' in sys.argv:
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
        if 'update' in sys.argv:
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
        db_dir = os.path.join(os.path.dirname(__file__), 'data', 'sugaroid.db')
        shutil.copy(db_dir, os.path.join(self.cfgpath, 'sugaroid.db'))
        self.corpusTrainer.train(
            "chatterbot.corpus.english.ai",
            "chatterbot.corpus.english.botprofile",
            "chatterbot.corpus.english.computers",
            "chatterbot.corpus.english.food",
            "chatterbot.corpus.english.history",
            "chatterbot.corpus.english.literature",
            "chatterbot.corpus.english.money",
            "chatterbot.corpus.english.movies",
            "chatterbot.corpus.english.politics",
            "chatterbot.corpus.english.science",
            "chatterbot.corpus.english.sports",
        )
        return True

    def invoke_brain(self):
        """
        Initiate the Brain
        :return:
        """
        self.neuron = Neuron(self.chatbot)

    def parse(self, args):
        """
        Do a simple parsing of the init statement. Classify statement on the type of inupt_statement
        and confidence of each statement
        :param args:
        :return:
        """
        if type(args) is str:
            response = self.neuron.parse(args)
            self.chatbot.history.append(response)
            self.chatbot.user_history.append(args)
            return response
        else:
            raise ValueError("Invalid data type passed to Sugaroid.parse")

    def prompt_cli(self):
        """
        Classic prompt for Sugaroid Command Line Interface
        :return:
        """
        try:
            response = self.parse(input('( ဖ‿ဖ) @> '))
            return response
        except (KeyboardInterrupt, EOFError):
            sys.exit()

    def display_cli(self, response):
        """
        Classic display adapter for TTY Sugaroid Command Line Interface
        :param response:
        :return:
        """
        print(emojize(response.text))
        if self.audio:
            self.tts.speak(str(response))

    def loop_cli(self):
        """
        Sugaroid loop_cli for Sugaroid Command Line Interface
        :return:
        """

        while True:
            self.display_cli(self.prompt_cli())

    def loop_gui(self):
        """
        Launch the sugaroid PyQt5 gui with Breeze theme and custom features
        If PyQt5 not installed, raise ModuleNotFoundError
        :return:
        """
        if not GUI_DEPS:
            raise ModuleNotFoundError(
                "PyQt5 is not Installed. Install it by pip3 install PyQt5")
        print("Launching GUI")
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
        QApplication.setAttribute(
            QtCore.Qt.AA_UseHighDpiPixmaps, True)  # use highdpi icons
        app = QtWidgets.QApplication(sys.argv)
        app.setStyle('Breeze')
        from sugaroid.gui.ux import InterfaceSugaroidQt
        window = InterfaceSugaroidQt(parent=self)
        window.init()
        try:
            app.exec_()
        except KeyboardInterrupt:
            sys.exit()


def main():
    """
    Launch a cli / gui based on the sys.argv
    Entrypoint in setup.py console_entry_points
    :return:
    """
    print(a)
    sg = Sugaroid()
    if 'qt' in sys.argv:
        os.environ['SUGAROID'] = 'GUI'
        sg.loop_gui()
    elif 'web' in sys.argv:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'sugaroid.web.websugaroid.websugaroid.settings')
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage', 'runserver', '0.0.0.0:8000'])
    else:
        os.environ['SUGAROID'] = 'CLI'
        sg.loop_cli()


if __name__ == "__main__":
    main()
