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

import time
from chatterbot.logic import LogicAdapter
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import spac_token
from sugaroid.sugaroid import SugaroidStatement


class PlayAdapter(LogicAdapter):
    """
    [DEPRECATED] Plays a game on desktops only
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        return False

    def process(self, statement, additional_response_selection_parameters=None):
        response = 'I can\t run the same game again. Soz!'
        confidence = .5
        sent = []
        for i in games:
            sent.append('play the game {}'.format(i))
            sent.append('can you play the game {}'.format(i))
        cos = []
        for j in sent:
            cos.append(self.chatbot.lp.similarity(j, str(statement)))
        maxcos = max(cos)
        response = 'Ok, I guess your game was great!'
        try:
            exec('from freegames import {}'.format(self.game))
        except Exception as e:
            response = 'Oops, it cant run on your system'
        import os
        try:
            if os.environ['SUGAROID'] == 'CLI':
                input('Enter any key to continue to Sugaroid')
            elif os.environ['SUGAROID'] == 'GUI':
                time.sleep(5)
        except KeyError:
            pass
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = maxcos

        selected_statement.emotion = Emotion.neutral
        return selected_statement
