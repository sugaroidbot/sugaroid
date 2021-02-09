from datetime import datetime

from sugaroid.brain.wiki import WikiAdapter
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.constants import (
    WHY_IDK,
    HOW_DO_YOU_FEEL,
    WHERE_LIVE,
    DONT_KNOW_WHERE, BIRTHDAY, DATE_STRFTIME,
)
from sugaroid.brain.ooo import Emotion
from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.sugaroid import SugaroidStatement


def get_age() -> str:
    delta = datetime.now() - BIRTHDAY
    years = delta.days // 365
    days = delta.days % 365
    hours = (delta.seconds - delta.days * 24 * 60 * 60) // 3600
    s_years = "years" if years != 1 else "year"
    s_days = "days" if days != 1 else "day"
    s_hours = "hours" if hours != 1 else "hour"
    return f"I am {years} {s_years}, {days} {s_days} and {hours} {s_hours} old."


class WhyWhenAdapter(SugaroidLogicAdapter):
    """
    Processes wh-adverbs
    """

    def can_process(self, statement: SugaroidStatement) -> bool:
        for i in statement.doc:
            if i.tag_ == "WRB":
                return True
        return False

    def process(self, statement: SugaroidStatement, additional_response_selection_parameters=None):
        """

        :param statement:
        :param additional_response_selection_parameters:
        :return:
        """
        emotion = Emotion.neutral
        if "when" in statement.lemma:
            if "you" in statement.lemma or "your" in statement.lemma:
                response = "When did you what?"
                confidence = 0.6
                for i in ["creator", "author", "developer"]:
                    if i in statement.lemma:
                        response = "Let's say, its TOP SECRET!!"
                        confidence = 0.8
                        emotion = Emotion.lol
                        break
                for i in [
                    "birthday",
                    "b'day",
                    "bday",
                    "born",
                    "birth",
                    "bear",
                    "create",
                    "manufactured",
                ]:
                    if i in statement.lemma:
                        # the person is asking my birthday
                        response = "I was born on {}".format(BIRTHDAY.strftime(DATE_STRFTIME))
                        confidence = 0.8
                        emotion = Emotion.blush
                        break
            else:
                # search in wikipedia
                return WikiAdapter(self.chatbot).process(statement)
        elif "why" in statement.lemma:
            # say idk
            response = random_response(WHY_IDK)
            confidence = 0.2
            emotion = Emotion.cry_overflow
        elif "how" in statement.lemma:
            if "old" in statement.lemma and "you" in statement.lemma:
                response = get_age()
                confidence = 1
            elif (
                "you" in statement.lemma
                and "be" in statement.lemma
                and not (
                    "can" in statement.lemma or
                    "could" in statement.lemma or
                    "should" in statement.lemma or
                    "would" in statement.lemma
                )
            ):
                # possibly the person asked
                # 'how are you'
                response = random_response(HOW_DO_YOU_FEEL)
                confidence = 0.75
            else:
                response = "😄"
                confidence = 0.1

        elif "where" in statement.lemma:
            if "you" in statement.lemma:
                if "live" in statement.lemma or "stay" in statement.lemma:
                    # the person is asking something like
                    # "where do you live"
                    response = random_response(WHERE_LIVE)
                    confidence = 0.75
                else:
                    response = random_response(DONT_KNOW_WHERE)
                    confidence = 0.65
            else:
                # the person is asking something like
                # where is india
                return WikiAdapter(self.chatbot).process(statement)
        else:
            # say idk
            response = "😄"
            confidence = 0.15
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion

        return selected_statement
