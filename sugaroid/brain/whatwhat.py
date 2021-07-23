from chatterbot.logic import LogicAdapter
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize
from sugaroid.core.statement import SugaroidStatement


class WhatWhatAdapter(LogicAdapter):
    """
    Handles statements that ask for a clarification. Wait what?
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.normalized = None
        self.intersect = None
        self.last_word_idx = None
        self.last_word = []

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        if self.chatbot.globals["history"]["total"][-1] == 0:
            return False
        if "what" in self.normalized:
            try:
                word_before_what = self.normalized[self.normalized.index("what") - 1]
            except IndexError:
                return False
            self.last_word = normalize(
                str(self.chatbot.globals["history"]["total"][-1])
            )
            if word_before_what in self.last_word:
                self.last_word_idx = self.last_word.index(word_before_what)
                return True
            else:
                return False
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        response = "What?"
        emotion = Emotion.angry_non_expressive
        words = self.last_word[self.last_word_idx + 1 :]
        for i in words:
            if i is None:
                break
        else:
            response = " ".join(words)

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = 1

        selected_statement.emotion = emotion

        return selected_statement
