class MySquareIterator:
    def __init__(self, lst):
        self.start = lst[0]
        self.stop = lst[-1]

    def __iter__(self):
        return self.lst

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        else:
            return self.lst**2



