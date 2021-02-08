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
        logging.info("AreYouAdapter: statement has the lemma of %s" % statement.lemma)
        if len(statement.lemma) < 2:
            return False
        if statement.lemma[0] == "are" and statement.lemma[1] == "you":
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
            "bot" in statement.lemma
            or "machine" in statement.lemma
            or "computer" in statement.lemma
        ):
            # the question is something like
            # are you a bot?
            response = random_response(ARE_YOU_A_BOT)
            confidence = 0.75
        elif "sugaroid" in statement.lemma:
            # this person asked
            # are you sugaroid?
            # FIXME: use a better constants
            response = random_response(INTRODUCE)
            confidence = 0.75
        elif (
            "human" in statement.lemma
            or "man" in statement.lemma
            or "woman" in statement.lemma
            or "sapien" in statement.lemma
        ):
            # this person asked the bot if its a human
            # are you a human?
            response = random_response(ARE_YOU_A_HUMAN)
            confidence = 0.75
        elif "boy" in statement.lemma or "girl" in statement.lemma:
            response = "I will leave it to your imagination. 😌"
            confidence = 0.75
        elif "python" in statement.lemma:
            # this person asked something like
            # are you written in python
            response = (
                "I am written in python. Specifically, on v%s"
                % sys.version.replace("\n", " ")
            )
            confidence = 1
        elif (
            "newborn" in statement.lemma
            or "infant" in statement.lemma
            or "child" in statement.lemma
        ):
            response = "I am a newbie bots. I am trying to learn from my uncle and aunty bots and learning from them."
        elif (
            "dumb" in statement.lemma
            or "foolish" in statement.lemma
            or "mad" in statement.lemma
            or "weird" in statement.lemma
            or "awkward" in statement.lemma
            or polarity_scores["pos"] > polarity_scores["neg"]
        ):
            response = random_response(BOT_DECLINE)
        elif (
            "alive" in statement.lemma
            or "online" in statement.lemma
            or "living" in statement.lemma
        ):
            response = random_response(BOT_AGREE)
        else:
            response = random_response(BOT_NEUTRAL)
            confidence = 0.5

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        emotion = Emotion.neutral
        selected_statement.emotion = emotion

        return selected_statement
