from chatterbot.logic import LogicAdapter
from nltk import pos_tag

from sugaroid.brain.constants import (
    WHO_AM_I,
    WHO_ARE_YOU,
    SUGAROID,
    HOW_DO_YOU_FEEL,
    HOW_DO_I_FEEL,
    HOW_DO_HE_FEEL,
)
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.preprocessors import normalize, spac_token
from sugaroid.sugaroid import SugaroidStatement


class FeelAdapter(LogicAdapter):
    """
    Handles sentences containing the word feel
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        self.token = pos_tag(self.normalized)
        if "feel" in self.normalized:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        confidence = 0.9
        # FIXME Creates unusual response
        nn = False
        it = False
        token = spac_token(statement, chatbot=self.chatbot)
        for i in token:
            if (i.tag_ == "NNP") or (i.tag_ == "NN"):
                nn = True
            if i.lower_ == "it":
                it = True

        if nn and not it:
            response = random_response(HOW_DO_HE_FEEL)
            emotion = Emotion.seriously
        elif it:
            response = "Ask it!"
            emotion = Emotion.o
        elif "I" in self.normalized:
            emotion = Emotion.depressed
            response = random_response(HOW_DO_I_FEEL)
        else:
            emotion = Emotion.blush
            response = random_response(HOW_DO_YOU_FEEL)

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion

        return selected_statement
