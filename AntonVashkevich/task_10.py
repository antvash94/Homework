from itertools import count
from time import sleep

endless_generator = count(1, 2)

while True:
    print(next(endless_generator), end=' ')
    sleep(1)

