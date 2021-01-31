import logging

from chatterbot.logic import LogicAdapter
from sugaroid.brain.postprocessor import random_response

from sugaroid.brain.constants import IMITATE
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize, spac_token


class ImitateAdapter(LogicAdapter):
    """
    Handles statements involving imitations of some sentences
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.normalized = None

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        more_words = len(self.normalized) > 3
        logging.info(
            "ImitatorSensei: userhistory {}, history: {}".format(
                self.chatbot.globals["history"]["user"],
                self.chatbot.globals["history"]["total"],
            )
        )
        if (
            self.chatbot.globals["history"]["user"][-1]
            and self.chatbot.globals["history"]["total"][-1]
            and more_words
        ):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        emotion = Emotion.lol
        sim = self.chatbot.lp.similarity(
            str(statement), str(self.chatbot.globals["history"]["total"][-1])
        )
        logging.info(
            "ImitatorSensei compared {} and {}. Sim: {}".format(
                str(statement), self.chatbot.globals["history"]["user"][-1], sim
            )
        )
        if sim > 0.8:
            response = random_response(IMITATE)
            confidence = sim
        else:
            response = "Ok!"
            confidence = 0
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        return selected_statement
