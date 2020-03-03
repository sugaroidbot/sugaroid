import logging

from time import strftime, localtime
from nltk.tokenize import WordPunctTokenizer

from sugaroid.brain.preprocessors import preprocess

ARITHEMETIC = ['+', '-', '*', '/', '^']


class Neuron:
    def __init__(self, bot):
        self.bot = bot
        if self.bot.spell_checker:
            from spellchecker import SpellChecker
            self.spell = SpellChecker(distance=1)
            # some privileges only for the creator
            self.spell.known(
                ['Sugaroid', 'Sugarlabs', "sugar", 'Srevin', 'Saju'])
        else:
            self.spell = False
        logging.info("Sugaroid Neuron Loaded to memory")

    def parse(self, var):
        if var.isspace():
            return 'Type something to begin'
        if 'time' in var:
            response = self.time()
        else:
            for i in ARITHEMETIC:
                if i in var:
                    response = self.alu(self.normalize(var), i)
                    break
            else:
                if self.spell:
                    wt = var.split(' ')
                    ct = []
                    for i in wt:
                        ct.append(self.spell.correction(i))
                    response = self.gen_best_match(' '.join(ct))
                else:

                    preprocessed = preprocess(var)
                    response = self.gen_best_match(preprocessed)

        return response

    def alu(self, var, i):
        conversation = ' '.join(var)
        return self.gen_arithmetic(conversation)

    def time(self):
        return self.gen_time()

    def gen_best_match(self, parsed):
        return self.bot.get_response(parsed)

    @staticmethod
    def gen_time():
        return 'The current time is {}'.format(strftime("%a, %d %b %Y %H:%M:%S", localtime()))

    def gen_arithmetic(self, parsed):
        return self.bot.get_response(parsed)

    @staticmethod
    def normalize(text):
        return WordPunctTokenizer().tokenize(text)
