import nltk
import wikipediaapi
from chatterbot.logic import LogicAdapter

from chatterbot.conversation import Statement
from mediawikiapi import MediaWikiAPI
from nltk import word_tokenize

from sugaroid.brain.ooo import Emotion
from sugaroid.google.google import chatbot_query
from sugaroid.sugaroid import SugaroidStatement


class WikiAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        # FIXME Add Language support
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        self.text = word_tokenize(str(statement))
        tagged = nltk.pos_tag(self.text)
        print(tagged)
        q = False
        pr = False
        for i in tagged:
            if i[1] == 'WP' or i[1] == 'WRB':
                q = True
            elif (i[1].startswith('PRP')) and (not i[0] == 'we'):
                pr = True
        if q and (not pr):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        # FIXME: This may printout unrelated data for phrase searches
        response = "I don't know"
        confidence = 0

        emotion = Emotion.neutral
        count = 0
        for i in self.text:
            if i.lower() == 'what':
                count += 1
        if count > 1:
            selected_statement = SugaroidStatement('Nothing ' * count)
            selected_statement.confidence = 0.99
            emotion = Emotion.seriously
            selected_statement.emotion = emotion
            return selected_statement
        else:
            nlp = self.chatbot.lp
            what = False
            norm = nlp.tokenize(str(statement))
            for i in range(len(norm) - 2):
                print(i, norm[i], norm[i].tag_, "J"*55)
                if norm[i].tag_ == 'WP':
                    if norm[i].lower_ == "what" or norm[i].lower_ == "who" or norm[i].lower_ == "where":
                        what = True
                    elif norm[i].lower_ == 'how':
                        what = False
                        how = True
                        break
                    else:
                        what = True
                    if what:
                        print(norm, norm[i + 1], len(norm) - 2)

                        for j in range(i + 1, len(norm)):

                            print(norm[j], "K"*5)
                            if (norm[j].tag_ == 'VBZ') or (norm[j].tag_ == 'DT'):
                                continue
                            else:
                                question = norm[j:]
                                response, confidence, stat = wikipedia_search(
                                    self, question)

                                break
                        else:
                            response = 'I am not sure what you are asking for.'
                            confidence = 0.4
                            emotion = Emotion.cry
                            break
                        if response:
                            break
                    else:
                        response = 'I can give a reason for that at the moment. Maybe you might want to search the ' \
                                   'internet. '
                        confidence = 0.4
                        emotion = Emotion.cry_overflow
                        break

                else:
                    response = 'Well. maybe I do not know'
                    confidence = 0

            selected_statement = SugaroidStatement(str(response))
            selected_statement.confidence = confidence

        selected_statement.emotion = emotion

        return selected_statement


def wikipedia_search(self, question):
    """
    :param self: self object where chatbot object is also located
    :param question:
    :return: A tuple of values:
    (response, confidence, stat)
    stat = Found or not found
    """
    mw = MediaWikiAPI()
    wiki = wikipediaapi.Wikipedia('en')
    a = mw.search(str(question))
    question = str(question)
    if len(a) >= 1:
        cos = self.chatbot.lp.similarity(question.lower(), a[0].lower())
    else:
        return "Oops, the item you wanted to know is not on wikipedia.", 0.9, False

    print(question.lower(), a[0].lower())
    print("cos", cos)
    if cos > 0.9:

        response = wiki.page(a[0]).summary
        confidence = cos
        stat = True
    else:
        self.chatbot.reverse = True
        self.chatbot.next = 30000000002
        self.chatbot.next_type = int
        self.chatbot.temp_data = a
        def bracketize(x): return '\n[{}] {}'.format(x[0]+1, str(x[1]))
        response = "Did you mean any of these {}".format(
            ' '.join([bracketize(x) for x in enumerate(a)]))
        confidence = 0.5
        stat = False

    return response, confidence, stat
