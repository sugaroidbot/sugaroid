import logging
from chatterbot.logic import LogicAdapter
from nltk import pos_tag
from sugaroid.brain.constants import (
    WHO_AM_I,
    WHO_ARE_YOU,
    SUGAROID,
    GREET,
    BURN_IDK,
    I_AM,
)
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.preprocessors import normalize, spac_token
from sugaroid.core.statement import SugaroidStatement
from sugaroid.version import VERSION


class MyNameAdapter(LogicAdapter):
    """
    Handles sentences featuring 'my' and 'name'
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        self.token = pos_tag(self.normalized)
        if str(statement).strip().lower().startswith("my name is"):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        confidence = 1
        # FIXME Creates unusual response

        nl = spac_token(statement, chatbot=self.chatbot)

        for i in nl:
            if (i.lower_ == "my") or (i.lemma_ == "be") or (i.lower_ == "name"):
                continue
            logging.info("{} {}".format(i, i.pos_))
            if (i.pos_ == "NOUN") or (i.pos_ == "PROPN"):
                response = random_response(GREET).format(str(i.text).capitalize())
                selected_statement = SugaroidStatement(response, chatbot=True)
                selected_statement.confidence = confidence
                emotion = Emotion.positive
                selected_statement.emotion = emotion
                self.chatbot.globals["USERNAME"] = i.text
                return selected_statement
        else:
            response = ":)"
            confidence = 0
            selected_statement = SugaroidStatement(response, chatbot=True)
            selected_statement.confidence = confidence
            emotion = Emotion.neutral
            selected_statement.emotion = emotion

            return selected_statement
