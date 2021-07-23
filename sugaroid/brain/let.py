from chatterbot.logic import LogicAdapter

from sugaroid.brain.constants import LET_THIS_HAPPEN
from sugaroid.brain.postprocessor import random_response

from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize
from sugaroid.core.statement import SugaroidStatement


class LetAdapter(LogicAdapter):
    """
    Takes care of assuming statements. Eg: Let a = 1
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        self.normalized = tuple(x.lower() for x in normalize(str(statement)))
        if len(self.normalized) > 1 and self.normalized[0] in ("let", "assume"):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        response = random_response(LET_THIS_HAPPEN)
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = 1

        selected_statement.emotion = Emotion.blush

        return selected_statement
