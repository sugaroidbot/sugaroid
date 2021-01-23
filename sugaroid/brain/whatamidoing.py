from sugaroid.brain.ooo import Emotion

from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.constants import WHAT_I_AM_GOING_TO_DO
from sugaroid.sugaroid import SugaroidStatement


def process_what_ami_doing(statement: SugaroidStatement):
    response = None
    for i in statement.doc:
        if i.lower_ in WHAT_I_AM_GOING_TO_DO.keys():
            _answers_subset = WHAT_I_AM_GOING_TO_DO[i.lower_]
            if isinstance(_answers_subset, str):
                response = str(_answers_subset)
            elif isinstance(_answers_subset, list) or isinstance(
                _answers_subset, tuple
            ):
                response = random_response(_answers_subset)
            else:
                # FIXME: Needs more testing
                response = _answers_subset
            break
    if response:
        st = SugaroidStatement(
            response, confidence=0.5, chatbot=True, emotion=Emotion.cry_overflow
        )
        st.confidence = 0.5
        return st
    else:
        return SugaroidStatement(
            "Ok", confidence=0, chatbot=True, emotion=Emotion.cry_overflow
        )
