def split_by_index(s, index):
    """Splits the s string by indexes specified in indexes."""
    index.insert(0, 0)
    if index[-1] < len(s):
        index.append(len(s))
    index_tpl = list(zip(index[:], index[1:]))
    result = [s[i[0]:i[1]] for i in index_tpl]
    return result
