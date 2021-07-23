from chatterbot.logic import LogicAdapter
from sugaroid.brain.ooo import Emotion
from sugaroid.core.statement import SugaroidStatement


class WaitWhatAdapter(LogicAdapter):
    """
    Handles statements that ask for a re-clarification. Compare WhatWhatAdapter
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):

        if statement.tokens.similarity(self.chatbot.lp.tokenize("Wait what ?")) > 0.8:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        response = "What?"
        selected_statement = SugaroidStatement(response, chatbot=True)
        if self.chatbot.globals["history"]["total"][-1] != 0:
            selected_statement = self.chatbot.globals["history"]["total"][-1]

        selected_statement.confidence = 1
        selected_statement.emotion = Emotion.angel
        return selected_statement
