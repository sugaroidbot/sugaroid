import random
import sys

from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.constants import BYE
from sugaroid.brain.preprocessors import normalize


class ByeAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        self.intersect = set(self.normalized).intersection(set(BYE))
        if (self.intersect and not ('can' in self.normalized)) or (self.normalized[0] == 'see' and self.normalized[1] == 'you'):
            sys.exit()
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        confidence = 1
        selected_statement = Statement("Bye")
        selected_statement.confidence = confidence
        return selected_statement
