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


from chatterbot.logic import LogicAdapter
from sugaroid.brain.constants import EMOJI_SMILE
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.sugaroid import SugaroidStatement


cl = [
    ['', '', ''],
    ['', '', '']
]


class FunAdapter(LogicAdapter):
    """
    FunAdapter
    Gives a random response, because Sugaroid tries not to say I don't know
    """
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        if self.chatbot.fun:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        emotion = Emotion.neutral
        confidence = 0.1
        parsed = str(statement)
        if 'not' in parsed:
            suffix = " either. "
            prefix = ""
            emotion = Emotion.wink
        else:
            interrogation = False
            token = self.chatbot.lp.tokenize(str(statement))
            for i in token:
                if i.tag_ == '.' and i.text == '?':
                    interrogation = True
                if i.tag_ == 'WP':
                    interrogation = True

            if interrogation:
                prefix, suffix = '', ''
                parsed = 'Well, I would also ask that question to you. {}'.format(str(statement).lower())
            else:
                suffix = " too {}".format(random_response(EMOJI_SMILE))
                prefix = "Let me try that, "
                emotion = Emotion.wink

        selected_statement = SugaroidStatement("{pre}{main}{fix}".format(pre=prefix, main=parsed, fix=suffix))
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        return selected_statement
