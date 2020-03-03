import logging

import nltk
from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter
from pyjokes import pyjokes

from sugaroid.brain.constants import RNDQUESTIONS
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import cosine_similarity, random_response, difference, text2int
from sugaroid.brain.preprocessors import normalize, tokenize
from sugaroid.brain.wiki import wikipedia_search
from sugaroid.sugaroid import SugaroidStatement


class ReReverseAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.chatbot = chatbot

    def can_process(self, statement):
        if self.chatbot.reverse:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        _ = normalize
        emotion = Emotion.neutral
        self.normalized = normalize(str(statement))
        print(self.chatbot.next)
        if self.chatbot.next_type is str:
            ordinal_statement = str(statement).replace('9th', 'ninth')
            if cosine_similarity(_(ordinal_statement), _(self.chatbot.next)) > 0.8:
                response = 'Exactly, you got it right!'
                emotion = Emotion.positive
                reset_reverse(self)
            else:
                response = 'Close! it was {}'.format(self.chatbot.next)
                emotion = Emotion.lol
                reset_reverse(self)
            confidence = 0.99
        elif self.chatbot.next_type is bool:

            if self.chatbot.next == 30000000001:
                """
                NameAdapter: token 30000000001
                """
                if ('yes' in self.normalized) or ('yea' in self.normalized):
                    response = "Ok, will keep that in mind!"
                    self.chatbot.username = self.chatbot.nn
                    self.chatbot.nn = None
                    reset_reverse(self)
                else:
                    response = "Ok, I guess I am smart"
                    emotion = Emotion.wink
                    reset_reverse(self)
                confidence = 1.0
            else:
                if ('yes' in self.normalized) or ('yea' in self.normalized):
                    if len(self.chatbot.history) > 1:
                        if 'joke' in _(str(self.chatbot.history[-1])):
                            joke = pyjokes.get_joke('en', 'all')
                            selected_statement = SugaroidStatement(joke)
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
        elif self.chatbot.next_type is None:
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
        elif self.chatbot.next_type is int:
            confidence = 2.0  # FIXME: Override Mathematical Evaluation when not necessary

            if self.chatbot.next == 30000000002:
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
                    l = self.chatbot.temp_data
                    tokenized = nltk.pos_tag(tokenize(str(statement)))
                    print(tokenized)
                    for i in tokenized:
                        print(i, "H")
                        if i[1] == 'CD':
                            try:
                                num = int(i[0])
                            except ValueError:
                                num = text2int(i[0].lower())
                            index = num - 1
                            if index < len(l):
                                response, confidence, stat = wikipedia_search(
                                    self, l[index])
                                logging.info('Reversei: {}'.format(response))
                                confidence = 1 + confidence  # FIXME override math evaluation adapter
                                if not stat:
                                    response = "I have some trouble connecting to Wikipedia. Something's not right"
                                    confidence = 1.1

                                emotion = Emotion.rich
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
                # TODO NOT IMPLEMENTED YET
                response = 'ok'
        else:
            response = "ok"
            # TODO NOT IMPLEMENTED YET
            confidence = 0

        selected_statement = SugaroidStatement(response)
        selected_statement.confidence = confidence

        selected_statement.emotion = emotion

        return selected_statement


def reset_reverse(self):
    self.chatbot.next = None
    self.chatbot.next_type = None
    self.chatbot.reverse = False
