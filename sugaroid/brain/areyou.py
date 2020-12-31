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

from chatterbot.logic import LogicAdapter
from nltk import pos_tag
from sugaroid.brain.constants import WHO_AM_I, WHO_ARE_YOU, SUGAROID
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.preprocessors import normalize
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.version import VERSION


class AreYouAdapter(LogicAdapter):
    """
    Adapter to process statements beginning with 'are you'
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        self.token = pos_tag(self.normalized)
        if str(statement).strip().lower().startswith('are'):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        confidence = 1
        # FIXME Creates unusual response

        if 'do you know' in str(statement).lower():
            if self.normalized[0] == 'do':
                self.normalized.pop(0)
                if self.normalized[0] == 'you':
                    self.normalized.pop(0)
                    if self.normalized[0] == 'know':
                        self.normalized.pop(0)

        if 'i' in self.normalized:
            response = random_response(WHO_AM_I)
        elif 'you' in self.normalized:
            if 'to' in self.normalized:
                confidence = 0.5
                response = 'You!'
            else:
                v = VERSION
                response = "\n{} \n{}. \nBuild: {}".format(
                    SUGAROID[0], random_response(WHO_ARE_YOU), v.get_commit())
        else:
            response = 'check the wiki'
            confidence = 0

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        emotion = Emotion.neutral
        selected_statement.emotion = emotion

        return selected_statement
