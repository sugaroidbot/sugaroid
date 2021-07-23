from chatterbot.logic import LogicAdapter
from nltk import word_tokenize, pos_tag

from sugaroid.version import VERSION
from sugaroid.brain.constants import BYE, ONE_WORD, WHO_AM_I, WHO_ARE_YOU, SUGAROID
from sugaroid.brain.myname import MyNameAdapter
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.preprocessors import normalize
from sugaroid.core.statement import SugaroidStatement


class TwoWordAdapter(LogicAdapter):
    """
    Hanfles sentences having two wrods
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.normalized = None
        self.intersect = None
        self.tokenized = None

    def can_process(self, statement):
        self.normalized = normalize(str(statement))

        if len(self.normalized) == 2:
            return True
        elif len(self.normalized) == 3:
            self.tokenized = pos_tag(self.normalized)
            if self.tokenized[2][1] == ".":
                return True
            else:
                return False
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        emotion = Emotion.seriously
        confidence = 0.81
        response = random_response(ONE_WORD)
        short = str(statement).lower()

        if ("name" in short) and ("my" in short):
            if self.chatbot.globals["USERNAME"]:
                response = "You are {}".format(self.chatbot.globals["USERNAME"])
            else:
                response = random_response(WHO_AM_I)

        elif ("name" in short) and ("your" in short):
            v = VERSION
            response = "\n{} \n{}. \nBuild: {}".format(
                SUGAROID[0], random_response(WHO_ARE_YOU), v.get_commit()
            )

        else:
            confidence = 0.2

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        selected_statement.adapter = None
        return selected_statement
