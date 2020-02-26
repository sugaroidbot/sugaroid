import nltk
from chatterbot.logic import LogicAdapter

from chatterbot.conversation import Statement
from nltk import word_tokenize

from sugaroid.brain.postprocessor import sigmaSimilarity, difference, random_response


class OrAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):

        self.text = word_tokenize(str(statement))
        self.tagged = nltk.pos_tag(self.text)
        print(self.tagged)
        for i in self.tagged:
            if i[1] == 'CC':
                return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        nouns = set()
        response = None
        confidence = 0
        if (len(self.tagged) == 1) or (self.tagged[0][1] == 'CC'):
            response = "Are you serious, just an {}".format(self.tagged[0][0])
            confidence = 0.8
        elif len(self.tagged) == 2:
            response = 'I expected you to provide an option, But what? 🐓'
            confidence = 0.8
        else:
            for i in range(len(self.tagged)-1):
                n1 = self.tagged[i-1]
                if n1[1].startswith('N'):
                    nouns = nouns.union({n1[0]})
                n2 = self.tagged[i + 1]
                if n2[1].startswith('N'):
                    nouns = nouns.union({n2[0]})
            if ('boy' in nouns) or ('girl' in nouns):
                response = "I am neither"
            else:
                response = "{} 🎃".format(random_response(list(nouns)))
            confidence = 0.8
        selected_statement = Statement(response)
        selected_statement.confidence = confidence
        return selected_statement
