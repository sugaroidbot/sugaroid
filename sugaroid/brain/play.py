import time
from chatterbot.logic import LogicAdapter
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import spac_token
from sugaroid.sugaroid import SugaroidStatement


class PlayAdapter(LogicAdapter):
    """
    [DEPRECATED] Plays a game on desktops only
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        return False

    def process(self, statement, additional_response_selection_parameters=None):
        response = "I can\t run the same game again. Soz!"
        confidence = 0.5
        sent = []
        for i in games:
            sent.append("play the game {}".format(i))
            sent.append("can you play the game {}".format(i))
        cos = []
        for j in sent:
            cos.append(self.chatbot.lp.similarity(j, str(statement)))
        maxcos = max(cos)
        response = "Ok, I guess your game was great!"
        try:
            exec("from freegames import {}".format(self.game))
        except Exception as e:
            response = "Oops, it cant run on your system"
        import os

        try:
            if os.environ["SUGAROID"] == "CLI":
                input("Enter any key to continue to Sugaroid")
            elif os.environ["SUGAROID"] == "GUI":
                time.sleep(5)
        except KeyError:
            pass
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = maxcos

        selected_statement.emotion = Emotion.neutral
        return selected_statement
