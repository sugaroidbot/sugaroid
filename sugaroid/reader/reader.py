from rstparse import Parser

from sugaroid.brain.utils import LanguageProcessor


class SugaroidCorpus:
    def __init__(self, path=None):
        if path is None:
            raise FileNotFoundError("Invalid file 'NONE'")
        self.path = path
        self.corpus = None
        self.parser = Parser()
        self.lp = LanguageProcessor()

    def read(self):
        with open(self.path, 'r') as r:
            self.parser.read(r)
        return True

    def rst(self):
        self.parser.parse()

    def txt(self):
        text = ''
        for i in self.parser.lines:
            text += " {} ".format(i)
        return text

    def parse(self, txt):
        doc = self.lp.tokenize(txt)
        l = list(doc.sent)
        return l

    def answer(self, lst, text):
        cos = []
        for i in lst:
            cos.append(self.lp.tokenize(i).similarity(self.lp.tokenize(text)))

        mx_cos = max(cos)
        return lst[cos.index(mx_cos)]

    def readonly(self):
        return True
