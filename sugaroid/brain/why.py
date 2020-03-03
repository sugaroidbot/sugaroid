import nltk
import wikipediaapi
from chatterbot.logic import LogicAdapter

from chatterbot.conversation import Statement
from mediawikiapi import MediaWikiAPI
from nltk import word_tokenize

from sugaroid.brain.ooo import Emotion
from sugaroid.google.google import chatbot_query
from sugaroid.sugaroid import SugaroidStatement


class WhyAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        # FIXME Add Language support
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        self.tokenized = self.chatbot.lp.tokenize(str(statement))
        for i in self.tokenized:
            if i.tag_ == 'WRB':
                return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        response = "Hmm, I cannot reason out your question"
        confidence = 0.2
        emotion = Emotion.cry_overflow

        selected_statement = SugaroidStatement(response)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion

        return selected_statement
