class EvenRange:
    def __init__(self, start, stop):
        if start % 2 == 0:
            self.start = start-2
        self.start = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 2
        if self.start >= self.stop:
            return "Out of numbers!"
        else:
            return self.start


er1 = EvenRange(7, 11)
next(er1)
print(next(er1))
print(next(er1))
print(next(er1))
