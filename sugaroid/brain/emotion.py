from random import random, randint

from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from sugaroid.brain.constants import GRATIFY, CONSOLATION
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import reverse
from sugaroid.brain.preprocessors import tokenize
from sugaroid.sugaroid import SugaroidStatement


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
        emotion = Emotion.neutral
        a = self.sia.polarity_scores(raw_statement)
        response = ":)"
        if (('love' in parsed) or ('hate' in parsed)) and (('you' in parsed) or ('myself' in parsed)):
            if a['pos'] > a['neg']:
                response = "I love you too"
                emotion = Emotion.blush
            else:
                response = "But still, I love you"
                emotion = Emotion.lol
        else:
            if a['pos'] > a['neg']:
                if 'you' in parsed:
                    response = GRATIFY[randint(0, len(GRATIFY)-1)]
                    emotion = Emotion.blush
                else:
                    if 'stop' in parsed:
                        if ('dont' in parsed) or ('do' in parsed and 'not' in parsed) or ('don\'t' in parsed):
                            response = 'I am here to continue my adventure forever'
                            emotion = Emotion.positive
                        else:
                            # optimize series of or statement
                            if \
                                    ('fun' in parsed) or \
                                    ('repeat' in parsed) or \
                                    ('imitation' in parsed) or \
                                    ('repetition' in parsed) or \
                                    ('irritate' in parsed) or \
                                    ('irritation' in parsed):
                                response = "Ok! I will switch off my fun mode for sometime"
                                emotion = Emotion.neutral
                                self.chatbot.fun = False
                            else:
                                response = "I am depressed. Is there anything which I hurt you? I apologize for that"
                                emotion = Emotion.depressed
                    else:
                        # FIXME : Make it more smart
                        response = "Well, I could only smile "
                        emotion = Emotion.lol
            else:
                if 'i' in parsed:
                    response = "Its ok,  {}.".format(
                        CONSOLATION[randint(0, len(CONSOLATION)-1)])
                    emotion = Emotion.positive
                else:
                    # well, I don't want to say ( I don't know )
                    reversed = reverse(parsed)
                    response = 'Why do you think {}?'.format(
                        ' '.join(reversed))
                    emotion = Emotion.dead

        selected_statement = SugaroidStatement(response)
        selected_statement.confidence = a['pos'] + a['neg']
        selected_statement.emotion = emotion
        return selected_statement
