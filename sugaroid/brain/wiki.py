import nltk
from chatterbot.logic import LogicAdapter

from chatterbot.conversation import Statement
from nltk import word_tokenize

from sugaroid.brain.ooo import Emotion
from sugaroid.google.google import chatbot_query
from sugaroid.sugaroid import SugaroidStatement


class WikiAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        # FIXME Add Language support
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        self.text = word_tokenize(str(statement))
        tagged = nltk.pos_tag(self.text)
        print(tagged)
        q = False
        pr = False
        for i in tagged:
            if i[1] == 'WP' or i[1] == 'WRB':
                q = True
            elif (i[1].startswith('PRP')) and (not i[0] == 'we'):
                pr = True
        if q and (not pr):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        # FIXME: This may printout unrelated data for phrase searches

        count = 0
        for i in self.text:
            if i.lower() == 'what':
                count += 1
        if count > 1:
            selected_statement = SugaroidStatement('Nothing ' * count)
            selected_statement.confidence = 0.99
        else:
            response = chatbot_query(str(statement))
            if response.lower() == 'loading':
                confidence = 0
            elif 'RANDOM ERROR' in response.lower():
                confidence = 0.05
            else:
                confidence = 0.95
            selected_statement = SugaroidStatement(str(response))
            selected_statement.confidence = confidence

        emotion = Emotion.neu
        selected_statement.emotion = emotion

        return selected_statement
