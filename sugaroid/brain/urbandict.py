"""
MIT License

Sugaroid Artificial Inteligence
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


This file has been adapted from https://github.com/TheAssassin/relbot
"""
import logging
import requests

from collections import namedtuple
from typing import Iterator
from urllib.parse import urlencode
from lxml import html
from chatterbot.logic import LogicAdapter
from chatterbot.trainers import ListTrainer
from nltk import word_tokenize

from sugaroid.sugaroid import SugaroidStatement
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize


class UrbanDictionaryError(Exception):
    pass


UrbanDictionaryDefinition = namedtuple("UrbanDictionaryDefinition", ["word", "meaning", "example"])


class UrbanDictionaryClient:
    @staticmethod
    def build_url(term: str):
        querystring = urlencode({
            "term": term,
        })

        url = "https://www.urbandictionary.com/define.php?{}".format(querystring)

        return url

    @classmethod
    def define_all(cls, term: str) -> Iterator[UrbanDictionaryDefinition]:
        url = cls.build_url(term)

        response = requests.get(url, allow_redirects=True)

        if response.status_code == 404:
            raise UrbanDictionaryError("no results for search term \"%s\"" % term)

        if response.status_code != 200:
            raise UrbanDictionaryError("HTTP status %d" % response.status_code)

        tree = html.fromstring(response.content)

        definitions = tree.cssselect("#content .def-panel")

        for definition in definitions:
            kwargs = {}

            for attribute in ["word", "meaning", "example"]:
                attrib_elem = definition.cssselect(".{}".format(attribute))[0]
                kwargs[attribute] = attrib_elem.text_content().replace("\n", " ")

            yield UrbanDictionaryDefinition(**kwargs)

    @classmethod
    def top_definition(cls, term: str):
        return next(cls.define_all(term))




class UrbanDictAdapter(LogicAdapter):
    """
    a specific adapter to get meanings of the word
    from the urban dictionary
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        normalized = word_tokenize(str(statement).lower())
        try:
            last_type = self.chatbot.globals['history']['types'][-1]
        except IndexError:
            last_type = False
        logging.info(
            'UrbanDictAdapter: can_process() last_adapter was {}'.format(last_type))

        if 'ud' in normalized and 'not' not in normalized and 'to' not in normalized:
            return True
        elif self.chatbot.globals.get('ud') and (last_type == 'UrbanDictAdapter'):
            return True
        else:
            if self.chatbot.globals.get("ud"):
                self.chatbot.globals["ud"] = False
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        response = None
        normalized = word_tokenize(str(statement).lower())
        if normalized[0].lower() == "ud":
            try:
                word = normalized[1].lower()
                ud_response = UrbanDictionaryClient.top_definition(word)
                response = f"{ud_response.word}:" \
                           f"{ud_response.meaning}\nExample: {ud_response.example}"
            except IndexError:
                response = "Usage: ud [WORD]"
            except UrbanDictionaryError as e:
                response = f"ud: Error: {e}"
        else:
            response = "Usage: ud [WORD]"

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = 9
        selected_statement.adapter = 'UrbanDictAdapter'
        emotion = Emotion.positive
        selected_statement.emotion = emotion
        return selected_statement
