
from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.constants import EMOJI_SMILE
from sugaroid.brain.postprocessor import random_response


class FunAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        return True

    def process(self, statement, additional_response_selection_parameters=None):
        import random

        # Randomly select a confidence between 0 and 1
        confidence = 0.1

        # For this example, we will just return the input as output
        parsed = str(statement)
        if 'not' in parsed:
            suffix = " either. "
            prefix = ""
        else:
            suffix = " too {}".format(random_response(EMOJI_SMILE))
            prefix = "Let me try that, "

        selected_statement = Statement(
            "{pre}{main}{fix}".format(pre=prefix, main=parsed, fix=suffix))
        selected_statement.confidence = confidence

        return selected_statement
