from random import randint

from sugaroid.brain.constants import (
    BOT_POSITIVE,
    BOT_NEGATIVE,
)
from sugaroid.brain.postprocessor import random_response

from sugaroid.brain.ooo import Emotion
from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.core.statement import SugaroidStatement


class HaveAdapter(SugaroidLogicAdapter):
    """
    Handles statements with have
    """

    @staticmethod
    def is_statement_with_have(statement: SugaroidStatement) -> bool:
        return (
            len(statement.words) >= 1
            and statement.words[0] == "have"
            and not statement.words[-1].endswith("?")
        )

    @staticmethod
    def is_question_with_have(statement: SugaroidStatement) -> bool:
        return (
            len(statement.words) > 3
            and statement.words[0] == "did"
            and statement.words[1] == "you"
            and statement.words[2] == "have"
            and statement.words[-1].endswith("?")
        )

    def can_process(self, statement: SugaroidStatement) -> bool:
        return self.is_statement_with_have(statement) or self.is_question_with_have(
            statement
        )

    def process(
        self,
        statement: SugaroidStatement,
        additional_response_selection_parameters=None,
    ):
        confidence = 1
        if "break" in statement.words:
            response = "Sure."
        elif (
            "chocolate" in statement.words
            or "sweet" in statement.words
            or "kitkat" in statement.words
            or "munch" in statement.words
            or "galaxy" in statement.words
        ):
            response = "🍫"
        elif (
            "food" in statement.words
            or "lunch" in statement.words
            or "brunch" in statement.words
            or "dinner" in statement.words
            or "lunner" in statement.words
            or "breakfast" in statement.words
        ):
            if self.is_question_with_have(statement):
                response = "Maybe, maybe not 😼"
            else:
                response = random_response(
                    "🍏🍎🍐🍊🍋🍌🍇🍓🍈🍒🍑🥭🍍🥬🥦🥑🍆🍅🥝🥥🥒🌶🌽🥕🧄🧅🥔🧀🥨🥖🍞🥯🥐🍠🥚🍳🧈🥞🧇🥓🥩🍕🍟🍔🌭🦴🍖🍗🥪🥙🧆"
                    "🌮🌯🥗🥘🍱🍣🍛🍲🍜🍝🥫🥟🦪🍤🍙🍚🍘🍥🍦🍨🍧🍡🍢🥮🥠🥧🧁🍰🎂🍮🍭🍬🍯🥜🌰🍪🍩🍿🍫🥛🍼☕️🍵🧃🥤🍶🍺🍻🥂🍷🥃"
                    "🍸🍹🥣"
                )

        else:
            ps = self.sia.polarity_scores(statement.text)
            if ps["neu"] == 1:
                response = "👀" * randint(1, 10) + ".."
            elif ps["pos"] > ps["neg"]:
                response = random_response(BOT_POSITIVE)
                confidence = 0.7
            else:
                response = random_response(BOT_NEGATIVE)
                confidence = 0.7

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.set_confidence(confidence)
        selected_statement.set_emotion(Emotion.angel)
        return selected_statement
