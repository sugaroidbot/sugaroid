from sugaroid.brain.ooo import Emotion

from sugaroid.brain.constants import WHAT_I_AM_GOING_TO_DO
from sugaroid.sugaroid import SugaroidStatement


def process_what_ami_doing(statement: SugaroidStatement):
    response = None
    for i in statement.doc:
        if i.lower_ in WHAT_I_AM_GOING_TO_DO.keys():
            response = WHAT_I_AM_GOING_TO_DO[i.lower_]
            break
    if response:
        st = SugaroidStatement(response, confidence=0.5,
                               chatbot=True, emotion=Emotion.cry_overflow)
        st.confidence = 0.5
        return st
    else:
        return SugaroidStatement("Ok", confidence=0, chatbot=True, emotion=Emotion.cry_overflow)
