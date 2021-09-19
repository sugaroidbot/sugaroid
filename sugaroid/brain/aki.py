"""
This module in Sugaroid uses a licensed term 'Akinator'. Sugaroid and its developer
attributes its author here
Elokence.com – SARL a limited liability company with a share capital of 80,000€,
whose head office is 8, rue Jules Vallès – 28 300 Mainvilliers – France,
and registered with the Chartres Register of Companies under the number
501 030 316. The design and contents of the Website constitute a protected
work under current intellectual property laws, of which Elokence is the
rightholder. The Publications Director is Mr Arnaud MÉGRET, manager of
Elokence.com.

The author takes no right over the information provided by Akinator and is
solely provided by the WebAPI Akinator.com.
All rights reserved to Akinator.

The creator of Akinator.py NinjaSnails is also attributed. The Akinator wrapper
for python is provided under OpenSource License (MIT)

"""
import akinator
import json
from sugaroid.brain.postprocessor import random_response

from sugaroid.brain.constants import HOPE_GAME_WAS_GOOD
from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.core.bot import SugaroidBot
from sugaroid.core.statement import SugaroidStatement
from sugaroid.brain.ooo import Emotion

try:
    from akinator import (
        Akinator,
        AkiServerDown,
        AkiTechnicalError,
        CantGoBackAnyFurther,
    )

    akinator_exists = True
except ModuleNotFoundError:
    akinator_exists = False


AKINATOR_RULES = """
How to Play:
+ think of a character, real or fictional, keep it well in mind
+ answer the questions as truthfully as possible
+ Sugaroid genie will try to guess your person out
+ Best of luck; have fun!
"""

AKINATOR_ACCEPTED_ANSWER = """
Accepted answers are:
yes: y, yes, 0
no: n, no, 1
probably not: pn, probably not, 4
probably: p, probably, 3
I don't know: idk, i dont know, i don't know, 2
"""


class SugaroidAkinator:
    def __init__(self, chatbot: SugaroidBot):
        self.chatbot = chatbot
        self.aki = Akinator()
        self.winning = False
        self.check = False
        try:
            self.game_instance = self.aki.start_game("en")
        except (AkiServerDown, AkiTechnicalError, json.decoder.JSONDecodeError):
            try:
                self.game_instance = self.aki.start_game("en")
            except (AkiServerDown, AkiTechnicalError, json.decoder.JSONDecodeError):
                self.game_instance = None

    def start_game(self):
        # We are about to start the game. Lets send a fascinating entry
        response = (
            "Lets start the play of Akinator™ with me. I, Sugaroid, am your host genie 🔮 for your "
            "competition{}"
            "Here is your first question\n{}".format(AKINATOR_RULES, self.game_instance)
        )
        self.chatbot.globals["akinator"]["enabled"] = True
        return response

    def progression(self, statement):
        if self.aki.progression <= 80:
            user_input = str(statement)
            if (
                (user_input.lower() == "back")
                or (user_input.lower() == "try again")
                or (user_input.lower() == "b")
            ):
                try:
                    self.game_instance = self.aki.back()
                except CantGoBackAnyFurther:
                    pass
            else:
                try:
                    self.game_instance = self.aki.answer(user_input)
                    return self.game_instance
                except akinator.exceptions.InvalidAnswerError:
                    return "Seems like I cannot understand your answer \n{}".format(
                        AKINATOR_ACCEPTED_ANSWER
                    )
        else:
            self.winning = True
            return False

    def win(self):
        self.aki.win()
        self.check = True
        return f"It's {self.aki.first_guess['name']} ({self.aki.first_guess['description']})! Was I correct?\n{self.aki.first_guess['absolute_picture_path']}\n\t"

    def start_check(self):
        return self.check

    def game_over(self):
        return self.winning

    def check_ans(self, statement):
        statement = str(statement)
        if (
            ("yes" in statement.lower())
            or ("yea" in statement.lower())
            or ("exactly" in statement.lower())
            or ("obviously" in statement.lower())
            or ("correct" in statement.lower())
            or ("right" in statement.lower())
            or ("you" in statement.lower() and "won" in statement.lower())
            or statement.lower() == "yes"
            or statement.lower() == "y"
            or statement.lower() == "yea"
        ):
            response = "Yay! I won the game! 👊🎃🎁🎉 "
        else:
            response = "Oh. I failed the same. Seems like you are smarter than me. 😩🙀"
        response = response + "\n{}\n I am back to my business".format(
            random_response(HOPE_GAME_WAS_GOOD)
        )
        self.chatbot.globals["akinator"]["enabled"] = False
        self.chatbot.globals["akinator"]["class"] = None
        return response


class AkinatorAdapter(SugaroidLogicAdapter):
    """
    Adapter which ports the wrapper of the Akinator game to Sugaroid
    """

    def can_process(self, statement):
        if (("akinator" in statement.words) and akinator_exists) and (
            "not" not in statement.words
        ):
            return True
        else:
            return self.chatbot.globals["akinator"]["enabled"]

    def process(
        self,
        statement: SugaroidStatement,
        additional_response_selection_parameters=None,
    ):
        response = None
        confidence = 2.0  # FIXME: Override all other answers
        emotion = Emotion.genie

        if "stop" in statement.words:
            self.chatbot.globals["akinator"]["enabled"] = False
            response = "I am sorry. You quit the game abrubtly. {}".format(
                random_response(HOPE_GAME_WAS_GOOD)
            )
        elif not self.chatbot.globals["akinator"]["enabled"]:
            sugaroid_akinator_instance = SugaroidAkinator(self.chatbot)
            if sugaroid_akinator_instance.game_instance is None:
                response = "Sorry dude. Better luck next time. I am feeling sleepy for a game. 🥱"
            else:
                self.chatbot.globals["akinator"]["class"] = sugaroid_akinator_instance
                response = self.chatbot.globals["akinator"]["class"].start_game()
                response += "<sugaroid:yesno>"
        else:
            if not self.chatbot.globals["akinator"]["class"].game_over():
                response = self.chatbot.globals["akinator"]["class"].progression(
                    statement
                )
                if not response:
                    response = self.chatbot.globals["akinator"]["class"].win()
                else:
                    response += "<sugaroid:yesno>"

            else:
                if self.chatbot.globals["akinator"]["class"].start_check():
                    response = self.chatbot.globals["akinator"]["class"].check_ans(
                        statement
                    )
                    response += "<sugaroid:yesno>"

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.set_confidence(confidence)
        selected_statement.set_emotion(emotion)
        return selected_statement
