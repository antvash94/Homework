class HistoryDict:
    history = []

    def __init__(self, dict_):
        if dict_:
            self.dict_ = dict_
        else:
            self.dict_ = {}

    def set_value(self, key, value):
        self.dict_[key] = value
        self.history.append(key)

    def get_history(self):
        return self.history[:10]


d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
print(d.get_history())