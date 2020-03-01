import random

from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.preprocessors import normalize
from sugaroid.sugaroid import SugaroidStatement


class OkayAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        normalized = normalize(str(statement))
        if 'ok' in normalized or 'okay' in normalized:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        confidence = 1
        ls = ['😀', '😁', '😂',
              '😏', '😝']
        selected_statement = SugaroidStatement(
            "ok ok {}".format(random_response(ls)))
        selected_statement.confidence = confidence
        emotion = Emotion.wink
        selected_statement.emotion = emotion
        return selected_statement
