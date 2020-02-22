from chatterbot.logic import LogicAdapter


class FunAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
     super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        return True

    def process(self, input_statement, additional_response_selection_parameters):
        import random

        # Randomly select a confidence between 0 and 1
        confidence = random.uniform(0, 0.2)

        # For this example, we will just return the input as output
        selected_statement = input_statement
        selected_statement.confidence = confidence

        return selected_statement