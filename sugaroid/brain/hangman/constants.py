from typing import List

from sugaroid.datasets.collector import Session

WORDS = dict()


def get_hangman_words(category: str, collector: Session) -> List[str]:
    global WORDS

    if WORDS.get(category):
        return WORDS[category]

    data = collector.get_dataset(f"hangman/{category}").splitlines()
    WORDS[category] = data
    return data
