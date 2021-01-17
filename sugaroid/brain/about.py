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
import nltk
from chatterbot.logic import LogicAdapter
from sugaroid.brain.constants import INTRODUCE
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response, any_in
from sugaroid.brain.preprocessors import normalize, spac_token
from sugaroid.sugaroid import SugaroidStatement


class AboutAdapter(LogicAdapter):
    """
    Defines the personality of sugaroid
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.chatbot = chatbot
        self.text = None
        self.tagged = None
        self.quest = None
        self.pronoun = None
        self.nn = None
        self.noun = None
        self.normalized = None
        self.lemma = None

    def can_process(self, statement):
        self.text = nltk.word_tokenize(str(statement))
        self.tagged = nltk.pos_tag(self.text)
        self.nn = False
        q = False
        pr = False
        self.pronoun = None
        self.quest = None
        for i in self.tagged:
            if i[1] == 'WP':
                q = True
                self.quest = i[0]
            elif i[1].startswith('PRP'):
                pr = True
                self.pronoun = i[0]
            elif i[1].startswith('NN'):
                self.nn = True
                self.noun = i[0]
        if q and pr:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        # FIXME : THIS ADAPTER IS INCOMPLETE
        self.normalized = normalize(str(statement))
        self.lemma = [x.lemma_ for x in spac_token(
            statement, chatbot=self.chatbot)]
        logging.info("{}".format(self.lemma))
        confidence = 0
        adapter = None

        emotion = Emotion.neutral
        if self.pronoun.lower().startswith('you'):
            if self.quest.lower() == 'who':
                confidence = 0.99
                if 'father' in self.normalized:
                    response = 'Mr Charles Babbage?'
                    emotion = Emotion.seriously
                elif 'hobby' in self.normalized:
                    response = "Calculating random binary sequences and chatting with you!"
                    emotion = Emotion.lol
                elif 'mother' in self.normalized:
                    response = 'Ada Lady Lovelace?'
                    emotion = Emotion.lol
                elif any_in(['sister', 'brother', 'uncle', 'aunty', 'auntie', 'grandfather',
                             'grandmother', 'nephew', 'neice'], self.normalized):
                    response = 'The entire coding community is my family, it includes you too'
                    emotion = Emotion.wink
                elif ('creator' in self.normalized) or ('create' in self.lemma) or ('make' in self.lemma) \
                        or ('maker' in self.normalized):
                    response = 'Srevin Saju aka @srevinsaju'
                    emotion = Emotion.neutral
                elif ('player' in self.normalized) or ('cricketer' in self.normalized) or \
                        ('footballer' in self.normalized):
                    response = 'I have many favorties, too many to count'
                    emotion = Emotion.wink
                elif 'politi' in self.normalized:
                    response = 'I believe politicians are great and I couldn\'t find anyone with 🔥greatness in my ' \
                               'database '
                    emotion = Emotion.wink
                elif 'comedian' in self.normalized:
                    response = 'My favorite comedian is Mr Bean'
                    emotion = Emotion.lol
                elif 'color' in self.normalized:
                    response = 'My favorite color is blue'
                    emotion = Emotion.lol
                elif 'actor' in self.normalized or ('actress' in self.normalized):
                    response = 'I do not watch movies, so yea!'
                    emotion = Emotion.neutral
                elif 'music' in self.normalized or ('song' in self.normalized):
                    response = 'I listen to the rotating CPU fan. Its a harmonic music! ' \
                               'At my server, we have tons of them.'
                    emotion = Emotion.lol
                elif 'bird' in self.normalized:
                    response = 'My favorite is a Puffin'
                    emotion = Emotion.lol
                elif 'animal' in self.normalized:
                    response = 'My favorite animal is a Fossa'
                    emotion = Emotion.positive
                elif 'number' in self.normalized:
                    response = 'My favorite number is 1'
                    emotion = Emotion.positive
                elif 'sweet' in self.normalized or 'dessert' in self.normalized:
                    response = 'My favorite is the donut although I have not tasted it yet'
                    emotion = Emotion.cry_overflow

                elif 'athelete' in self.normalized:
                    response = 'I am not a sport lover, I don\'t have a favorite athelete'
                    emotion = Emotion.neutral
                elif ('friend' in self.normalized) or ('bestie' in self.normalized):
                    if self.chatbot.globals['USERNAME']:
                        name = self.chatbot.globals['USERNAME']
                    else:
                        name = ''
                    response = "No doubts, its you {n}".format(
                        n=name.capitalize())
                    emotion = Emotion.adorable
                elif 'teacher' in self.normalized:
                    response = "I don't have a single favorite teacher. All the teachers together are my favorite who" \
                               " taught me how to talk with you "
                    emotion = Emotion.positive
                else:
                    if self.nn:
                        response = 'Well, I guess I do not have a favorite {p}'.format(
                            p=self.noun)
                        emotion = Emotion.cry
                    else:
                        response = 'I am not sure what you are asking is right'
                        emotion = Emotion.seriously
                        confidence = 0.5

            else:
                if 'name' in self.normalized:
                    # not sure if this is right. anyway FIXME
                    response = random_response(INTRODUCE)
                    adapter = 'about'
                    confidence = 1.0
                else:

                    response = 'FIXME'

        elif self.pronoun.lower().startswith('i'):
            if self.quest.lower() == 'who':
                response = 'I do not know who you like'
                confidence = 0.8
                emotion = Emotion.non_expressive_left

            elif self.quest.lower() == 'which':
                response = "Hmm. tough question. Can't think of an answer"
                emotion = Emotion.non_expressive
            elif self.quest.lower() == 'when':
                response = "I cannot find the date or time you are asking for. Well, I can give a raw guess, " \
                           "its after you were born "
                emotion = Emotion.wink
            else:
                response = 'FIXME'
        else:
            response = "I do not have enough courage to give you that answer"
            confidence = 0.5
            emotion = Emotion.cry
        selected_statement = SugaroidStatement(response, chatbot=True)

        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        selected_statement.adapter = adapter

        return selected_statement
