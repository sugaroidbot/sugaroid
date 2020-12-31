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

"""
import logging

from chatterbot.logic import LogicAdapter
from chatterbot.trainers import ListTrainer
from nltk import word_tokenize

from sugaroid.sugaroid import SugaroidStatement
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize


class LearnAdapter(LogicAdapter):
    """
    a specific adapter for learning responses
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
            'LearnAdapter: can_process() last_adapter was {}'.format(last_type))

        if 'learn' in normalized and 'not' not in normalized and 'to' not in normalized:
            return True
        elif self.chatbot.globals['learn'] and (last_type == 'LearnAdapter'):
            return True
        else:
            if self.chatbot.globals['learn']:
                self.chatbot.globals['learn'] = False
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        response = None
        if not self.chatbot.globals['learn']:
            response = 'Enter something you want to teach me. What is the statement that you want me to learn.'
            self.chatbot.globals['learn'] = 2
        elif self.chatbot.globals['learn'] == 2:
            response = 'What should I respond to the above statement?'
            self.chatbot.globals['learn_last_conversation'].append(
                str(statement))
            self.chatbot.globals['learn'] -= 1
        elif self.chatbot.globals['learn'] == 1:
            response = 'Thanks for teaching me something new. I will always try to remember that'
            self.chatbot.globals['learn_last_conversation'].append(
                str(statement))
            self.chatbot.globals['learn'] -= 1
            list_trainer = ListTrainer(self.chatbot)
            list_trainer.train(self.chatbot.globals['learn_last_conversation'])

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = 9
        selected_statement.adapter = 'LearnAdapter'
        emotion = Emotion.lol
        selected_statement.emotion = emotion
        return selected_statement
