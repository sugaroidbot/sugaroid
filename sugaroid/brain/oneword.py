from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.version import VERSION
from sugaroid.brain.constants import (
    ONE_WORD,
    DISCLAIMER,
    HI_WORDS,
    HI_RESPONSES,
    LICENSE,
    CREDITS,
)
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.sugaroid import SugaroidStatement


class OneWordAdapter(SugaroidLogicAdapter):
    """
    Logical adapter for processing data with one words
    """

    def can_process(self, statement: SugaroidStatement) -> bool:
        if len(statement.lemma) == 1:
            return True
        elif len(statement.lemma) == 2:
            if statement.doc[-1].tag_ == ".":
                return True
        return False

    def process(
        self,
        statement: SugaroidStatement,
        additional_response_selection_parameters=None,
    ) -> SugaroidStatement:
        emotion = Emotion.seriously
        confidence = 0.60
        response = random_response(ONE_WORD)
        short = str(statement).lower()
        if "ver" in short:
            response = VERSION
            confidence = 1
        elif "name" in short:
            response = "What name? You should probably use better english"

        elif ("help404" in short) or ("help" in short and "404" in short):
            import sugaroid  # noqa:
            import chatterbot  # noqa:

            help_files = []
            for i in self.chatbot.globals["adapters"]:
                help_files.append(
                    "{}: {}".format(
                        i.split(".")[-1].strip(), eval(i).__doc__.strip()
                    ).strip()
                )
            response = "hmm. Sure. \n {}".format("\n ".join(help_files))
            confidence = 1

        elif "help" in short:
            response = (
                "The help is not very easily provided. "
                "If you are serious of what you are asking, "
                "type help404"
            )
            confidence = 1
        elif "disclaimer" in short:
            response = DISCLAIMER
            confidence = 1
        elif "license" in short:
            response = LICENSE
            confidence = 1

        elif "credit" in short or "acknow" in short or "people" in short:

            response = "❇️ " + "\n ❇️ ".join(CREDITS)
            confidence = 1

        elif short in HI_WORDS:
            response = random_response(HI_RESPONSES)
            confidence = 0.99
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        selected_statement.adapter = None
        return selected_statement
