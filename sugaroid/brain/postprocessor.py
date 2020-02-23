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
        if i.lower() == 'i':
            processed.append('you')
        elif i.lower() == 'you':
            processed.append('I')
        else:
            if len(processed) >= 1:
                if (processed[-1] == 'you') and (i.lower() == 'am'):
                    processed.append('are')
                elif (processed[-1] == 'I') and (i.lower() == 'are'):
                    processed.append('am')
                else:
                    processed.append(i)
            else:
                processed.append(i)
    return processed
