import random

import pyjokes
import requests
from chatterbot.logic import LogicAdapter
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize


class JokeAdapter(LogicAdapter):
    """
    Gets a random joke from the Chuck Norris Database
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        normalized = normalize(str(statement).lower())
        if (
            ("tell" in normalized) or ("say" in normalized) or ("crack" in normalized)
        ) and ("joke" in normalized):
            return True
        elif (len(normalized) == 1) and (
            self.chatbot.lp.similarity("joke", str(statement).lower()) >= 0.9
        ):
            return True
        elif "joke" in normalized:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        # https://github.com/pratishrai/doraemon/blob/302a78f8ace4b4675f3cd293dce101ea448b3e13/cogs/fun.py#L1
        try:
            response2 = requests.get(
                "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
            ).json()
            joke = response2["joke"]
        except Exception as e:
            joke = f"I think I am a joke sometimes.. {e}"

        selected_statement = SugaroidStatement(joke, chatbot=True)
        selected_statement.confidence = 0.95

        emotion = Emotion.lol
        selected_statement.emotion = emotion
        return selected_statement
