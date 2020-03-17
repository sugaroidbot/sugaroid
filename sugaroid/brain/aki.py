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
try:
    from akinator import Akinator, AkiServerDown, AkiTechnicalError

    akinator_exists = True
except ModuleNotFoundError:
    akinator_exists = False

from chatterbot.logic import LogicAdapter
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize


class AkinatorAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.aki = False

    def can_process(self, statement):
        normalized = normalize(str(statement).lower())
        if ('akinator' in normalized) and akinator_exists:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        response = None
        confidence = 2.0  # FIXME: Override all other answers
        emotion = Emotion.rich


        selected_statement = SugaroidStatement(response)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        return selected_statement


    def akinator_init(self):
        self.aki = Akinator()
        try:
            game_instance = self.aki.start_game("en2")
        except (AkiServerDown, AkiTechnicalError):
            try:
                game_instance = self.aki.start_game("en3")
            except (AkiServerDown, AkiTechnicalError):
                game_instance = self.aki.start_game("en3")

        if not self.chatbot.akinator:
            # We are about to start the game. Lets send a fascinating entry
            response = "Lets start the play of Akinator with me. I, Sugaroid is your host genie for your competition\n" \
                       "Here is your first question\n\n{}".format(game_instance)
            self.chatbot.akinator = True
            return response



while aki.progression <= 80:
    a = input(q + "\n\t")
    if a == "b":
        try:
            q = aki.back()
        except akinator.CantGoBackAnyFurther:
            pass
    else:
        q = aki.answer(a)
aki.win()

correct = input(f"It's {aki.name} ({aki.description})! Was I correct?\n{aki.picture}\n\t")
if correct.lower() == "yes" or correct.lower() == "y":
    print("Yay\n")
else:
    print("Oof\n")