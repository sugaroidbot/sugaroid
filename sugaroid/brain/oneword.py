from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.version import VERSION
from sugaroid.brain.constants import (
    ONE_WORD,
    DISCLAIMER,
    HI_WORDS,
    HI_RESPONSES,
    LICENSE,
    CREDITS,
)
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.core.statement import SugaroidStatement


class OneWordAdapter(SugaroidLogicAdapter):
    """
    Logical adapter for processing data with one words
    """

    def can_process(self, statement: SugaroidStatement) -> bool:
        if len(statement.words) == 1:
            return True
        elif len(statement.words) == 2:
            if statement.doc[-1].tag_ == ".":
                return True
        return False

    def process(
        self,
        statement: SugaroidStatement,
        additional_response_selection_parameters=None,
    ) -> SugaroidStatement:
        emotion = Emotion.seriously
        confidence = 0.40
        response = random_response(ONE_WORD)
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        selected_statement.adapter = None
        return selected_statement
