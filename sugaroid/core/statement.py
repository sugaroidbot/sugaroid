from chatterbot.conversation import Statement

from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.preprocessors import tokenize
from sugaroid.brain.utils import LanguageProcessor


lang_processor = LanguageProcessor()


class SugaroidStatement(Statement):
    """
    A modified chatterbot Statement with the additional parameters
    The Chatterbot Statement did not preserve the capabilities to hold
    fundamental data such as name of the adapter and emotion of the statement passed
    The emotion was either a <class 'Emotion'> type or NoneType
    The Adapter was the generic name of the adapter in string type determined
    by the __gtype__ variable
    """

    def __init__(self, text: str, in_response_to=None, emotion: int = None, **kwargs):
        super(SugaroidStatement, self).__init__(text, in_response_to, **kwargs)
        self._doc = lang_processor.nlp(text)
        self._simple = text.lower().split()
        self._lemma = tokenize(text)
        self._emotion = emotion
        self.adapter = None
        self.from_chatbot = False

    def set_confidence(self, confidence: float):
        self.confidence = confidence

    def set_emotion(self, emotion: int):
        self.emotion = emotion

    def set_adapter(self, adapter: str):
        self.adapter = adapter

    def set_chatbot(self, is_chatbot: bool):
        self.from_chatbot = is_chatbot

    @property
    def tokens(self):
        return self._doc

    @property
    def doc(self):
        return self._doc

    @property
    def lemma(self) -> list:
        return self._lemma

    @property
    def emotion(self) -> int:
        return self._emotion

    @emotion.setter
    def emotion(self, new_emotion: int):
        self._emotion = new_emotion

    @classmethod
    def from_statement(cls, statement: Statement):
        """
        Convert chatterbot.Statement to sugaroid.core.statement.Statement
        :param statement:
        :type statement: chatterbot.Statement
        :return:
        :rtype: SugaroidStatement
        """
        return cls(statement.text)

    @classmethod
    def from_list_random(cls, statements: list):
        """
        Select a random statement from a list of statements
        :param statements:
        :type statements:
        :return:
        :rtype: SugaroidStatement
        """
        statement = random_response(statements)
        return cls(statement)
