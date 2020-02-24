from random import random, randint

from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from sugaroid.brain.constants import GRATIFY, CONSOLATION
from sugaroid.brain.postprocessor import reverse
from sugaroid.brain.preprocessors import tokenize


class EmotionAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.sia = SentimentIntensityAnalyzer()

    def can_process(self, statement):
        a = self.sia.polarity_scores(str(statement))
        if a['neu'] < 0.5:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        # parsed = str(statement).lower().strip()
        raw_statement = str(statement)
        parsed = tokenize(str(statement))
        print(parsed)

        a = self.sia.polarity_scores(raw_statement)
        response = ":)"
        if (('love' in parsed) or ('hate' in parsed)) and (('you' in parsed) or ('myself' in parsed)):
            if a['pos'] > a['neg']:
                response = "I love you too"
            else:
                response = "But still, I love you"
        else:
            if a['pos'] > a['neg']:
                if 'you' in parsed:
                    response = GRATIFY[randint(0, len(GRATIFY)-1)]
                else:
                    # FIXME : Make it more smart
                    response = "Well, I could only (^‿^) "
            else:

                if 'i' in parsed:
                    response = "Its ok,  {}.".format(
                        CONSOLATION[randint(0, len(CONSOLATION)-1)])
                else:
                    # well, I don't want to say ( I don't know )
                    reversed = reverse(parsed)
                    response = 'Why do you think {}?'.format(
                        ' '.join(reversed))
        selected_statement = Statement(response)
        selected_statement.confidence = a['pos'] + a['neg']
        return selected_statement
