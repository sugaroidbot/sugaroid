from sugaroid.brain.constants import SUGAROID_CAN_AGREE, SUGAROID_CAN_DISAGREE
from sugaroid.brain.postprocessor import random_response

from sugaroid.brain.ooo import Emotion
from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.core.statement import SugaroidStatement


class AssertiveAdapter(SugaroidLogicAdapter):
    """
    Handles assertive and imperative statements
    """

    def can_process(self, statement: SugaroidStatement) -> bool:
        if len(str(statement).split()) >= 3:
            s = statement.doc
            if (s[0].pos_ in ["its", "this"] or s[0].lower_ == "it") and (
                s[1].pos_ == "NOUN"
                or s[1].pos_ == "VERB"
                or (s[1].pos_ == "ADV" and s[2].pos_ == "VERB")
            ):
                return True
        elif len(str(statement).split()) >= 2:
            s = statement.doc
            if (s[0].pos_ == "DET" or s[0].lower_ == "it's") and (
                s[1].pos_ == "NOUN" or s[1].pos_ == "VERB"
            ):
                return True

        return False

    def process(
        self,
        statement: SugaroidStatement,
        additional_response_selection_parameters=None,
    ):
        ps = self.sia.polarity_scores(statement.text)
        if ps["neu"] == 1 or (ps["pos"] > ps["neg"]):
            response = random_response(SUGAROID_CAN_AGREE)
            confidence = 0.81
        else:
            response = random_response(SUGAROID_CAN_DISAGREE)
            confidence = 0.3

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.set_confidence(confidence)
        selected_statement.set_emotion(Emotion.angel)
        return selected_statement
