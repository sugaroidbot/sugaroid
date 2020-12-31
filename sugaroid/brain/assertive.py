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
from nltk.sentiment import SentimentIntensityAnalyzer

from sugaroid.brain.constants import SUGAROID_CAN_AGREE, SUGAROID_CAN_DISAGREE
from sugaroid.brain.postprocessor import random_response

from sugaroid.brain.ooo import Emotion
from sugaroid.sugaroid import SugaroidStatement


class AssertiveAdapter(LogicAdapter):
    """
    Handles assertive and imperative statements
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        if len(str(statement).split()) >= 3:
            s = statement.doc
            if (s[0].pos_ in ["its", 'this'] or s[0].lower_ == "it") and (s[1].pos_ ==
                                                                          "NOUN" or s[1].pos_ == "VERB" or (s[1].pos_ == "ADV" and s[2].pos_ == "VERB")):
                return True
            else:
                return False
        elif len(str(statement).split()) >= 2:
            s = statement.doc
            if (s[0].pos_ == "DET" or s[0].lower_ == "it's") and (
                    s[1].pos_ == "NOUN" or s[1].pos_ == "VERB"):
                return True
            else:
                return False

        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        response = "What?"
        confidence = 0

        sia = SentimentIntensityAnalyzer()
        ps = sia.polarity_scores(str(statement))
        if ps['neu'] == 1 or (ps['pos'] > ps['neg']):
            response = random_response(SUGAROID_CAN_AGREE)
            confidence = 0.81
        else:
            response = random_response(SUGAROID_CAN_DISAGREE)
            confidence = 0.3

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = Emotion.angel
        return selected_statement
