import random
import sys

from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.constants import BYE
from sugaroid.brain.preprocessors import normalize


class ByeAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.normalized = None
        self.intersect = None

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        if len(self.normalized) >= 2:
            for i in range(0, len(self.normalized)-2):
                if (self.normalized[i] == 'see') and (self.normalized[i+1] == 'you'):
                    return True
        self.intersect = set(self.normalized).intersection(set(BYE))
        if self.intersect and not ('can' in self.normalized):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        confidence = 1
        selected_statement = Statement("Bye")
        selected_statement.confidence = confidence
        return selected_statement
