import random
import sys

from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter
from nltk import word_tokenize, pos_tag

from sugaroid.brain.constants import BYE, ANNOYED
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.preprocessors import normalize
from sugaroid.sugaroid import SugaroidStatement


class OneWordAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.normalized = None
        self.intersect = None
        self.tokenized = None

    def can_process(self, statement):
        self.normalized = normalize(str(statement))

        if len(self.normalized) == 1:
            return True
        elif len(self.normalized) == 2:
            self.tokenized = pos_tag(self.normalized)
            if self.tokenized[1][1] == ".":
                return True
            else:
                return False
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        emotion = Emotion.seriously
        confidence = 0.2
        selected_statement = SugaroidStatement(random_response(ANNOYED))
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        selected_statement.adapter = None
        return selected_statement
