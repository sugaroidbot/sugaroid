from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter
from nltk.sentiment.vader import SentimentIntensityAnalyzer


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
        parsed = str(statement)
        a = self.sia.polarity_scores(parsed)
        response = ":)"
        if (('love' in parsed) or ('hate' in parsed)) and (('you' in parsed) or ('myself' in parsed)):
            if a['pos'] > a['neg']:
                response = "I love you too"
            else:
                response = "But still, I love you"
        else:
            response = 'Why do you think {}?'.format(
                parsed
                .lower()
                .replace(' are ', ' ARE ')
                .replace(' you ', ' I ')
                .replace(' i ', ' you ')
                .replace(' am ', ' are ')
                .replace(' ARE ', ' am ')
                .replace(' are I ', ' I am ')
            )


        selected_statement = Statement(response)
        selected_statement.confidence = a['pos'] + a['neg']
        return selected_statement




