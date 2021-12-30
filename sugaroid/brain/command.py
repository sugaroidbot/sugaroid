import os

from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.version import VERSION
from sugaroid.brain.constants import (
    DISCLAIMER,
    HI_WORDS,
    HI_RESPONSES,
    LICENSE,
    CREDITS,
)
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.core.statement import SugaroidStatement


class CommandAdapter(SugaroidLogicAdapter):
    """
    Adapter for processing commands
    """

    def can_process(self, statement: SugaroidStatement) -> bool:
        return len(statement.words) == 1

    def process(
        self,
        statement: SugaroidStatement,
        additional_response_selection_parameters=None,
    ) -> SugaroidStatement:

        emotion = Emotion.smirking
        confidence = 1
        short = statement.words[0]

        if "version" in short:
            version = VERSION
            if not os.getenv("DYNO"):
                version = f"{version}.dev0 (local build)"
            response = version
        elif short == "name":
            response = "What name? You should probably use better english"
        elif short == "nevermind":
            response = "Ok, I will forget about that."
        elif short == "refresh":
            self.chatbot.session.refresh()
            response = "Cleared cached data."
        elif short == "stats":
            import psutil

            process = psutil.Process(os.getpid())
            megabytes_used = process.memory_info().rss / (10 ** 6)
            version = VERSION
            if not os.getenv("DYNO"):
                version = f"{version}.dev0 (local build)"

            response = (
                f"Up since: {self.chatbot.start_time.isoformat()} \n"
                f"Memory usage: {megabytes_used} \n"
                f"Version: {version}\n"
            )

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
            confidence = 1
        else:
            response = "None"
            confidence = 0
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        selected_statement.adapter = None
        return selected_statement
