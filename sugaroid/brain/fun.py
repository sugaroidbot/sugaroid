
from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.constants import EMOJI_SMILE
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.sugaroid import SugaroidStatement


class FunAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        if self.chatbot.fun:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):

        emotion = Emotion.neutral
        # Randomly select a confidence between 0 and 1
        confidence = 0.1

        #  we will just return the input as output
        parsed = str(statement)
        if 'not' in parsed:
            suffix = " either. "
            prefix = ""
            emotion = Emotion.wink
        else:

            suffix = " too {}".format(random_response(EMOJI_SMILE))
            prefix = "Let me try that, "
            emotion = Emotion.wink

        selected_statement = SugaroidStatement(
            "{pre}{main}{fix}".format(pre=prefix, main=parsed, fix=suffix))
        selected_statement.confidence = confidence

        selected_statement.emotion = emotion
        return selected_statement
