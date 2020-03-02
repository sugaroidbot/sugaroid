
import random

import nltk
from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.constants import INTRODUCE
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.preprocessors import normalize
from sugaroid.sugaroid import SugaroidStatement


class AboutAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.chatbot = chatbot

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
        confidence = 0
        response = None
        adapter = None
        emotion = Emotion.neutral
        if self.pronoun.lower().startswith('you'):
            if self.quest.lower() == 'who':
                if 'creator' in self.normalized:
                    response = 'Srevin Saju aka @srevinsaju'
                    emotion = Emotion.neutral
                elif ('player' in self.normalized) or ('cricketer' in self.normalized) or ('footballer' in self.normalized):
                    response = 'I have many favorties, too many to count'
                    emotion = Emotion.wink
                elif 'politi' in self.normalized:
                    response = 'I believe politicians are great and I couldn\'t find anyone with 🔥greatness in my database'
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
                elif 'athelete' in self.normalized:
                    response = 'I am not a sport lover, I don\'t have a favorite athelete'
                    emotion = Emotion.neutral
                elif ('friend' in self.normalized) or ('bestie' in self.normalized):
                    if self.chatbot.username:
                        name = self.chatbot.username
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
                confidence = 0.99
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
        selected_statement = SugaroidStatement(response)

        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        selected_statement.adapter = adapter

        return selected_statement
