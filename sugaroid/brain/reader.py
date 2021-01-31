import logging

from sugaroid.reader.scrawled import SCRAWLED
from chatterbot.logic import LogicAdapter
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize, spac_token, purify
from sugaroid.sugaroid import SugaroidStatement


class ReaderAdapter(LogicAdapter):
    """
    Logical adapter for processing data with one words
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.normalized = None
        self.intersect = None
        self.tokenized = None

    def can_process(self, statement):
        self.normalized = normalize(str(statement).lower())

        if "reader" in self.normalized:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        emotion = Emotion.seriously
        confidence = 0
        closest_cos = 0
        response = "I couldn't find a similar heading in scrawled data"
        cleaned_text = []
        for i in spac_token(statement, chatbot=self.chatbot):
            if i.is_stop:
                pass
            elif i.lower_ == "reader":
                pass
            else:
                cleaned_text.append(str(i.lower_))
        md = False
        similarity = self.chatbot.lp.similarity
        for file in SCRAWLED:
            headings, content = SCRAWLED[file]
            for k in cleaned_text:

                if ".md" in k:
                    response = "The markdown file {} is not scrawled".format(k)
                    if k in SCRAWLED.keys():
                        md = k
                if md:
                    response = "\n".join(SCRAWLED[k][1])
                    break
            if md:
                break

            for heading in headings:
                input_statement = " ".join(
                    purify(
                        self.chatbot.lp.tokenize(str(statement).lower()),
                        ["how", "to", "sugar"],
                        lemma=True,
                    )
                )
                heading_processed = " ".join(
                    purify(
                        self.chatbot.lp.tokenize(str(heading).lower()),
                        ["how", "to", "sugar"],
                        lemma=True,
                    )
                )

                sim = similarity(input_statement, heading_processed)
                if sim > 0.9:
                    suffix = "⬆"
                else:
                    suffix = ""
                logging.info(
                    "ReaderAdapter: scanned {} against {}. cosine index of {}{}".format(
                        input_statement, heading_processed, sim, suffix
                    )
                )

                if sim > confidence:
                    response = "The closest match I could find is this:\n" + "\n".join(
                        content
                    )
                    confidence = sim
                    break

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = 8 + confidence
        selected_statement.emotion = emotion
        selected_statement.adapter = None
        return selected_statement
