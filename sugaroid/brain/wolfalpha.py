import os
import requests
from chatterbot.logic import LogicAdapter
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize


class WolframAlphaAdapter(LogicAdapter):
    """
    Wolfram Alpha Adapter for Sugaroid
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.normalized = None

    def can_process(self, statement):
        self.normalized = str(statement).strip("?,+/.;!").lower().split()
        contains_numbers = False
        for i in self.normalized:
            if any((j.isdigit() for j in i)):
                contains_numbers = True
        return (
            (
                "why" in self.normalized
                or "who" in self.normalized
                or "int" in self.normalized
                or "when" in self.normalized
                or "which" in self.normalized
                or "where" in self.normalized
                or "how" in self.normalized
                or contains_numbers
            )
            and os.getenv("WOLFRAM_ALPHA_API")
            and not (
                "you" in self.normalized
                or "favorite" in self.normalized
                or "favourite" in self.normalized
                or "me" in self.normalized
                or "like" in self.normalized
                or "your" in self.normalized
                or "what" in self.normalized
                or "him" in self.normalized
                or "her" in self.normalized
                or "she" in self.normalized
                or "he" in self.normalized
                or "them" in self.normalized
                or "i" in self.normalized
            )
        )

    def process(self, statement, additional_response_selection_parameters=None):
        url = (
            "https://api.wolframalpha.com/v2/query?"
            "input={query}"
            "&format=plaintext&output=JSON&appid={appid}"
        )
        url = url.format(
            query="+".join(self.normalized),
            appid=os.getenv("WOLFRAM_ALPHA_API", "DEMO"),
        )
        response = requests.get(url, headers={"Accept": "application/json"}).json()
        if not response["queryresult"]["success"]:
            confidence = 0.3
            try:
                text = response["queryresult"]["tips"]["text"]
            except KeyError:
                text = "Wolfram Alpha didnt send back a response"
                confidence = 0
            selected_statement = SugaroidStatement(text, chatbot=True)
            selected_statement.confidence = confidence
            selected_statement.emotion = Emotion.positive
            return selected_statement

        information = []
        for i in response["queryresult"]["pods"]:
            for j in i["subpods"]:
                try:
                    if j["img"]["alt"] == "Plot":
                        information.append(j["img"]["src"])
                except KeyError:
                    pass
                if j["plaintext"]:
                    information.append(j["plaintext"])

        interpretation = "\n".join(information)
        selected_statement = SugaroidStatement(interpretation, chatbot=True)
        selected_statement.confidence = 1
        emotion = Emotion.lol
        selected_statement.emotion = emotion
        return selected_statement
