def my_split(string, sep=" "):
    """Works the same as str.split method """
    result = []
    word = ''
    for i in string:
        if i == sep and word:
            result.append(word)
            word = ''
        elif i != sep:
            word += i
    if word:
        result.append(word)

    return result
