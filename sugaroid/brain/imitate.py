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

from chatterbot.logic import LogicAdapter
from sugaroid.brain.postprocessor import random_response

from sugaroid.brain.constants import IMITATE
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize, spac_token


class ImitateAdapter(LogicAdapter):
    """
    Handles statements involving imitations of some sentences
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.normalized = None

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        more_words = len(self.normalized) > 3
        logging.info("ImitatorSensei: userhistory {}, history: {}".format(
            self.chatbot.globals['history']['user'], self.chatbot.globals['history']['total']))
        if self.chatbot.globals['history']['user'][-1] and self.chatbot.globals['history']['total'][-1] and more_words:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        emotion = Emotion.lol
        sim = self.chatbot.lp.similarity(str(statement), str(
            self.chatbot.globals['history']['total'][-1]))
        logging.info("ImitatorSensei compared {} and {}. Sim: {}"
                     .format(str(statement), self.chatbot.globals['history']['user'][-1], sim))
        if sim > 0.8:
            response = random_response(IMITATE)
            confidence = sim
        else:
            response = 'Ok!'
            confidence = 0
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        return selected_statement
