from chatterbot.logic import LogicAdapter
from sugaroid.brain.ooo import Emotion
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.trivia.trivia import SugaroidTrivia


class TriviaAdapter(LogicAdapter):
    """
    Plays a short game of trivia
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.cos = None

    def can_process(self, statement):
        self.cos = max(
            [
                self.chatbot.lp.similarity(str(statement), "Ask me a question"),
                self.chatbot.lp.similarity(str(statement), "Lets have some trivia"),
                self.chatbot.lp.similarity(str(statement), "Play trivia"),
                self.chatbot.lp.similarity(str(statement), "Can you ask some quiz"),
                self.chatbot.lp.similarity(str(statement), "Can you quiz"),
                self.chatbot.lp.similarity(str(statement), "Can you play trivia"),
            ]
        )
        if self.cos > 0.9:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        st = SugaroidTrivia()
        response = st.ask()
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = self.cos
        self.chatbot.globals["trivia_answer"] = st.answer()
        emotion = Emotion.neutral
        selected_statement.emotion = emotion
        return selected_statement
