class Counter:
    def __init__(self,  start=0, stop=None  ):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.stop is None or self.start <= self.stop:
            self.start += 1
        else:
            raise IndexError("Maximal value is reached.")

    def get(self):
        print(self.start)



a = Counter()

for i in range(1000):
    a.increment()
    a.get()
