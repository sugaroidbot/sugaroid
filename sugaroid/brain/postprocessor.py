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