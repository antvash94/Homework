import string


def check_all(*strings):
    """characters that appear in all strings"""
    set_list = [set(i) for i in strings]
    result = set.intersection(*set_list)
    return result


def check_one(*strings):
    """characters that appear in at least one string"""
    set_list = [set(i) for i in strings]
    result = set.union(*set_list)
    return result


def check_two(*strings):
    """characters that appear at least in two strings"""
    set_list = [set(i) for i in strings]
    result = set()
    for i, s in enumerate(set_list):
        set_list.remove(s)
        for st in set_list:
            result.update(s.intersection(st))
        set_list.insert(i, s)
    return result


def check_alphabet(*strings):
    """characters of alphabet, that were not used in any string"""
    alpha_set = set(string.ascii_lowercase)
    set_list = [set(i) for i in strings]
    result = alpha_set - set.union(*set_list)
    return result
