from random import randint

from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.constants import TIME, TIME_RESPONSE
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.preprocessors import normalize, current_time


class TimeAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.normalized = None
        self.intersect = None

    def can_process(self, statement):
        self.normalized = normalize(str(statement))
        self.intersect = set(self.normalized).intersection(set(TIME))
        if self.intersect:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):

        hour, minutes = current_time()
        alert = False
        if hour <= 0:
            alert = True
            time = ''
        elif hour <= 11:
            time = 'morning'
        elif hour <= 15:
            time = 'afternoon'
        elif hour <= 19:
            time = 'evening'
        elif hour <= 20:
            time = 'night'
        else:
            alert = True
            time = ''
        if not alert:
            if (time in self.intersect) or ('time' in self.intersect):
                response = 'Good {}'.format(time)
            else:
                response = 'Good {}. {}'.format(time, random_response(TIME_RESPONSE).format(list(self.intersect)[0]))
        else:
            response = "You are staying up late, you should sleep right now."

        selected_statement = Statement("{}".format(response))
        selected_statement.confidence = 1
        return selected_statement

