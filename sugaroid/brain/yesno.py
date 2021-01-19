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

import nltk
from chatterbot.logic import LogicAdapter
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize
from sugaroid.brain.rereversei import reset_reverse
from sugaroid.sugaroid import SugaroidStatement


class BoolAdapter(LogicAdapter):
    """
    Processes Boolean based answers
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.chatbot = chatbot
        self.normalized = None
        self.intersect = None
        self.normalized = None
        self.tagged = None
        self.last_normalized = None
        self.bool = None

    def can_process(self, statement):
        self.normalized = normalize(str(statement).lower())
        if self.chatbot.globals["akinator"]["enabled"]:
            return False
        elif ('yes' in self.normalized) or ('yea' in self.normalized) or (
                'no' in self.normalized) or ('true' in self.normalized) or ('false' in self.normalized):
            if ('yes' in self.normalized) or ('yea' in self.normalized) or ('true' in self.normalized):
                self.bool = True
            else:
                self.bool = False
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        bool_yes = self.bool
        emotion = Emotion.neutral
        if self.chatbot.report:
            if bool_yes:
                response = 'Sure, I would connect to the Developer to report this issue right away'
                self.chatbot.report = False
                # TODO: Add report function
                # report_here() FIXME
            else:
                response = 'Ok, I will not report it.'
                self.chatbot.report = False
            confidence = 1.0
        elif self.chatbot.globals['trivia_answer']:
            if self.chatbot.globals['trivia_answer'] == self.bool:
                response = "Exactly! You are right"
                reset_reverse(self)
            else:
                response = 'Nope, You got it wrong. The correct answer was {}'.format(
                    self.chatbot.globals['trivia_answer'])
                reset_reverse(self)
            self.chatbot.globals['trivia_answer'] = None
            confidence = 1.1
        else:
            if self.chatbot.globals['history']['total'][-1] == 0:
                if bool_yes:
                    response = 'I shall annoy you. A big NO'
                else:
                    response = 'I would rather have fun, YES ?'
            else:
                md = False
                vb = False
                nn = False
                self.last_normalized = normalize(
                    str(self.chatbot.globals['history']['total'][-1]))
                self.tagged = nltk.pos_tag(self.last_normalized)
                iteration = 0
                for j in self.tagged:
                    if j[1].startswith('MD'):
                        md = True
                    elif (j[1].startswith('VB')) and (not j[0] == 'be'):
                        vb = True
                        verb = j[0]
                    elif j[1].startswith('NN'):
                        if not nn:
                            nn_index = iteration
                        nn = True
                        noun = j[0]
                    iteration += 1

                if md:
                    if nn:
                        some_nouns = ' '.join(self.last_normalized[nn_index:])
                    if bool_yes:
                        if nn:
                            response = 'Ok, here comes your {} 😝😝'.format(
                                some_nouns)
                        elif vb:
                            response = 'You should {}'.format(
                                verb.replace('ing', ''))
                        else:
                            response = 'I will keep thinking 🚀'
                    else:
                        if nn:
                            response = 'Ok, I will have the {}'.format(
                                some_nouns)
                        elif vb:
                            response = "You shouldn't {} then".format(
                                verb.replace('ing', ''))
                        else:
                            response = 'Okay!'
                else:
                    if bool_yes:
                        response = "Why is this 'yes' here? I couldn't find the question. Anyway, I agree with you"
                    else:
                        response = 'No? for what?.'
                        emotion = Emotion.angry

            confidence = 0.95
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence

        selected_statement.emotion = emotion

        return selected_statement
