"""
MIT License

Sugaroid Artificial Inteligence
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

import logging
import nltk
from chatterbot.logic import LogicAdapter
from pyjokes import pyjokes

from nltk.sentiment import SentimentIntensityAnalyzer
from sugaroid.brain.covid import COVID_QUESTIONS
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import cosine_similarity, difference, text2int, any_in
from sugaroid.brain.preprocessors import normalize, tokenize
from sugaroid.brain.wiki import wikipedia_search
from sugaroid.sugaroid import SugaroidStatement


class ReReverseAdapter(LogicAdapter):
    """
    Processes statements featuring conversational flow. It scans the previous statements
    and takes a cosine similarity of the statemnts, and TFiD Vector cross product to get
    the most probable answer
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.chatbot = chatbot
        self.normalized = None

    def can_process(self, statement):
        soln = self.chatbot.get_global('reversei')['enabled']
        logging.info(f"ReReverseiAdapter: {soln}")
        return soln

    def process(self, statement, additional_response_selection_parameters=None):
        _ = normalize
        emotion = Emotion.neutral
        self.normalized = normalize(str(statement))
        if self.chatbot.globals['reversei']['type'] is str:
            ordinal_statement = str(statement).replace('9th', 'ninth')
            # FIXME PORT RO
            if cosine_similarity(_(ordinal_statement), _(self.chatbot.globals['reversei']['uid'])) > 0.8:
                response = 'Exactly, you got it right!'
                emotion = Emotion.positive
                reset_reverse(self)
            else:
                response = 'Close! it was {}'.format(
                    self.chatbot.globals['reversei']['uid'])
                emotion = Emotion.lol
                reset_reverse(self)
            confidence = 0.99
        elif self.chatbot.globals['reversei']['type'] is bool:

            if self.chatbot.globals['reversei']['uid'] == 30000000001:
                """
                NameAdapter: token 30000000001
                """
                if ('yes' in self.normalized) or ('yea' in self.normalized):
                    response = "Ok, will keep that in mind!"
                    self.chatbot.globals['USERNAME'] = self.chatbot.globals['nn']
                    self.chatbot.globals['nn'] = None
                    reset_reverse(self)
                else:
                    response = "Ok, I guess I am smart"
                    emotion = Emotion.wink
                    reset_reverse(self)
                confidence = 1.0
            else:
                if ('yes' in self.normalized) or ('yea' in self.normalized):
                    if len(self.chatbot.globals['history']['total']) > 1:
                        if 'joke' in _(str(self.chatbot.globals['history']['total'][-1])):
                            joke = pyjokes.get_joke('en', 'all')
                            selected_statement = SugaroidStatement(
                                joke, chatbot=True)
                            selected_statement.emotion = Emotion.lol
                            selected_statement.confidence = 0.95
                            return selected_statement

                        else:
                            # TODO: Not Implemented yet
                            response = 'Ok. (# Not Implemented yet. LOL)'
                else:
                    response = 'Ok then, probably next time'
                    reset_reverse(self)
                confidence = 1.0
        elif self.chatbot.globals['reversei']['type'] is None and \
                (not self.chatbot.globals['reversei']['uid'] == 'CORONAVIRUS'):
            fname = False
            name = difference(self.normalized, [
                              'my', 'name', 'is', 'good', 'be'])
            tokenized = nltk.pos_tag(name)
            for i in tokenized:
                if i[1] == 'NN':
                    fname = i[0]
                    break
            if fname:
                response = "Nice to meet you {}".format(fname)
                emotion = Emotion.positive
                reset_reverse(self)
            else:
                response = "I couldn't find your name. 🥦"
                emotion = Emotion.non_expressive_left
                reset_reverse(self)
            confidence = 1
        elif self.chatbot.globals['reversei']['type'] is int:
            confidence = 2.0  # FIXME: Override Mathematical Evaluation when not necessary

            if self.chatbot.globals['reversei']['uid'] == 30000000002:
                """
                WikiAdapter: token 30000000002
                """
                if ('yes' in self.normalized) or ('yea' in self.normalized):
                    response = "I thought you would tell me a number to choose from :/"
                    emotion = Emotion.seriously

                elif ('no' in self.normalized) or ('no' in self.normalized):
                    response = 'Oops! Sorry about that, seems like what you\'re searching for is not on Wikipedia yet'
                    emotion = Emotion.dead
                    reset_reverse(self)
                else:
                    chatbot_temporary_data = self.chatbot.globals['temp_data']
                    tokenized = nltk.pos_tag(tokenize(str(statement)))
                    for i in tokenized:
                        if i[1] == 'CD':
                            try:
                                num = int(i[0])
                            except ValueError:
                                num = text2int(i[0].lower())
                            index = num - 1
                            if index < len(chatbot_temporary_data):
                                response, confidence, stat = wikipedia_search(
                                    self, chatbot_temporary_data[index])
                                logging.info('REVERSEI: {}'.format(response))
                                confidence = 1 + confidence  # FIXME override math evaluation adapter
                                if not stat:
                                    response = "I have some trouble connecting to Wikipedia. Something's not right"
                                    confidence = 1.1

                                emotion = Emotion.rich
                                reset_reverse(self)
                                break
                            else:
                                response = "Sorry, I couldn't find the item you were choosing. "
                                confidence = 1.1
                                emotion = Emotion.cry_overflow
                                reset_reverse(self)
                                break
                    else:
                        response = 'I thought you wanted to know something from wikipedia. ' \
                                   'Ok, I will try something else'
                        emotion = Emotion.seriously
                        reset_reverse(self)
                        confidence = 1.2
        else:
            if self.chatbot.globals['reversei']['uid'] == 'CORONAVIRUS':
                confidence = 1
                NUM = self.chatbot.globals['reversei']['data'][0]

                score = self.chatbot.globals['reversei']['data'][1]
                if NUM == 6:
                    self.chatbot.globals['reversei']['enabled'] = False
                    if score > 3:
                        response = 'You have a high risk of COVID-19'
                    else:
                        response = 'As per my approximation, you do not have a high risk of COVID-19'
                    response += "\n My approximations might not be correct. " \
                                "You might confirm my results by a legal test"
                else:
                    sia = SentimentIntensityAnalyzer()
                    _scores = sia.polarity_scores(str(statement))
                    true_responses = ['yes', 'yea', 'y', 'yup', 'true']
                    if any_in(
                        true_responses +
                        [x.capitalize() for x in true_responses],
                        self.normalized
                    ) or (_scores['pos'] > _scores['neg']):
                        score += COVID_QUESTIONS[NUM - 1][2]
                    response = COVID_QUESTIONS[NUM][1]

                    self.chatbot.globals['reversei']['data'] = [NUM + 1, score]

            else:
                response = 'ok'

                confidence = 0

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence

        selected_statement.emotion = emotion

        return selected_statement


def reset_reverse(self):
    self.chatbot.globals['reversei']['uid'] = None
    self.chatbot.globals['reversei']['type'] = None
    self.chatbot.globals['reversei']['enabled'] = False
