"""
Sugaroid Neuron preprocesses the text and fixes user input
problems so that it is easier for the other adapters to process.
Sugaroid Neuron replaces spellings (when spell checker is enabled)
and prefers the Arithemetic operator to process the statements 
when necessary
"""

import logging
from time import strftime, localtime

from chatterbot.conversation import Statement
from chatterbot.logic import MathematicalEvaluation
from nltk.tokenize import WordPunctTokenizer

from sugaroid.brain.preprocessors import preprocess

ARITHMETIC = ["+", "-", "*", "/", "^"]


class Neuron:
    """
    Main processing object.
    sugaroid.brain.Neuron classifies texts initially
    """

    def __init__(self, bot):
        self.bot = bot
        if self.bot.spell_checker:
            from spellchecker import SpellChecker

            self.spell = SpellChecker(distance=1)
            # some privileges only for the creator
            self.spell.known(["Sugaroid", "Sugarlabs", "sugar", "Srevin", "Saju"])

        logging.info("Sugaroid Neuron Loaded to memory")

    def parse(self, var):
        """
        Ask sugaroid to parse a statement. ``Neuron.parse`` 
        processes the statement with different adapters and 
        returns a SugaroidStatement, Statement, or a string object
        on every instance processed.

            >>> neuron = Neuron(bot)
            >>> neuron.parse("Hello World")
            Hi There!

        """
        if var.isspace():
            return "Type something to begin"
        if var.lower().strip() == "time":
            response = self.time()
        else:

            for i in ARITHMETIC:
                if i in var:
                    response = self.alu(self.normalize(var))
                    if str(response).strip() == "-" or str(response).strip() == "/":
                        pass
                    elif response:
                        break
            else:
                if self.bot.spell_checker:
                    wt = var.split(" ")
                    ct = []
                    for i in wt:
                        ct.append(self.spell.correction(i))
                    response = self.gen_best_match(" ".join(ct))
                else:

                    preprocessed = preprocess(var)
                    response = self.gen_best_match(preprocessed)

        return response

    def alu(self, var):
        """
        Puts spaces between arithemetic operators
        """
        conversation = " ".join(var)
        return self.gen_arithmetic(conversation)

    def time(self):
        """
        Returns the current time
        """
        return self.gen_time()

    def gen_best_match(self, parsed):
        """
        Returns the best match of ``parsed`` object in the 
        the list of stored data

        :type parsed: str
        :return The closed match to ``parsed``
        """
        return self.bot.get_response(parsed)

    @staticmethod
    def gen_time() -> str:
        """
        Returns the current local time, formatted by strftime

        :return: The current local time
        :rtype: str
        """
        return "The current time is {}".format(
            strftime("%a, %d %b %Y %H:%M:%S", localtime())
        )

    def gen_arithmetic(self, parsed: str):
        """
        Parse a arithemetic statement using the
        ``MathematicalEvaluation`` Adapter
        """
        try:
            me = MathematicalEvaluation(self.bot)
            return me.process(Statement(parsed))
        except Exception:
            return None

    @staticmethod
    def normalize(text: str) -> str:
        """
        Normalize a text using ``WordPunctTokenizer``

        :param text: The text to be normalized
        :type text: str
        :return: The normalized text
        :rtype: str
        """
        return WordPunctTokenizer().tokenize(text)
