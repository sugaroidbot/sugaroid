
import pyjokes

from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize


class SelectedStatement(object):
    pass


class JokeAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        normalized = normalize(str(statement))
        if (('tell' in normalized) or ('say' in normalized)) and ('joke' in normalized):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        joke = pyjokes.get_joke('en', 'all')
        selected_statement = SelectedStatement(joke)
        selected_statement.confidence = 0.95

        emotion = Emotion.lol
        selected_statement.emotion = emotion
        return selected_statement
