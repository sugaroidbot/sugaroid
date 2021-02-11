from difflib import SequenceMatcher

from sugaroid.brain.constants import BOT_REASONS
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import random_response
from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.core.statement import SugaroidStatement


def pos_tag(statement: SugaroidStatement):
    return [(str(i), i.tag_) for i in statement.doc]


class BecauseAdapter(SugaroidLogicAdapter):
    """
    Processes statements which starts with Because or gives a reason
    """

    def can_process(self, statement: SugaroidStatement):
        return "because" in statement.words

    def process(
        self,
        statement: SugaroidStatement,
        additional_response_selection_parameters=None,
    ):
        # add emotion output
        adj = None
        verb = None
        confidence = 0.90
        last_response = self.chatbot.globals["history"]["total"][-1]
        emotion = Emotion.neutral
        if last_response:
            tagged_last = pos_tag(last_response)
            tagged_now = pos_tag(statement)
            sm = SequenceMatcher(None, tagged_last, tagged_now)
            for i in statement.doc:
                if i.tag_ == "JJ":
                    adj = i.lemma_
                elif i.tag_ == "VB" and (not i.lemma_ == "be"):
                    verb = i.lemma_
            if sm.ratio() > 0.5:
                if adj:
                    response = "Well, Its not a good reason for me to be {}".format(adj)
                else:
                    response = "Well, its not a good reason you have told me 😭"
            else:
                if verb:
                    if verb in ["think", "breath", "eat", "hear", "feel", "taste"]:
                        response = "Robots are computer devices. I cannot {}".format(
                            verb.replace("ing", "")
                        )
                        emotion = Emotion.cry
                    else:
                        response = (
                            "I may not be able to {}. "
                            "This might not be my builtin quality".format(
                                verb.replace("ing", "")
                            )
                        )
                        emotion = Emotion.cry_overflow
                else:
                    if adj:

                        sia_scores = self.sia.polarity_scores(str(statement))
                        if sia_scores["neu"] == 1:
                            response = "Ok! Thanks for your feedback"
                            emotion = Emotion.positive
                        elif sia_scores["pos"] > sia_scores["neg"]:
                            response = "I will try to be more {} in future".format(adj)
                            emotion = Emotion.adorable
                        else:
                            response = "I will never try to be {}.".format(adj)
                            emotion = Emotion.angry
                    else:
                        response = random_response(BOT_REASONS)
                        emotion = Emotion.non_expressive_left

        else:
            response = "Well, I cannot think of saying something. Your conversation began with reason. 🤯"
            emotion = Emotion.angry

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.set_confidence(confidence)
        selected_statement.set_emotion(emotion)

        return selected_statement
