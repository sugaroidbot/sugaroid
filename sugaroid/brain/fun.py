from chatterbot.logic import LogicAdapter
from nltk import word_tokenize

from sugaroid.brain.constants import EMOJI_SMILE, FUN_ASK_QUESTION, FUN_LET_ME_TRY
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response, reverse
from sugaroid.brain.preprocessors import spac_token
from sugaroid.sugaroid import SugaroidStatement


class FunAdapter(LogicAdapter):
    """
    Gives a random response, because Sugaroid tries not to say I don't know
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        if self.chatbot.globals["fun"]:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        emotion = Emotion.neutral
        confidence = 0.05
        parsed = str(statement)
        if "not" in parsed:
            # if you are not, who then is?
            suffix = " either. "
            prefix = ""
            emotion = Emotion.wink
            confidence *= 2
        else:
            interrogation = False
            token = spac_token(statement, chatbot=self.chatbot)
            for i in token:
                # checks if the statement contains any sequence of interrogative type of words
                if i.tag_ == "." and i.text == "?":
                    interrogation = True
                if str(i.tag_).startswith("W"):
                    interrogation = True

            if interrogation:
                prefix, suffix = "", ""
                confidence *= 2
                parsed = random_response(FUN_ASK_QUESTION).format(
                    " ".join(reverse(word_tokenize(str(statement))))
                )  # This seems complex.
                # The tokenized input statement is reversed using the reverse unction
                # Reverse in this sense means switching first person and second person nouns
                # The returned list of tokens are then converted into a string by joining each element
                # to a whitespace making a sentence, which is then converted to lower case
                # for the visibility sake
            else:
                prefix, suffix = random_response(FUN_LET_ME_TRY)
                suffix = "' {}".format(suffix.format(random_response(EMOJI_SMILE)))
                prefix = "{} '".format(prefix)
                emotion = Emotion.wink

        selected_statement = SugaroidStatement(
            "{pre}{main}{fix}".format(pre=prefix, main=parsed, fix=suffix), chatbot=True
        )
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        return selected_statement
