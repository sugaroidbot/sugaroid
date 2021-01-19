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


from random import randint
from chatterbot.logic import LogicAdapter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sugaroid.brain.constants import GRATIFY, CONSOLATION, SIT_AND_SMILE, APPRECIATION
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import reverse, random_response, any_in
from sugaroid.brain.preprocessors import tokenize
from sugaroid.sugaroid import SugaroidStatement


class EmotionAdapter(LogicAdapter):
    """
    Handles positive and negative emotional statements
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.sia = SentimentIntensityAnalyzer()

    def can_process(self, statement):
        a = self.sia.polarity_scores(str(statement))
        # do not enable emotion adapter when 
        # we are playing akinator
        if self.chatbot.globals["akinator"]["enabled"]:
            return False
        elif a['neu'] < 0.5:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        # parsed = str(statement).lower().strip()
        raw_statement = str(statement)
        parsed = tokenize(str(statement))
        emotion = Emotion.neutral
        a = self.sia.polarity_scores(raw_statement)
        response = ":)"
        confidence = a['pos'] + a['neg']
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
                    response = GRATIFY[randint(0, len(GRATIFY) - 1)]
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
                                self.chatbot.globals['fun'] = False
                            else:
                                response = "I am depressed. Is there anything which I hurt you? I apologize for that"
                                emotion = Emotion.depressed
                    else:
                        if any_in(APPRECIATION, parsed):
                            response = random_response(GRATIFY)
                            emotion = Emotion.angel
                            confidence = 0.8
                        else:
                            # FIXME : Make it more smart
                            response = random_response(SIT_AND_SMILE)
                            emotion = Emotion.lol
                            if confidence > 0.8:
                                confidence -= 0.2
            else:
                if 'i' in parsed:
                    response = "Its ok,  {}.".format(
                        CONSOLATION[randint(0, len(CONSOLATION) - 1)])
                    emotion = Emotion.positive
                else:
                    # well, I don't want to say ( I don't know )
                    # FIXME : Use a better algorithm to detect sentences
                    reversed = reverse(parsed)
                    response = 'Why do you think {}?'.format(
                        ' '.join(reversed))
                    emotion = Emotion.dead

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion
        return selected_statement
