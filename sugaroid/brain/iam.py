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
import spacy
from chatterbot.logic import LogicAdapter
from nltk.sentiment import SentimentIntensityAnalyzer
from sugaroid.brain.constants import GREET, BURN_IDK, I_AM
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import cosine_similarity, random_response, raw_in, raw_lower_in
from sugaroid.brain.whatamidoing import process_what_ami_doing
from sugaroid.sugaroid import SugaroidStatement


class MeAdapter(LogicAdapter):
    """
    Processes the statements showing possessive
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

        self.normalized = None
        self.tokenized = None
        self.nlp = spacy.load("en_core_web_sm")

    def can_process(self, statement):
        # TODO Fix this
        self.tokenized = self.nlp(str(statement))

        for i in range(len(self.tokenized) - 1):
            if self.tokenized[i].pos_ == 'PRON' and str(self.tokenized[i + 1].tag_).startswith('VB'):
                return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        response = 'ok'
        confidence = 0
        emotion = Emotion.neutral
        if raw_in('I', self.tokenized):
            logging.info(str(["{} {} {}".format(k, k.tag_, k.pos_)
                              for k in self.tokenized]))
            # check if the pronoun has been reached yet, otherwise may detect some other nouns
            start_scanning = False
            for i in self.tokenized:
                if i.pos_ == 'PRON' and not i.tag_.startswith("W"):
                    start_scanning = True
                if start_scanning:
                    pass
                elif (i.pos_ != 'PRON') or (not start_scanning) or (i.tag_.startswith('W')):
                    logging.info(
                        "MeAdapter: Skipping {} {}".format(i.lower_, i.tag_))
                    continue
                logging.info(
                    "MeAdapter: Scanning :: {} : {}".format(i.text, i.pos_))
                if (i.pos_ == 'PROPN') or (i.tag_ == 'NN'):
                    nn = i.text
                    if self.chatbot.globals['USERNAME']:
                        response = "Are you sure you are {n}? I thought you were {u}".format(
                            n=nn, u=self.chatbot.globals['USERNAME'])
                        emotion = Emotion.wink
                        if i.pos_ == 'PROPN':
                            confidence = 0.95
                        else:
                            confidence = 0.8
                        self.chatbot.globals['nn'] = nn
                        self.chatbot.globals['reversei']['uid'] = 30000000001
                        self.chatbot.globals['reversei']['type'] = bool
                        self.chatbot.globals['reversei']['enabled'] = True
                        emotion = Emotion.non_expressive_left
                        break
                    else:
                        if not ('not' in str(statement)):
                            if i.lower_ == 'sugaroid':
                                response = random_response(I_AM)
                                emotion = Emotion.lol
                                confidence = 0.95
                            else:
                                response = random_response(
                                    GREET).format(str(nn).capitalize())
                                confidence = 0.9
                                self.chatbot.globals['USERNAME'] = nn
                                emotion = Emotion.positive
                            break
                        else:
                            response = 'Ok!'
                            confidence = 0.5
                            emotion = Emotion.seriously
                            break
                elif i.lower_ == 'sugaroid':
                    response = random_response(I_AM)
                    emotion = Emotion.lol
                    confidence = 0.95
                else:
                    sia = SentimentIntensityAnalyzer()
                    ps = sia.polarity_scores(str(i.sent))
                    confidence = 0.35
                    if ps['neu'] == 1:
                        response = 'Ok! Thats great to hear from you'
                        emotion = Emotion.lol
                    elif ps['pos'] > ps['neg']:
                        response = 'Yay! I agree to you'
                        emotion = Emotion.positive
                    else:
                        confidence = 0.2
                        response = 'Think again'
                        emotion = Emotion.non_expressive_left
        elif raw_lower_in('you', self.tokenized):
            logging.info(str(["{} {} {}".format(k, k.tag_, k.pos_)
                              for k in self.tokenized]))
            nn = ''
            start_scanning = False
            for i in self.tokenized:
                if i.pos_ == 'PRON' and not i.tag_.startswith("W"):
                    start_scanning = True
                if start_scanning:
                    pass
                elif (i.pos_ != 'PRON') or (not start_scanning) or (i.tag_.startswith('W')):
                    logging.info("MeAdapter: Skipping {} {} ss={} {}"
                                 .format(i.lower_, i.tag_, not start_scanning, i.pos_))
                    continue
                logging.info(
                    "MeAdapter: Scanning :: {} : {}".format(i.text, i.pos_))
                if i.pos_ == 'ADJ':
                    try:
                        cos = cosine_similarity([str(i.lower_)], ['sugaroid'])
                    except ZeroDivisionError:
                        cos = 0.0
                    if i.lower_ == 'sugaroid':
                        nn = i.text
                        response = "Yup, that's my name. I am sugaroid"
                        emotion = Emotion.lol
                        confidence = 0.9
                        break
                    elif cos > 0.9:
                        response = "Yes, you were close! My name is sugaroid"
                        emotion = Emotion.positive
                        confidence = 0.9
                        break
                    else:
                        if i.lower_ in ['human', 'animal', 'bird']:
                            response = 'No, I am not a {adj}. I am a robot'.format(
                                adj=i.lower_)
                            emotion = Emotion.angry_non_expressive
                            confidence = 0.9
                        else:
                            response = 'seriously?'
                            emotion = Emotion.angry
                            confidence = 0.09

                elif i.pos_ == 'PROPN':
                    cos = cosine_similarity([str(i.lower_)], ['sugaroid'])

                    if i.lower_ == 'sugaroid':
                        nn = i.text
                        response = "Yup, that's my name. I am sugaroid"
                        emotion = Emotion.lol
                        confidence = 0.9
                        break
                    elif cos > 0.9:
                        response = "Yes, you were close! My name is sugaroid"
                        emotion = Emotion.positive
                        confidence = 0.9
                        break
                    else:

                        nn = i.text
                        response = "Nope, I am not {n}, I am sugaroid".format(
                            n=nn)
                        emotion = Emotion.angry
                        confidence = 0.9

                elif i.tag_ == 'NN':
                    if i.lower_ in ['bot', 'robot', 'computer', 'silicon', 'infant']:
                        response = 'You are right! I am a {}'.format(i.lower_)
                        confidence = 0.9
                        emotion = Emotion.positive
                    elif i.lower_ in ['human', 'bird', 'animal', 'tree', 'politician', 'player', 'liar', 'priest']:
                        response = 'No way! I can\'t imagine myself to be a {}'.format(
                            i.lower_)
                        confidence = 0.9
                        emotion = Emotion.vomit
                    else:
                        logging.info(
                            "MeAdapter: Couldn't classify type of noun {}".format(i.lower_))
                        confidence = 0.9
                        sia = SentimentIntensityAnalyzer()
                        ps = sia.polarity_scores(str(i.sent))
                        if ps['neu'] == 1.0:
                            # try presence adapter pieces
                            presence_statement = process_what_ami_doing(
                                statement)
                            if presence_statement.confidence == 0:

                                response = 'I will need more time to learn if that actually makes sense with respect to ' \
                                           'myself. '
                                emotion = Emotion.cry
                            else:
                                return presence_statement
                        elif ps['pos'] > ps['neg']:
                            response = 'I guess I am {}. Thanks!'.format(
                                i.text)
                            emotion = Emotion.wink
                        else:
                            response = 'I am not {}! I am Sugaroid.'.format(
                                i.lower_)
                            emotion = Emotion.angry

                elif i.tag_.startswith('VB'):
                    root_verb = i.lemma_
                    if root_verb in ['say', 'tell', 'speak', 'murmur', 'blabber', 'flirt']:
                        response = random_response(BURN_IDK)
                        emotion = Emotion.lol
                        confidence = 0.8

        else:
            presence_statement = process_what_ami_doing(statement)
            if presence_statement.confidence == 0:
                # FIXME : Add more logic here
                response = 'Ok'
                confidence = 0.05
                emotion = Emotion.non_expressive_left
            else:
                return presence_statement

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        return selected_statement
