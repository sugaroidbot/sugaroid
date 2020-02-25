from difflib import SequenceMatcher

import nltk
from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from sugaroid.brain.postprocessor import reverse
from sugaroid.brain.preprocessors import normalize


class BecauseAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.chatbot = chatbot

    def can_process(self, statement):
        self.normalized = normalize(str(statement))

        if 'because' in self.normalized:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        adj = None
        verb = None
        confidence = 0.90
        last_response = self.chatbot.history[-1]
        self.last_normalized = normalize(str(last_response))
        print(self.last_normalized)
        if last_response:
            self.tagged_last = nltk.pos_tag(self.last_normalized)
            self.tagged_now = nltk.pos_tag(self.normalized)
            print(self.tagged_last)
            print(self.tagged_now)
            sm = SequenceMatcher(None, self.tagged_last, self.tagged_now)
            for i in self.tagged_now:
                if i[1] == 'JJ':
                    adj = i[0]
                elif i[1] == 'VB' and (not i[0] == 'be'):
                    verb = i[0]
            print(sm.ratio())
            if sm.ratio() > 0.5:
                if adj:
                    response = 'Well, Its not a good reason for me to be {}'.format(adj)
                else:
                    response = 'Well, its not a good reason you have told me 😭'
            else:
                if verb:
                    if verb in ['think', 'breath', 'eat', 'hear', 'feel', 'taste']:
                        response = 'Robots are computer devices. I cannot {}'.format(verb.replace('ing', ''))
                    else:
                        response = "I may not be able to {}. " \
                                   "This might not be my builtin quality".format(verb.replace('ing', ''))
                else:
                    if adj:
                        response = 'I will try to be more {} in future'.replace(adj)
                        pass
                    else:
                        response = 'Are you sure this is the reason? I would love to report to my creator.'
                        self.chatbot.report = True
                        pass


        else:
            response = 'Well, I cannot think of saying something. Your conversation began with reason. 🤯'

        selected_statement = Statement(response)
        selected_statement.confidence = confidence
        return selected_statement
