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
import importlib
import logging
import shutil
import subprocess
import shlex

from chatterbot.logic import LogicAdapter
from chatterbot.trainers import ListTrainer
from nltk import word_tokenize

from sugaroid.sugaroid import SugaroidStatement
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize


class UpdateAdapter(LogicAdapter):
    """
    [DO NOT CONNECT] a specific adapter for updating the sugaroid bot
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        normalized = word_tokenize(str(statement).lower())
        if 'update' in normalized and 'admin' not in normalized:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        pop = subprocess.Popen(
            shlex.split('{pip} install -U https://github.com/srevinsaju/sugaroid/archive/master.zip'
                        .format(pip=shutil.which('pip'))),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        pop.communicate()
        response = f"Reload : Traceback {pop.stdout.read().decode()} {pop.stdin.read().decode()} . Restarting bot"
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = 10
        self.chatbot.update = True
        emotion = Emotion.rich
        selected_statement.emotion = emotion
        return selected_statement
