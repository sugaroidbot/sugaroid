from random import randint
from typing import Tuple

from chatterbot.logic import LogicAdapter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sugaroid.brain.constants import GRATIFY, CONSOLATION, SIT_AND_SMILE, APPRECIATION, WELCOME
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import reverse, random_response, any_in
from sugaroid.brain.preprocessors import tokenize
from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.core.statement import SugaroidStatement


def handle_dead_statements(statement: SugaroidStatement) -> Tuple[str, int]:
    """
    Handles those statements which contains words like dead
    some people dead, everyone dead.

    >>> statement = SugaroidStatement("Everyone is dead. Sed indeed")
    >>> response, _ = handle_dead_statements(statement)
    >>> print(response)
    Very sed

    :param statement: the statement to process
    :type statement: SugaroidStatement
    """

    if "everyone" in statement.lemma or "every" in statement.lemma:
        if ("except" in statement.lemma or "apart" in statement.lemma) and "me" in statement.lemma:
            response = (
                "So sad. Its a great feeling that only"
                " me and you are the only person alive "
                "on the face of this world."
            )
        else:
            response = "So, am I speaking to you in heaven?"
        emotion = Emotion.dead
    else:
        responses = (
            "I hope you are not dead too. I am sorry.",
            "My 💐 for them",
            "My condolences...",
            "So sad. I want to cry 😭",
            "At least you are there for me!",
        )
        response = random_response(responses)
        emotion = Emotion.lol
    return response, emotion


def handle_give_consolation(_: SugaroidStatement) -> Tuple[str, int]:
    """
    Give consolation to the user when the user is depressed
    :param _:
    :type _:
    :return:
    :rtype:
    """
    response = "Its ok,  {}.".format(random_response(CONSOLATION))
    emotion = Emotion.positive
    return response, emotion


def handle_thanks(_: SugaroidStatement) -> Tuple[str, int]:
    """
    Say welcome when the user says thank you!
    :param _:
    :type _:
    :return:
    :rtype:
    """
    response = random_response(WELCOME)
    emotion = Emotion.positive
    return response, emotion


class EmotionAdapter(SugaroidLogicAdapter):
    """
    Handles positive and negative emotional statements
    """

    def can_process(self, statement: SugaroidStatement) -> bool:
        a = self.sia.polarity_scores(statement.text)
        # do not enable emotion adapter when
        # we are playing akinator
        if self.chatbot.globals["akinator"]["enabled"]:
            return False
        # only process if the statement is too emotional
        return a["neu"] < 0.5

    def process(self, statement: SugaroidStatement, additional_response_selection_parameters=None):
        # parsed = str(statement).lower().strip()
        raw_statement = str(statement)

        polarity = self.sia.polarity_scores(statement.text)

        confidence = polarity["pos"] + polarity["neg"]
        if (("love" in statement.lemma) or ("hate" in statement.lemma)) and (
            ("you" in statement.lemma) or ("myself" in statement.lemma)
        ):
            if polarity["pos"] >= polarity["neg"]:
                response = "I love you too"
                emotion = Emotion.blush
            else:
                response = "But still, I love you"
                emotion = Emotion.lol
        else:
            if polarity["pos"] > polarity["neg"]:
                if "you" in statement.lemma:
                    if "thank" in statement.lemma:
                        # this is a positive statement
                        # but we are expecting something like 'You're welcome' here
                        response = random_response(WELCOME)
                    else:
                        response = random_response(GRATIFY)
                    emotion = Emotion.blush
                else:
                    if "stop" in statement.lemma:
                        if (
                            ("dont" in statement.lemma)
                            or ("do" in statement.lemma and "not" in statement.lemma)
                            or ("don't" in statement.lemma)
                        ):
                            response = "I am here to continue my adventure forever"
                            emotion = Emotion.positive
                        else:
                            # optimize series of or statement
                            if (
                                ("fun" in statement.lemma)
                                or ("repeat" in statement.lemma)
                                or ("imitation" in statement.lemma)
                                or ("repetition" in statement.lemma)
                                or ("irritate" in statement.lemma)
                                or ("irritation" in statement.lemma)
                            ):
                                response = (
                                    "Ok! I will switch off my fun mode for sometime"
                                )
                                emotion = Emotion.neutral
                                self.chatbot.globals["fun"] = False
                            else:
                                response = "I am depressed. Is there anything which I hurt you? I apologize for that"
                                emotion = Emotion.depressed
                    else:
                        if any_in(APPRECIATION, statement.lemma):
                            response = random_response(GRATIFY)
                            emotion = Emotion.angel
                            confidence = 0.8
                        else:
                            if "thank" in statement.lemma or "thanks" in statement.lemma:
                                response, emotion = handle_thanks(statement)
                            else:
                                # FIXME : Make it more smart
                                response = random_response(SIT_AND_SMILE)
                                emotion = Emotion.lol
                            if confidence > 0.8:
                                confidence -= 0.2
            else:
                if "i" in statement.lemma:
                    response, emotion = handle_give_consolation(statement)
                elif "dead" in statement.lemma:
                    response, emotion = handle_dead_statements(statement)
                else:

                    # well, I don't want to say ( I don't know )
                    # FIXME : Use a better algorithm to detect sentences
                    reversed_response = reverse(statement.lemma)
                    response = "Why do you think {}?".format(" ".join(reversed_response))
                    emotion = Emotion.dead

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.set_emotion(emotion)
        selected_statement.set_confidence(confidence)
        return selected_statement
