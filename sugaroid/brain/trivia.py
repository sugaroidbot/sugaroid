from sugaroid.brain.ooo import Emotion
from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.core.statement import SugaroidStatement
from sugaroid.trivia.trivia import SugaroidTrivia


class TriviaAdapter(SugaroidLogicAdapter):
    """
    Plays a short game of trivia
    """

    def can_process(self, statement: SugaroidStatement):
        if self.chatbot.globals["trivia"]["enabled"]:
            return True

        for i in (
            "Ask me a question",
            "Lets have some trivia",
            "play trivia",
            "Lets have some trivia",
            "Lets have some trivia",
            "Can you ask some quiz",
            "Quiz me" "Can you quiz",
            "Can you play trivia",
        ):
            cos = self.chatbot.lp.similarity(str(statement), i)
            if cos > 0.9:
                return True

        return False

    def process(
        self,
        statement: SugaroidStatement,
        additional_response_selection_parameters=None,
    ):
        if self.chatbot.globals["trivia"]["enabled"]:
            # this is the turn for the user to answer
            st = self.chatbot.globals["trivia"]["class"]
            if st.check_answer():
                response = "Correct! You got it right!"
            else:
                response = f"Oops. You got it wrong. The correct answer was {st.correct_answer}"
            self.chatbot.globals["trivia"]["enabled"] = False
            del self.chatbot.globals["trivia"]["class"]
            self.chatbot.globals["trivia"]["class"] = None
        else:
            st = SugaroidTrivia()
            self.chatbot.globals["trivia"]["enabled"] = True
            self.chatbot.globals["trivia"]["class"] = st
            response = st.ask()

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = 1.0
        emotion = Emotion.neutral
        selected_statement.emotion = emotion
        return selected_statement
