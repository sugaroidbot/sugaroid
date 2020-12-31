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

from chatterbot.logic import LogicAdapter
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize
from sugaroid.sugaroid import SugaroidStatement


class TriviaAdapter(LogicAdapter):
    """
    Resets the game of a trivia game
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.cos = None
        self.normalized = None
        self.bool = None

    def can_process(self, statement):
        self.normalized = normalize(str(statement).lower())
        if ('yes' in self.normalized) or ('no' in self.normalized) or ('true' in self.normalized) or \
                ('false' in self.normalized):
            boolean = True
        else:
            boolean = False
        if self.chatbot.globals['trivia_answer'] and boolean:
            return True
        else:
            self.chatbot.globals['trivia_answer'] = None
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        selected_statement = SugaroidStatement('Ok!', chatbot=True)
        selected_statement.confidence = 0
        selected_statement.emotion = Emotion.neutral
        return selected_statement
