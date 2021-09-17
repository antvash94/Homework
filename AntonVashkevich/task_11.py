def combine_dicts(*args):
    """Function, that receives changeable number of dictionaries
    (keys - letters, values - numbers) and combines them
    into one dictionary. Dict values should be summarized in case of identical keys"""
    result = {}
    for dct in args:
        for k, v in dct.items():
            if result.get(k):
                result[k] += v
            else:
                result[k] = v
    return result
