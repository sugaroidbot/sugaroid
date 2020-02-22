
from chatterbot.logic import LogicAdapter
import wikipedia
from chatterbot.conversation import Statement
from sugaroid.brain.postprocessor import sigmaSimilarity, difference
from sugaroid.brain.preprocessors import normalize
from sklearn.feature_extraction.text import TfidfVectorizer


class WikiAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        # FIXME Add Language support
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        normalized = normalize(str(statement))
        if ('what' in normalized) or ('wikipedia' in normalized):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        # FIXME: This may printout unrelated data for phrase searches

        normalized = normalize(str(input_statement))
        question = ["what", "be", "is", "can", "you", "tell", "me", "please"]
        confidence = 0.85
        core = difference(normalized, question)
        wkpage = wikipedia.page(' '.join(core))
        if wkpage:
            selected_statement = Statement("{} \n\t ~ Wikipedia".format(wkpage.summary))
        else:
            selected_statement = Statement("Oops, couldn't find it on Wikipedia")
        selected_statement.confidence = confidence

        return selected_statement
