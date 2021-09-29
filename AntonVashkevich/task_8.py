class MySquareIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.lst):
            raise StopIteration
        else:
            return self.lst[self.index]**2


a = MySquareIterator([1, 2, 3, 4, 5])
for i in a:
    print(i)
