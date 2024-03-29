import nltk
import wikipediaapi
from chatterbot.logic import LogicAdapter
from nltk import word_tokenize
from sugaroid.brain.brain import Neuron
from sugaroid.brain.ooo import Emotion
from sugaroid.core.statement import SugaroidStatement
from sugaroid.brain.constants import WHATSUP
from sugaroid.brain.postprocessor import random_response, any_in

try:
    from mediawikiapi import MediaWikiAPI

    media_wiki_found = True
except ModuleNotFoundError:
    media_wiki_found = False


class WikiAdapter(LogicAdapter):
    """
    Handles Wikipedia based questions
    """

    def can_process(self, statement) -> bool:
        self.text = word_tokenize(str(statement))
        if "$wolf" in self.text:
            return False
        tagged = nltk.pos_tag(self.text)
        q = False
        pr = False
        for i in tagged:
            if i[1] == "WP" or i[1] == "WRB":
                q = True
            elif (i[1].startswith("PRP")) and (not i[0] == "we"):
                pr = True
        if q and (not pr):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        # FIXME: This may printout unrelated data for phrase searches
        self.text = word_tokenize(str(statement))
        response = "I don't know"
        confidence = 0

        emotion = Emotion.neutral
        count = 0
        for i in self.text:
            if i.lower() == "what":
                count += 1
        if count > 1:
            selected_statement = SugaroidStatement("Nothing " * count, chatbot=True)
            selected_statement.confidence = 0.99
            emotion = Emotion.seriously
            selected_statement.emotion = emotion
            return selected_statement
        elif ("Srevin" in self.text) or ("srevin" in self.text):
            response = "Srevin Saju is the creator of Sugaroid bot"
            selected_statement = SugaroidStatement(response, chatbot=True)
            selected_statement.confidence = 1.0
            selected_statement.emotion = emotion
            return selected_statement
        elif "sugaroid" in self.text or "Sugaroid" in self.text:
            response = "I am Sugaroid. 😎"
            selected_statement = SugaroidStatement(response, chatbot=True)
            selected_statement.confidence = 1.0
            selected_statement.emotion = emotion
            return selected_statement
        elif "up" in self.text or "Up" in self.text:
            # FIXME will introduce a regression in future
            response = random_response(WHATSUP)
            selected_statement = SugaroidStatement(response, chatbot=True)
            selected_statement.confidence = 1.0
            selected_statement.emotion = emotion
            return selected_statement

        else:
            nlp = self.chatbot.lp
            what = False
            norm = nlp.tokenize(str(statement))
            for i in range(len(norm) - 2):
                if norm[i].tag_ == "WP":
                    if (
                        norm[i].lower_ == "what"
                        or norm[i].lower_ == "who"
                        or norm[i].lower_ == "where"
                    ):
                        what = True
                    elif norm[i].lower_ == "how":
                        what = False
                        how = True
                        break
                    else:
                        what = True
                    if what:
                        for j in range(i + 1, len(norm)):
                            if (norm[j].tag_ == "VBZ") or (norm[j].tag_ == "DT"):
                                continue
                            else:
                                question = norm[j:]
                                if question[0].lower_ == "time":
                                    response = Neuron.gen_time()
                                    confidence = 1.0
                                    stat = True
                                    break
                                else:
                                    if media_wiki_found:
                                        response, confidence, stat = wikipedia_search(
                                            self, question
                                        )
                                        break
                                    else:
                                        response = "Seems like MediaWikiAPI is not installed on your PC"
                                        confidence = 0.9
                                        break
                        else:
                            response = "I am not sure what you are asking for."
                            confidence = 0.4
                            emotion = Emotion.cry
                            break
                        if response:
                            break
                    else:
                        response = (
                            "I can't give a reason for that at the moment. Maybe you might want to search the "
                            "internet."
                        )
                        confidence = 0.4
                        emotion = Emotion.cry_overflow
                        break

                else:
                    response = "Well. maybe I do not know"
                    confidence = 0

            selected_statement = SugaroidStatement(str(response), chatbot=True)
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
    wiki = wikipediaapi.Wikipedia("en")
    a = mw.search(str(question))
    question = str(question)
    if len(a) >= 1:
        cos = self.chatbot.lp.similarity(question.lower(), a[0].lower())
    else:
        return "Oops, the item you wanted to know is not on wikipedia.", 0.9, False
    if cos > 0.9:
        self.chatbot.globals["reversei"]["enabled"] = False
        self.chatbot.globals["reversei"]["uid"] = False
        response = wiki.page(a[0]).summary
        confidence = cos
        stat = True
    else:
        self.chatbot.globals["reversei"]["enabled"] = True
        self.chatbot.globals["reversei"]["uid"] = 30000000002
        self.chatbot.globals["reversei"]["type"] = int
        self.chatbot.globals["temp_data"] = a

        def bracketize(x):
            return "\n[{}] {}".format(x[0] + 1, str(x[1]))

        response = "Did you mean any of these {}".format(
            " ".join([bracketize(x) for x in enumerate(a)])
        )
        confidence = 1.0
        stat = False

    return response, confidence, stat
