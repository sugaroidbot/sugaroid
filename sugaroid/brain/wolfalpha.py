"""
Wolfram|Alpha Adapter is an adapter which is used to
fetch results from the Wolfram ALpha server

MARKS LICENSE AND ATTRIBUTION"Wolfram|Alpha Marks" means the trade names, trademarks,
service marks, logos, domain names and other distinctive marks of
Wolfram|Alpha. Wolfram|Alpha grants You a non-exclusive license to use the
Wolfram|Alpha Marks solely in connection with their display on or through the
API Client as delivered by Wolfram|Alpha. Your API Client shall provide proper
attribution to Wolfram|Alpha whenever such content is displayed or accessed by
providing the end user with a direct link to the specific Wolfram|Alpha result
page from which the content was derived. Wolfram|Alpha may terminate Your license
 to use the Wolfram|Alpha Marks at any time for any or no reason. You shall not at
  any time challenge or assist others to challenge Wolfram|Alpha Marks or their
   registration (except to the extent You cannot give up that right by law) or to
   register any trademarks, marks, domains or trade names obviously similar, in
    Wolfram|Alpha's discretion, to those of Wolfram|Alpha. This prohibition
    survives any termination or expiration of this Agreement.
LINKINGUnless part of a written agreement to the contrary, You are required
to provide a conspicuous hyperlink directly to the corresponding results page
of the Wolfram|Alpha website (http://www.wolframalpha.com) on every page with Results.
"""


import os
import requests

from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.core.statement import SugaroidStatement
from sugaroid.sugaroid import sugaroid_logger
from sugaroid.brain.ooo import Emotion


class WolframAlphaAdapter(SugaroidLogicAdapter):
    """
    Wolfram Alpha Adapter for Sugaroid
    """

    def can_process(self, statement: SugaroidStatement):
        contains_numbers = False
        for i in statement.simple:
            if any((j.isdigit() for j in i)):
                contains_numbers = True
        return (
            (
                "why" in statement.simple
                or "who" in statement.simple
                or "int" in statement.simple
                or "when" in statement.simple
                or "which" in statement.simple
                or "where" in statement.simple
                or "how" in statement.simple
                or "$wolf" in statement.simple
                or contains_numbers
            )
            and os.getenv("WOLFRAM_ALPHA_API")
            and not (
                "you" in statement.simple
                or "favorite" in statement.simple
                or "favourite" in statement.simple
                or "me" in statement.simple
                or "like" in statement.simple
                or "your" in statement.simple
                or "what" in statement.simple
                or "him" in statement.simple
                or "her" in statement.simple
                or "she" in statement.simple
                or "he" in statement.simple
                or "them" in statement.simple
                or "i" in statement.simple
            )
        )

    def process(
        self,
        statement: SugaroidStatement,
        additional_response_selection_parameters=None,
    ):
        wolf_command = False
        user_requests_text = False
        supports_media = self.chatbot.globals["media"]
        rich_text = self.chatbot.globals["rich"]

        if "$wolf" in statement.simple:
            # this is a command type wolfram alpha request
            wolf_command = True
            statement.simple.remove("$wolf")
            if "$text" in statement.simple:
                user_requests_text = True
                statement.simple.remove("$text")

        url = (
            "https://api.wolframalpha.com/v2/query?"
            "input={query}"
            "&format={format}&output=JSON&appid={appid}"
        )
        url = url.format(
            query="+".join(statement.simple),
            appid=os.getenv("WOLFRAM_ALPHA_API", "DEMO"),
            format="image,plaintext" if supports_media else "plaintext",
        )
        sugaroid_logger.info(f"WolframAlpha endpoint: {url}")
        response = requests.get(url, headers={"Accept": "application/json"}).json()

        if not response["queryresult"]["success"]:
            confidence = 0.3
            try:
                text = response["queryresult"]["tips"]["text"]
            except KeyError:
                text = "Wolfram Alpha didnt send back a response"
                confidence = 0
                if wolf_command:
                    confidence = 1
            selected_statement = SugaroidStatement(text, chatbot=True)
            selected_statement.confidence = confidence
            selected_statement.emotion = Emotion.positive
            return selected_statement

        information = []

        for i in response["queryresult"]["pods"]:
            for j in i["subpods"]:
                if j["plaintext"]:
                    plaintext_answer = j["plaintext"].split("\n")
                    for ans in plaintext_answer:
                        splitted_ans = ans.split("|")
                        sugaroid_logger.info("splitted_ans")
                        if len(splitted_ans) == 1:
                            front = splitted_ans[0]
                            back, rest = "", ""
                        elif len(splitted_ans) == 2:
                            front, back = splitted_ans
                            rest = ""
                        else:
                            front, back, rest = (
                                splitted_ans[0],
                                splitted_ans[1],
                                splitted_ans[2:],
                            )

                        if rich_text:
                            if not back:
                                information.append(f"<b>{front}</b>")
                            else:
                                information.append(
                                    f"<b>{front}</b>: {back} {' '.join(rest)}"
                                )
                        else:
                            if not back:
                                information.append(f"{front}")
                            else:
                                information.append(f"{front}: {back} {' '.join(rest)}")

        if supports_media:
            information.append("<sugaroid:br>")
            for i in response["queryresult"]["pods"]:
                for j in i["subpods"]:
                    if not j.get("plaintext") and j.get("img") and j["img"].get("src"):
                        information.append(
                            f'<sugaroid:img>{j["img"]["src"]}<sugaroid:br>'
                        )

        information.append("Results powered by Wolfram|Alpha (wolframalpha.com)")

        interpretation = "\n".join(information)

        selected_statement = SugaroidStatement(interpretation, chatbot=True)
        selected_statement.set_confidence(1)
        selected_statement.set_emotion(Emotion.lol)
        return selected_statement
