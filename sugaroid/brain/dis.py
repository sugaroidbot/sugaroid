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
import logging
from chatterbot.logic import LogicAdapter
from nltk.sentiment import SentimentIntensityAnalyzer
from pyinflect import getInflection
from sugaroid.brain.postprocessor import any_in, random_response
from sugaroid.brain.constants import BYE, DIS_RESPONSES_YOU, CONSOLATION, DIS_RESPONSES_I, DIS_RESPONSES_HIM
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize, spac_token
from sugaroid.sugaroid import SugaroidStatement


class DisAdapter(LogicAdapter):
    """
    A complex algorithm sorting the words beginning with negative based on the probability.
    and achieving a similar confidence ratio of the word percentage.
    The DisAdapter keeps the confidence below 0.5 so that the BestAdapter may find some
    other answer similar to
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.normalized = None
        self.dis = None

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        self.dis = None
        for i in self.normalized:
            if i.startswith('dis'):
                self.dis = i
                return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        confidence = 0
        dis_word = False
        if any_in(['distinguish', 'disfigure', 'distinct', 'distinction', 'distant',
                   'distance', 'distribution', 'distilled'], self.normalized):
            confidence = 0
        else:
            logging.info(
                "DisAdapter: Starting Advanced scan. dis_word == {}".format(self.dis)[0])
            dis_word = self.dis[3:]
            logging.info("DisAdapter: Distilled word == {}".format(dis_word))
            sia = SentimentIntensityAnalyzer().polarity_scores(dis_word)
            if dis_word[0] in ['a', 'e', 'i', 'o', 'u', 'g', 'm', 'p']:
                confidence += 0.4
            if 'infect' in dis_word:
                confidence -= 0.3
            if 'spirit' in dis_word:
                confidence += 0.2
            if any_in(['play', 'pensary', 'pense', 'patch', 'port',
                       'persal', 'perse', 'persion', 'praise'], dis_word):
                confidence -= 0.2

            confidence += sia['neg']
        inflection = getInflection(
            self.chatbot.lp.tokenize(self.dis)[0].lemma_, 'VBD')
        if inflection is None:
            past_participle_form_of_verb = self.dis
        else:
            past_participle_form_of_verb = inflection[0]
        if 'you' in self.normalized:
            response = random_response(DIS_RESPONSES_YOU).format(
                past_participle_form_of_verb)
            emotion = Emotion.angry_non_expressive
        elif 'I' in self.normalized:
            response = "{} {}".format(random_response(
                DIS_RESPONSES_I), random_response(CONSOLATION))
            emotion = Emotion.angel
        else:
            nn = None
            pn = None
            tokenized = spac_token(statement, chatbot=self.chatbot)
            for i in tokenized:
                if (i.pos_ == "NOUN") or (i.pos_ == 'PROPN'):
                    nn = i.text
                elif i.pos_ == 'PRON':
                    pn = i.text
            if not (nn or pn):
                response = 'Lol. What?'
                emotion = Emotion.seriously
            else:
                response = random_response(DIS_RESPONSES_HIM).format(nn or pn)
                emotion = Emotion.cry_overflow
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        selected_statement.adapter = None
        return selected_statement
