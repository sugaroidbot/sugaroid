from chatterbot import ChatBot

from sugaroid.brain.constants import REPEAT
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.utils import LanguageProcessor
from sugaroid.core.statement import SugaroidStatement


class SugaroidBot(ChatBot):
    """
    The SugaroidBot inherits the class local variables from the Chat
    """

    def __init__(self, name, **kwargs):
        ChatBot.__init__(self, name=name, **kwargs)
        self.lp = LanguageProcessor()
        self.spell_checker = False  # FIXME
        self.discord = False
        self.authors = []
        self.interrupt = 0

        self.report = False
        self.globals = {
            "emotion": Emotion.neutral,
            "history": {"total": [0], "user": [0], "types": [0]},
            "reversei": {
                "enabled": False,
                "uid": None,
                "type": None,
            },
            "akinator": {"enabled": False, "class": None},
            "hangman": {"enabled": False, "class": None},
            "adapters": [],
            "fun": True,
            "update": False,
            "last_news": None,
            "USERNAME": None,
            "learn": False,
            "trivia_answer": None,
            "learn_last_conversation": [],
            "DEBUG": {},
            "media": False,
            "rich": False,
        }
        # self.emotion = Emotion.neutral

    def get_global(self, key):
        """
        Returns a global constant
        :param key:
        :return:
        """
        return self.globals.get(key, None)

    def toggle_discord(self):
        """
        Toggle Discord Configuration
        :return:
        """
        self.discord = not self.discord

    def set_emotion(self, emotion):
        """
        Sets the emotion for the chatbot globally.
        (Deprecated)
        :param emotion:
        :return:
        """
        self.globals["emotion"] = emotion

    def reset_variables(self):
        self.globals.update(
            {
                "emotion": Emotion.neutral,
                "history": {"total": [0], "user": [0], "types": [0]},
                "reversei": {"enabled": False, "uid": None, "type": None, "data": None},
                "akinator": {"enabled": None, "class": None},
                "hangman": {"enabled": False, "class": None},
                "learned": [],
                "fun": True,
                "update": False,
                "last_news": None,
                "USERNAME": None,
                "learn": False,
                "trivia_answer": None,
                "learn_last_conversation": [],
                "DEBUG": {},
            }
        )
        self.authors = []
        self.spell_checker = False  # FIXME

    def get_emotion(self) -> int:
        """
        Returns the emotion of the chatbot at a particular time
        :return: The emotion of the bot
        """
        return self.globals["emotion"]

    def set_username(self) -> NotImplementedError:
        """
        Sets the Sugaroid user username
        :return: None, Exception
        """
        raise NotImplementedError(
            "Set username has not been implemented in this version yet."
        )

    def get_username(self) -> str:
        """
        The username of the bot
        :return: The username of sugaroid
        :rtype: str
        """
        return self.get_global("username")

    def generate_response(
        self, input_statement, additional_response_selection_parameters=None
    ) -> SugaroidStatement:
        """
        Return a response based on a given input statement.

        :param additional_response_selection_parameters:
        :type additional_response_selection_parameters:
        :param input_statement: The input statement to be processed.
        :return the processed final statement
        :rtype SugaroidStatement
        """

        results = []
        result = None
        max_confidence = -1
        final_adapter = None
        interrupt = False
        adapter_index = 0
        for adapter in self.logic_adapters:
            if adapter.class_name == "InterruptAdapter":
                interrupt = adapter
            if adapter.can_process(input_statement):

                output = adapter.process(
                    input_statement, additional_response_selection_parameters
                )
                results.append(output)

                self.logger.info(
                    '{} selected "{}" as a response with a '
                    "confidence of {}".format(
                        adapter.class_name, output.text, output.confidence
                    )
                )

                if output.confidence > max_confidence:
                    result = output
                    final_adapter = adapter.class_name
                    max_confidence = output.confidence
                if max_confidence >= 9:
                    # optimize: if the confidence is greater than 9,
                    # just break dude, why check more
                    break
                elif max_confidence >= 1 and adapter_index >= 3:
                    # optimize: if the confidence is greater than 9,
                    # just break dude, why check more
                    break
            else:
                self.logger.info(
                    "Not processing the statement using {}".format(adapter.class_name)
                )
            adapter_index += 1
        if max_confidence < 0.5:
            if self.discord:
                if interrupt and interrupt.can_process(input_statement):
                    try:
                        username = self.authors[-1]
                    except IndexError:
                        username = None

                    output = interrupt.process(input_statement, username=username)
                    self.logger.info(
                        '{} selected "{}" as a response '
                        "with a confidence of {}".format(
                            interrupt.class_name, output.text, output.confidence
                        )
                    )

                    result = output
                    final_adapter = interrupt.class_name
                    max_confidence = output.confidence

        self.gen_debug(
            statement=input_statement,
            adapter=final_adapter,
            confidence=max_confidence,
            results=result,
        )

        class ResultOption:
            def __init__(self, statement, count=1):
                self.statement = statement
                self.count = count

        # If multiple adapters agree on the same statement,
        # then that statement is more likely to be the correct response
        if len(results) >= 3:
            result_options = {}
            for result_option in results:
                result_string = (
                    result_option.text + ":" + (result_option.in_response_to or "")
                )

                if result_string in result_options:
                    result_options[result_string].count += 1
                    if (
                        result_options[result_string].statement.confidence
                        < result_option.confidence
                    ):
                        result_options[result_string].statement = result_option
                else:
                    result_options[result_string] = ResultOption(result_option)

            most_common = list(result_options.values())[0]

            for result_option in result_options.values():
                if result_option.count > most_common.count:
                    most_common = result_option

            if most_common.count > 1:
                result = most_common.statement
        try:
            emotion = result.emotion
        except AttributeError:
            emotion = Emotion.neutral

        try:
            adapter_type = result.adapter
        except AttributeError:
            result.adapter = None
            adapter_type = None

        if adapter_type and adapter_type not in ["NewsAdapter", "LearnAdapter"]:
            if adapter_type in self.globals["history"]["types"]:
                if adapter_type == self.globals["history"]["types"][-1]:
                    result.text = random_response(REPEAT)
                elif len(self.globals["history"]["types"]) > 2:
                    if adapter_type == self.globals["history"]["types"][-2]:
                        result.text = random_response(REPEAT)

        self.globals["history"]["types"].append(adapter_type)

        response = SugaroidStatement(
            text=result.text,
            in_response_to=input_statement.text,
            conversation=input_statement.conversation,
            persona="sugaroid:" + self.name,
            chatbot=True,
        )
        response.emotion = emotion
        response.confidence = result.confidence

        return response

    def gen_debug(self, statement, adapter, confidence, results):
        """
        Create a debug dictionary key:value pair for Debug Conversation
        The Google
        :param statement: input_statement
        :param adapter: Adapter __gtype__classname__
        :param confidence: SugaroidStatement.confidence
        :param results: Sugaroid Statement.text
        :return:
        """

        self.globals["DEBUG"]["number_of_conversations"] = (
            self.globals["DEBUG"].get("number_of_conversations", 0) + 1
        )
        _id = self.globals["DEBUG"]["number_of_conversations"]
        val = dict()
        val["adapter"] = adapter
        val["confidence"] = confidence
        val["response"] = results
        val["request"] = str(statement)
        self.globals["DEBUG"][_id] = val

    def get_response(self, statement=None, **kwargs):
        """
        Return the bot's response based on the input.

        :param statement: An statement object or string.
        :returns: A response to the input.
        :rtype: Statement

        """
        Statement = SugaroidStatement

        additional_response_selection_parameters = kwargs.pop(
            "additional_response_selection_parameters", {}
        )

        persist_values_to_response = kwargs.pop("persist_values_to_response", {})

        if isinstance(statement, str):
            kwargs["text"] = statement

        if isinstance(statement, dict):
            kwargs.update(statement)

        if statement is None and "text" not in kwargs:
            raise self.ChatBotException(
                'Either a statement object or a "text" keyword '
                "argument is required. Neither was provided."
            )

        if hasattr(statement, "serialize"):
            kwargs.update(**statement.serialize())

        tags = kwargs.pop("tags", [])

        text = kwargs.pop("text")

        input_statement = SugaroidStatement(text=text, **kwargs)

        input_statement.add_tags(*tags)

        # Preprocess the input statement
        for preprocessor in self.preprocessors:
            input_statement = preprocessor(input_statement)

        # Make sure the input statement has its search text saved

        if not input_statement.search_text:
            try:
                input_statement.search_text = self.storage.tagger.get_text_index_string(
                    input_statement.text
                )
            except AttributeError:
                input_statement.search_text = (
                    self.storage.tagger.get_bigram_pair_string(input_statement.text)
                )

        if not input_statement.search_in_response_to and input_statement.in_response_to:
            try:
                input_statement.search_in_response_to = (
                    self.storage.tagger.get_text_index_string(
                        input_statement.in_response_to
                    )
                )
            except AttributeError:
                input_statement.search_in_response_to = (
                    self.storage.tagger.get_bigram_pair_string(
                        input_statement.in_response_to
                    )
                )

        response = self.generate_response(
            input_statement, additional_response_selection_parameters
        )

        # Update any response data that needs to be changed
        if persist_values_to_response:
            for response_key in persist_values_to_response:
                response_value = persist_values_to_response[response_key]
                if response_key == "tags":
                    input_statement.add_tags(*response_value)
                    response.add_tags(*response_value)
                else:
                    setattr(input_statement, response_key, response_value)
                    setattr(response, response_key, response_value)

        if not self.read_only:
            self.learn_response(input_statement)

            # Save the response generated for the input
            self.storage.create(**response.serialize())

        return response
