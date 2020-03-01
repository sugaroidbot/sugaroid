import random
import sys

import nltk
from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.constants import BYE
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize
from sugaroid.sugaroid import SugaroidStatement


class BoolAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.chatbot = chatbot
        self.normalized = None
        self.intersect = None

    def can_process(self, statement):
        self.normalized = normalize(str(statement).lower())
        if ('yes' in self.normalized) or ('no' in self.normalized) or ('true' in self.normalized) or ('false' in self.normalized):
            if ('yes' in self.normalized) or ('true' in self.normalized):
                self.bool = True
            else:
                self.bool = False
            return True

    def process(self, statement, additional_response_selection_parameters=None):
        bool_yes = 'yes' in self.normalized
        emotion = Emotion.neutral
        if self.chatbot.report:
            if bool_yes:
                response = 'Sure, I would connect to the Developer to report this issue right away'
            else:
                response = 'Ok, I will not report it.'
            confidence = 1.0
        elif self.chatbot.trivia_answer:
            if self.chatbot.trivia_answer == self.bool:
                response = "Exactly! You are right"
            else:
                response = 'Nope, You got it wrong. The correct answer was {}'.format(
                    self.chatbot.trivia_answer)
            self.chatbot.trivia_answer = None
            confidence = 1.1
        else:
            if self.chatbot.history[-1] == 0:
                if bool_yes:
                    response = 'I shall annoy you. A big NO'
                else:
                    response = 'I would rather have fun, YES ?'
            else:
                md = False
                vb = False
                nn = False
                self.last_normalized = normalize(str(self.chatbot.history[-1]))
                self.tagged = nltk.pos_tag(self.last_normalized)
                iteration = 0
                for j in self.tagged:
                    if j[1].startswith('MD'):
                        md = True
                    elif (j[1].startswith('VB')) and (not j[0] == 'be'):
                        vb = True
                        verb = j[0]
                    elif j[1].startswith('NN'):
                        if not nn:
                            nn_index = iteration
                        nn = True
                        noun = j[0]
                    iteration += 1

                if md:
                    if nn:
                        some_nouns = ' '.join(self.last_normalized[nn_index:])
                    if bool_yes:
                        if nn:

                            response = 'Ok, here comes your {} 😝😝'.format(
                                some_nouns)
                        elif vb:
                            response = 'You should {}'.format(
                                verb.replace('ing', ''))
                        else:
                            response = 'I will keep thinking 🚀'
                    else:
                        if nn:
                            response = 'Ok, I will have the {}'.format(
                                some_nouns)
                        elif vb:
                            response = "You shouldn't {} then".format(
                                verb.replace('ing', ''))
                        else:
                            response = 'Okay!'
                else:
                    if bool_yes:
                        response = "Why is this 'yes' here? I couldn't find the question. Anyway, I agree with you"
                    else:
                        response = 'No? for what?.'
                        emotion = Emotion.angry

            confidence = 0.95
        selected_statement = SugaroidStatement(response)
        selected_statement.confidence = confidence

        selected_statement.emotion = emotion

        return selected_statement
