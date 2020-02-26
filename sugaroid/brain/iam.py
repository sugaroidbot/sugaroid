import nltk
from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.constants import GREET
from sugaroid.brain.postprocessor import cosine_similarity, random_response
from sugaroid.brain.preprocessors import normalize


class MeAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.chatbot = chatbot
        self.normalized = None
        self.tokenized = None

    def can_process(self, statement):
        self.normalized = nltk.word_tokenize(str(statement).lower())
        self.tokenized = nltk.pos_tag(['I' if x == 'i' else x for x in self.normalized])
        for i in range(len(self.tokenized)-2):
            if (self.tokenized[i][1] == 'PRP') and \
                    ((self.tokenized[i+1][1] == 'VBP') or (self.tokenized[i+1][1] == 'VBZ')):
                return True
        else:
            return False


    def process(self, statement, additional_response_selection_parameters=None):
        response = 'ok'
        confidence = 0
        print("MEAdapter", self.normalized, self.tokenized)
        if ('I', 'PRP') in self.tokenized:
            for i in self.tokenized:
                if i[1] == 'JJ' or i[1] == 'NN':
                    nn = i[0]
                    if self.chatbot.username:
                        response = "Are you sure you are {n}? I thought you were {u}".format(n=nn, u=self.chatbot.username)
                        confidence = 0.95
                        self.chatbot.nn = nn
                        self.chatbot.next = 30000000001
                        self.chatbot.next_type = bool
                        self.chatbot.reverse = True
                    else:
                        response = random_response(GREET).format(str(nn).capitalize())
                        confidence = 0.9
                        self.chatbot.username = nn
        elif 'you' in self.normalized:
            for i in self.tokenized:
                if i[1] == 'JJ' or i[1] == 'NN':
                    nn = i[0]
                    cos = cosine_similarity([nn], ['sugaroid'])
                    if cos > 0.9:
                        response = "Yup, that's my name. I am sugaroid"
                    else:
                        response = "Nope, I am not {n}, I am sugaroid".format(n=nn)
                    confidence = 0.9
        else:
            response = 'Ok'
            confidence = 0.8

        selected_statement = Statement(response)
        selected_statement.confidence = confidence
        return selected_statement
