def my_split(string, sep=" "):
    """Works the same as str.split method """
    if sep in string:
        index_list = [(i, i+len(sep)) for i in range(len(string)) if string.startswith(sep, i)]
        result = []
        start = 0
        for i in index_list:
            result.append(string[start:i[0]])
            start = i[1]
        result.append(string[index_list[-1][1]: len(string)])
        return result
    return [string, ]
