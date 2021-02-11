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
        # https://github.com/pratishrai/doraemon/blob/302a78f8ace4b4675f3cd293dce101ea448b3e13/cogs/fun.py#L15
        url = "https://icanhazdadjoke.com/"
        response1 = requests.get(url, headers={"Accept": "application/json"}).json()
        response2 = requests.get(
            "https://sv443.net/jokeapi/v2/joke/Miscellaneous,Dark?type=single"
        ).json()
        responses = [response1, response2, response3]
        joke = random.choice(responses)
        selected_statement = SugaroidStatement(joke, chatbot=True)
        selected_statement.confidence = 0.95

        emotion = Emotion.lol
        selected_statement.emotion = emotion
        return selected_statement
