"""
MIT License

Sugaroid Artificial Intelligence
Chatbot Core
Copyright (c) 2020 Srevin Saju

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

import pyjokes
from chatterbot.logic import LogicAdapter
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize


class JokeAdapter(LogicAdapter):
    """
    Gets a random joke from the Chuck Norris Database
    """
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        normalized = normalize(str(statement).lower())
        if (('tell' in normalized) or ('say' in normalized) or ('crack' in normalized)) and ('joke' in normalized):
            return True
        elif (len(normalized) == 1) and (self.chatbot.lp.similarity("joke", str(statement).lower()) >= 0.9):
            return True
        elif 'joke' in normalized:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        joke = pyjokes.get_joke('en', 'all')
        selected_statement = SugaroidStatement(joke, chatbot=True)
        selected_statement.confidence = 0.95

        emotion = Emotion.lol
        selected_statement.emotion = emotion
        return selected_statement
