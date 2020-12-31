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


import logging
from time import strftime, localtime

from chatterbot.conversation import Statement
from chatterbot.logic import MathematicalEvaluation
from nltk.tokenize import WordPunctTokenizer

from sugaroid.brain.preprocessors import preprocess

ARITHMETIC = ['+', '-', '*', '/', '^']


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
            self.spell.known(
                ['Sugaroid', 'Sugarlabs', "sugar", 'Srevin', 'Saju']
            )

        logging.info("Sugaroid Neuron Loaded to memory")

    def parse(self, var):
        if var.isspace():
            return 'Type something to begin'
        if 'time ' in var:
            response = self.time()
        else:

            for i in ARITHMETIC:
                if i in var:
                    response = self.alu(self.normalize(var))
                    if str(response).strip() == '-':
                        pass
                    elif response:
                        break
            else:
                if self.bot.spell_checker:
                    wt = var.split(' ')
                    ct = []
                    for i in wt:
                        ct.append(self.spell.correction(i))
                    response = self.gen_best_match(' '.join(ct))
                else:

                    preprocessed = preprocess(var)
                    response = self.gen_best_match(preprocessed)

        return response

    def alu(self, var):
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
        try:
            me = MathematicalEvaluation(self.bot)
            return me.process(Statement(parsed))
        except Exception as e:
            return False

    @staticmethod
    def normalize(text):
        return WordPunctTokenizer().tokenize(text)
