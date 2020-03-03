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
    def __init__(self, text, in_response_to=None, **kwargs):
        Statement.__init__(self, text, in_response_to, **kwargs)
        self.emotion = kwargs.get('emotion', '')
        self.adapter = kwargs.get('type_', '')


class SugaroidBot(ChatBot):
    """
    Copyrighted (c) 2020 Adavanced NLP and personalized chatbot class
    Use with caution
    May give unrelated answers

    """

    def __init__(self, name, **kwargs):
        ChatBot.__init__(self, name=name, **kwargs)
        self.emotion = Emotion.neutral
        self.history = [0]
        self.history_types = [0]
        self.fun = True
        self.lp = LanguageProcessor()
        self.reverse = False
        self.next = None
        self.next_type = None
        self.temp_data = []
        self.username = None
        self.spell_checker = False  # FIXME

    def set_emotion(self, emotion):
        self.emotion = emotion

    def get_emotion(self):
        return self.emotion

    def set_username(self):
        raise NotImplementedError("LOL")

    def get_username(self):
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
        if adapter_type:
            if adapter_type in self.history_types:
                if adapter_type == self.history_types[-1]:
                    result.text = random_response(REPEAT)
                elif len(self.history_types) > 2:
                    if adapter_type == self.history_types[-2]:
                        result.text = random_response(REPEAT)

        # if self.history[-1]:
        #     if self.lp.similarity(result.text, str(self.history[-1])) > 0.9:
        #         result.text = random_response(REPEAT)

        self.history_types.append(adapter_type)

        # Clear attributes of ReverseiAdapter when ReverseiAdapter gave the answer
        """  # FIXME once code base is static
        if final_adapter == 'ReReverseAdapter':
            logging.info("Reversei variables reset")
            self.reverse = False
            self.next = None
            self.next_type = None
        """

        response = Statement(
            text=result.text,
            in_response_to=input_statement.text,
            conversation=input_statement.conversation,
            persona='sugaroid:' + self.name
        )
        response.emotion = emotion
        response.confidence = result.confidence

        return response


class Sugaroid:
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

        if self.audio:
            self.tts = Text2Speech()
        else:
            self.tts = None

        # Create a new chat bot named Charlie
        self.chatbot = SugaroidBot(
            'Sugaroid',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                'chatterbot.logic.MathematicalEvaluation',
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'maximum_similarity_threshold': 0.80
                },
                {
                    'import_path': 'sugaroid.brain.yesno.BoolAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.either.OrAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.ok.OkayAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.bye.ByeAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.time.TimeAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.trivia.TriviaAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.whoami.WhoAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.joke.JokeAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.play.PlayAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.canmay.CanAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.because.BecauseAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.rereversei.ReReverseAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.reversethink.ReverseAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.iam.MeAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.about.AboutAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.wiki.WikiAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.do.DoAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.emotion.EmotionAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.oneword.OneWordAdapter',
                },
                {
                    'import_path': 'sugaroid.brain.fun.FunAdapter',
                },
                # {
                #    'import_path': 'sugaroid.brain.idk.DontKnowAdapter',
                # }
            ],
            database_uri='sqlite+pysqlite:///{}/sugaroid.db'.format(
                self.cfgpath),
        )
        # initialize language processs
        self.chatbot.lp = LanguageProcessor()

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

    def invoke_brain(self):
        self.neuron = Neuron(self.chatbot)

    def parse(self, args):

        if type(args) is str:
            response = self.neuron.parse(args)
            self.chatbot.history.append(response)
            return response
        else:
            raise ValueError("Invalid data type passed to Sugaroid.parse")

    def prompt_cli(self):
        try:
            response = self.parse(input('( ဖ‿ဖ) @> '))
            return response
        except (KeyboardInterrupt, EOFError):
            sys.exit()

    def display_cli(self, response):
        print(response)
        if self.audio:
            self.tts.speak(str(response))

    def loop_cli(self):
        while True:
            self.display_cli(self.prompt_cli())

    def loop_gui(self):
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
