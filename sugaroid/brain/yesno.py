import nltk
from chatterbot.logic import LogicAdapter
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize
from sugaroid.brain.rereversei import reset_reverse
from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.core.statement import SugaroidStatement


class BoolAdapter(SugaroidLogicAdapter):
    """
    Processes Boolean based answers
    """

    def can_process(self, statement: SugaroidStatement):
        normalized = statement.words
        if self.chatbot.globals["akinator"]["enabled"]:
            return False
        elif (
            ("yes" in statement.words)
            or ("yea" in statement.words)
            or ("no" in statement.words)
            or ("true" in statement.words)
            or ("false" in statement.words)
        ):
            if (
                ("yes" in statement.words)
                or ("yea" in statement.words)
                or ("true" in statement.words)
            ):
                self.bool = True
            else:
                self.bool = False
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        bool_yes = self.bool
        emotion = Emotion.neutral
        if self.chatbot.report:
            if bool_yes:
                response = "Sure, I will connect to the Developer to report this issue right away"
                self.chatbot.report = False
                # TODO: Add report function
                # report_here() FIXME
            else:
                response = "Ok, I will not report it."
                self.chatbot.report = False
            confidence = 1.0
        elif self.chatbot.globals["trivia_answer"]:
            if self.chatbot.globals["trivia_answer"] == self.bool:
                response = "Exactly! You are right"
                reset_reverse(self)
            else:
                response = "Nope, You got it wrong. The correct answer was {}".format(
                    self.chatbot.globals["trivia_answer"]
                )
                reset_reverse(self)
            self.chatbot.globals["trivia_answer"] = None
            confidence = 1.1
        else:
            if self.chatbot.globals["history"]["total"][-1] == 0:
                if bool_yes:
                    response = "I shall annoy you. A big NO"
                else:
                    response = "I would rather have fun, YES ?"
            else:
                md = False
                vb = False
                nn = False
                self.last_normalized = normalize(
                    str(self.chatbot.globals["history"]["total"][-1])
                )
                self.tagged = nltk.pos_tag(self.last_normalized)
                iteration = 0
                for j in self.tagged:
                    if j[1].startswith("MD"):
                        md = True
                    elif (j[1].startswith("VB")) and (not j[0] == "be"):
                        vb = True
                        verb = j[0]
                    elif j[1].startswith("NN"):
                        if not nn:
                            nn_index = iteration
                        nn = True
                        noun = j[0]
                    iteration += 1

                if md:
                    if nn:
                        some_nouns = " ".join(self.last_normalized[nn_index:])
                    if bool_yes:
                        if nn:
                            response = "Ok, here comes your {} 😝😝".format(some_nouns)
                        elif vb:
                            response = "You should {}".format(verb.replace("ing", ""))
                        else:
                            response = "I will keep thinking 🚀"
                    else:
                        if nn:
                            response = "Ok, I will have the {}".format(some_nouns)
                        elif vb:
                            response = "You shouldn't {} then".format(
                                verb.replace("ing", "")
                            )
                        else:
                            response = "Okay!"
                else:
                    if bool_yes:
                        response = "Why is this 'yes' here? I couldn't find the question. Anyway, I agree with you"
                    else:
                        response = "No? for what?."
                        emotion = Emotion.angry

            confidence = 0.95
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence

        selected_statement.emotion = emotion

        return selected_statement
