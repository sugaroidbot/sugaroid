"""
MIT License

Sugaroid Artificial Inteligence
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
from chatterbot.logic import LogicAdapter
from chatterbot.trainers import ListTrainer
from sugaroid.brain.postprocessor import random_response, any_in
from sugaroid.brain.constants import ASK_AND_YOU_SHALL_RECEIVE, SEEK_AND_YOU_SHALL_FIND, THANK
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.brain.ooo import Emotion


class InterruptAdapter(LogicAdapter):
    __adapter__ = 'interr'

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.tokenized = None
        self.nn = False

    def can_process(self, statement):

        if self.chatbot.interrupt == 2:
            logging.info("InterruptAdapter: Found Discord")
            self.tokenized = self.chatbot.lp.nlp(str(statement))
            if 6 > len(self.tokenized) > 2:
                for i in self.tokenized:
                    if str(i.tag_).startswith('NNP'):
                        self.nn = i.lemma_
                        if self.nn in self.chatbot.globals['learned']:
                            return False
                return True
            else:
                self.chatbot.interrupt = False
                return False
        elif self.chatbot.interrupt == 1:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None, username=None):
        if self.chatbot.interrupt == 2:
            if self.nn:
                response = "{} {} what is {}" .format(
                    random_response(ASK_AND_YOU_SHALL_RECEIVE),
                    random_response(SEEK_AND_YOU_SHALL_FIND),
                    self.nn)
                self.chatbot.interrupt = self.nn
            else:
                if username:
                    response = "{} {} what is actually meant in {}'s message?" \
                        .format(
                            random_response(ASK_AND_YOU_SHALL_RECEIVE),
                            random_response(SEEK_AND_YOU_SHALL_FIND),
                            username
                        )

                else:
                    response = "{} {} what is actually meant in the previous message?" \
                        .format(
                            random_response(ASK_AND_YOU_SHALL_RECEIVE),
                            random_response(SEEK_AND_YOU_SHALL_FIND),
                        )
                self.chatbot.interrupt = str(statement)
        else:
            if any_in(['no', 'not', 'later', 'busy', 'nah'], self.tokenized) or \
                    (('next' in self.tokenized or 'another' in self.tokenized) and 'time' in self.tokenized):
                response = 'Ok.'
                self.chatbot.interrupt = False
            else:
                response = random_response(THANK)
                learner = ListTrainer(self.chatbot)
                learner.train([
                    'What is {} ?'.format(self.chatbot.interrupt),
                    str(statement)
                ])
                self.chatbot.globals['learned'].append(self.chatbot.interrupt)
                self.chatbot.interrupt = False
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = 9
        emotion = Emotion.lol
        selected_statement.emotion = emotion
        return selected_statement
