import nltk
from chatterbot.logic import LogicAdapter
import wikipedia
from chatterbot.conversation import Statement
from nltk import word_tokenize

from sugaroid.brain.postprocessor import sigmaSimilarity, difference
from sugaroid.brain.preprocessors import normalize
from sklearn.feature_extraction.text import TfidfVectorizer

from sugaroid.google.google import chatbot_query


class WikiAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        # FIXME Add Language support
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        """"""
        text = word_tokenize(str(statement))
        tagged = nltk.pos_tag(text)
        y = lambda x: x[0][1] == "WP"
        boo = (y(tagged)) and ('you' not in text)
        if boo:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        # FIXME: This may printout unrelated data for phrase searches
        """"
            normalized = normalize(str(statement))
            question = ["what", "be", "is", "can", "you", "tell", "me", "please"]
            confidence = 0.85
            core = difference(normalized, question)
            wkpage = wikipedia.page(' '.join(core))
            if wkpage:
                selected_statement = Statement(
                    "{} \n\t ~ Wikipedia".format(wkpage.summary))
            else:
                selected_statement = Statement(
                    "Oops, couldn't find it on Wikipedia")
            selected_statement.confidence = confidence

            return selected_statement
        """
        selected_statement = Statement(chatbot_query(str(statement)))
        selected_statement.confidence = 0.94
        return selected_statement
