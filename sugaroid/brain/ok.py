import random

from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter


class OkayAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        if (str(statement).lower() == 'ok') or (str(statement).lower() == 'okay'):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        confidence = 1
        ls = ['༼ つ ◕_◕ ༽', '( ͡° ͜ʖ ͡°)', '(⌐■_■)',
              '(စ__စ )', '(ၜ冖ၜ)', '( ဖ‿ဖ)']
        random.randint(0, 5)
        selected_statement = Statement("ok ok ")
        selected_statement.confidence = confidence
        return selected_statement
