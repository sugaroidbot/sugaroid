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
from sugaroid.brain.constants import TIME, TIME_RESPONSE
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.preprocessors import normalize, current_time
from sugaroid.sugaroid import SugaroidStatement


class TimeAdapter(LogicAdapter):
    """
    Provides time and time related functions except time conversion
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.normalized = None
        self.intersect = None

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        self.intersect = set(self.normalized).intersection(set(TIME))
        if self.intersect:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        emotion = Emotion.positive
        hour, minutes = current_time()
        alert = False
        if hour <= 0:
            alert = True
            time = ''
        elif hour <= 11:
            time = 'morning'
        elif hour <= 15:
            time = 'afternoon'
        elif hour <= 19:
            time = 'evening'
        elif hour <= 20:
            time = 'night'
        else:
            alert = True
            time = ''
        if not alert:
            if (time in self.intersect) or ('time' in self.intersect):
                response = 'Good {}'.format(time)
            else:
                response = 'Good {}. {}'.format(time, random_response(
                    TIME_RESPONSE).format(list(self.intersect)[0]))
        else:
            if self.chatbot.lp.similarity('good night', str(statement)) > 0.9:
                response = 'Sweet Dreams'
                emotion = Emotion.sleep
            else:
                response = "You are staying up late, you should sleep right now."
                emotion = Emotion.seriously
        if "what" in str(statement).lower():
            # the user might be asking the time
            # so we have to inform it instead of wishing
            # the person good morning
            response = "The current time is {:02d}:{:02d}".format(hour, minutes)
            emotion = Emotion.adorable
        selected_statement = SugaroidStatement(
            "{}".format(response), chatbot=True)
        selected_statement.confidence = 1

        selected_statement.emotion = emotion

        return selected_statement
