import logging
import string

import nltk

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


ARITHEMETIC = ['add', 'plus', 'sutract', 'difference', '+', '-', '*', 'multiply', 'product', 'division', 'quotient', 'divide']

class Neuron:
    def __init__(self, parent):
        self.parent = parent
        logging.info("Sugaroid Neuron Loaded to memory")
        self.lemmer = nltk.stem.WordNetLemmatizer()

    def parse(self, var):
        normal = self.normalize(var)
        if 'time' in normal:
            self.time()
        else:
            for i in ARITHEMETIC:
                if i in normal:
                    self.alu()
                    break
            else:
                # TODO not implemented
                raise NotImplementedError

    def alu(self):
        pass

    def time(self):
        pass

    def lem_tokens(self, tokens):
        return [self.lemmer.lemmatize(token) for token in tokens]

    def normalize(self, text):
        return self.lem_tokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))