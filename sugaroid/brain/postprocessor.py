from random import randint
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import nltk


def sigmaSimilarity(src, dest):
    """

    :param src: a list of literals
    :param dest: a list of final literals
    :return: Probaability
    """
    total = len(src)
    sum = 0
    for i in src:
        for j in dest:
            if i == j:
                sum += 1
    return sum/total


def difference(lst1, lst2):
    lst3 = [value for value in lst1 if value not in lst2]
    return lst3


def reverse(token):
    processed = []
    has_am = 'am' in token
    has_is = 'are' in token

    for i in token:
        tagged = nltk.pos_tag([i])
        if tagged[0][1] == 'PRP':
            if i == 'you':
                processed = ['I'] + processed
            elif i.lower() == 'i':
                processed = ['you'] + processed
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

    for j in range(0, len(processed)-2):
        if processed[j] == 'I' and processed[j+1] == 'are':
            processed[j+1] = 'am'
        elif processed[j] == 'you' and processed[j+1] == 'am':
            processed[j + 1] = 'are'
        else:
            continue

    """
    for i in token:
        if i.lower() == 'i':
            processed.append('you')
        elif i.lower() == 'you':
            processed.append('I')
        else:
            if len(processed) >= 1:
                try:
                    print(processed)
                    if (processed[-1] == 'you') and (i.lower() == 'am'):
                        processed.append('are')
                    elif (processed[-1] == 'I') and (i.lower() == 'are'):
                        processed.append('am')
                    elif (processed[-1] == 'you') and (i.lower() == 'are'):
                        processed.append('am')
                    else:
                        processed.append(i)
                except IndexError:
                    processed.append(i)
            else:
                processed.append(i)
    """
    return processed


def random_response(iterable=[]):
    return iterable[randint(0, len(iterable)-1)]


def cosine_similarity(X_list, Y_list):

    # Program to measure similarity between
    # two sentences using cosine similarity.

    # sw contains the list of stopwords
    sw = stopwords.words('english')
    l1 = [];
    l2 = []

    # remove stop words from string
    X_set = {w for w in X_list if not w in sw}
    Y_set = {w for w in Y_list if not w in sw}

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