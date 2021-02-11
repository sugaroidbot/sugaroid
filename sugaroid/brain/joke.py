import random

import requests
from chatterbot.logic import LogicAdapter

from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize


class JokeAdapter(SugaroidLogicAdapter):
    """
    Gets a random joke from the v2.joke api
    """

    def can_process(self, statement: SugaroidStatement) -> bool:
        if (
            ("tell" in statement.words)
            or ("say" in statement.words)
            or ("crack" in statement.words)
        ) and ("joke" in statement.words):
            return True
        elif (len(statement.words) == 1) and (
            self.chatbot.lp.similarity("joke", statement.text) >= 0.9
        ):
            return True
        elif "joke" in statement.words:
            return True
        return False

    def process(
        self,
        statement: SugaroidStatement,
        additional_response_selection_parameters=None,
    ):
        # https://github.com/pratishrai/doraemon/blob/302a78f8ace4b4675f3cd293dce101ea448b3e13/cogs/fun.py#L1
        try:
            response2 = requests.get(
                "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
            ).json()
            try:
                joke = response2["joke"]
            except KeyError:
                setup = response2["setup"]
                delivery = response2["delivery"]
                if self.chatbot.globals["rich"]:
                    joke = f"{setup}\n\n<i>{delivery}</i>"
                else:
                    joke = f"{setup}\n\n{delivery}"
        except Exception as e:
            joke = f"I think I am a joke sometimes.. {e}"

        selected_statement = SugaroidStatement(joke, chatbot=True)
        selected_statement.set_confidence(1)
        selected_statement.set_emotion(Emotion.lol)
        return selected_statement
