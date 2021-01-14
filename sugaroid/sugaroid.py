"""
MIT License

Sugaroid Artificial Intelligence
Chatbot Core
Copyright (c) 2020-2021 Srevin Saju
Copyright (c) 2021 The Sugaroid Project

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
import time

from colorama import Fore, Style
from colorama import init as colorama_init
from emoji import emojize

from sugaroid.backend.sql import SqlDatabaseManagement, PossibleSQLInjectionPanicError
from sugaroid.brain.constants import SUGAROID_INTRO, REPEAT
from sugaroid.brain.postprocessor import random_response
from sugaroid.config.config import ConfigManager
from sugaroid.brain.brain import Neuron
from sugaroid.trainer.trainer import SugaroidTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from sugaroid.brain.utils import LanguageProcessor
import logging
import os
import sys
import warnings
from chatterbot.conversation import Statement
from sugaroid.brain.ooo import Emotion
from sugaroid.version import VERSION

warnings.filterwarnings("ignore")

try:
    from sugaroid.tts.tts import Text2Speech
    AUD_DEPS = True
except ModuleNotFoundError:
    AUD_DEPS = False


if os.getenv('SUGAROID_DEBUG') in ('true', 'True'):
    # set the verbosity
    verbosity = logging.INFO
    logging.basicConfig(level=verbosity)


try:
    from PyQt5 import QtCore, QtWidgets  # noqa:
    from PyQt5.QtWidgets import QApplication  # noqa:

    GUI_DEPS = True
except (ModuleNotFoundError, ImportError) as e:
    print("warn: Could not import PyQt5", e)
    GUI_DEPS = False


SPACY_LANG_PROCESSOR = LanguageProcessor()


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
        self.chatbot = kwargs.get('chatbot', False)
        if not self.chatbot:
            self.doc = SPACY_LANG_PROCESSOR.nlp(text)
        else:
            self.doc = None


class SugaroidBot(ChatBot):
    """
    The SugaroidBot inherits the class local variables from the Chat
    """

    def __init__(self, name, **kwargs):
        ChatBot.__init__(self, name=name, **kwargs)
        self.lp = LanguageProcessor()
        self.spell_checker = False  # FIXME
        self.discord = False
        self.authors = []
        self.interrupt = 0

        self.report = False
        self.globals = {
            'emotion': Emotion.neutral,
            'history': {
                'total': [0],
                'user': [0],
                'types': [0]
            },
            'reversei': {
                'enabled': False,
                'uid': None,
                'type': None,
            },
            'akinator': {
                'enabled': False,
                'class': None
            },
            'hangman': {
                'enabled': False,
                'class': None
            },
            'adapters': [],
            'fun': True,
            'update': False,
            'last_news': None,
            'USERNAME': None,
            'learn': False,
            'trivia_answer': None,
            'learn_last_conversation': [],
            'DEBUG': {}
        }
        # self.emotion = Emotion.neutral

    def get_global(self, key):
        """
        Returns a global constant
        :param key:
        :return:
        """
        return self.globals.get(key, None)

    def toggle_discord(self):
        """
        Toggle Discord Configuration
        :return:
        """
        self.discord = not self.discord

    def set_emotion(self, emotion):
        """
        Sets the emotion for the chatbot globally.
        (Deprecated)
        :param emotion:
        :return:
        """
        self.emotion = emotion

    def reset_variables(self):
        self.globals.update({
            'emotion': Emotion.neutral,
            'history': {
                'total': [0],
                'user': [0],
                'types': [0]
            },
            'reversei': {
                'enabled': False,
                'uid': None,
                'type': None,
                'data': None
            },
            'akinator': {
                'enabled': None,
                'class': None
            },
            'hangman': {
                'enabled': False,
                'class': None
            },
            'learned': [],
            'fun': True,
            'update': False,
            'last_news': None,
            'USERNAME': None,
            'learn': False,
            'trivia_answer': None,
            'learn_last_conversation': [],
            'DEBUG': {}
        })
        self.authors = []
        self.spell_checker = False  # FIXME

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
        return self.get_global('USERNAME')

    def generate_response(
            self,
            input_statement,
            additional_response_selection_parameters=None):
        """
        Return a response based on a given input statement.

        :param input_statement: The input statement to be processed.
        """

        results = []
        result = None
        max_confidence = -1
        final_adapter = None
        interrupt = False
        adapter_index = 0
        for adapter in self.logic_adapters:
            if adapter.class_name == 'InterruptAdapter':
                interrupt = adapter
            if adapter.can_process(input_statement):

                output = adapter.process(
                    input_statement, additional_response_selection_parameters)
                results.append(output)

                self.logger.info(
                    '{} selected "{}" as a response with a '
                    'confidence of {}'.format(
                        adapter.class_name, output.text, output.confidence
                    )
                )

                if output.confidence > max_confidence:
                    result = output
                    final_adapter = adapter.class_name
                    max_confidence = output.confidence
                if max_confidence >= 9:
                    # optimize: if the confidence is greater than 9,
                    # just break dude, why check more
                    break
                elif max_confidence >= 1 and adapter_index >= 3:
                    # optimize: if the confidence is greater than 9,
                    # just break dude, why check more
                    break
            else:
                self.logger.info(
                    'Not processing the statement using {}'.format(
                        adapter.class_name)
                )
            adapter_index += 1
        if max_confidence < 0.5:
            if self.discord:
                if interrupt and interrupt.can_process(input_statement):
                    try:
                        username = self.authors[-1]
                    except IndexError:
                        username = None

                    output = interrupt.process(
                        input_statement,
                        username=username
                    )
                    self.logger.info(
                        '{} selected "{}" as a response '
                        'with a confidence of {}'.format(
                            interrupt.class_name,
                            output.text,
                            output.confidence
                        )
                    )

                    result = output
                    final_adapter = interrupt.class_name
                    max_confidence = output.confidence

        self.gen_debug(
            statement=input_statement,
            adapter=final_adapter,
            confidence=max_confidence,
            results=result
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
                    if result_options[result_string].statement.confidence < \
                            result_option.confidence:
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

        if adapter_type and \
                adapter_type not in ['NewsAdapter', 'LearnAdapter']:
            if adapter_type in self.globals['history']['types']:
                if adapter_type == self.globals['history']['types'][-1]:
                    result.text = random_response(REPEAT)
                elif len(self.globals['history']['types']) > 2:
                    if adapter_type == self.globals['history']['types'][-2]:
                        result.text = random_response(REPEAT)

        self.globals['history']['types'].append(adapter_type)

        response = SugaroidStatement(
            text=result.text,
            in_response_to=input_statement.text,
            conversation=input_statement.conversation,
            persona='sugaroid:' + self.name,
            chatbot=True
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

        self.globals['DEBUG']['number_of_conversations'] = \
            self.globals['DEBUG'].get('number_of_conversations', 0) + 1
        _id = self.globals['DEBUG']['number_of_conversations']
        val = dict()
        val['adapter'] = adapter
        val['confidence'] = confidence
        val['response'] = results
        val['request'] = str(statement)
        self.globals['DEBUG'][_id] = val

    def get_response(self, statement=None, **kwargs):
        """
        Return the bot's response based on the input.

        :param statement: An statement object or string.
        :returns: A response to the input.
        :rtype: Statement

        :param additional_response_selection_parameters: Parameters to pass to
            chat bot's logic adapters to control response selection.
        :type additional_response_selection_parameters: dict

        :param persist_values_to_response: Values that should be saved to the
            response that the chat bot generates.
        :type persist_values_to_response: dict
        """
        Statement = SugaroidStatement

        additional_response_selection_parameters = \
            kwargs.pop('additional_response_selection_parameters', {})

        persist_values_to_response = \
            kwargs.pop('persist_values_to_response', {})

        if isinstance(statement, str):
            kwargs['text'] = statement

        if isinstance(statement, dict):
            kwargs.update(statement)

        if statement is None and 'text' not in kwargs:
            raise self.ChatBotException(
                'Either a statement object or a "text" keyword '
                'argument is required. Neither was provided.'
            )

        if hasattr(statement, 'serialize'):
            kwargs.update(**statement.serialize())

        tags = kwargs.pop('tags', [])

        text = kwargs.pop('text')

        input_statement = SugaroidStatement(text=text, **kwargs)

        input_statement.add_tags(*tags)

        # Preprocess the input statement
        for preprocessor in self.preprocessors:
            input_statement = preprocessor(input_statement)

        # Make sure the input statement has its search text saved

        if not input_statement.search_text:
            try:
                input_statement.search_text = \
                    self.storage.tagger.get_text_index_string(
                        input_statement.text
                    )
            except AttributeError:
                input_statement.search_text = \
                    self.storage.tagger.get_bigram_pair_string(
                        input_statement.text
                    )

        if not input_statement.search_in_response_to and \
                input_statement.in_response_to:
            try:
                input_statement.search_in_response_to = \
                    self.storage.tagger.get_text_index_string(
                        input_statement.in_response_to
                    )
            except AttributeError:
                input_statement.search_in_response_to = \
                    self.storage.tagger.get_bigram_pair_string(
                        input_statement.in_response_to
                    )

        response = self.generate_response(
            input_statement,
            additional_response_selection_parameters
        )

        # Update any response data that needs to be changed
        if persist_values_to_response:
            for response_key in persist_values_to_response:
                response_value = persist_values_to_response[response_key]
                if response_key == 'tags':
                    input_statement.add_tags(*response_value)
                    response.add_tags(*response_value)
                else:
                    setattr(input_statement, response_key, response_value)
                    setattr(response, response_key, response_value)

        if not self.read_only:
            self.learn_response(input_statement)

            # Save the response generated for the input
            self.storage.create(**response.serialize())

        return response


class Sugaroid:
    """
    Sugaroid
    Initates the chatbot class and connects logic Adapters together.
    Initates the ConfigManager to store sugaroid data and connects scans
    sys.argv

    """

    def __init__(self, readonly=True):
        self.trainer = None
        self.corpusTrainer = None
        self.neuron = None
        self.audio = 'audio' in sys.argv
        self.cfgmgr = ConfigManager()
        self.cfgpath = self.cfgmgr.get_cfgpath()
        self.database = SqlDatabaseManagement(
            os.path.join(self.cfgpath, 'sugaroid_internal.db'))
        self.database_exists = os.path.exists(
            os.path.join(self.cfgpath, 'sugaroid.db'))
        self.commands = [
            'sugaroid.brain.debug.DebugAdapter',
            'sugaroid.brain.interrupt.InterruptAdapter',
            'sugaroid.brain.learn.LearnAdapter',
        ]
        self.adapters = [
            'sugaroid.brain.yesno.BoolAdapter',
            'sugaroid.brain.aki.AkinatorAdapter',
            'sugaroid.brain.hangman.HangmanAdapter',
            'sugaroid.brain.either.OrAdapter',
            'sugaroid.brain.ok.OkayAdapter',
            'sugaroid.brain.bye.ByeAdapter',
            'sugaroid.brain.time.TimeAdapter',
            'sugaroid.brain.convert.CurrencyAdapter',
            'sugaroid.brain.trivia.TriviaAdapter',
            'sugaroid.brain.whoami.WhoAdapter',
            'sugaroid.brain.news.NewsAdapter',
            'sugaroid.brain.joke.JokeAdapter',
            'sugaroid.brain.play.PlayAdapter',
            'sugaroid.brain.let.LetAdapter',
            'sugaroid.brain.whatwhat.WhatWhatAdapter',
            'sugaroid.brain.waitwhat.WaitWhatAdapter',
            'sugaroid.brain.assertive.AssertiveAdapter',
            'sugaroid.brain.canmay.CanAdapter',
            'sugaroid.brain.because.BecauseAdapter',
            'sugaroid.brain.rereversei.ReReverseAdapter',
            'sugaroid.brain.reversethink.ReverseAdapter',
            'sugaroid.brain.covid.CovidAdapter',
            'sugaroid.brain.myname.MyNameAdapter',
            'sugaroid.brain.iam.MeAdapter',
            'sugaroid.brain.about.AboutAdapter',
            'sugaroid.brain.wiki.WikiAdapter',
            'sugaroid.brain.dolike.DoLikeAdapter',
            'sugaroid.brain.feel.FeelAdapter',
            'sugaroid.brain.dolike.DoLikeAdapter',
            'sugaroid.brain.do.DoAdapter',
            'sugaroid.brain.emotion.EmotionAdapter',
            'sugaroid.brain.dis.DisAdapter',
            'sugaroid.brain.twoword.TwoWordAdapter',
            'sugaroid.brain.oneword.OneWordAdapter',
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

        self.chatbot = SugaroidBot(
            'Sugaroid',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=self.commands +
            [
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                                   'maximum_similarity_threshold': 0.80
                }
            ] + self.adapters,
            database_uri='sqlite+pysqlite:///{}/sugaroid.db'.format(self.cfgpath),
            read_only=readonly
        )
        self.chatbot.globals['adapters'] = self.adapters

        self.read()
        self.invoke_brain()

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
            self.chatbot.globals['history']['total'].append(response)
            self.chatbot.globals['history']['user'].append(args)
            success_time = time.time()
            delta_time = success_time - preflight_time
            try:
                _text_response = response.text
            except AttributeError:
                _text_response = response

            assert isinstance(_text_response, str)
            if 'gui' not in sys.argv:
                try:
                    self.database.append(
                        statement=_text_response,
                        in_reponse_to=args,
                        time=preflight_time,
                        processing_time=delta_time
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

        response = self.parse(input(
            Fore.CYAN +
            '( ဖ‿ဖ) @> ' + Fore.RESET))
        return response

    def display_cli(self, response):
        """
        Classic display adapter for TTY Sugaroid Command Line Interface
        :param response:
        :return:
        """
        try:
            print(
                Style.BRIGHT + Fore.GREEN +
                "sugaroid: " + Fore.RESET + Style.RESET_ALL + Fore.BLUE +
                emojize(response.text) + Fore.RESET + "\n"
            )
        except AttributeError:
            print(
                Style.BRIGHT + Fore.GREEN +
                "sugaroid: " + Fore.RESET + Style.RESET_ALL + Fore.BLUE +
                emojize(response) + Fore.RESET + "\n"
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
            pass
        self.database.close()


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
    read_only = False if 'update' in sys.argv else True
    print("Sugaroid v{} RO:{}\n".format(VERSION, read_only))
    sg = Sugaroid(readonly=read_only)
    if 'gui' in sys.argv:
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
