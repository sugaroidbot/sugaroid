import nltk
from chatterbot.logic import LogicAdapter

from chatterbot.conversation import Statement
from nltk import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

from sugaroid.brain.constants import CANYOU
from sugaroid.brain.postprocessor import sigmaSimilarity, difference, random_response
from sugaroid.brain.preprocessors import normalize


class CanAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):

        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        self.normalized = normalize(str(statement).lower())
        text = word_tokenize(str(statement))
        self.tagged = nltk.pos_tag(text)
        for k in self.tagged:
            if k[1].startswith('MD'):
                return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        # FIXME: This may printout unrelated data for phrase searches
        noun = None
        propernoun = None
        verb = None
        adj = None
        third_person = None

        if 'you' in self.normalized and ('i' in self.normalized or 'me' in self.normalized):
            # Complex statement
            # Needs extra process
            aimed = 100
        elif 'you' in self.normalized:
            aimed = 75
        elif 'i' in self.normalized or 'me' in self.normalized:
            aimed = 50
        else:
            aimed = 25

        if 'help' in self.normalized:
            aimed += 2

        for i in self.tagged:
            if i[1] == 'NN':
                noun = i[0]
            if i[1].endswith('NP'):
                # FIXME classify it properly
                noun = i[0]
                propernoun = i[0]
                aimed = 25
            elif i[0] == 'help' and (verb is None):
                verb = i[0]
            elif i[1] == 'VB':
                verb = i[0]
            elif i[1] == 'VBG':
                verb = i[0]
            elif i[1] == 'VBP' and not i[0] == 'help':
                verb = i[0]
            elif i[1].startswith('JJ') or i[1].startswith('VBN'):
                adj = i[0]

        self.sia = SentimentIntensityAnalyzer()
        sentiments = self.sia.polarity_scores(str(statement))
        positive_statement = sentiments['pos'] >= sentiments['neg']
        neutral_statement = (sentiments['pos'] + sentiments['neg']) < sentiments['neu']

        print(self.tagged, "SSSS")

        if aimed >=100:
            if neutral_statement:
                if 'help' in self.normalized:
                    # Randomize answer
                    response = 'Yes, I can say a joke to you, answer some questions,' \
                               ' do some mathematical sums, and talk like' \
                               ' this'
                else:
                    if verb and (verb in ['play', 'joke', 'sing', 'dance', 'read']):
                        response = 'I should be able to {}, ' \
                                   'but it all depends on updates which I have received'.format(verb.replace('ing', ''))
                    elif noun and (noun in ['play', 'joke', 'sing', 'dance', 'read']):
                        response = 'I should be able to {}, ' \
                                   'but it all depends on updates which I have received'.format(noun)
                    else:
                        if verb == 'die':
                            response = "I wouild die only when you say 'Bye'"
                        elif verb.lower().replace('ing', '') in ['teach', 'tell', 'say', 'speak', 'go']:
                            response = \
                                "Sure! Just don't ask if I can {}. Just ask".format(verb.lower().replace('ing', ''))
                        else:
                            response = "I think I would not be able to {}. I apologize".format(verb.replace('ing', ''))
            elif positive_statement:
                if noun:
                    if verb:
                        response = "Sure, I would love to help {n} to {v}. " \
                                   "Share sugaroid with {n].".format(n=noun, v=verb.replace('ing', ''))
                    else:
                        response = "I would be glad to help {n}, the reason I was created is to fullfil that " \
                                   "The best way to help {n} is to share sugaroid to {n}".format(n=noun)
                else:
                    # TODO test case
                    response = "Are you sure this is right?"
            else:
                if noun:
                    response = "Well, I would not dare to " \
                               "help you {verb} {noun}".format(verb=verb.replace('ing', ''), noun=noun)
                else:
                    response = 'I am not sure if I could {verb}'.format(verb=verb.replace('ing', ''))
            confidence = aimed / 100 + 0.9
        elif aimed >= 75:
            if 'help' in self.normalized:
                response = 'Yes, I can say a joke to you, answer ' \
                           'some questions, do some mathematical sums, and talk like' \
                           ' this'
            else:
                if verb and (verb in ['play', 'joke', 'sing', 'dance', 'read']):
                    response = 'I should be able to {}, but it all depends on updates which I have received'.format(
                        verb.replace('ing', ''))
                elif noun and (noun in ['play', 'joke', 'sing', 'dance', 'read']):
                    response = 'I should be able to {}, but it all depends on updates which I have received'.format(
                        noun)
                else:
                    if verb == 'die':
                        response = "I would die only when you say 'Bye'"
                    else:
                        if adj:
                            polarity_adj = self.sia.polarity_scores(adj)
                            if polarity_adj['neu'] == 1:
                                response = "I will try to be a {}".format(adj)
                            elif polarity_adj['pos'] > polarity_adj['neg']:
                                response = random_response(CANYOU).format(adj)
                            else:
                                response = "Am I really {}".format(adj)
                        else:

                            response = "I think I would not be able to {}. I apologize".format(verb.replace('ing', ''))
            confidence = aimed/100 +0.9
        elif aimed >= 50:
            if neutral_statement:
                if verb == 'help':
                    response = 'Of Course, If you would like to help me, ' \
                           'try writing some more code to https://github.com/srevinsaju/sugaroid'
                else:
                    if verb:
                        response = 'Do you really want to {}. ' \
                                   'Try rethinking your decision'.format(verb.replace('ing', ''))
                    else:
                        response = 'Well, you should ask that yourself'
            elif positive_statement:
                response = "I guess, you would achieve your goal of {}ing".format(verb.replace('ing', ''))
            else:
                if verb.replace('ing', '') in ['cry', 'sob', 'sleep', 'depress', 'die', 'suicide']:
                    response = "Why do you want to {}, " \
                               "there are many better things to do in life".format(verb.replace('ing', ''))
                else:
                    response = "No, probably not, you shouldn't {}".format(verb.replace('ing', ''))
            confidence = aimed / 100 + 0.9
        else:
            if 'you' not in self.normalized:
                if sentiments['neg'] > sentiments['pos']:
                    response = \
                        'Well I think, its a bad thing to do. ' \
                        'You shouldn\'t {} {}'.format(verb.replace('ing', ''), noun)
                else:
                    response = \
                        'I guess its good thing which you have thought about. You should {} {}'\
                            .format(verb.replace('ing', ''), noun)
                confidence = (sentiments['neg'] + sentiments['pos']) + ((sentiments['neg'] + sentiments['pos'])/2)
            else:
                if sentiments['neu'] == 1:
                    response = "I apologize. I would never be able to be {}".format(noun)
                elif sentiments['neg'] > sentiments['pos']:
                    response = \
                        'Well I think, its a bad thing to do. I wouldn\'t {} {}'.format(verb.replace('ing', ''), noun)
                else:
                    if 'like' in self.normalized:
                        response = \
                            'I guess its good thing which you have thought about. Me being a bot, ' \
                            'wouldn\'t be able to do that. You should {} like {}'\
                                .format(verb.replace('ing', ''), noun)
                    else:
                        response = \
                            'I guess its good thing which you have thought about. Me being a bot, ' \
                            'wouldn\'t be able to do that. You should probably {} {}'\
                                .format(verb.replace('ing', ''), noun)
                if sentiments['neu'] > 0.8:
                    confidence = sentiments['neu']
                else:
                    confidence = (sentiments['neg'] + sentiments['pos']) + ((sentiments['neg'] + sentiments['pos'])/2)

        if verb == 'be':
            print("OK")
            ind = self.normalized.index('be')
            for j in range(ind, len(self.normalized)-1):
                print(self.tagged[j])
                if self.tagged[j][1].startswith('NN'):
                    print("OKOK")
                    polarity_adj = self.sia.polarity_scores(self.tagged[j][0])
                    if polarity_adj['pos'] + polarity_adj['neg'] < polarity_adj['neu']:
                        response = "I am not sure if I can ever be a '{}'".format(self.tagged[j][0])
                    elif polarity_adj['pos'] > polarity_adj['neg']:
                        response = "I am always trying to be {}".format(self.tagged[j][0])
                    else:
                        response = "I would never try to be a {}".format(self.tagged[j][0])
                    confidence = aimed / 100 + 0.9

        selected_statement = Statement(response)
        selected_statement.confidence = confidence
        return selected_statement
