"""
MIT License

Sugaroid Artificial Inteligence
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
import logging
from random import randint
from nltk.corpus import stopwords
import nltk
from sugaroid.brain.utils import LanguageProcessor


def sigmaSimilarity(src, dest):
    """
    :param src: a list of literals
    :param dest: a list of final literals
    :return: Probability
    """
    total = len(src)
    sum = 0
    for i in src:
        for j in dest:
            if i == j:
                sum += 1
    return sum / total


def difference(lst1, lst2):
    lst3 = [value for value in lst1 if value not in lst2]
    return lst3


def reverse(token):
    """
    Reverses the first person pronouns to second person pronouns and vice versa
    :param token: a nltk.word_tokenize type list
    :return: a list similar to nltk.word_tokenize
    """
    processed = []
    has_am = 'am' in token
    has_is = 'are' in token
    logging.info("Reverse: Received {}".format(token))
    interrogation = False
    for i in token:
        lps = LanguageProcessor().tokenize(i)[0]
        if lps.tag_ == '.' and lps.lower_ == '?':
            interrogation = True
        elif str(lps.tag_).startswith('W'):
            interrogation = True
    for i in token:
        tagged = nltk.pos_tag([i])
        if tagged[0][1] == 'PRP':
            if i == 'you':
                if interrogation:
                    processed.append('I')
                else:
                    processed = processed[:-1] + ['I'] + processed[-1:]
            elif i.lower() == 'i':
                processed.append('you')
        elif tagged[0][1] == 'VBP':
            if i == 'are':
                if 'I' in processed:
                    processed.append('am')
                else:
                    processed.append('are')
            elif i == 'am':
                if 'I' in processed:
                    processed.append('am')
                else:
                    processed.append('are')
            else:
                processed.append('are')
        else:
            processed.append(i)

    for j in range(0, len(processed) - 2):
        if processed[j] == 'I' and processed[j + 1] == 'are':
            processed[j + 1] = 'am'
        elif processed[j] == 'you' and processed[j + 1] == 'am':
            processed[j + 1] = 'are'
        else:
            continue

    for j in range(0, len(processed) - 2):
        if processed[j] == 'I' and processed[j + 1] == 'are':
            processed[j] = 'you'
        elif processed[j] == 'you' and processed[j + 1] == 'am':
            processed[j] = 'I'
        else:
            continue

    for j in range(0, len(processed) - 2):
        if processed[j] == 'are' and processed[j + 1] == 'I':
            processed[j] = 'am'
        elif processed[j] == 'am' and processed[j + 1] == 'you':
            processed[j] = 'are'
        else:
            continue

    logging.info("Reverse: Pushing {}".format(processed))
    return processed


def random_response(iterable=()):
    """
    Selects a random response from the given set of iterable types
    :param iterable:
    :return: a selected value of the iterable
    """
    return iterable[randint(0, len(iterable) - 1)]


def cosine_similarity(X_list, Y_list):

    # Program to measure similarity between
    # two sentences using cosine similarity.

    # sw contains the list of stopwords
    sw = stopwords.words('english')
    l1 = []
    l2 = []

    # remove stop words from string
    X_set = {w for w in X_list if w not in sw}
    Y_set = {w for w in Y_list if w not in sw}

    # form a set containing keywords of both strings
    rvector = X_set.union(Y_set)
    for w in rvector:
        if w in X_set:
            l1.append(1)  # create a vector
        else:
            l1.append(0)
        if w in Y_set:
            l2.append(1)
        else:
            l2.append(0)
    c = 0

    # cosine formula
    for i in range(len(rvector)):
        c += l1[i] * l2[i]
    cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
    return cosine


def any_in(arg1: list, string1: list):
    """
    Advanced in operator
    Checks any of the list item exists in in the string
    :param arg1:
    :param string1:
    :return:
    """
    for i in arg1:
        if i in string1:
            return True
    else:
        return False


def raw_in(arg, spacy_tokenized):
    for i in spacy_tokenized:
        if i.text == arg:
            return True
    else:
        return False


def raw_lower_in(arg, spacy_tokenized):
    for i in spacy_tokenized:
        if i.lower_ == arg:
            return True
    else:
        return False


def lemma_in(arg, spacy_tokenized):
    for i in spacy_tokenized:
        if i.lemma_ == arg:
            return True
    else:
        return False


def pos_in(arg, spacy_tokenized):
    for i in spacy_tokenized:
        if i.pos_ == arg:
            return True
    else:
        return False


def text2int(textnum, numwords={}):
    """
    Converts words to numbers
    from https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers
    :param textnum:
    :param numwords:
    :return:
    """
    if not numwords:
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty",
                "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):
            numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current
