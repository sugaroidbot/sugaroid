"""
MIT License

Sugaroid Artificial Inteligence
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
import logging
from chatterbot.logic import LogicAdapter
from nltk import pos_tag
from sugaroid.brain.constants import WHO_AM_I, WHO_ARE_YOU, SUGAROID, GREET, BURN_IDK, I_AM
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.preprocessors import normalize
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.ver import version


class MyNameAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        self.token = pos_tag(self.normalized)
        if str(statement).strip().lower().startswith('my name is'):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        confidence = 1
        # FIXME Creates unusual response

        nl = self.chatbot.lp.tokenize(str(statement))

        for i in nl:
            if (i.lower_ == 'my') or (i.lemma_ == 'be') or (i.lower_ == 'name'):
                continue
            logging.info("{} {}".format(i, i.pos_))
            if (i.pos_ == 'NOUN') or (i.pos_ == 'PROPN'):
                response = random_response(GREET).format(str(i.text).capitalize())
                selected_statement = SugaroidStatement(response)
                selected_statement.confidence = confidence
                emotion = Emotion.positive
                selected_statement.emotion = emotion
                self.chatbot.username = i.text
                return selected_statement
        else:
            confidence = 0
            elected_statement = SugaroidStatement(response)
            selected_statement.confidence = confidence
            emotion = Emotion.neutral
            selected_statement.emotion = emotion

            return selected_statement

