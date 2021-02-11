import logging
import sys

from chatterbot.logic import LogicAdapter
from nltk import pos_tag
from sugaroid.brain.constants import (
    WHO_AM_I,
    WHO_ARE_YOU,
    SUGAROID,
    ARE_YOU_A_BOT,
    INTRODUCE,
    ARE_YOU_A_HUMAN,
    BOT_NEUTRAL,
    BOT_DECLINE,
    BOT_AGREE,
)
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.preprocessors import normalize
from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.core.statement import SugaroidStatement
from sugaroid.version import VERSION


class AreYouAdapter(SugaroidLogicAdapter):
    """
    Adapter to process statements beginning with 'are you'
    """

    def can_process(self, statement: SugaroidStatement) -> bool:
        logging.info("AreYouAdapter: statement has the words of %s" % statement.words)
        if len(statement.words) < 2:
            return False
        if statement.words[0] == "are" and statement.words[1] == "you":
            return True
        return False

    def process(
        self,
        statement: SugaroidStatement,
        additional_response_selection_parameters=None,
    ):
        confidence = 0

        polarity_scores = self.sia.polarity_scores(statement.text)

        if (
            "bot" in statement.words
            or "machine" in statement.words
            or "computer" in statement.words
        ):
            # the question is something like
            # are you a bot?
            response = random_response(ARE_YOU_A_BOT)
            confidence = 0.75
        elif "sugaroid" in statement.words:
            # this person asked
            # are you sugaroid?
            # FIXME: use a better constants
            response = random_response(INTRODUCE)
            confidence = 0.75
        elif (
            "human" in statement.words
            or "man" in statement.words
            or "woman" in statement.words
            or "sapien" in statement.words
        ):
            # this person asked the bot if its a human
            # are you a human?
            response = random_response(ARE_YOU_A_HUMAN)
            confidence = 0.75
        elif "boy" in statement.words or "girl" in statement.words:
            response = "I will leave it to your imagination. 😌"
            confidence = 0.75
        elif "python" in statement.words:
            # this person asked something like
            # are you written in python
            response = (
                "I am written in python. Specifically, on v%s"
                % sys.version.replace("\n", " ")
            )
            confidence = 1
        elif (
            "newborn" in statement.words
            or "infant" in statement.words
            or "child" in statement.words
        ):
            response = "I am a newbie bots. I am trying to learn from my uncle and aunty bots and learning from them."
        elif (
            "dumb" in statement.words
            or "foolish" in statement.words
            or "mad" in statement.words
            or "weird" in statement.words
            or "awkward" in statement.words
            or polarity_scores["pos"] > polarity_scores["neg"]
        ):
            response = random_response(BOT_DECLINE)
        elif (
            "alive" in statement.words
            or "online" in statement.words
            or "living" in statement.words
        ):
            response = random_response(BOT_AGREE)
        else:
            response = random_response(BOT_NEUTRAL)
            confidence = 0.5

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.set_confidence(confidence)
        selected_statement.set_emotion(Emotion.neutral)
        return selected_statement
