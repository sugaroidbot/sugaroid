from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.constants import RNDQUESTIONS
from sugaroid.brain.postprocessor import cosine_similarity, random_response
from sugaroid.brain.preprocessors import normalize


class ReverseAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.chatbot = chatbot

    def can_process(self, statement):
        normalized = normalize(str(statement))
        if (('think' in normalized) or ('ask' in normalized)) and ('me' in normalized):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        _ = normalize
        cos = max([
            cosine_similarity(_(str(statement)), _('Make me think')),
            cosine_similarity(_(str(statement)), _('Ask me something')),
            cosine_similarity(_(str(statement)), _('Ask me a question'))
        ])

        response_raw = random_response(RNDQUESTIONS)
        response = response_raw[0]
        self.chatbot.reverse = True
        self.chatbot.next = response_raw[1]
        self.chatbot.next_type = response_raw[2]

        confidence = cos + (cos/(cos+10))
        print(self.chatbot.next)
        selected_statement = Statement(response)
        selected_statement.confidence = confidence
        return selected_statement
