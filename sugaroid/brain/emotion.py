from random import random, randint

from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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
        gratify = [
            "Thank you, indeed its my pleasure ",
            "All my 0s and 1s are still smiling",
            "You knocked me off my feet!",
            "I'm touched beyond words",
            "Thank you for being my angel.",
        ]
        do = [
            "Sometimes later becomes never.Do it now."
        ]
        console = [
            "Your limitation—it’s only your imagination.",
            "Push yourself, because no one else is going to do it for you.",
            "Great things never come from comfort zones.",
            "Success doesn’t just find you. You have to go out and get it.",
            "The harder you work for something, the greater you’ll feel when you achieve it.",
            "Dream bigger. Do bigger.",
            "Don’t stop when you’re tired. Stop when you’re done.",
            "Wake up with determination. Go to bed with satisfaction.",
            "Do something today that your future self will thank you for.",
            "It’s going to be hard, but hard does not mean impossible."
        ]
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
                    response = gratify[randint(0, len(gratify)-1)]
                else:
                    # FIXME : Make it more smart
                    response = "Well, I could only (^‿^) "
            else:

                if 'i' in parsed:
                    response = "Its ok,  {}.".format(
                        console[randint(0, len(console)-1)])
                else:
                    # well, I don't want to say ( I don't know )
                    reversed = reverse(parsed)
                    response = 'Why do you think {}?'.format(
                        ' '.join(reversed))
        selected_statement = Statement(response)
        selected_statement.confidence = a['pos'] + a['neg']
        return selected_statement
