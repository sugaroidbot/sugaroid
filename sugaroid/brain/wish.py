from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.version import VERSION
from sugaroid.brain.constants import (
    ONE_WORD,
    DISCLAIMER,
    HI_WORDS,
    HI_RESPONSES,
    LICENSE,
    CREDITS,
    WISH,
)
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.core.statement import SugaroidStatement


class WishAdapter(SugaroidLogicAdapter):
    """
    Logical adapter for receiving and wishing others
    a wonderful day and accepting wishes randomly

    .. warning::
       This adapter is incomplete
    """

    def can_process(self, statement: SugaroidStatement) -> bool:
        for i in statement.words:
            if i in WISH:
                return True

    def process(
        self,
        statement: SugaroidStatement,
        additional_response_selection_parameters=None,
    ) -> SugaroidStatement:
        emotion = Emotion.lol
        confidence = 0.60
        response = random_response(ONE_WORD)

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.set_confidence(confidence)

        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        selected_statement.adapter = None
        return selected_statement
