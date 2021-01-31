from chatterbot.logic import LogicAdapter
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize


class ResetAdapter(LogicAdapter):
    """
    Resets the Sugaroid global variables
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        normalized = normalize(str(statement).lower())
        if "reset" in normalized and "admin" in normalized:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        self.chatbot.reset_variables()
        selected_statement = SugaroidStatement(
            "Reset of chatbot variables. SUCCESS", chatbot=True
        )
        selected_statement.confidence = 0.95

        emotion = Emotion.neutral
        selected_statement.emotion = emotion
        return selected_statement
