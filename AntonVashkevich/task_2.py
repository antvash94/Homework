from string import punctuation


def most_common_word(path, number_of_words=3):
    res = {}
    with open(path, "r") as f:
        for i in f.read().lower().split():
            i.strip(punctuation)
            if res.get(i) is None:
                res[i] = 1
            else:
                res[i] += 1
    res = sorted(res.items(), reverse=True, key=lambda x: x[1])
    return [word[0] for word in res[:number_of_words]]


print(most_common_word("data/lorem_ipsum.txt", 15))
