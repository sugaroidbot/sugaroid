import re
import string
import unicodedata
from nltk.corpus import wordnet as wn
import nltk


def non_punkt_normalize(txt):
    return nltk.WordNetLemmatizer(txt)


def normalize(text):
    remove_punct_dict = dict((ord(punct), None)
                             for punct in string.punctuation)
    # word tokenization
    word_token = nltk.word_tokenize(text.lower().translate(remove_punct_dict))

    # remove ascii
    new_words = []
    for word in word_token:
        new_word = unicodedata.normalize('NFKD', word).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)

    # Remove tags
    rmv = []
    for w in new_words:
        text = re.sub("&lt;/?.*?&gt;", "&lt;&gt;", w)
        rmv.append(text)

    # pos tagging and lemmatization
    tag_map = nltk.defaultdict(lambda: wn.NOUN)
    tag_map['J'] = wn.ADJ
    tag_map['V'] = wn.VERB
    tag_map['R'] = wn.ADV
    lemmatizer = nltk.WordNetLemmatizer()
    lemma_list = []
    rmv = [i for i in rmv if i]
    for token, tag in nltk.pos_tag(rmv):
        lemma = lemmatizer.lemmatize(token, tag_map[tag[0]])
        lemma_list.append(lemma)
    return lemma_list


def tokenize(txt):
    word_token = nltk.word_tokenize(txt.lower())
    return word_token


def current_time():
    """Returns a tuple containing (hour, minute) for current local time."""
    import time
    local_time = time.localtime(time.time())
    return local_time.tm_hour, local_time.tm_min
