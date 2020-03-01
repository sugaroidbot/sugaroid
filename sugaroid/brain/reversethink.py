from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.constants import RNDQUESTIONS
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import cosine_similarity, random_response
from sugaroid.brain.preprocessors import normalize
from sugaroid.sugaroid import SugaroidStatement


class ReverseAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.chatbot = chatbot

    def can_process(self, statement):
        normalized = normalize(str(statement))
        if (('think' in normalized) or ('ask' in normalized)) and ('me' in normalized):
            return True
        else:
            if self.chatbot.lp.similarity(str(statement), 'What can you do?') > 0.9:
                return True
            else:
                return False

    def process(self, statement, additional_response_selection_parameters=None):

        cos = max([
            self.chatbot.lp.similarity(str(statement), 'Tell me something'),
            self.chatbot.lp.similarity(str(statement), 'Ask me something'),
            self.chatbot.lp.similarity(str(statement), 'Ask me a question'),
            self.chatbot.lp.similarity(str(statement), 'What can you do?'),
        ])
        if self.chatbot.lp.similarity(str(statement), 'What can you do?') > 0.9:
            response = 'I can say a joke, read a book and answer some questions'
        else:
            response_raw = random_response(RNDQUESTIONS)
            response = response_raw[0]
            self.chatbot.reverse = True
            self.chatbot.next = response_raw[1]
            self.chatbot.next_type = response_raw[2]

        print(self.chatbot.next)
        selected_statement = SugaroidStatement(response)
        selected_statement.confidence = cos
        emotion = Emotion.neutral
        selected_statement.emotion = emotion

        return selected_statement
