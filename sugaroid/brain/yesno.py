import random
import sys

import nltk
from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.constants import BYE
from sugaroid.brain.preprocessors import normalize


class BoolAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.chatbot = chatbot
        self.normalized = None
        self.intersect = None

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        if ('yes' in self.normalized) or ('no' in self.normalized):
            return True

    def process(self, statement, additional_response_selection_parameters=None):
        bool_yes = 'yes' in self.normalized
        if self.chatbot.report:
            if bool_yes:
                response = 'Sure, I would connect to the Developer to report this issue right away'
            else:
                response = 'Ok, I will not report it.'
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

                            response = 'Ok, here comes your {} 😝😝'.format(some_nouns)
                        elif vb:
                            response = 'You should {}'.format(verb.replace('ing', ''))
                        else:
                            response = 'I will keep thinking 🚀'
                    else:
                        if nn:
                            response = 'Ok, I will have the {}'.format(some_nouns)
                        elif vb:
                            response = "You shouldn't {} then".format(verb.replace('ing', ''))
                        else:
                            response = 'Okay!'
                else:
                    if bool_yes:
                        response = "Why is this 'yes' here? I couldn't find the question. Anyway, I agree with you"
                    else:
                        response = 'No? for what?.'

        confidence = 0.95
        selected_statement = Statement(response)
        selected_statement.confidence = confidence
        return selected_statement
