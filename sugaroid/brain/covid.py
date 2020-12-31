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
import logging

from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response, any_in
from sugaroid.brain.preprocessors import normalize
from sugaroid.sugaroid import SugaroidStatement


ABOUT_CORONAVIRUS = """
Coronavirus disease (COVID-19) is an infectious disease caused by a new virus.
The disease causes respiratory illness (like the flu) with symptoms such as a
cough, fever, and in more severe cases, difficulty breathing. You can protect
yourself by washing your hands frequently, avoiding touching your face, and
avoiding close contact (1 meter or 3 feet) with people who are unwell.

Lets stay safe during covid 19 by staying at home.
I can do an approximation if you do have coronavirus.
"""

COVID_QUESTIONS = [
    [1, 'Do you have fever?', 1],
    [2, 'Do you have cough?', 1],
    [3, 'Do you have shortness of breath', 2],
    [4, 'Have you travelled outside your house in the last 14 days?', 1],
    [5, 'Have you been tested for covid before, with negative results?', 0.1],
    [6, 'Do you have any chronic diseases, eg: asthma or faced pneumonia in the past', 1],
    [7, '{}', 0]
]


class CovidAdapter(LogicAdapter):
    """
    A COVID-19 dedicated Adapter
    In the **memory** of cancelled Google Code In, Grand Prize Winner's trip, 2019-2020 :
    """
    """
    "Nor Mars his sword nor war’s quick fire shall burn
    The living record of (GCI GPW-19's) memory.
    ’Gainst death and all-oblivious enmity
    Shall you pace forth; your praise shall still find room
    Even in the eyes of all posterity (future GPWs)
    That wear this world out to the ending doom.
    So, till the Judgement that yourself arise,
    You (GCI GPW 2019) live in this, and dwell in lovers’ (coder's) eyes."
            ~ William Shakespeare (Sonnet 55)
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.normalized = None
        self.chatbot = chatbot

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        if any_in(['covid', 'covid19', 'covid-19', 'corona', 'coronavirus'], self.normalized):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        confidence = 1
        # FIXME Creates unusual response
        response = ABOUT_CORONAVIRUS

        if any_in(['I', 'i'], self.normalized):
            response = "I will do a short approximation if you do have coronavirus\n{covidq}"\
                .format(covidq=COVID_QUESTIONS[0][1])
            self.chatbot.globals['reversei']['uid'] = 'CORONAVIRUS'
            self.chatbot.globals['reversei']['enabled'] = True
            logging.info(
                f"CovidAdapter sets ['reversei']['enabled'] as {self.chatbot.globals['reversei']['enabled']}")
            self.chatbot.globals['reversei']['data'] = [1, 0]

        elif 'you' in self.normalized:
            response = 'Someone told that I had been contracted with corona from somewhere, but thats extremely wrong.'\
                       ' I will not get infected by any physical virus, (except Trojan or NO_HEROKU_CREDIT virus)'

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        emotion = Emotion.neutral
        selected_statement.emotion = emotion

        return selected_statement
