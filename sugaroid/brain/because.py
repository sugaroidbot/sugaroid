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


from difflib import SequenceMatcher

import nltk
from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import reverse
from sugaroid.brain.preprocessors import normalize
from sugaroid.sugaroid import SugaroidStatement


class BecauseAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.chatbot = chatbot

    def can_process(self, statement):
        self.normalized = normalize(str(statement))

        if 'because' in self.normalized:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        # add emotion output
        adj = None
        verb = None
        confidence = 0.90
        last_response = self.chatbot.history[-1]
        emotion = Emotion.neutral
        self.last_normalized = normalize(str(last_response))
        print(self.last_normalized)
        if last_response:
            self.tagged_last = nltk.pos_tag(self.last_normalized)
            self.tagged_now = nltk.pos_tag(self.normalized)
            print(self.tagged_last)
            print(self.tagged_now)
            sm = SequenceMatcher(None, self.tagged_last, self.tagged_now)
            for i in self.tagged_now:
                if i[1] == 'JJ':
                    adj = i[0]
                elif i[1] == 'VB' and (not i[0] == 'be'):
                    verb = i[0]
            print(sm.ratio())
            if sm.ratio() > 0.5:
                if adj:
                    response = 'Well, Its not a good reason for me to be {}'.format(
                        adj)
                else:
                    response = 'Well, its not a good reason you have told me 😭'
            else:
                if verb:
                    if verb in ['think', 'breath', 'eat', 'hear', 'feel', 'taste']:
                        response = 'Robots are computer devices. I cannot {}'.format(
                            verb.replace('ing', ''))
                        emotion = Emotion.cry
                    else:
                        response = "I may not be able to {}. " \
                                   "This might not be my builtin quality".format(
                                       verb.replace('ing', ''))
                        emotion = Emotion.cry_overflow
                else:
                    if adj:
                        response = 'I will try to be more {} in future'.format(
                            adj)
                        emotion = Emotion.adorable
                    else:
                        response = 'Are you sure this is the reason? I would love to report to my creator.'
                        self.chatbot.report = True
                        emotion = Emotion.non_expressive_left

        else:
            response = 'Well, I cannot think of saying something. Your conversation began with reason. 🤯'
            emotion = Emotion.angry

        selected_statement = SugaroidStatement(response)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        selected_statement.adapter = None
        return selected_statement
