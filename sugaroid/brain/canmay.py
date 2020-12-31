"""
MIT License

Sugaroid Artificial Intelligence
Chatbot Core
Copyright (c) 2020-2021 Srevin Saju
Copyright (c) 2021 The Sugaroid Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import nltk
from chatterbot.logic import LogicAdapter

from chatterbot.conversation import Statement
from nltk import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

from sugaroid.brain.constants import CANYOU
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import sigmaSimilarity, difference, random_response
from sugaroid.brain.preprocessors import normalize
from sugaroid.sugaroid import SugaroidStatement


class CanAdapter(LogicAdapter):
    """
    Processes statements which features a Modal question (can, may)
    """

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
        adapter = None
        emotion = Emotion.neutral
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
        neutral_statement = (
            sentiments['pos'] + sentiments['neg']) < sentiments['neu']

        if aimed >= 100:
            if neutral_statement:
                confidence = aimed / 100 + 0.7
                if 'help' in self.normalized:
                    # Randomize answer
                    response = 'Yes, I can say a joke to you, answer some questions,' \
                               ' do some mathematical sums, and talk like' \
                               ' this. I can also play a game of Akinator'
                    adapter = 'what_can'
                else:
                    if verb and (verb in ['play', 'joke', 'sing', 'dance', 'read']):
                        if verb == 'play':
                            from sugaroid.game.game import games
                            response = 'I can play some games like {}'.format(
                                ', '.join(games))

                        else:
                            response = 'I should be able to {}, ' \
                                       'but it all depends on updates which I have received'.format(
                                           self.chatbot.lp.lemma(verb)[0])
                            emotion = Emotion.rich
                    elif noun and (noun in ['play', 'joke', 'sing', 'dance', 'read']):
                        if noun == 'play':
                            from sugaroid.game.game import games
                            response = 'I can play some games like {}'.format(
                                ', '.join(games))
                        else:
                            response = 'I should be able to {}, ' \
                                'but it all depends on updates which I have received'.format(
                                    noun)
                            emotion = Emotion.rich
                    else:
                        if verb == 'die':
                            response = "I wouild die only when you say 'Bye'"
                        elif self.chatbot.lp.lemma(verb)[0] in ['teach', 'tell', 'say', 'speak', 'go']:
                            response = \
                                "Sure! Just don't ask if I can {}. Just ask".format(
                                    self.chatbot.lp.lemma(verb)[0])
                            emotion = Emotion.angel
                        else:
                            if self.chatbot.lp.lemma(verb)[0] == 'do':
                                confidence = 0
                            response = "I think I would not be able to {}. I apologize".format(
                                self.chatbot.lp.lemma(verb)[0])
                            emotion = Emotion.cry_overflow

            elif positive_statement:
                if noun:
                    if verb:
                        response = "Sure, I would love to help {n} to {v}. " \
                                   "Share sugaroid with {n].".format(
                                       n=noun, v=self.chatbot.lp.lemma(verb)[0])
                        emotion = Emotion.positive
                    else:
                        response = "I would be glad to help {n}, the reason I was created is to fullfil that " \
                                   "The best way to help {n} is to share sugaroid to {n}".format(
                                       n=noun)

                else:
                    # TODO test case
                    response = "Are you sure this is right?"
                    emotion = Emotion.non_expressive_left
                confidence = aimed / 100 + 0.9
            else:
                if noun:
                    response = "Well, I would not dare to " \
                               "help you {verb} {noun}".format(
                                   verb=verb.replace('ing', ''), noun=noun)
                    emotion = Emotion.angry
                else:
                    response = 'I am not sure if I could {verb}'.format(
                        verb=self.chatbot.lp.lemma(verb)[0])
                confidence = aimed / 100 + 0.7
        elif aimed >= 75:
            confidence = aimed / 100 + 0.7
            if 'help' in self.normalized:
                response = 'Yes, I can say a joke to you, answer ' \
                           'some questions, do some mathematical sums, and talk like' \
                           ' this'
                adapter = 'what_can'
            else:
                if verb and (verb in ['play', 'joke', 'sing', 'dance', 'read']):
                    if verb == 'play':
                        from sugaroid.game.game import games
                        response = 'I can play some games like {}'.format(
                            ', '.join(games))

                    else:
                        response = 'I should be able to {}, but it all depends on updates which I have received'.format(
                            self.chatbot.lp.lemma(verb)[0])
                        emotion = Emotion.rich

                elif noun and (noun in ['play', 'joke', 'sing', 'dance', 'read']):
                    if verb == 'play':
                        from sugaroid.game.game import games
                        response = 'I can play some games like {}'.format(
                            ', '.join(games))
                    else:
                        response = 'I should be able to {}, but it all depends on updates which I have received'.format(
                            noun)
                        emotion = Emotion.rich
                else:
                    if verb == 'die':
                        response = "I would die only when you say 'Bye'"
                        emotion = Emotion.cry
                    else:
                        if adj:
                            polarity_adj = self.sia.polarity_scores(adj)
                            if polarity_adj['neu'] == 1:
                                # as in I will try to be 'a good bot'
                                article_or_pronoun = "a"

                                # some wicked users try to ask it weird
                                # questions
                                if "your" in self.normalized:
                                    # hey, its asking about me!!
                                    # eg: can you be yourself?
                                    article_or_pronoun = "your"

                                response = "I will try to be {} {}".format(
                                    article_or_pronoun,
                                    adj
                                )
                                emotion = Emotion.adorable
                            elif polarity_adj['pos'] > polarity_adj['neg']:
                                response = random_response(CANYOU).format(adj)
                                emotion = Emotion.angel
                            else:
                                response = "Am I really {}".format(adj)
                                emotion = Emotion.non_expressive
                        elif verb:
                            if self.chatbot.lp.lemma(verb)[0] == 'do':
                                confidence = 0
                            response = "I think I would not be able to {}. I apologize".format(
                                self.chatbot.lp.lemma(verb)[0])
                        else:
                            response = "Oops. I didn't get what you just told? Try rephrasing it out"
                            confidence = 0.2

        elif aimed >= 50:
            if neutral_statement:
                if verb == 'help':
                    response = 'Of Course, If you would like to help me, ' \
                        'try writing some more code to https://github.com/srevinsaju/sugaroid'
                    emotion = Emotion.github
                else:
                    if verb:
                        response = 'Do you really want to {}. ' \
                                   'Try rethinking your decision'.format(
                                       self.chatbot.lp.lemma(verb)[0])
                        emotion = Emotion.non_expressive_left
                    else:
                        response = 'Well, you should ask that yourself'
                        emotion = Emotion.angry_non_expressive
            elif positive_statement:
                if verb == 'help':
                    response = 'Of Course, If you would like to help me, ' \
                        'try writing some more code to https://github.com/srevinsaju/sugaroid'
                    emotion = Emotion.github
                else:
                    response = "I guess, you would achieve your goal of {}ing".format(
                        self.chatbot.lp.lemma(verb)[0])
                    emotion = Emotion.positive
            else:
                if self.chatbot.lp.lemma(verb)[0] in ['cry', 'sob', 'sleep', 'depress', 'die', 'suicide']:
                    response = "Why do you want to {}, " \
                               "there are many better things to do in life".format(
                                   self.chatbot.lp.lemma(verb)[0])
                    emotion = Emotion.adorable
                else:
                    response = "No, probably not, you shouldn't {}".format(
                        self.chatbot.lp.lemma(verb)[0])
                    emotion = Emotion.positive
            confidence = aimed / 100 + 0.9
        else:
            if 'you' not in self.normalized:
                confidence = (sentiments['neg'] + sentiments['pos']) + \
                    ((sentiments['neg'] + sentiments['pos']) / 2)
                if sentiments['neu'] == 1:
                    if not verb:
                        verb = "do"
                        noun = "that"
                    response = "Well. I am unsure if you really need to {} {}".format(
                        self.chatbot.lp.lemma(verb)[0], noun)
                    confidence = confidence - 0.2
                    emotion = Emotion.cry_overflow
                elif sentiments['neg'] > sentiments['pos']:
                    response = \
                        'Well I think, its a bad thing to do. ' \
                        'You shouldn\'t {} {}'.format(
                            self.chatbot.lp.lemma(verb)[0], noun)
                    emotion = Emotion.negative
                else:
                    response = \
                        'I guess its good thing which you have thought about. You should {} {}'\
                        .format(self.chatbot.lp.lemma(verb)[0], noun)
                    emotion = Emotion.positive

            else:
                if sentiments['neu'] == 1:
                    response = "I apologize. I would never be able to be {}".format(
                        noun)
                    emotion = Emotion.cry_overflow
                elif sentiments['neg'] > sentiments['pos']:
                    response = \
                        'Well I think, its a bad thing to do. I wouldn\'t {} {}'.format(
                            self.chatbot.lp.lemma(verb)[0], noun)
                    emotion = Emotion.dead
                else:
                    if 'like' in self.normalized:
                        # FIXME
                        response = \
                            'I guess its good thing which you have thought about. Me being a bot, ' \
                            'wouldn\'t be able to do that. You should {} like {}'\
                            .format(self.chatbot.lp.lemma(verb)[0], noun)
                        emotion = Emotion.dead
                    else:
                        response = \
                            'I guess its good thing which you have thought about. Me being a bot, ' \
                            'wouldn\'t be able to do that. You should probably {} {}'\
                            .format(self.chatbot.lp.lemma(verb)[0], noun)
                        emotion = Emotion.neutral
                if sentiments['neu'] > 0.8:
                    confidence = sentiments['neu']
                else:
                    confidence = (sentiments['neg'] + sentiments['pos']) + \
                        ((sentiments['neg'] + sentiments['pos']) / 2)

        if verb == 'be':
            ind = self.normalized.index('be')
            for j in range(ind, len(self.normalized) - 1):
                if self.tagged[j][1].startswith('NN'):
                    polarity_adj = self.sia.polarity_scores(self.tagged[j][0])
                    if polarity_adj['pos'] + polarity_adj['neg'] < polarity_adj['neu']:
                        response = "I am not sure if I can ever be a '{}'".format(
                            self.tagged[j][0])
                        emotion = Emotion.cry_overflow
                    elif polarity_adj['pos'] > polarity_adj['neg']:
                        response = "I am always trying to be {}".format(
                            self.tagged[j][0])
                        emotion = Emotion.wink
                    else:
                        response = "I would never try to be a {}".format(
                            self.tagged[j][0])
                        emotion = Emotion.cry
                    confidence = aimed / 100 + 0.7

        if confidence >= 1.4:
            confidence /= 2
        elif confidence >= 1.0:
            confidence /= 1.2

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence + 0.2
        selected_statement.emotion = emotion
        selected_statement.adapter = adapter
        return selected_statement
