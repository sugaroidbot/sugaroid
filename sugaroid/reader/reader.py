"""
MIT License

Sugaroid Artificial Inteligence
Chatbot Core
Copyright (c) 2020 Srevin Saju

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
