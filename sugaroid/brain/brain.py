import logging
import string
import sys
from time import strftime, localtime
from nltk.tokenize import WordPunctTokenizer

from sugaroid.brain.constants import BYE
from sugaroid.brain.preprocessors import normalize

ARITHEMETIC = ['+', '-', '*', '/', '^']


class Neuron:
    def __init__(self, bot):
        self.bot = bot
        logging.info("Sugaroid Neuron Loaded to memory")

    def parse(self, var):
        if 'time' in var:
            return self.time()
        else:
            for i in ARITHEMETIC:
                if i in var:
                    return self.alu(self.normalize(var), i)
            else:
                return self.gen_best_match(var)

    def alu(self, var, i):
        conversation = ' '.join(var)
        return self.gen_arithemetic(conversation)

    def time(self):
        return self.gen_time()

    def gen_best_match(self, parsed):
        return self.bot.get_response(parsed)

    def gen_time(self):
        return 'The current time is {}'.format(strftime("%a, %d %b %Y %H:%M:%S", localtime()))

    def gen_arithemetic(self, parsed):
        return self.bot.get_response(parsed)

    def normalize(self, text):
        return WordPunctTokenizer().tokenize(text)