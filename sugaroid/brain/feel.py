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
from nltk import pos_tag

from sugaroid.brain.constants import WHO_AM_I, WHO_ARE_YOU, SUGAROID, HOW_DO_YOU_FEEL, HOW_DO_I_FEEL, HOW_DO_HE_FEEL
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.preprocessors import normalize, spac_token
from sugaroid.sugaroid import SugaroidStatement


class FeelAdapter(LogicAdapter):
    """
    Handles sentences containing the word feel
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        self.token = pos_tag(self.normalized)
        if 'feel' in self.normalized:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        confidence = 0.9
        # FIXME Creates unusual response
        nn = False
        it = False
        token = spac_token(statement, chatbot=self.chatbot)
        for i in token:
            if (i.tag_ == 'NNP') or (i.tag_ == 'NN'):
                nn = True
            if i.lower_ == 'it':
                it = True

        if nn and not it:
            response = random_response(HOW_DO_HE_FEEL)
            emotion = Emotion.seriously
        elif it:
            response = "Ask it!"
            emotion = Emotion.o
        elif 'I' in self.normalized:
            emotion = Emotion.depressed
            response = random_response(HOW_DO_I_FEEL)
        else:
            emotion = Emotion.blush
            response = random_response(HOW_DO_YOU_FEEL)

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion

        return selected_statement
