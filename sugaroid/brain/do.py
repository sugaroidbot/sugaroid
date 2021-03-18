import nltk
from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.wiki import WikiAdapter
from sugaroid.sugaroid import SugaroidStatement


class DoAdapter(LogicAdapter):
    """
    Processes statements beginning with 'Do' and 'know'
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.normalized = False

    def can_process(self, statement):
        self.normalized = nltk.word_tokenize(str(statement).lower())
        if "do" in self.normalized and "know" in self.normalized:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        emotion = Emotion.neutral
        response = "ok"
        confidence = 0

        rectified = []
        tokenized = nltk.pos_tag(self.normalized)
        for i in range(len(tokenized)):
            if tokenized[i][1] == "WP":
                rectified.extend(self.normalized[i:])
                break
            else:
                continue
        else:
            if ("my" in self.normalized) and ("name" in self.normalized):
                if self.chatbot.get_username():
                    response = "Your name is {}".format(
                        self.chatbot.globals["username"]
                    )
                    emotion = Emotion.neutral
                    confidence = 1
                else:
                    response = "No, I don't know your name"
                    emotion = Emotion.cry_overflow
                    confidence = 0.8
            elif "my" in self.normalized:
                response = "Lol, maybe not"
                emotion = Emotion.lol
                confidence = 0.8
            else:
                response = "Yes, Yes I do!"
                emotion = Emotion.wink
                confidence = 0.8

        if rectified:
            if "Srevin" in rectified:
                response = "Srevin Saju is the creator of Sugaroid bot"
                confidence = 1
            else:
                wk = WikiAdapter(self.chatbot)
                wk.text = self.normalized
                response = WikiAdapter.process(wk, Statement(" ".join(rectified)))
                return response

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence

        selected_statement.emotion = emotion
        return selected_statement
