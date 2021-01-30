"""
MIT License

Sugaroid Artificial Intelligence
Chatbot Core
Copyright (c) 2020-2021 Srevin Saju
Copyright (c) 2021 The Sugaroid Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
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
                and "favorite" in self.normalized
                and "favourite" in self.normalized
                and "me" in self.normalized
                and "like" in self.normalized
                and "your" in self.normalized
                and "what" in self.normalized
                and "him" in self.normalized
                and "her" in self.normalized
                and "she" in self.normalized
                and "he" in self.normalized
                and "them" in self.normalized
                and "i" in self.normalized
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
