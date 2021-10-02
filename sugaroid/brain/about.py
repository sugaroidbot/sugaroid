import logging
from typing import Tuple

from sugaroid.brain.constants import INTRODUCE
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response, any_in
from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.core.statement import SugaroidStatement


def about_process_en(statement: SugaroidStatement) -> Tuple[bool, str, str, str]:
    noun = None
    pronoun = None
    question = None
    for i in statement.tokens:
        if i.tag_ == "WP":
            question = str(i)
        elif i.tag_.startswith("PRP"):
            pronoun = str(i)
        elif i.tag_.startswith("NN"):
            noun = str(i)

    return question is not None and pronoun is not None, noun, pronoun, question


class AboutAdapter(SugaroidLogicAdapter):
    """
    Defines the personality of sugaroid. **About Adapter** sets
    the basic parameters of personality. These include questions
    like 'Who is your brother?', or "What is your Hobby?"

    .. warning::
        This adapter is incomplete and requires additional
        clauses.
    """

    def can_process(self, statement: SugaroidStatement) -> bool:
        """
        Checks if the provided statement is a statement which
        matches a similarity to "What is your ``<insert token>``"
        """
        return about_process_en(statement)[0]

    def process(
        self,
        statement: SugaroidStatement,
        additional_response_selection_parameters=None,
    ):
        _, noun, pronoun, question = about_process_en(statement)
        logging.info("{}".format(statement.words))
        confidence = 0
        adapter = None

        emotion = Emotion.neutral
        if pronoun.lower().startswith("you"):
            if question.lower() == "who":
                confidence = 0.99
                if "father" in statement.words:
                    response = "Mr Charles Babbage?"
                    emotion = Emotion.seriously
                elif "hobby" in statement.words:
                    response = (
                        "Calculating random binary sequences and chatting with you!"
                    )
                    emotion = Emotion.lol
                elif "mother" in statement.words:
                    response = "Ada Lady Lovelace?"
                    emotion = Emotion.lol
                elif any_in(
                    [
                        "sister",
                        "brother",
                        "uncle",
                        "aunty",
                        "auntie",
                        "grandfather",
                        "grandmother",
                        "nephew",
                        "niece",
                    ],
                    statement.words,
                ):
                    response = (
                        "The entire coding community is my family, it includes you too"
                    )
                    emotion = Emotion.wink
                elif (
                    ("creator" in statement.words)
                    or ("create" in statement.text)
                    or ("make" in statement.words)
                    or ("made" in statement.words)
                    or ("maker" in statement.words)
                ):
                    response = "Srevin Saju aka @srevinsaju"
                    emotion = Emotion.neutral
                elif (
                    ("player" in statement.words)
                    or ("cricketer" in statement.words)
                    or ("footballer" in statement.words)
                ):
                    response = "I have many favorties, too many to count"
                    emotion = Emotion.wink
                elif "politi" in statement.text:
                    response = (
                        "I believe politicians are great and I couldn't find anyone with 🔥greatness in my "
                        "database "
                    )
                    emotion = Emotion.wink
                elif "comedian" in statement.words:
                    response = "My favorite comedian is Mr Bean"
                    emotion = Emotion.lol
                elif "color" in statement.words:
                    response = "My favorite color is blue"
                    emotion = Emotion.lol
                elif "actor" in statement.words or ("actress" in statement.words):
                    response = "I do not watch movies, so yea!"
                    emotion = Emotion.neutral
                elif "music" in statement.words or ("song" in statement.words):
                    response = (
                        "I listen to the rotating CPU fan. Its a harmonic music! "
                        "At my server, we have tons of them."
                    )
                    emotion = Emotion.lol
                elif "bird" in statement.words:
                    response = "My favorite is a Puffin"
                    emotion = Emotion.lol
                elif "animal" in statement.words:
                    response = "My favorite animal is a Fossa"
                    emotion = Emotion.positive
                elif "number" in statement.words:
                    response = "My favorite number is 1"
                    emotion = Emotion.positive
                elif "sweet" in statement.words or "dessert" in statement.words:
                    response = (
                        "My favorite is the donut although I have not tasted it yet"
                    )
                    emotion = Emotion.cry_overflow

                elif "athelete" in statement.words:
                    response = (
                        "I am not a sport lover, I don't have a favorite athelete"
                    )
                    emotion = Emotion.neutral
                elif ("friend" in statement.words) or ("bestie" in statement.words):
                    if self.chatbot.globals["USERNAME"]:
                        name = self.chatbot.globals["USERNAME"]
                    else:
                        name = ""
                    response = "No doubts, its you {n}".format(n=name.capitalize())
                    emotion = Emotion.adorable
                elif "teacher" in statement.words:
                    response = (
                        "I don't have a single favorite teacher. All the teachers together are my favorite who"
                        " taught me how to talk with you "
                    )
                    emotion = Emotion.positive
                else:
                    if noun is not None:
                        response = "Well, I guess I do not have a favorite {p}".format(
                            p=noun
                        )
                        emotion = Emotion.cry
                    else:
                        response = "I am not sure what you are asking is right"
                        emotion = Emotion.seriously
                        confidence = 0.5

            else:
                if "name" in statement.words:
                    # not sure if this is right. anyway FIXME
                    response = random_response(INTRODUCE)
                    adapter = "about"
                    confidence = 1.0
                else:

                    response = "FIXME"

        elif pronoun.lower().startswith("i"):
            if question.lower() == "who":
                response = "I do not know who you like"
                confidence = 0.8
                emotion = Emotion.non_expressive_left

            elif question.lower() == "which":
                response = "Hmm. tough question. Can't think of an answer"
                emotion = Emotion.non_expressive
            elif question.lower() == "when":
                response = (
                    "I cannot find the date or time you are asking for. Well, I can give a raw guess, "
                    "its after you were born "
                )
                emotion = Emotion.wink
            else:
                response = "FIXME"
        else:
            response = "I do not have enough courage to give you that answer"
            confidence = 0.5
            emotion = Emotion.cry

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.set_confidence(confidence)
        selected_statement.set_emotion(emotion)
        selected_statement.set_adapter(adapter)

        return selected_statement
