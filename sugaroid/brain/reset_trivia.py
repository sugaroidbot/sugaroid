from chatterbot.logic import LogicAdapter
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize
from sugaroid.core.statement import SugaroidStatement


class TriviaAdapter(LogicAdapter):
    """
    Resets the game of a trivia game
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.cos = None
        self.normalized = None
        self.bool = None

    def can_process(self, statement):
        self.normalized = normalize(str(statement).lower())
        if (
            ("yes" in self.normalized)
            or ("no" in self.normalized)
            or ("true" in self.normalized)
            or ("false" in self.normalized)
        ):
            boolean = True
        else:
            boolean = False
        if self.chatbot.globals["trivia_answer"] and boolean:
            return True
        else:
            self.chatbot.globals["trivia_answer"] = None
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        selected_statement = SugaroidStatement("Ok!", chatbot=True)
        selected_statement.confidence = 0
        selected_statement.emotion = Emotion.neutral
        return selected_statement
