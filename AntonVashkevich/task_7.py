class MyNumberCollection:
    def __init__(self, start, end=None, step=1):
        self.my_col = []
        self.step = step
        self._i = -1
        if isinstance(start, (list, tuple)) and all(self.is_integer(i) for i in start):
            self.my_col.extend(start)
        elif all(self.is_integer(i) for i in (start, end, step)):
            self.my_col.extend([i for i in range(start, end+1, step)])
            if end not in self.my_col:
                self.my_col.append(end)
        else:
            raise ValueError("ERROR")

    @staticmethod
    def is_integer(value):
        if isinstance(value,int):
            return True
        raise TypeError("Value must be integer")

    def append(self, item):
        if self.is_integer(item):
            self.my_col.append(item)

    def __add__(self, other):
        return self.my_col + other.my_col

    def __getitem__(self, ind):
        if self.is_integer(ind) and ind < len(self.my_col):
            return self.my_col[ind] ** 2
        raise IndexError("Index out of range")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self._i += 1
            return self.my_col[self._i]
        except IndexError:
            raise StopIteration

    def __repr__(self):
        return f"{self.my_col}"


col1 = MyNumberCollection(0, 5, )
print(col1)
col2 = MyNumberCollection((1, 2, 3, 4, 5))
print(col2+col1)
for i in col2:
    print(i)