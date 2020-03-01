import spacy


class LanguageProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def tokenize(self, arg):
        doc = self.nlp(arg)
        return doc

    def similarity(self, arg1, arg2):
        return self.nlp(arg1).similarity(self.nlp(arg2))
