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

from nltk import word_tokenize

from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.sugaroid import SugaroidStatement


class OrAdapter(LogicAdapter):
    """
    Selects a random operand of the provided statement
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):

        self.text = word_tokenize(str(statement))
        self.tagged = nltk.pos_tag(self.text)
        for i in self.tagged:
            if i[1] == 'CC':
                return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        nouns = set()
        response = None
        emotion = Emotion.neutral
        confidence = 0.8
        if (len(self.tagged) == 1) or (self.tagged[0][1] == 'CC'):
            response = "Are you serious, just an {}".format(self.tagged[0][0])
            emotion = Emotion.angry
            confidence = 0.8
        elif len(self.tagged) == 2:
            response = 'I expected you to provide an option, But what? 🐓'
            emotion = Emotion.angry_non_expressive
            confidence = 0.8
        else:
            for i in range(len(self.tagged) - 1):
                n1 = self.tagged[i - 1]
                if n1[1].startswith('N'):
                    nouns = nouns.union({n1[0]})
                n2 = self.tagged[i + 1]
                if n2[1].startswith('N'):
                    nouns = nouns.union({n2[0]})
            if ('boy' in nouns) or ('girl' in nouns):
                response = "I am neither"
                emotion = Emotion.angry_non_expressive
            elif len(tuple(nouns)) == 0:
                # implies that the list is empty
                # we might not know what is the answer
                # because we did not detect any nouns
                # just say neither
                response = "Neither"
                confidence = 0.8
            else:
                response = "{} 🎃".format(random_response(list(nouns)))

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion

        return selected_statement
