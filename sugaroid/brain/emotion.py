from chatterbot.logic import LogicAdapter
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class EmotionAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)