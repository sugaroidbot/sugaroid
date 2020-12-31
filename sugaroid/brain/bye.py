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


import random
import sys

from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.constants import BYE, BYE_RESPONSE
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize
from sugaroid.sugaroid import SugaroidStatement


class ByeAdapter(LogicAdapter):
    """
    Destroys Sugaroid on bye
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.normalized = None
        self.intersect = None

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        if len(self.normalized) >= 2:
            for i in range(0, len(self.normalized) - 2):
                if (self.normalized[i] == 'see') and (self.normalized[i + 1] == 'you'):
                    return True
        self.intersect = set(self.normalized).intersection(set(BYE))
        if self.intersect and not ('can' in self.normalized):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        emotion = Emotion.neutral
        confidence = 1
        selected_statement = SugaroidStatement(random_response(BYE_RESPONSE), chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        selected_statement.adapter = None
        return selected_statement
