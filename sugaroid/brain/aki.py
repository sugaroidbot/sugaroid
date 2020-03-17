"""
MIT License

Sugaroid Artificial Inteligence
Chatbot Core
Copyright (c) 2020 Srevin Saju

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
from sugaroid.brain.constants import HOPE_GAME_WAS_GOOD

try:
    from akinator import Akinator, AkiServerDown, AkiTechnicalError, CantGoBackAnyFurther
    akinator_exists = True
except ModuleNotFoundError:
    akinator_exists = False
from chatterbot.logic import LogicAdapter
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize


class SugaroidAkinator:
    def __init__(self, chatbot):
        self.chatbot = chatbot
        self.aki = Akinator()
        self.winning = False
        self.check = False
        try:
            self.game_instance = self.aki.start_game("en2")
        except (AkiServerDown, AkiTechnicalError):
            try:
                self.game_instance = self.aki.start_game("en3")
            except (AkiServerDown, AkiTechnicalError):
                self.game_instance = self.aki.start_game("en3")

    def start_game(self):
        # We are about to start the game. Lets send a fascinating entry
        response = "Lets start the play of Akinator™ with me. I, Sugaroid is your host genie :crystal_ball: for your " \
            "competition\n" \
            "Here is your first question\n\n{}".format(self.game_instance)
        self.chatbot.akinator = True
        return response

    def progression(self, statement):
        if self.aki.progression <= 80:
            user_input = str(statement)
            if (user_input.lower() == "back") or (user_input.lower() == "try again") \
                    or (user_input.lower() == "b"):
                try:
                    self.game_instance = self.aki.back()
                except CantGoBackAnyFurther:
                    pass
            else:
                self.game_instance = self.aki.answer(user_input)
                return self.game_instance
        else:
            self.winning = True
            return False

    def win(self):
        self.aki.win()
        self.check = True
        return f"It's {self.aki.name} ({self.aki.description})! Was I correct? :thinking_face:\n{self.aki.picture}\n"

    def start_check(self):
        return self.check

    def game_over(self):
        return self.winning

    def check_ans(self, statement):
        statement = str(statement)
        if statement.lower() == "yes" or statement.lower() == "y" or statement.lower() == "yea":
            response = "Yay! I won the game! :punch: :jack_o_lantern: :gift: :tada:"
        else:
            response = "Oh. I failed the same. Seems like you are smarter than me. :weary:"
        response = response + \
            "\n{}\n I am back to my business".format(HOPE_GAME_WAS_GOOD)
        self.chatbot.akinator = False
        self.chatbot.aki = None
        return response


class AkinatorAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.aki = False
        self.game_instance = None

    def can_process(self, statement):
        normalized = normalize(str(statement).lower())
        if (('akinator' in normalized) and akinator_exists) and ('not' not in normalized):
            return True
        else:
            return self.chatbot.akinator

    def process(self, statement, additional_response_selection_parameters=None):
        response = None
        confidence = 2.0  # FIXME: Override all other answers
        emotion = Emotion.genie
        if not self.chatbot.akinator:
            self.chatbot.aki = SugaroidAkinator(self.chatbot)
            response = self.chatbot.aki.start_game()
        else:
            if not self.chatbot.aki.game_over():
                response = self.chatbot.aki.progression(statement)
                if not response:
                    response = self.chatbot.aki.win()
            else:
                if self.chatbot.aki.start_check():
                    response = self.chatbot.aki.check_ans(statement)

        selected_statement = SugaroidStatement(response)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        return selected_statement
