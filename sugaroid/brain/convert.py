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

from chatterbot.logic import LogicAdapter
from currency_converter import CurrencyConverter
from sugaroid.sugaroid import SugaroidStatement

from sugaroid.brain.ooo import Emotion


class SugaroidCurrency:
    def __init__(self):
        self.currency_api = CurrencyConverter()

    def convert(self, src: str, dest: str, amount: float):
        if (src in self.currency_api.currencies) and (dest in self.currency_api.currencies):
            return self.currency_api.convert(amount, src, dest)
        else:
            if src not in self.currency_api.currencies:
                bad_cur = src
            else:
                bad_cur = dest
            return 'Hmm. Seems like {} is not a recognized currency.'.format(bad_cur)


class CurrencyAdapter(LogicAdapter):
    """
    Gives a random response, because Sugaroid tries not to say I don't know
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.currencies_src_ord = None
        self.currencies_dest = None
        self.currencies_src = None
        self.tokenized = None

    def can_process(self, statement):
        self.tokenized = self.chatbot.lp.tokenize(
            str(statement).replace('$', ' USD ').replace(
                '₹', ' INR ').replace('€', ' EUR ').replace('£', ' GBP ')
        )
        self.currencies_dest = []
        self.currencies_src = None
        if len(self.tokenized) >= 3:
            for i in range(len(self.tokenized) - 1):
                if self.tokenized[i].tag_ == 'TO':
                    dst = str(self.tokenized[i + 1].text).upper()
                    if len(dst) < 4:
                        self.currencies_dest.append(dst)
                    try:
                        if len(self.tokenized[i - 1].lower_) < 4:
                            self.currencies_src = str(
                                self.tokenized[i - 1].text).upper()
                    except IndexError:
                        pass
                elif self.tokenized[i].lower_ == 'is':

                    for j in range(i + 1, len(self.tokenized)):
                        if self.tokenized[j].tag_ == 'IN':
                            dst = str(self.tokenized[j + 1].text).upper()
                            if len(dst) < 4:
                                self.currencies_dest.append(dst)
                            try:
                                src = str(self.tokenized[j - 1].text).upper()
                                if len(src) < 4:
                                    self.currencies_src = src
                            except IndexError:
                                pass
                    if self.currencies_dest and self.currencies_src:
                        return True
                    else:
                        return False
                elif self.tokenized[i].tag_ == 'IN':
                    dst = str(self.tokenized[i + 1].text).upper()
                    if len(dst) < 4:
                        self.currencies_dest.append(dst)

        if self.currencies_dest and self.currencies_src:
            logging.info(
                "CurrencyAdapter: Recognized source and destination currency types. src: {} and dest: {}" .format(
                    self.currencies_src, self.currencies_dest))
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        emotion = Emotion.rich
        confidence = 0.9
        response = None
        converted = []

        for i in self.tokenized:
            if i.tag_ in ['LS', 'CD']:
                self.currencies_src_ord = i.text

        if self.currencies_src_ord:
            try:
                self.currencies_src_ord = float(self.currencies_src_ord)
                sg_currency = SugaroidCurrency()
                for destination in self.currencies_dest:
                    converted.append('{} {}'.format(
                        sg_currency.convert(self.currencies_src.upper(
                        ), destination.upper(), self.currencies_src_ord),
                        destination.upper())
                    )
                response = ' '.join(converted)
            except ValueError:
                response = 'Seems like I cannot process {}. Maybe try a numerical value for me to understand better' \
                    .format(self.currencies_src_ord)

        else:
            response = 'Seems like you forgot the important part of your currency conversion statement. The number!'
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        return selected_statement
